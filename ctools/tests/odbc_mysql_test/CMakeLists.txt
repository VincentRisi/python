project (tests_odbc_mysql_test)

set (ODBC_MYSQL_DIR ${BUILD_SQL_DIR}/odbc/mysql)

include_directories(
  ${LIBS_SOURCE_DIR}/portal/odbc_general/include
  ${ODBC_MYSQL_DIR}
)

add_definitions (
  -DDRIVER="Postgre 14 ODBC 64"
  -DUSERID="bbdmsg"
  -DPWD="postgre"
  )

set (generated 
  ${ODBC_MYSQL_DIR}/accuitycontact.cpp
  ${ODBC_MYSQL_DIR}/accuitycontact.sh
  ${ODBC_MYSQL_DIR}/accuitycontact_snips.h
  ${ODBC_MYSQL_DIR}/accuitycorrespondent.cpp
  ${ODBC_MYSQL_DIR}/accuitycorrespondent.sh
  ${ODBC_MYSQL_DIR}/accuitycorrespondentsub.cpp
  ${ODBC_MYSQL_DIR}/accuitycorrespondentsub.sh
  ${ODBC_MYSQL_DIR}/accuitycorrespondentsub_snips.h
  ${ODBC_MYSQL_DIR}/accuitycorrespondent_snips.h
  ${ODBC_MYSQL_DIR}/accuitylocation.cpp
  ${ODBC_MYSQL_DIR}/accuitylocation.sh
  ${ODBC_MYSQL_DIR}/accuitylocation_snips.h
  ${ODBC_MYSQL_DIR}/accuityofficer.cpp
  ${ODBC_MYSQL_DIR}/accuityofficer.sh
  ${ODBC_MYSQL_DIR}/accuityofficer_snips.h
  ${ODBC_MYSQL_DIR}/accuityroutingatt.cpp
  ${ODBC_MYSQL_DIR}/accuityroutingatt.sh
  ${ODBC_MYSQL_DIR}/accuityroutingatt_snips.h
  ${ODBC_MYSQL_DIR}/accuityroutingcode.cpp
  ${ODBC_MYSQL_DIR}/accuityroutingcode.sh
  ${ODBC_MYSQL_DIR}/accuityroutingcode_snips.h
  ${ODBC_MYSQL_DIR}/accuityuseroverride.cpp
  ${ODBC_MYSQL_DIR}/accuityuseroverride.sh
  ${ODBC_MYSQL_DIR}/accuityuseroverride_snips.h
  ${ODBC_MYSQL_DIR}/audits.cpp
  ${ODBC_MYSQL_DIR}/audits.sh
  ${ODBC_MYSQL_DIR}/audits_snips.h
  ${ODBC_MYSQL_DIR}/bankfile.cpp
  ${ODBC_MYSQL_DIR}/bankfile.sh
  ${ODBC_MYSQL_DIR}/bankfile_snips.h
  )

source_group("generated" FILES ${generated})

set (source
  main.cpp
  )

add_executable (odbc_mysql_test ${source} ${generated})

target_link_libraries (odbc_mysql_test odbc_general winmm)

set_target_properties(odbc_mysql_test PROPERTIES PROJECT_LABEL tests_odbc_mysql_test)
set_property(TARGET odbc_mysql_test PROPERTY FOLDER ${TESTS_FOLDER}/odbc_mysql_test)
