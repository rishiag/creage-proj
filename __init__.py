from . import islandGenerator

bl_info = {
    "name": "Island Generator",
    "author": "Multiple Authors",
    "version": (0, 1),
    "blender": (2, 6, 0),
    "location": "Not Decided",
    "description": "Procedural generation of Bora Bora Island",
    "warning": "",
    "wiki_url": "To be announced",
    "tracker_url": "To be announced",
    "category": "Meshes"}
  
#imports
import bpy

# Register all operators and panels
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
