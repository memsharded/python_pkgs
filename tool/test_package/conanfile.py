import os

from conans import ConanFile


class ToolTestConan(ConanFile):
    settings = "os"

    def test(self):
        import mytool
        mytool.myfunction()
