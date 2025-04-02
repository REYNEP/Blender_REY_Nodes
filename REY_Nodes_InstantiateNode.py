import bpy

class REY_InstantiateNode(bpy.types.Operator):
      # will be added as `bpy.ops.rey.instantiate_node()`
    bl_idname  : str = "rey.instantiate_node"
    bl_label   : str = "Instantiate Node"
    bl_options : str = {'REGISTER', 'UNDO'}

    # BLENDER OPERATOR/Function arguments (properties)
    node_group_name: bpy.props.StringProperty(          # type: ignore
        name="REY Node Name",                           # https://github.com/microsoft/pylance-release/issues/5457
        description="Name of the REY_NodeGroup to Instantiate",
        default="REY_BumpNormDisp_V1"
    )

    def execute(self, context):
        # Are we in the Shader Editor?
        if not context.space_data or context.space_data.tree_type != 'ShaderNodeTree':
            self.report({'WARNING'}, "Not in Shader Editor!")
            return {'CANCELLED'}
        
        else:
            nodeTree = context.space_data.edit_tree
            
            # Instantiate The Node
            bpy.ops.node.add_node(type="ShaderNodeGroup", use_transform=True)
            if True:
                node = nodeTree.nodes.active
                NG = bpy.data.node_groups.get(self.node_group_name)

                if not NG:
                    self.report({'ERROR'}, f"Node group '{self.node_group_name}' not found!")
                    return {'CANCELLED'}
                
                node.node_tree = NG
                node.width     = NG.default_group_node_width
                    # Yeah, NodeGroup is a type of NodeTree 💁‍♀️
                
            return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
        # https://github.com/blender/blender/blob/4499ae45051c7710f5287717d98fba9fd7d5bc1b/scripts/startup/bl_operators/node.py#L41

def register():
    bpy.utils.register_class(REY_InstantiateNode)

def unregister():
    bpy.utils.unregister_class(REY_InstantiateNode)
