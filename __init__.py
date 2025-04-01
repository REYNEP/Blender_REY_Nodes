bl_info = {
    "name": "REY Nodes V0.1",
    "author": "REYNEP",
    "blender": (4, 0, 0),
    "category": "Node"
}

import bpy
import os

print("")
print("")
print("Loading & Registering REY_Nodes")

def load_rey_node_groups():
    """Load the node group from an external .blend file into the current Blender session."""
    print("")
    print("REY_Nodes")
    print(os.path.dirname(__file__))
    blend_file_path = os.path.join(os.path.dirname(__file__), "REY_Nodes.blend")
    
    if not os.path.exists(blend_file_path):
        print(f"❌ File not found: {blend_file_path}")
        return

    node_group_name = "REY_BumpNormDisp_V1"

    # Check if the node group is already loaded
    if node_group_name in bpy.data.node_groups:
        print(f"✅ Node group '{node_group_name}' is already loaded.")
        return

    with bpy.data.libraries.load(blend_file_path, link=False) as (data_from, data_to):
        if node_group_name in data_from.node_groups:
            data_to.node_groups = [node_group_name]
            print(f"✅ Loaded Node Group: {node_group_name}")
        else:
            print(f"❌ Node group '{node_group_name}' not found in the file.")
    print("")

class REY_BumpNormDisp_V1(bpy.types.Operator):
    bl_idname = "rey.node1"
    bl_label = "Add REY_BumpNormDisp_V1"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        nodeTree = context.space_data.edit_tree
        
        # Ensure we are in the Shader Editor
        if not context.space_data or context.space_data.tree_type != 'ShaderNodeTree':
            self.report({'WARNING'}, "Not in Shader Editor!")
            return {'CANCELLED'}
        
        # Add Noise Texture node
        bpy.ops.node.add_node(type="ShaderNodeGroup", use_transform=True)
        if True:
            node = nodeTree.nodes.active
            temp_name = bpy.data.node_groups.get("REY_BumpNormDisp_V1")
            
            node.node_tree = temp_name
            node.width     = temp_name.default_group_node_width
            
        return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
    # https://github.com/blender/blender/blob/4499ae45051c7710f5287717d98fba9fd7d5bc1b/scripts/startup/bl_operators/node.py#L41






# AM = "Add Menu" = SHIFT + A Menu
    
# Function to add our custom menu into the Shader Editor's Add Menu
def AM_ENTRY(self, context):
    self.layout.menu("AM_MT_REY_Nodes")
    # Ensure the node group is loaded
    load_rey_node_groups()
    
# Class to add a new category to Shift + A
class AM_MT_REY_NODES(bpy.types.Menu):
    bl_label = "REY_Nodes"
    bl_idname = "AM_MT_REY_Nodes"

    def draw(self, context):
        layout = self.layout
        # Add your custom node operator to the dropdown
        layout.operator(REY_BumpNormDisp_V1.bl_idname, text="REY_BumpNormDisp_V1")







def register():
    bpy.utils.register_class(REY_BumpNormDisp_V1)
    bpy.utils.register_class(AM_MT_REY_NODES)
    bpy.types.NODE_MT_add.append(AM_ENTRY)  # Add to Shift + A menu
        # SHIFT + A   = "Add Menu"
        # NODE_MT_add = "Add Menu"
        # NODE_MT_add = node.add_menu
        # https://docs.blender.org/api/current/bpy.ops.node.html#bpy.ops.node.add_file

def unregister():
    bpy.types.NODE_MT_add.remove(AM_ENTRY)
    bpy.utils.unregister_class(AM_MT_REY_NODES)
    bpy.utils.unregister_class(REY_BumpNormDisp_V1)

if __name__ == "__main__":
    register()


print("Loaded  & Registered REY_Nodes")
print("")
print("")