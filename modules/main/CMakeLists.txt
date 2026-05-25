cmake_minimum_required (VERSION 4.2)

project ("main_modules")

set(CMAKE_CXX_STANDARD 23)

include_directories (. testers)

add_library (main
  machine.ixx
  xdir.ixx
  xcstring.ixx
  tbuffer.ixx
  logfile.ixx
  mutex.ixx
  addlist.ixx 
  getargs.ixx
  splits.ixx
  date.ixx
  obsocket_msvc.ixx
  cbsocket_msvc.ixx
  blackboard.ixx
  encoders.ixx
  #jsoncpp.ixx
  )

add_executable (getargs_test testers/getargs_test.cpp)
target_link_libraries (getargs_test main)

add_executable (encoders_test testers/encoders_test.cpp)
target_link_libraries (encoders_test main)

add_executable (splits_test testers/splits_test.cpp testers/aaxlist.h)
target_link_libraries (splits_test main)

include_external_msproject("aaxbuild" "./testers/aaxbuild.pyproj"
    GUID "a704a7dd-44df-41fd-ba66-cb85f359e7bf"
    PLATFORM "Any CPU"
    )


