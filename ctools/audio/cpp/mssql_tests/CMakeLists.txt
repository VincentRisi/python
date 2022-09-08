project (mssql_tests)

set (MSSSH_DIR ${JTOOLS_DIR}/out/audio/sql/msssh)

set (source
  ${CMAKE_CURRENT_SOURCE_DIR}/main.cpp ${CMAKE_CURRENT_SOURCE_DIR}/main.h
  #${MSSSH_DIR}/cover.cpp ${MSSSH_DIR}/cover.sh ${MSSSH_DIR}/cover_snips.h
  ${MSSSH_DIR}/message.cpp ${MSSSH_DIR}/message.sh ${MSSSH_DIR}/message_snips.h
  ${MSSSH_DIR}/reply.cpp ${MSSSH_DIR}/reply.sh ${MSSSH_DIR}/reply_snips.h
  ${MSSSH_DIR}/response.cpp ${MSSSH_DIR}/response.sh ${MSSSH_DIR}/response_snips.h
  ${MSSSH_DIR}/streams.cpp ${MSSSH_DIR}/streams.sh ${MSSSH_DIR}/streams_snips.h
  )

if (WIN32)
  set (MSS_17_INCLUDE_DIR ${LIBS_SOURCE_DIR}/portal/mss_17/mss/win/include)
else ()
  set (MSS_17_INCLUDE_DIR ${LIBS_SOURCE_DIR}/portal/mss_17/mss/linux/include)
endif ()

add_executable (mssql_tests ${source})
target_link_directories (mssql_tests PUBLIC ${CTOOLS_DIR}/libs/portal/mss_17/mss/win/lib/x64)
target_include_directories (mssql_tests PUBLIC
  ${CMAKE_CURRENT_SOURCE_DIR}
  ${MSSSH_DIR}
  ${LIBS_SOURCE_DIR}/portal/mss_17
  ${LIBS_SOURCE_DIR}/portal/mss_17/include
  ${MSS_17_INCLUDE_DIR}
  )
target_link_libraries (mssql_tests mss_17 winmm odbc32 msodbcsql17 main)

set_property(TARGET mssql_tests PROPERTY FOLDER "audio/cpp_tests/mssql_tests")