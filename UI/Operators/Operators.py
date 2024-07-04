import os

import bpy
from ...API.Requests import Requests
from pathlib import Path
from ...UI.PopUp import PopUp

current_dir = Path(__file__).resolve().parent
creds_file = os.path.join(current_dir.parents[1], "creds", "user_creds.json")


class ExportModelOperator(bpy.types.Operator):
    """Export model to MetaFlow3d  ecosystem"""
    bl_idname = "object.export_model_op"
    bl_label = "Export Model"

    def execute(self, context):
        scene = context.scene

        PopUp.show_message('Export started', 'INFO')

        user_id = scene.metaflow_user_id
        file_name = scene.file_name or "temp"
        filepath = os.path.join(current_dir.parents[1], "tmp", file_name + '.glb')
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.export_scene.gltf(
            export_format='GLB',
            export_draco_mesh_compression_enable=False,
            filepath=str(filepath))

        with open(filepath, 'rb') as file:
            try:
                Requests.upload_model(user_id, file)
                self.report({'INFO'}, "File has been uploaded successfully.")
            except (Exception,):
                self.report({'ERROR'}, "Error, File not uploaded.")
                pass

        os.remove(filepath)

        return {'FINISHED'}


class SignOutOperator(bpy.types.Operator):
    """Sign Out from Metaflow3D"""
    bl_idname = "wm.signout_op"
    bl_label = "Sign Out"

    def execute(self, context):
        is_file_exists = os.path.isfile(creds_file)
        if is_file_exists:
            os.remove(creds_file)

        return {'FINISHED'}
