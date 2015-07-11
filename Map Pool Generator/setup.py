from cx_Freeze import setup, Executable

setup( name = "MapPoolGenerator" , version = "1.0" , description = "Map Pool Generator" , executables = [Executable(script = "MapPoolInterface.py")] , base = "Win32GUI" )
