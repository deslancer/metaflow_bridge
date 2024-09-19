import os
import threading
import bpy
from ...API.Requests import Requests
from pathlib import Path
from ...UI.PopUp import PopUp
from queue import Queue
import uuid

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
        file_name = scene.file_name or f"temp_${uuid.uuid4().hex}"
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


class TakeScreenshotOperator(bpy.types.Operator):
    """Take a screenshot of View3d to MetaFlow3d  ecosystem"""
    bl_idname = "object.take_a_shot_op"
    bl_label = "Take a screenshot"

    def execute(self, context):
        scene = context.scene
        camera = scene.camera
        user_id = scene.metaflow_user_id
        filepath = os.path.join(current_dir.parents[1], "tmp", f"screenshot_{uuid.uuid4().hex}.png")

        if camera:
            # Set render resolution and other settings
            scene.render.resolution_x = 1024
            scene.render.resolution_y = 1024
            scene.render.filepath = filepath

            # Create a queue to communicate between threads
            render_queue = Queue()

            # Define a function to render the image and notify completion
            def render_and_notify(queue):
                bpy.ops.render.render(write_still=True)
                queue.put(True)  # Signal that rendering is complete

            # Start rendering in a separate thread
            render_thread = threading.Thread(target=render_and_notify, args=(render_queue,))
            render_thread.start()

            # Wait for rendering to complete
            render_thread.join()

            # Once rendering is done, proceed to upload
            if not render_queue.empty():
                with open(filepath, 'rb') as file:
                    try:
                        Requests.upload_draft_img(user_id, file)
                        self.report({'INFO'}, "Image has been uploaded successfully.")
                    except Exception as e:
                        self.report({'ERROR'}, f"Error, Image not uploaded - {e}")
            else:
                self.report({'ERROR'}, "Error rendering the image.")

        else:
            self.report({'WARNING'}, "No active camera found in the scene.")

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
