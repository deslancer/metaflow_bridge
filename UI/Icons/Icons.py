import os

import bpy

preview_collections = {}


def register_icon():
    # Define the path to your icon file
    icon_path = os.path.join(os.path.dirname(__file__), "my_icon.png")  # Adjust path as necessary

    # Load the icon
    bpy.types.Scene.metaflow_icon = bpy.props.PointerProperty(
        type=bpy.types.ImagePreview
    )

    pcoll = bpy.utils.previews.new()
    pcoll.load("metaflow_icon", icon_path, 'IMAGE')
    preview_collections["metaflow_icon"] = pcoll
    bpy.types.Scene.metaflow_icon = pcoll


# Unregister the icon
def unregister_icon():
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()
