import bpy


def log_message(message="", level='INFO'):
    bpy.ops.wm.append_error_message(message=message, message_type=level)

