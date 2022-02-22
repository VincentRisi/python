project (accuity)

set (jportal_jar ${JTOOLS_DIR}/build/jportal.jar)
set (crackle_jar ${JTOOLS_DIR}/build/crackle.jar)

set (ACCUITY_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR})
set (ACCUITY_BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR})

add_subdirectory (sql_build)
add_subdirectory (idl2_build)
add_subdirectory (httpserver)
