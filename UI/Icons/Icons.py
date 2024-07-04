import bpy
import bpy.utils.previews
import os
from pathlib import Path

# Global dictionary to hold preview collections
preview_collections = {}


# Register the icon
def register_icon():
    global preview_collections

    import bpy.utils.previews
    pcoll = bpy.utils.previews.new()

    current_dir = Path(__file__).resolve().parent
    root_dir = current_dir.parents[1]

    icons_path = os.path.join(root_dir, "resources", "icons")

    pcoll.load("metaicon", os.path.join(icons_path, "metaicon_32x32.png"), 'IMAGE')
    pcoll.load("login_icon", os.path.join(icons_path, "login.png"), 'IMAGE')
    pcoll.load("logout_icon", os.path.join(icons_path, "logout.png"), 'IMAGE')
    pcoll.load("export_icon", os.path.join(icons_path, "export-variant.png"), 'IMAGE')

    preview_collections["main"] = pcoll


def unregister_icon():
    global preview_collections

    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()
