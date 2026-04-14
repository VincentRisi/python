cmake_minimum_required (VERSION 4.2)

project ("main_modules")

set(CMAKE_CXX_STANDARD 23)

include_directories (old_h_and_cpp)

add_library (main
  mutex_msvc.ixx
  addlist.ixx 
  getargs.ixx
  xcstring.ixx
  tbuffer.ixx
  splits.ixx
  date.ixx
  obsocket_msvc.ixx
  cbsocket_msvc.ixx
  )

add_executable (getargs_test getargs_test.cpp)
target_link_libraries (getargs_test main)

