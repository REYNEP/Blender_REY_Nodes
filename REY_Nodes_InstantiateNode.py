import bpy
from . import REY_Utils

class REY_InstantiateNode(bpy.types.Operator):
    """ 
        Adds / Instantiates a REY_Node into the ShaderEditor. 
        This Operator also gets called inside 
            -> REY_Nodes_AddMenuEntry::AM_DRAW_ENTRY::AM_MT_REY_NODES.draw()
    """
      # this function/operator will be added as `bpy.ops.rey.instantiate_node()`
    bl_idname  : str = "rey.instantiate_node"
    bl_label   : str = "Instantiate a REY_Node"
    bl_options : str = {'REGISTER', 'UNDO'}

    # BLENDER OPERATOR/Function arguments (properties)
    node_group_name: bpy.props.StringProperty(      # type: ignore
        name="REY Node Name",                       # https://github.com/microsoft/pylance-release/issues/5457
        description="Name of the REY_Node to Instantiate",
        default="REY_BumpNormDisp_V1"
    )

    def MESSAGE_notShaderEditor(self):
        self.report({'WARNING'}, "[REY_Nodes] Not in Shader Editor!")
    def MESSAGE_notFound_REY_Node(self):
        self.report({'ERROR'}, f"Node group '{self.node_group_name}' not found!")

    def execute(self, context):
        if (not REY_Utils.isShaderEditor(context)):
            self.MESSAGE_notShaderEditor()
            return {'CANCELLED'}

        else:
            NT = context.space_data.edit_tree
            return REY_Utils.add_ShaderNodeGroup(self.node_group_name, NT, self.MESSAGE_notFound_REY_Node)
                # this way you can see/understand various types of functions/stuffs to do with blender python

def register():
    bpy.utils.register_class(REY_InstantiateNode)

def unregister():
    bpy.utils.unregister_class(REY_InstantiateNode)
