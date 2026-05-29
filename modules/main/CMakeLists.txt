cmake_minimum_required (VERSION 4.2)

project (main_modules)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF) # Set to ON if you want compiler-specific extensions 
                              # (e.g., -std=gnu++23)

include_directories (. testers)

add_library (main
  machine.cppm
  xdir.cppm
  xcstring.cppm
  tbuffer.cppm
  logfile.cppm
  mutex.cppm
  addlist.cppm
  getargs.cppm
  splits.cppm
  date.cppm
  obsocket.cppm
  cbsocket.cppm
  blackboard.cppm
  encoders.cppm
  )

add_executable (getargs_test testers/getargs_test.cpp)
target_link_libraries (getargs_test main)

add_executable (encoders_test testers/encoders_test.cpp)
target_link_libraries (encoders_test main)

add_executable (splits_test testers/splits_test.cpp testers/aaxlist.h)
target_link_libraries (splits_test main)
