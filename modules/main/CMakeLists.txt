cmake_minimum_required (VERSION 4.2)

project ("main_modules")

set(CMAKE_CXX_STANDARD 23)

add_library (main
  #machine.ixx
  addlist.ixx 
  getargs.ixx
  xcstring.ixx
  tbuffer.ixx
  splits.ixx
  )

add_executable (getargs_test getargs_test.cpp)
target_link_libraries (getargs_test main)

