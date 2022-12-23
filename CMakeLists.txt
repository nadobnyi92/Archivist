cmake_minimum_required(VERSION 3.5)

project(Archivist)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

include(${CMAKE_SOURCE_DIR}/conan.cmake)
conan_cmake_run(
    CONANFILE conanfile.txt
    BASIC_SETUP
    BUILD missing)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(Qt5 COMPONENTS Core Widgets REQUIRED)
find_package(Boost REQUIRED system)

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(SRC src/main.cpp
        src/mainwindow.cpp)

qt5_wrap_ui(UI ui/mainwindow.ui)

add_executable( ${PROJECT_NAME} ${SRC} ${UI} )

target_link_libraries(${PROJECT_NAME} Qt5::Core Qt5::Widgets)

file(CREATE_LINK ${CMAKE_BINARY_DIR}/compile_commands.json ${CMAKE_SOURCE_DIR}/compile_commands.json SYMBOLIC)

