cmake_minimum_required(VERSION 3.5)

project(CMake-Project CXX)
add_subdirectory(B)

find_package(PythonInterp 3.5 REQUIRED)
find_package(PythonLibs 3.5 REQUIRED)

# Varibales
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall")
set(INDEX_SOURCES_LIST_PY "A/preparing.py")
set(INDEX_SOURCES_LIST "A/index.cpp A/index.h")
set(MAIN_SOURCES_LIST "C/main.cpp C/main.h")

# Creating libraries
add_executable(preparing "${INDEX_SOURCES_LIST_PY}")
add_custom_command(
  COMMAND preparing
)
add_library(index "${INDEX_SOURCES_LIST}")

# Linking
add_executable(project "${MAIN_SOURCES_LIST}")
target_link_libraries(project PRIVATE lib)
target_link_libraries(project PRIVATE index)