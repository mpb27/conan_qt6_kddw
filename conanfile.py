from conans import ConanFile, CMake, tools

class ConanQtConan(ConanFile):
    name = "conan_qt6_kddw"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    build_requires = ["cmake/3.19.2", "ninja/1.10.2"]
    requires = [ 
        "qt/6.0.1@bincrafters/stable",
        "kddockwidgets/1.3.0@kdab/stable"
    ]

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

    def imports(self):
        self.copy("*.dll",     dst="bin", src="bin")
        self.copy("plugins/*", dst="bin", src="")       # Plugins for Qt6
        self.copy("*.dylib",   dst="",    src="lib")
