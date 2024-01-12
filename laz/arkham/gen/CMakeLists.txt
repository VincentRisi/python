project (arkham_gen)

include(${CMAKE_SOURCE_DIR}/cmake/dbportal.cmake)

pathed(sqlDir ${CMAKE_CURRENT_BINARY_DIR}/sql)
pathed(pyDir  ${CMAKE_CURRENT_BINARY_DIR}/py)
pathed(cppDir ${CMAKE_CURRENT_BINARY_DIR}/cpp)
pathed(pasDir ${CMAKE_CURRENT_BINARY_DIR}/pas)

set (siFiles
  ${CMAKE_CURRENT_SOURCE_DIR}/si/ancients.si
  ${CMAKE_CURRENT_SOURCE_DIR}/si/districts.si
  ${CMAKE_CURRENT_SOURCE_DIR}/si/encounters.si
  ${CMAKE_CURRENT_SOURCE_DIR}/si/gates.si
  ${CMAKE_CURRENT_SOURCE_DIR}/si/investigators.si
  ${CMAKE_CURRENT_SOURCE_DIR}/si/items.si
  ${CMAKE_CURRENT_SOURCE_DIR}/si/maps.si
  ${CMAKE_CURRENT_SOURCE_DIR}/si/monsters.si
  ${CMAKE_CURRENT_SOURCE_DIR}/si/mythos.si
  ${CMAKE_CURRENT_SOURCE_DIR}/si/otherworlds.si
  ${CMAKE_CURRENT_SOURCE_DIR}/si/places.si
  ${CMAKE_CURRENT_SOURCE_DIR}/si/placetypes.si
  ${CMAKE_CURRENT_SOURCE_DIR}/si/possessions.si
  ${CMAKE_CURRENT_SOURCE_DIR}/si/roads.si
)

set (switches
  "-o" "${sqlDir}" "Lite3DDL"
  "-o" "${pyDir}"  "Lite3PyCode"
  "-o" "${cppDir}" "Lite3CCode"
  "-o" "${pasDir}" "Lite3PasCode"
)

jportal(arkham_gen "${siFiles}" ${switches})

set (dbFile ${CMAKE_BINARY_DIR}/arkham/bin/arkham.db)

lite3sql(${dbFile} "${sqlFiles}")
