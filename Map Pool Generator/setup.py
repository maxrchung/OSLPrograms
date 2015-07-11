from cx_Freeze import setup, Executable

setup( name = "" , version = "0.1" , description = "" , executables = [Executable(script = "MapPoolInterface.py")] , base="Win32GUI" )
