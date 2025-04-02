import bpy




# AM = "Add Menu" = SHIFT + A Menu
    
# Function to add our custom menu into the Shader Editor's Add Menu
def AM_DRAW_ENTRY(self, context):
    """
        Yeah, So, This Function is like.... gets called everytime
            -> someone presses SHIFT + A"

        So we must not call any heavy functions / bpy.operators inside this
    """
    self.layout.menu("AM_MT_REY_Nodes")
    
# Class to add a new category to Shift + A
class AM_MT_REY_NODES(bpy.types.Menu):
    """MT probably means MenuType"""
    bl_label = "REY_Nodes"
    bl_idname = "AM_MT_REY_Nodes"

    def draw(self, context):
        layout = self.layout

        # Add your custom node operator to the dropdown
        op = layout.operator("rey.nodes_append", text="Append REY_Nodes")
        op = layout.operator("rey.instantiate_node", text="REY_BumpNormDisp_V1")
        op.node_group_name = "REY_BumpNormDisp_V1"
            # Call the operator with a parameter
            # https://docs.blender.org/api/current/bpy.types.UILayout.html#bpy.types.UILayout.operator





def register():
    bpy.utils.register_class(AM_MT_REY_NODES)
    bpy.types.NODE_MT_add.append(AM_DRAW_ENTRY)  # Add to Shift + A menu
        # SHIFT + A   = "Add Menu"
        # NODE_MT_add = "Add Menu"
        # NODE_MT_add = node.add_menu
        # https://docs.blender.org/api/current/bpy.ops.node.html#bpy.ops.node.add_file

def unregister():
    bpy.types.NODE_MT_add.remove(AM_DRAW_ENTRY)
    bpy.utils.unregister_class(AM_MT_REY_NODES)