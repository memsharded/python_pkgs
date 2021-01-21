import textwrap
from conans import ConanFile
from conans.tools import save


class ToolConan(ConanFile):
    name = "tool"
    version = "0.1"
    settings = "os"

    def build(self):
        content = textwrap.dedent("""
            def myfunction():
                print("Tool running {{}}!!!!!".format("{}"))
            """.format(self.settings.os))
        save("mytool.py", content)

    def package(self):
        self.copy("*.py")

    def package_info(self):
        self.env_info.PYTHONPATH = [self.package_folder]