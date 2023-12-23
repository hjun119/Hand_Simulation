cmake_minimum_required(VERSION 3.12 FATAL_ERROR)

project(ReadSTL)

find_package(VTK COMPONENTS
    CommonColor
    CommonCore
    CommonDataModel
    IOGeometry
    InteractionStyle
    RenderingContextOpenGL2
    RenderingCore
    RenderingFreeType
    RenderingGL2PSOpenGL2
    RenderingContextOpenGL2
)

if (NOT VTK_FOUND)
    message(FATAL_ERROR "ReadSTL : Unable to find the VTK build folder.")
endif()

# Prevent a "command line is too long" failure in Windows.
set(CMAKE_NINJA_FORCE_RESPONSE_FILE "ON" CACHE BOOL "Force Ninja to use response files.")
add_executable(ReadSTL MACOSX_BUNDLE ReadSTL.cxx )
    target_link_libraries(ReadSTL PRIVATE ${VTK_LIBRAIES}
)
# vtk_module_autoinit is needed
vtk_module_autoinit(
    TARGETS ReadSTL
    MODULES ${VTK_LIBRARIES}
)