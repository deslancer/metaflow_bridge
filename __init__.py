from bpy.props import StringProperty

bl_info = {
    "name": "MetaFlow3D Bridge",
    "author": "deslancer",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "description": "Bridge between Blender and MetaFlow3D for seamless data exchange.",
    "warning": "",
    "doc_url": "",
    "category": "Import-Export",
}

import sys
import bpy

sys.path.insert(0, '/UI/Panel')
sys.path.insert(0, '/UI/Dialog')
sys.path.insert(0, '/API')

from .UI.Panel import Panel
from .UI.Dialog import Dialog


def register():
    bpy.utils.register_class(Panel.VE_PT_Panel)
    bpy.utils.register_class(Dialog.WM_OP_VEDialog)
    bpy.types.Scene.metaflow_username = StringProperty(name="Username", default="")


def unregister():
    bpy.utils.unregister_class(Panel.VE_PT_Panel)
    bpy.utils.unregister_class(Dialog.WM_OP_VEDialog)
    del bpy.types.Scene.metaflow_username


if __name__ == "__main__":
    register()
