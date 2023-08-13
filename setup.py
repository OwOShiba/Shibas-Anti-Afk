from cx_Freeze import setup, Executable

base = None    

executables = [Executable("AntiAFK.py", base=base)]

packages = ["idna", "time", "random", "pydirectinput", "re", "PIL", "pytesseract"]
options = {
    'build_exe': {    
        'packages':packages,
        'include_files':["shiba/"]
    },    
}

setup(
    name = "Shiba's Anti-AFK",
    options = options,
    version = "1.0",
    description = 'Anti-AFK in UnConventional',
    executables = executables
)