project (azure)

set (jportal_jar ${JTOOLS_DIR}/build/jportal.jar)
set (crackle_jar ${JTOOLS_DIR}/build/crackle.jar)

set (AZURE_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR})
set (AZURE_BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR})

include_directories (
  ${LIBS_SOURCE_DIR}/portal/mss_17
  ${LIBS_SOURCE_DIR}/portal/mss_17/include
  ${LIBS_SOURCE_DIR}/portal/mss_17/src
)

if (LINUX)
  include_directories (${LIBS_SOURCE_DIR}/portal/mss_17/include)
  include_directories (${LIBS_SOURCE_DIR}/portal/mss_17/mss/linux/include)
elseif (WIN32)
  include_directories (${LIBS_SOURCE_DIR}/portal/mss_17/win/include)
  include_directories (${LIBS_SOURCE_DIR}/portal/mss_17/mss/win/include)
endif ()

add_subdirectory (sql_build)
