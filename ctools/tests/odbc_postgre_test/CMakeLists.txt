project (tests_odbc_postgre_test)

set (ODBC_POSTGRE_DIR ${BUILD_SQL_DIR}/odbc/postgre)

include_directories(
  ${LIBS_SOURCE_DIR}/portal/odbc_general/include
  ${ODBC_POSTGRE_DIR}
)

add_definitions (
  -DDRIVER="Postgre 14 ODBC 64"
  -DUSERID="bbdmsg"
  -DPWD="postgre"
  )

set (generated 
  ${ODBC_POSTGRE_DIR}/accuitycontact.cpp
  ${ODBC_POSTGRE_DIR}/accuitycontact.sh
  ${ODBC_POSTGRE_DIR}/accuitycontact_snips.h
  ${ODBC_POSTGRE_DIR}/accuitycorrespondent.cpp
  ${ODBC_POSTGRE_DIR}/accuitycorrespondent.sh
  ${ODBC_POSTGRE_DIR}/accuitycorrespondentsub.cpp
  ${ODBC_POSTGRE_DIR}/accuitycorrespondentsub.sh
  ${ODBC_POSTGRE_DIR}/accuitycorrespondentsub_snips.h
  ${ODBC_POSTGRE_DIR}/accuitycorrespondent_snips.h
  ${ODBC_POSTGRE_DIR}/accuitylocation.cpp
  ${ODBC_POSTGRE_DIR}/accuitylocation.sh
  ${ODBC_POSTGRE_DIR}/accuitylocation_snips.h
  ${ODBC_POSTGRE_DIR}/accuityofficer.cpp
  ${ODBC_POSTGRE_DIR}/accuityofficer.sh
  ${ODBC_POSTGRE_DIR}/accuityofficer_snips.h
  ${ODBC_POSTGRE_DIR}/accuityroutingatt.cpp
  ${ODBC_POSTGRE_DIR}/accuityroutingatt.sh
  ${ODBC_POSTGRE_DIR}/accuityroutingatt_snips.h
  ${ODBC_POSTGRE_DIR}/accuityroutingcode.cpp
  ${ODBC_POSTGRE_DIR}/accuityroutingcode.sh
  ${ODBC_POSTGRE_DIR}/accuityroutingcode_snips.h
  ${ODBC_POSTGRE_DIR}/accuityuseroverride.cpp
  ${ODBC_POSTGRE_DIR}/accuityuseroverride.sh
  ${ODBC_POSTGRE_DIR}/accuityuseroverride_snips.h
  ${ODBC_POSTGRE_DIR}/audits.cpp
  ${ODBC_POSTGRE_DIR}/audits.sh
  ${ODBC_POSTGRE_DIR}/audits_snips.h
  ${ODBC_POSTGRE_DIR}/bankfile.cpp
  ${ODBC_POSTGRE_DIR}/bankfile.sh
  ${ODBC_POSTGRE_DIR}/bankfile_snips.h
  )

source_group("generated" FILES ${generated})

set (source
  main.cpp
  )

add_executable (odbc_postgre_test ${source} ${generated})

target_link_libraries (odbc_postgre_test odbc_general winmm)

set_target_properties(odbc_postgre_test PROPERTIES PROJECT_LABEL tests_odbc_postgre_test)
set_property(TARGET odbc_postgre_test PROPERTY FOLDER ${TESTS_FOLDER}/odbc_postgre_test)
