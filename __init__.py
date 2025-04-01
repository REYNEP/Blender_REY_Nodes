bl_info = {
    "name": "REY Nodes V0.1",
    "author": "REYNEP",
    "blender": (4, 0, 0),
    "category": "Node"
}

from .InstantiateNode import REY_BumpNormDisp_V1
    # ./InstantiateNode/REY_BumpNormDisp_V1.py
    # Yeah, Python is just weird, like that.... kinda forgot, over time, anyway.

from . import REY_Nodes_Append
from . import REY_Nodes_AddMenuEntry

def register():
    REY_BumpNormDisp_V1.register()
    REY_Nodes_Append.register()
    REY_Nodes_AddMenuEntry.register()

def unregister():
    REY_BumpNormDisp_V1.unregister()
    REY_Nodes_Append.unregister()
    REY_Nodes_AddMenuEntry.unregister()

if __name__ == "__main__":
    register()