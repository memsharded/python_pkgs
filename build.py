import os


def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception("cmd failed: {}".format(cmd))


run("conan create tool -s os=Windows")
run("conan create tool -s os=Linux")
run("conan create tool -s os=Macos")


run("conan create consumer -s os=Windows")
run("conan create consumer -s os=Linux")
run("conan create consumer -s os=Macos")
