# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\VendingMachine_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\VendingMachine_autogen.dir\\ParseCache.txt"
  "VendingMachine_autogen"
  )
endif()
