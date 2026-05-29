cmake_minimum_required (VERSION 4.2)

project ("main_modules")

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF) # Set to ON if you want compiler-specific extensions 
                              # (e.g., -std=gnu++23)

include_directories (. testers)

add_library (main
  machine.cpp
  xdir.cpp
  xcstring.cpp
  tbuffer.cpp
  logfile.cpp
  mutex.cpp
  addlist.cpp 
  getargs.cpp
  splits.cpp
  date.cpp
  obsocket.cpp
  cbsocket.cpp
  blackboard.cpp
  encoders.cpp
  )

add_executable (getargs_test testers/getargs_test.cpp)
target_link_libraries (getargs_test main)

add_executable (encoders_test testers/encoders_test.cpp)
target_link_libraries (encoders_test main)

add_executable (splits_test testers/splits_test.cpp testers/aaxlist.h)
target_link_libraries (splits_test main)

#include_external_msproject("aaxbuild" "./testers/aaxbuild.pyproj"
#    GUID "a704a7dd-44df-41fd-ba66-cb85f359e7bf"
#    PLATFORM "Any CPU"
#    )


