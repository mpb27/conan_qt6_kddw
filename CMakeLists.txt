cmake_minimum_required(VERSION 3.17)
project(conan_qt6_kddw LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add libraries distributed via Conan.
if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    conan_basic_setup()
else()
    message(WARNING "The file conanbuildinfo.cmake doesn't exist, you have to run conan install first.")
endif()

find_package(Qt6 COMPONENTS Core Gui Widgets)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

# Trying find_package tries to load Qt5 instead of Qt6.
# find_package(KDDockWidgets REQUIRED)

# Add define.
add_definitions(-DQT_WIDGETS_LIB)

add_executable(conan_qt6_kddw
    src/main.cpp
)
target_link_libraries(conan_qt6_kddw
        ${CONAN_LIBS}
        kddockwidgets1.lib
        )
