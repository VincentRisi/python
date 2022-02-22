project (accuity_httpserver)

add_definitions(-DACCUITY_STANDALONE -DHTTP_SERVER)

include_directories (
  ${CMAKE_CURRENT_SOURCE_DIR}
  ${PYTHON_DIR}
  ${PYTHON_INCLUDE_DIR}
  ${ACCUITY_SOURCE_DIR}
  ${JTOOLS_DIR}/out/idl2/http
  ## ${ACCUITY_BINARY_DIR}/server/idl
  ## ${ACCUITY_BINARY_DIR}/server/http
  ## ${ACCUITY_BINARY_DIR}/sh
  ## ${PUTTY3_SOURCE_DIR}/idl2/src
  ${LIBS_SOURCE_DIR}
  ${LIBS_SOURCE_DIR}/http/src
  ${LIBS_SOURCE_DIR}/jsoncpp
  ${LIBS_SOURCE_DIR}/jsoncpp/src
  ${PUTTY3_INCLUDE_DIR}
  )

include (${CMAKE_CURRENT_SOURCE_DIR}/inifile.cmake)

set (source
  ${ACCUITY_BINARY_DIR}/http/accuityserver_http.h
  ${ACCUITY_BINARY_DIR}/http/accuityserver_http.cpp
  ${ACCUITY_BINARY_DIR}/server/idl/accuity.h
  ${ACCUITY_BINARY_DIR}/server/idl/accuityimpl.cpp
  ${ACCUITY_BINARY_DIR}/http/accuity_main.cpp
  ${outfile}
  ${pyfile}
  )

set_source_files_properties (${source} PROPERTIES GENERATED TRUE)

if (WIN32)
  set (winlibs ws2_32 winmm)
else ()  
  set (winlibs)
endif ()

set (added_source
  ${PUTTY3_SOURCE_DIR}/idl2/src/dbapishell.cpp
  ${PUTTY3_SOURCE_DIR}/idl2/src/dbapishell.h
  )

add_executable(accuity_httpserver ${source} ${added_source})
target_link_libraries (accuity_httpserver ${bbdlibs} ${winlibs} ${bbdextra} jsoncpp http ${PYTHONLIBS})
add_dependencies (accuity_httpserver accuity_idl2_build pyportal)
## if (WIN32)
##   add_dependencies (accuityhttp Accuityhttp_cs_build)
##   add_custom_command (TARGET accuityhttp POST_BUILD
##     COMMAND ${CMAKE_COMMAND} -E copy ${ACCUITY_BINARY_DIR}/bin/accuity.bin ${CMAKE_BINARY_DIR}/bin/accuity.bin
##     COMMAND ${CMAKE_COMMAND} -E copy ${ACCUITY_BINARY_DIR}/bin/accuityhttp.ini ${CMAKE_BINARY_DIR}/bin/accuityhttp.ini
##     COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_BINARY_DIR}/bin/Debug/accuityhttp.exe ${ACCUITY_BINARY_DIR}/bin/accuityhttp.exe
##     COMMAND ${CMAKE_COMMAND} -E copy ${ACCUITY_BINARY_DIR}/bin/accuityhttp.cmd ${CMAKE_BINARY_DIR}/bin/accuityhttp.cmd
##     )
## else ()
##   add_custom_command (TARGET accuityhttp POST_BUILD
##     COMMAND ${CMAKE_COMMAND} -E copy ${ACCUITY_BINARY_DIR}/bin/accuity.bin ${CMAKE_BINARY_DIR}/bin/accuity.bin
##     COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_BINARY_DIR}/bin/accuityhttp.ini ${ACCUITY_BINARY_DIR}/bin/accuityhttp.ini
##     COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_BINARY_DIR}/bin/accuityhttp ${ACCUITY_BINARY_DIR}/bin/accuityhttp
##     COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_BINARY_DIR}/bin/accuityhttp.sh ${ACCUITY_BINARY_DIR}/bin/accuityhttp.sh
##     )
## endif ()

## set_target_properties (accuityhttp PROPERTIES PROJECT_LABEL putty3_idl2_accuity_httpserver)
## set_property(TARGET accuityhttp PROPERTY FOLDER "putty3/idl2/accuity/httpserver")

