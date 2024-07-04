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

import bpy

from .UI.Panel import Panel
from .UI.Dialog import Dialog
from .UI.Icons import Icons
from .UI.Operators import Operators
from bpy.props import StringProperty


def register():
    bpy.utils.register_class(Panel.VE_PT_Panel)
    bpy.utils.register_class(Dialog.WM_OP_VEDialog)
    bpy.utils.register_class(Operators.ExportModelOperator)
    bpy.utils.register_class(Operators.SignOutOperator)
    bpy.types.Scene.metaflow_user_name = StringProperty(name="Username", default="")
    bpy.types.Scene.metaflow_user_id = StringProperty(name="UserID", default="")
    bpy.types.Scene.file_name = bpy.props.StringProperty(name="FileName", default="")
    Icons.register_icon()


def unregister():
    bpy.utils.unregister_class(Panel.VE_PT_Panel)
    bpy.utils.unregister_class(Dialog.WM_OP_VEDialog)
    bpy.utils.unregister_class(Operators.ExportModelOperator)
    bpy.utils.unregister_class(Operators.SignOutOperator)
    del bpy.types.Scene.metaflow_user_name
    del bpy.types.Scene.metaflow_user_id
    del bpy.types.Scene.file_name
    Icons.unregister_icon()


if __name__ == "__main__":
    register()
