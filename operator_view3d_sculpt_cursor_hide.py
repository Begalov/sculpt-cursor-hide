import bpy

class ViewOperatorSculptCursorHide(bpy.types.Operator):
    """Hide cursor in sculpt mode"""
    bl_idname = "view3d.sculpt_operator_cursor_hide"
    bl_label = "Hide cursor Operator"

    def execute(self, context):
        if context.space_data.type == 'VIEW_3D':
            context.window.cursor_set('NONE')
        return {'FINISHED'}

    def invoke(self, context, event):
        if context.mode == 'SCULPT':# and context.space_data.type == 'VIEW_3D':
            return self.execute(context)


def register():
    bpy.utils.register_class(ViewOperatorSculptCursorHide)


def unregister():
    bpy.utils.unregister_class(ViewOperatorSculptCursorHide)


if __name__ == "__main__":
    register()
