#----------------------------------------------------------
# File meshes.py
#----------------------------------------------------------
import bpy

def createMesh(name, origin, verts, edges, faces):
    # Create mesh and object
    me = bpy.data.meshes.new(name+'Mesh')
    ob = bpy.data.objects.new(name, me)
    ob.location = origin
    ob.show_name = True
    # Link object to scene
    bpy.context.scene.objects.link(ob)

    # Create mesh from given verts, edges, faces. Either edges or
    # faces should be []
    me.from_pydata(verts, edges, faces)

    # Update mesh with new data
    me.update(calc_edges=True)
    return ob

def run(origin):
    (x,y,z) = (0.707107, 0.258819, 0.965926)
    verts1 = ((x,x,-1), (x,-x,-1), (-x,-x,-1), (-x,x,-1), (0,0,1))
    faces1 = ((1,0,4), (4,2,1), (4,3,2), (4,0,3), (0,1,2,3))
    ob1 = createMesh('Solid', origin, verts1, [], faces1)
    verts2 = ((x,x,0), (y,-z,0), (-z,y,0))
    edges2 = ((1,0), (1,2), (2,0))
    ob2 = createMesh('Edgy', origin, verts2, edges2, [])

    # Move second object out of the way
    ob1.select = False
    ob2.select = True
    bpy.ops.transform.translate(value=(0,2,0))
    return

if __name__ == "__main__":
    run((0,0,0))
