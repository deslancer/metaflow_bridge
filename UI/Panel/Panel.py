import bpy


class VE_PT_Panel(bpy.types.Panel):
    bl_label = "Metaflow3d"
    bl_idname = "VE_PT_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Metaflow3d"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        if scene.metaflow_username:
            row = layout.row()
            row.label(text=f"Hello, {scene.metaflow_username}!")
        else:
            row = layout.row()
            row.label(text="Welcome to Metaflow3D Bridge")
            row = layout.row()
            row.operator("wm.veop", text="Sign In", icon="USER")
