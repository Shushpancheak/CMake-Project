cmake_minimum_required(VERSION 3.5)

project(CMake-Project CXX)

include(FindPythonInterp)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall")
set(INDEX_SOURCES_LIST_PY "A/preparing.py")
set(INDEX_SOURCES_LIST "A/index.cpp")
set(MAIN_SOURCES_LIST "C/main.cpp")

include_directories(include)
add_subdirectory("B")

add_executable(project ${MAIN_SOURCES_LIST})

add_executable(preparing ${INDEX_SOURCES_LIST_PY})
add_custom_target(preparing_run
  COMMAND preparing
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  SOURCES ${INDEX_SOURCES_LIST_PY}
)

add_dependencies(project preparing_run)