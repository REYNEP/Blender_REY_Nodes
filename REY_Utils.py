#   Are we in the ShaderEditor?
def isShaderEditor(context):
    if not context.space_data or context.space_data.tree_type != 'ShaderNodeTree':
        return False
    else:
        return True

import bpy
def add_ShaderNodeGroup():
    bpy.ops.node.add_node(type="ShaderNodeGroup", use_transform=True)

def add_Node_MoveWithMouse():
    return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')


def add_NodeGroup(group_name, pNodeTree, pMSG_notFound):
    # Instantiate The Node
    bpy.ops.node.add_node(type="ShaderNodeGroup", use_transform=True)

    if True:
        NT = pNodeTree                                  # NodeTree
        NG = bpy.data.node_groups.get(group_name)       # REY_Node

        if not NG:
            pMSG_notFound()
            return {'CANCELLED'}
        
        node = NT.nodes.active                          # Node
        node.node_tree = NG                             # REY_Node -> Node
        node.width     = NG.default_group_node_width    # Width
            # Yeah, NodeGroup is a type of NodeTree 💁‍♀️
        
    return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')