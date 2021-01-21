from conans import ConanFile


class ToolConan(ConanFile):
    name = "consumer"
    version = "0.1"
    settings = "os"
    build_requires = "tool/0.1"

    def build(self):
        import mytool
        mytool.myfunction()
