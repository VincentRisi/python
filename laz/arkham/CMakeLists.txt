cmake_minimum_required(VERSION 2.8)

project (main_arkham)

set (ARKHAM_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src)

## Find the python libraries on this system
find_package (PythonInterp)
find_package (PythonLibs)

message (STATUS ${PYTHON_EXECUTABLE})

add_subdirectory(gen)
