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
            # Instantiate The Node
            bpy.ops.node.add_node(type="ShaderNodeGroup", use_transform=True)
                # https://github.com/blender/blender/blob/4499ae45051c7710f5287717d98fba9fd7d5bc1b/scripts/startup/bl_operators/node.py#L41

            if True:
                NT = context.space_data.edit_tree               # NodeTree
                NGN = self.node_group_name                      # REY_NodeName
                NG = bpy.data.node_groups.get(NGN)              # REY_Node

                if not NG:
                    bpy.ops.rey.nodes_append()
                    NG = bpy.data.node_groups.get(NGN)          # REY_Node

                if not NG:
                    self.MESSAGE_notFound_REY_Node()
                    return {'CANCELLED'}
                
                node = NT.nodes.active                          # Node
                node.node_tree = NG                             # REY_Node -> Node
                node.width     = NG.default_group_node_width    # Width
                    # Yeah, NodeGroup is a type of NodeTree 💁‍♀️
                
            return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')

def register():
    bpy.utils.register_class(REY_InstantiateNode)

def unregister():
    bpy.utils.unregister_class(REY_InstantiateNode)
