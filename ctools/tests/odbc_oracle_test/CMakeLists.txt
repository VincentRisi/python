project (tests_odbc_oracle_test)

set (ODBC_ORACLE_DIR ${BUILD_SQL_DIR}/odbc/oracle)

include_directories(
  ${LIBS_SOURCE_DIR}/portal/odbc_general/include
  ${LIBS_SOURCE_DIR}/utfpp
  ${ODBC_ORACLE_DIR}
)

add_definitions (
  -DDRIVER="Oracle 12 ODBC 64"
  -DUSERID="bbdmsg"
  -DPWD="oracle"
  )

set (generated 
  ${ODBC_ORACLE_DIR}/accuitycontact.cpp
  ${ODBC_ORACLE_DIR}/accuitycontact.sh
  ${ODBC_ORACLE_DIR}/accuitycontact_snips.h
  ${ODBC_ORACLE_DIR}/accuitycorrespondent.cpp
  ${ODBC_ORACLE_DIR}/accuitycorrespondent.sh
  ${ODBC_ORACLE_DIR}/accuitycorrespondentsub.cpp
  ${ODBC_ORACLE_DIR}/accuitycorrespondentsub.sh
  ${ODBC_ORACLE_DIR}/accuitycorrespondentsub_snips.h
  ${ODBC_ORACLE_DIR}/accuitycorrespondent_snips.h
  ${ODBC_ORACLE_DIR}/accuitylocation.cpp
  ${ODBC_ORACLE_DIR}/accuitylocation.sh
  ${ODBC_ORACLE_DIR}/accuitylocation_snips.h
  ${ODBC_ORACLE_DIR}/accuityofficer.cpp
  ${ODBC_ORACLE_DIR}/accuityofficer.sh
  ${ODBC_ORACLE_DIR}/accuityofficer_snips.h
  ${ODBC_ORACLE_DIR}/accuityroutingatt.cpp
  ${ODBC_ORACLE_DIR}/accuityroutingatt.sh
  ${ODBC_ORACLE_DIR}/accuityroutingatt_snips.h
  ${ODBC_ORACLE_DIR}/accuityroutingcode.cpp
  ${ODBC_ORACLE_DIR}/accuityroutingcode.sh
  ${ODBC_ORACLE_DIR}/accuityroutingcode_snips.h
  ${ODBC_ORACLE_DIR}/accuityuseroverride.cpp
  ${ODBC_ORACLE_DIR}/accuityuseroverride.sh
  ${ODBC_ORACLE_DIR}/accuityuseroverride_snips.h
  ${ODBC_ORACLE_DIR}/audits.cpp
  ${ODBC_ORACLE_DIR}/audits.sh
  ${ODBC_ORACLE_DIR}/audits_snips.h
  ${ODBC_ORACLE_DIR}/bankfile.cpp
  ${ODBC_ORACLE_DIR}/bankfile.sh
  ${ODBC_ORACLE_DIR}/bankfile_snips.h
  )

source_group("generated" FILES ${generated})

set (source
  main.cpp
  )

add_executable (odbc_oracle_test ${source} ${generated})

target_link_libraries (odbc_oracle_test odbc_general winmm)

set_target_properties(odbc_oracle_test PROPERTIES PROJECT_LABEL tests_odbc_oracle_test)
set_property(TARGET odbc_oracle_test PROPERTY FOLDER ${TESTS_FOLDER}/odbc_oracle_test)
