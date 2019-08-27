from conans import ConanFile


class HarfbuzzConan(ConanFile):
    name = "harfbuzz"
    version = "1.0"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Harfbuzz here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    requires = "freetype2/1.0@tamas/repro", "fontconfig/1.0@tamas/repro"

    def source(self):
        pass

    def build(self):
        self.run("touch libharfbuzz.so")
        print(self.deps_cpp_info["zlib"].lib_paths)

    def package(self):
        self.copy("*.so", dst="lib")

    def package_info(self):
        self.cpp_info.libs = ["harfbuzz"]
