To build a CMake project using clang++ in Visual Studio Community 2026, you need to ensure the correct Clang components are installed and then configure your CMake toolset or preset to target Clang instead of the default MSVC compiler.

Here is the step-by-step guide to setting it up.

1. Install Required Workloads and Components

You must explicitly add Clang and CMake tools to your Visual Studio installation.
Open the Visual Studio Installer from your Windows Start Menu.
Click Modify next to your Visual Studio Community 2026 installation.
Under the Workloads tab, check the box for Desktop development with C++.
Look at the Installation details pane on the right side and check these optional components:
C++ CMake tools for Windows
C++ Clang compiler for Windows
Click Modify in the bottom right corner to download and install the tools.