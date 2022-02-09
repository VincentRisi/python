project (tests_ocitest)

set (DB2_DIR ${BUILD_SQL_DIR}/clish)

include_directories (
  ${LIBS_SOURCE_DIR}/portal/cli9/db2/win
  ${LIBS_SOURCE_DIR}/portal/cli9/src
  ${DB2_DIR}
)

set (generated 
  ${DB2_DIR}/accuitycontact.cpp
  ${DB2_DIR}/accuitycontact.sh
  ${DB2_DIR}/accuitycontact_snips.h
  ${DB2_DIR}/accuitycorrespondent.cpp
  ${DB2_DIR}/accuitycorrespondent.sh
  ${DB2_DIR}/accuitycorrespondentsub.cpp
  ${DB2_DIR}/accuitycorrespondentsub.sh
  ${DB2_DIR}/accuitycorrespondentsub_snips.h
  ${DB2_DIR}/accuitycorrespondent_snips.h
  ${DB2_DIR}/accuitylocation.cpp
  ${DB2_DIR}/accuitylocation.sh
  ${DB2_DIR}/accuitylocation_snips.h
  ${DB2_DIR}/accuityofficer.cpp
  ${DB2_DIR}/accuityofficer.sh
  ${DB2_DIR}/accuityofficer_snips.h
  ${DB2_DIR}/accuityroutingatt.cpp
  ${DB2_DIR}/accuityroutingatt.sh
  ${DB2_DIR}/accuityroutingatt_snips.h
  ${DB2_DIR}/accuityroutingcode.cpp
  ${DB2_DIR}/accuityroutingcode.sh
  ${DB2_DIR}/accuityroutingcode_snips.h
  ${DB2_DIR}/accuityuseroverride.cpp
  ${DB2_DIR}/accuityuseroverride.sh
  ${DB2_DIR}/accuityuseroverride_snips.h
  ${DB2_DIR}/audits.cpp
  ${DB2_DIR}/audits.sh
  ${DB2_DIR}/audits_snips.h
  ${DB2_DIR}/bankfile.cpp
  ${DB2_DIR}/bankfile.sh
  ${DB2_DIR}/bankfile_snips.h
  )

source_group("generated" FILES ${generated})

set (source
  main.cpp
  )

add_executable (db2_test ${source} ${generated})

link_directories(${ORACLE_LIBRARY_DIR})

set_target_properties(db2_test PROPERTIES PROJECT_LABEL tests-db2-test)
set_property(TARGET db2_test PROPERTY FOLDER ${TESTS_FOLDER}/db2_test)

