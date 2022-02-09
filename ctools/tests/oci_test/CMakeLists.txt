project (tests_ocitest)

set (OCI_DIR ${BUILD_SQL_DIR}/ocish)

include_directories(
  ${LIBS_SOURCE_DIR}/portal/oci_12/oracle
  ${LIBS_SOURCE_DIR}/portal/oci_12/src
  ${LIBS_SOURCE_DIR}/utfpp
  ${OCI_DIR}
)

set (generated 
  ${OCI_DIR}/accuitycontact.cpp
  ${OCI_DIR}/accuitycontact.sh
  ${OCI_DIR}/accuitycontact_snips.h
  ${OCI_DIR}/accuitycorrespondent.cpp
  ${OCI_DIR}/accuitycorrespondent.sh
  ${OCI_DIR}/accuitycorrespondentsub.cpp
  ${OCI_DIR}/accuitycorrespondentsub.sh
  ${OCI_DIR}/accuitycorrespondentsub_snips.h
  ${OCI_DIR}/accuitycorrespondent_snips.h
  ${OCI_DIR}/accuitylocation.cpp
  ${OCI_DIR}/accuitylocation.sh
  ${OCI_DIR}/accuitylocation_snips.h
  ${OCI_DIR}/accuityofficer.cpp
  ${OCI_DIR}/accuityofficer.sh
  ${OCI_DIR}/accuityofficer_snips.h
  ${OCI_DIR}/accuityroutingatt.cpp
  ${OCI_DIR}/accuityroutingatt.sh
  ${OCI_DIR}/accuityroutingatt_snips.h
  ${OCI_DIR}/accuityroutingcode.cpp
  ${OCI_DIR}/accuityroutingcode.sh
  ${OCI_DIR}/accuityroutingcode_snips.h
  ${OCI_DIR}/accuityuseroverride.cpp
  ${OCI_DIR}/accuityuseroverride.sh
  ${OCI_DIR}/accuityuseroverride_snips.h
  ${OCI_DIR}/audits.cpp
  ${OCI_DIR}/audits.sh
  ${OCI_DIR}/audits_snips.h
  ${OCI_DIR}/bankfile.cpp
  ${OCI_DIR}/bankfile.sh
  ${OCI_DIR}/bankfile_snips.h
  )

source_group("generated" FILES ${generated})

set (source
  main.cpp
  )

add_executable (oci_test ${source} ${generated})

link_directories(${ORACLE_LIBRARY_DIR})
target_link_libraries (oci_test oci_12)

set_target_properties(oci_test PROPERTIES PROJECT_LABEL tests_oci_test)
set_property(TARGET oci_test PROPERTY FOLDER ${TESTS_FOLDER}/oci_test)
