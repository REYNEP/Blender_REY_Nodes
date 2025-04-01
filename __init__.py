import importlib
import os
import sys
import time

bl_info = {
    "name": "REY Nodes V0.1",
    "author": "REYNEP",
    "blender": (4, 0, 0),
    "category": "Node"
}

files = {
    "REY_Nodes_AddMenuEntry.py",
    "REY_Nodes_Append.py",
    "REY_Nodes_List.py",
    "InstantiateNode/REY_BumpNormDisp_V1.py"
}

pycache_folderName = "__pycache__"
pycache_suffix = ".cpython-311.pyc"

# Helper function to reload a module if it has changed
# Needed for Testing without closing & re-running blender, everytime i change a line of code in imported files
def reload_if_changed(module):
    # Check if the module has a valid __file__ attribute
    module_file = getattr(module, "__file__", None)
    if module_file is None:
        print(f"Skipping reload for module: {module.__name__} (no associated file)")
        return

    # Handle compiled files (.pyc)
    if module_file.endswith(".pyc"):
        module_file = module_file[:-1]

    # Check if the file exists
    if not os.path.exists(module_file):
        print(f"File not found for module: {module.__name__}")
        return

    # Get the last modification time
    last_modified = os.path.getmtime(module_file)
    last_loaded = getattr(module, "__last_loaded__", 0)

    # Reload the module if it has changed
    if last_modified > last_loaded:
        print(f"Reloading module: {module.__name__}")
        module.__last_loaded__ = time.time()
        importlib.reload(module)
    

# Import modules
from .InstantiateNode import REY_BumpNormDisp_V1
from . import REY_Nodes_Append
from . import REY_Nodes_AddMenuEntry

def register():
    reload_if_changed(REY_BumpNormDisp_V1)
    reload_if_changed(REY_Nodes_Append)
    reload_if_changed(REY_Nodes_AddMenuEntry)
        # Read docs of this function above
    
    print("Registering REY_Nodes")
    REY_BumpNormDisp_V1.register()
    REY_Nodes_Append.register()
    REY_Nodes_AddMenuEntry.register()

def unregister():
    print("UnRegistering REY_Nodes")
    REY_BumpNormDisp_V1.unregister()
    REY_Nodes_Append.unregister()
    REY_Nodes_AddMenuEntry.unregister()

if __name__ == "__main__":
    register()