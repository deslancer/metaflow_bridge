import json
import os

import bpy
from ...UI.Icons import Icons
from pathlib import Path

current_dir = Path(__file__).resolve().parent
creds_file = os.path.join(current_dir.parents[1], "creds", "user_creds.json")


class VE_PT_Panel(bpy.types.Panel):
    bl_label = "Metaflow3d"
    bl_idname = "VE_PT_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Metaflow3d"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        pcoll = Icons.preview_collections["main"]
        layout.scale_y = 1.5
        check_file = os.path.isfile(creds_file)
        if check_file:
            with open(creds_file, 'r') as file:
                creds = json.load(file)
                export_icon = pcoll["export_icon"]
                logout_icon = pcoll["logout_icon"]

                row = layout.row()
                row.label(text=f"Hello, {creds['data']['user_metadata']['user_name']}!")
                layout.separator(factor=1)
                box = layout.box()
                box.label(text="File Name:")
                box.prop(scene, "file_name", text='')
                box.operator("object.export_model_op", text="Export model", icon_value=export_icon.icon_id)
                layout.separator(factor=1)
                row = layout.row()
                row.operator("wm.signout_op", text="Sign Out", icon_value=logout_icon.icon_id)

        else:
            metaflow_icon = pcoll["metaicon"]
            login_icon = pcoll["login_icon"]
            row = layout.row()
            row.label(text="Welcome to Metaflow3D Bridge", icon_value=metaflow_icon.icon_id)
            row = layout.row()
            row.operator("wm.signin_op", text="Sign In", icon_value=login_icon.icon_id)



