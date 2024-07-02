import json
import sys

import bpy
from bpy.props import StringProperty
from ...API.Requests import Requests


class WM_OP_VEDialog(bpy.types.Operator):
    """Open VE Dialog"""
    bl_label = "SignIn in Metaflow3D CMS"
    bl_idname = "wm.veop"

    email: StringProperty(name="Enter your email", default="")
    password: StringProperty(name="Enter your password", subtype="PASSWORD")

    def execute(self, context):
        mail = self.email
        passwd = self.password

        creds = Requests.sign_in(mail, passwd)
        context.scene.metaflow_username = creds["data"]["user_metadata"]["user_name"]

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
