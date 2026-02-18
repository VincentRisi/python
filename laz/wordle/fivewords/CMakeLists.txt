# CMakeList.txt : CMake project for five_words, include source and define
# project specific logic here.
#
cmake_minimum_required (VERSION 4.2)

# Enable Hot Reload for MSVC compilers if supported.
if (POLICY CMP0145)
  cmake_policy(SET CMP0145 NEW)
  set(CMAKE_MSVC_DEBUG_INFORMATION_FORMAT "$<IF:$<AND:$<C_COMPILER_ID:MSVC>,$<CXX_COMPILER_ID:MSVC>>,$<$<CONFIG:Debug,RelWithDebInfo>:EditAndContinue>,$<$<CONFIG:Debug,RelWithDebInfo>:ProgramDatabase>>")
endif()

project ("five_words")

# Add source to this project's executable.
add_executable (five_words "five_words.cpp" "five_words.h" "addlist.h")

add_executable (five_words_bits "five_words_bits.cpp" "five_words.h" "addlist.h")

add_executable (five_words_mod "five_words_mod.cpp" "five_words.h" "WordList.ixx" "addlist.h")

add_executable (four_words "four_words.cpp" "four_words.h" "WordList.ixx" "addlist.h" "getargs.cpp" "getargs.h")

set_property(TARGET five_words PROPERTY CXX_STANDARD 23)
set_property(TARGET five_words_bits PROPERTY CXX_STANDARD 23)
set_property(TARGET five_words_mod PROPERTY CXX_STANDARD 23)
set_property(TARGET four_words PROPERTY CXX_STANDARD 23)

