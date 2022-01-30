import platform
import sys
info = 'OS info is \n{}\n\nPython version is {} {}'.format(
platform.uname(), sys.version, platform.architecture(), platform.version())
print(info)