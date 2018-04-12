FREECADPATH = '/usr/lib/freecad/lib/'
MACRONAME= 'step_to_stl.FCMacro'

import sys
sys.path.append(FREECADPATH)
import glob, os


try:
    import FreeCAD, FreeCADGui
except ValueError:
    print('FreeCAD not found')

grp=App.ParamGet("User parameter:BaseApp/Preferences/Macro")
path_to_macros = grp.GetString("MacroPath", App.getUserAppDataDir())
fc_macros= glob.glob(path_to_macros+'*.FCMacro')

print(path_to_macros)
print(fc_macros)

for filename in fc_macros:
    if [(len(filename)-len(MACRONAME)] == MACRONAME:
        execfile(filename)

