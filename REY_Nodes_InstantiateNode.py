import bpy
import REY_Utils

class REY_InstantiateNode(bpy.types.Operator):
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

    def MSG_notShaderEditor(self):
        self.report({'WARNING'}, "[REY_Nodes] Not in Shader Editor!")
    def MSG_notFound_REY_Node(self):
        self.report({'ERROR'}, f"Node group '{self.node_group_name}' not found!")

    def execute(self, context):
        if REY_Utils .isShaderEditor():
            self.MSG_notShaderEditor()
            return {'CANCELLED'}
        
        else:
            # Instantiate The Node
            bpy.ops.node.add_node(type="ShaderNodeGroup", use_transform=True)
            if True:
                NT = context.space_data.edit_tree                       # NodeTree
                NG = bpy.data.node_groups.get(self.node_group_name)     # REY_Node

                if not NG:
                    self.MSG_notFound_REY_Node()
                    return {'CANCELLED'}
                
                node = NT.nodes.active                                  # Node
                node.node_tree = NG                                     # REY_Node -> Node
                node.width     = NG.default_group_node_width            # Width
                    # Yeah, NodeGroup is a type of NodeTree 💁‍♀️
                
            return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
        # https://github.com/blender/blender/blob/4499ae45051c7710f5287717d98fba9fd7d5bc1b/scripts/startup/bl_operators/node.py#L41

def register():
    bpy.utils.register_class(REY_InstantiateNode)

def unregister():
    bpy.utils.unregister_class(REY_InstantiateNode)
