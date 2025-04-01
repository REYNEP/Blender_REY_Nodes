import bpy
import os

class REY_BumpNormDisp_V1(bpy.types.Operator):
      # will be added as `bpy.ops.rey.node1()`
    bl_idname  : str = "rey.ng1"
    bl_label   : str = "Instantiate REY_BumpNormDisp_V1"
    bl_options : str = {'REGISTER', 'UNDO'}

    REY_NG1    : str = "REY_BumpNormDisp_V1"
      # NODE will be imported/loaded/appended by "Append_REY_Nodes.py"

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
                NG1 = bpy.data.node_groups.get(self.REY_NG1)
                
                node.node_tree = NG1
                node.width     = NG1.default_group_node_width
                    # Yeah, NodeGroup is a type of NodeTree 💁‍♀️
                
            return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
        # https://github.com/blender/blender/blob/4499ae45051c7710f5287717d98fba9fd7d5bc1b/scripts/startup/bl_operators/node.py#L41

def register():
    bpy.utils.register_class(REY_BumpNormDisp_V1)

def unregister():
    bpy.utils.unregister_class(REY_BumpNormDisp_V1)
