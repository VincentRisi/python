cmake_minimum_required (VERSION 4.2)

project (main_modules)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF) # Set to ON if you want compiler-specific extensions 
                              # (e.g., -std=gnu++23)

include_directories (. testers expat jsoncpp portal/oci_21/oracle)

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
  portal/databuilder.cppm
  portal/json_databuilder.cppm
  portal/xmlmake.cppm
  portal/xmlrecord.cppm
  portal/ociapi.cppm
  )

add_library (expat
  expat/xmldef.h
  expat/xmlparse.h 
  expat/xmlparse.c 
  expat/xmlrole.c 
  expat/xmlrole.h
  expat/xmltok.c 
  expat/xmltok.h
  )

add_library(jsoncpp 
  jsoncpp/json/allocator.h
  jsoncpp/json/assertions.h
  jsoncpp/json/autolink.h
  jsoncpp/json/config.h
  jsoncpp/json/features.h
  jsoncpp/json/forwards.h
  jsoncpp/json/json.h
  jsoncpp/json/reader.h
  jsoncpp/json/value.h
  jsoncpp/json/version.h
  jsoncpp/json/writer.h
  jsoncpp/src/json_tool.h
  jsoncpp/src/json_reader.cpp
  jsoncpp/src/json_valueiterator.inl
  jsoncpp/src/json_value.cpp
  jsoncpp/src/json_writer.cpp
  )

add_executable (getargs_test testers/getargs_test.cpp)
target_link_libraries (getargs_test main)

add_executable (encoders_test testers/encoders_test.cpp)
target_link_libraries (encoders_test main)

add_executable (splits_test testers/splits_test.cpp testers/aaxlist.h)
target_link_libraries (splits_test main)
