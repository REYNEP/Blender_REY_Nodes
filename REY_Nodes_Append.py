import bpy
import os
from . import REY_Utils

LOADED_REY_NODES : bool = False

class REY_Nodes_Append(bpy.types.Operator):
      # will be added as `bpy.ops.rey.nodes_append()`
    bl_idname  : str = "rey.nodes_append"
    bl_label   : str = "REY_Nodes_Append"
    bl_options : str = {'REGISTER'}



    def execute(self, context):
        print("")
        print("")
        print("[REY_Nodes_Append.py] :: bpy.ops.rey.nodes_append()")

        global  LOADED_REY_NODES
        print( "LOADED_REY_NODES:- ", LOADED_REY_NODES )

        if (LOADED_REY_NODES):
            return {'CANCELLED'}
        else:
            BlendFile = os.path.join(os.path.dirname(__file__), "REY_Nodes.blend")

            if (REY_Utils._doesEXIST_(BlendFile) == False):     # Automatically Logs if not found
                return {'CANCELLED'}
            
            else:
                print(" REY_Nodes.blend:- ", BlendFile)

                print("")
                print("Loading/Appending REY_Nodes")
                self._LOAD_REY_NODES_(BlendFile)
                print("Loaded/Appended   REY_Nodes")
                print("")

                return {'FINISHED'}
            
            

    def _LOAD_REY_NODES_(self, BlendFile):
        """Load the node group from an external .blend file into the current Blender session."""
        
        global LOADED_REY_NODES
        node_group_name = "REY_BumpNormDisp_V1"

        # Check if the node group is already loaded
        if node_group_name in bpy.data.node_groups:
            print(f"✅ Node group '{node_group_name}' is already loaded.")
            
            LOADED_REY_NODES = True
            print("LOADED_REY_NODES:- ", LOADED_REY_NODES)
            return

        with bpy.data.libraries.load(BlendFile, link=False) as (data_from, data_to):
            if node_group_name in data_from.node_groups:
                data_to.node_groups = [node_group_name]
                print(f"✅ Loaded Node Group: {node_group_name}")

                LOADED_REY_NODES = True
                print("LOADED_REY_NODES:- ", LOADED_REY_NODES)
            else:
                print(f"❌ Node group '{node_group_name}' not found in the file.")
            

def register():
    bpy.utils.register_class(REY_Nodes_Append)

def unregister():
    bpy.utils.unregister_class(REY_Nodes_Append)