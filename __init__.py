bl_info = {
    "name": "REY Nodes V0.1",
    "author": "REYNEP",
    "blender": (4, 0, 0),
    "category": "Node"
}

from . import RealtimeTesting

# Import modules
from . import REY_Nodes_InstantiateNode
from . import REY_Nodes_Append
from . import REY_Nodes_AddMenuEntry

def register():
    RealtimeTesting.reload_if_changed(REY_Nodes_InstantiateNode)
    RealtimeTesting.reload_if_changed(REY_Nodes_Append)
    RealtimeTesting.reload_if_changed(REY_Nodes_AddMenuEntry)
        # Read docs of this function in it's file 😉
    
    print("Registering REY_Nodes")
    REY_Nodes_InstantiateNode.register()
    REY_Nodes_Append.register()
    REY_Nodes_AddMenuEntry.register()

def unregister():
    print("UnRegistering REY_Nodes")
    REY_Nodes_InstantiateNode.unregister()
    REY_Nodes_Append.unregister()
    REY_Nodes_AddMenuEntry.unregister()

if __name__ == "__main__":
    register()