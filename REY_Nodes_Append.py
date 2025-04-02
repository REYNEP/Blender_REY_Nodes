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
        print("")


        global  LOADED_REY_NODES
        print( "    LOADED_REY_NODES:- ", LOADED_REY_NODES )

        if (LOADED_REY_NODES):
            return {'CANCELLED'}
        else:
            BlendFile = os.path.join(os.path.dirname(__file__), "REY_Nodes.blend")

            if (REY_Utils.doesEXIST(BlendFile) == False):     # Automatically Logs if not found
                return {'CANCELLED'}
            
            else:
                print("     REY_Nodes.blend:- ", BlendFile)

                print("")
                print("    Loading/Appending REY_Nodes")
                self._LOAD_REY_NODES_(BlendFile)
                print("    Loaded/Appended   REY_Nodes")
                print("")


        print("[REY_Nodes_Append.py] :: bpy.ops.rey.nodes_append()")
        print("")
        print("")
        return {'FINISHED'}
            
            

    def _LOAD_REY_NODES_(self, BlendFile):
        """Load the node group from an external .blend file into the current Blender session."""
        
        global LOADED_REY_NODES
        NodeGroupNames_List = {"REY_BumpNormDisp_V1"}

        for NGN in NodeGroupNames_List:
            # Check if the node group is already loaded
            if NGN in bpy.data.node_groups:
                print(f"        ✅ Node group '{NGN}' is already loaded.")
                continue
            
            with bpy.data.libraries.load(BlendFile, link=False) as (Source_BlendFile_Data, Dest_BlendFile_Data):
                if NGN in Source_BlendFile_Data.node_groups:
                    Dest_BlendFile_Data.node_groups.append(NGN)
                    print(f"        ✅ Loaded Node Group: {NGN}")
                else:
                    print(f"        ❌ Node group '{NGN}' not found in the file.")
        
        LOADED_REY_NODES = True
        print("        LOADED_REY_NODES:- ", LOADED_REY_NODES)
            

def register():
    bpy.utils.register_class(REY_Nodes_Append)

def unregister():
    bpy.utils.unregister_class(REY_Nodes_Append)