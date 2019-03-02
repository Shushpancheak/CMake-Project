cmake_minimum_required(VERSION 3.5)

project(CMake-Project CXX)
add_subdirectory(B)

find_package(PythonInterp 3.5 REQUIRED)
find_package(PythonLibs 3.5 REQUIRED)

# Varibales
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall")
set(INDEX_SOURCES_LIST_PY "A/preparing.py")
set(INDEX_GENERATED_HEADER_NAME "index.h")
set(MAIN_SOURCES_LIST "C/main.cpp")

# Creating library from python script

set(gen_dir "${PROJECT_BINARY_DIR}/generated_headers")
set(INDEX_GENERATED_FOLDER "A")
set(INDEX_SOURCES_LIST "A/index.cpp" "${gen_dir}/${INDEX_GENERATED_HEADER_NAME}")

add_custom_command(
  OUTPUT "${gen_dir}/${INDEX_GENERATED_HEADER_NAME}"
  COMMAND python3 "${CMAKE_CURRENT_SOURCE_DIR}/${INDEX_SOURCES_LIST_PY}" --dir "${gen_dir}/${INDEX_GENERATED_FOLDER}"
  DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/${INDEX_SOURCES_LIST_PY}"
)
add_library(index SHARED ${INDEX_SOURCES_LIST})
target_include_directories(index PUBLIC "${gen_dir}")

# Linking
add_executable(project ${MAIN_SOURCES_LIST})
target_include_directories(project PRIVATE "${gen_dir}")
target_include_directories(project PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}")
target_link_libraries(project PRIVATE lib)
target_link_libraries(project PRIVATE index)
