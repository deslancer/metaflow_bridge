import json
import sys

import bpy
from bpy.props import StringProperty
from ...API.Requests import Requests


class WM_OP_VEDialog(bpy.types.Operator):
    """Sign In in Metaflow3D CMS"""
    bl_label = "Sign In in Metaflow3D CMS"
    bl_idname = "wm.signin_op"

    email: StringProperty(name="Email:", default="")
    password: StringProperty(name="Password:", subtype="PASSWORD")

    def execute(self, context):
        mail = self.email
        passwd = self.password

        creds = Requests.sign_in(mail, passwd)
        context.scene.metaflow_user_name = creds["data"]['user_metadata']['user_name']
        context.scene.metaflow_user_id = creds["data"]['id']

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
