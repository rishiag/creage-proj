"""Program: mesh_sf.py
Author: Rishi Agarwal
Last Date Modified: 1/8/2013

The purpose of this program is to generate a simple star fort island.
Example island is this: http://commons.wikimedia.org/wiki/File:Neuf_Brisach.jpg"""
import bpy
from math import *

def createMesh(name, origin, verts, edges, faces):
    # Create mesh and object
    me = bpy.data.meshes.new(name+'Mesh')
    ob = bpy.data.objects.new(name, me)
    #ob.location = origin
    ob.show_name = True
    # Link object to scene
    bpy.context.scene.objects.link(ob)

    # Create mesh from given verts, edges, faces. Either edges or
    # faces should be []
    me.from_pydata(verts, edges, faces)

    # Update mesh with new data
    #me.update(calc_edges=True)
    return ob

def run(origin):
    (x,y,z) = (0.707107, 0.258819, 0.965926)
    verts1 = ((x,x,-1), (x,-x,-1), (-x,-x,-1), (-x,x,-1), (0,0,1))
    faces1 = ((1,0,4), (4,2,1), (4,3,2), (4,0,3), (0,1,2,3))
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

def outerwall(origin):
    cor=8.2
    cir=cor-0.2
    sor=7.2
    sir=sor-0.2
    sp16=sin(pi/16)
    cp16=cos(pi/16) 
    x=8
    crb=[[0,0,0]]
    for n in range(0,32):
        #print "check"
        if (n%2==0):
            crb.append([cor*sin((pi*n)/16),cor*cos((pi*n)/16),0])
        elif (n%2==1):
            crb.append([sor*sin((pi*n)/16),sor*cos((pi*n)/16),0])
    for n in range(0,32):
        #print "check"
        if (n%2==0):
            crb.append([cor*sin((pi*n)/16),cor*cos((pi*n)/16),1])
        elif (n%2==1):
            crb.append([sor*sin((pi*n)/16),sor*cos((pi*n)/16),1])
    for n in range(0,32):
        #print "check"
        if (n%2==0):
            crb.append([cir*sin((pi*n)/16),cir*cos((pi*n)/16),0])
        elif (n%2==1):
            crb.append([sir*sin((pi*n)/16),sir*cos((pi*n)/16),0])
    for n in range(0,32):
        #print "check"
        if (n%2==0):
            crb.append([cir*sin((pi*n)/16),cir*cos((pi*n)/16),1])
        elif (n%2==1):
            crb.append([sir*sin((pi*n)/16),sir*cos((pi*n)/16),1])
    faces=[]

    for n in range(1,32):
        faces.append([n,n+1,n+33,n+32])
    faces.append([32,1,33,64])
    for n in range(1,32):
        faces.append([n+64,n+65,n+97,n+96])
    faces.append([96,65,97,128])
    for n in range(1,32):
        faces.append([n,n+1,n+65,n+64])
    faces.append([32,1,96,65])
    for n in range(1,32):
        faces.append([n+32,n+33,n+97,n+96])
    faces.append([64,33,97,128])

    #for index, item in enumerate(faces):
    #    print index, item
    ob1 = createMesh('Solid', origin, crb, [], faces)
    return

def courtyard(origin):
    #courtyard outer radius
    cor = 4
    #courtyard inner radius
    cir= 3.8
    sp8=sin(pi/8)
    cp8=cos(pi/8) 
    x=8
    #courtyard boundary. first 8 points are outer side base, next 8 are outer side top, next 8 are inner side base, next 8 are inner side top 
    crb = ((0,0,0),(cor*sp8,cor*cp8,0),(cor*cp8,cor*sp8,0),(cor*cp8,-cor*sp8,0),(cor*sp8,-cor*cp8,0),(-cor*sp8,-cor*cp8,0),(-cor*cp8,-cor*sp8,0),(-cor*cp8,-cor*sp8,0),(-cor*sp8,cor*cp8,0),
        (cor*sp8,cor*cp8,1),(cor*cp8,cor*sp8,1),(cor*cp8,-cor*sp8,1),(cor*sp8,-cor*cp8,1),(-cor*sp8,-cor*cp8,1),(-cor*cp8,-cor*sp8,1),(-cor*cp8,-cor*sp8,1),(-cor*sp8,cor*cp8,1),
        (cir*sp8,cir*cp8,0),(cir*cp8,cir*sp8,0),(cir*cp8,-cir*sp8,0),(cir*sp8,-cir*cp8,0),(-cir*sp8,-cir*cp8,0),(-cir*cp8,-cir*sp8,0),(-cir*cp8,-cir*sp8,0),(-cir*sp8,cir*cp8,0),
        (cir*sp8,cir*cp8,1),(cir*cp8,cir*sp8,1),(cir*cp8,-cir*sp8,1),(cir*sp8,-cir*cp8,1),(-cir*sp8,-cir*cp8,1),(-cir*cp8,-cir*sp8,1),(-cir*cp8,-cir*sp8,1),(-cir*sp8,cir*cp8,1))
    faces =  ((1,2,10,9),(2,3,11,10),(3,4,12,11),(4,5,13,12),(5,6,14,13),(6,7,15,14),(7,8,16,15), (8,1,9,16),
        (1+x,2+x,10+x,9+x),(2+x,3+x,11+x,10+x),(3+x,4+x,12+x,11+x),(4+x,5+x,13+x,12+x),(5+x,6+x,14+x,13+x),(6+x,7+x,15+x,14+x),(7+x,8+x,16+x,15+x),(8+x,1+x,9+x,16+x),
        (1,2,18,17),(2,3,19,18),(3,4,20,19),(4,5,21,20),(5,6,22,21),(6,7,23,22),(7,8,24,23),(8,1,17,24),
        (1+x,2+x,18+x,17+x),(2+x,3+x,19+x,18+x),(3+x,4+x,20+x,19+x),(4+x,5+x,21+x,20+x),(5+x,6+x,22+x,21+x),(6+x,7+x,23+x,22+x),(7+x,8+x,24+x,23+x),(8+x,1+x,17+x,24+x))
    ob1 = createMesh('Solid', origin, crb, [], faces)
    return

def innerwall(origin):
    cor = 6
    #innerwall inner radius
    cir= 5.8
    sp8=sin(pi/8)
    cp8=cos(pi/8) 
    x=8
    #innerwall boundary. first 8 points are outer side base, next 8 are outer side top, next 8 are inner side base, next 8 are inner side top 
    crb = ((0,0,0),(cor*sp8,cor*cp8,0),(cor*cp8,cor*sp8,0),(cor*cp8,-cor*sp8,0),(cor*sp8,-cor*cp8,0),(-cor*sp8,-cor*cp8,0),(-cor*cp8,-cor*sp8,0),(-cor*cp8,-cor*sp8,0),(-cor*sp8,cor*cp8,0),
        (cor*sp8,cor*cp8,1),(cor*cp8,cor*sp8,1),(cor*cp8,-cor*sp8,1),(cor*sp8,-cor*cp8,1),(-cor*sp8,-cor*cp8,1),(-cor*cp8,-cor*sp8,1),(-cor*cp8,-cor*sp8,1),(-cor*sp8,cor*cp8,1),
        (cir*sp8,cir*cp8,0),(cir*cp8,cir*sp8,0),(cir*cp8,-cir*sp8,0),(cir*sp8,-cir*cp8,0),(-cir*sp8,-cir*cp8,0),(-cir*cp8,-cir*sp8,0),(-cir*cp8,-cir*sp8,0),(-cir*sp8,cir*cp8,0),
        (cir*sp8,cir*cp8,1),(cir*cp8,cir*sp8,1),(cir*cp8,-cir*sp8,1),(cir*sp8,-cir*cp8,1),(-cir*sp8,-cir*cp8,1),(-cir*cp8,-cir*sp8,1),(-cir*cp8,-cir*sp8,1),(-cir*sp8,cir*cp8,1))
    faces =  ((1,2,10,9),(2,3,11,10),(3,4,12,11),(4,5,13,12),(5,6,14,13),(6,7,15,14),(7,8,16,15), (8,1,9,16),
        (1+x,2+x,10+x,9+x),(2+x,3+x,11+x,10+x),(3+x,4+x,12+x,11+x),(4+x,5+x,13+x,12+x),(5+x,6+x,14+x,13+x),(6+x,7+x,15+x,14+x),(7+x,8+x,16+x,15+x),(8+x,1+x,9+x,16+x),
        (1,2,18,17),(2,3,19,18),(3,4,20,19),(4,5,21,20),(5,6,22,21),(6,7,23,22),(7,8,24,23),(8,1,17,24),
        (1+x,2+x,18+x,17+x),(2+x,3+x,19+x,18+x),(3+x,4+x,20+x,19+x),(4+x,5+x,21+x,20+x),(5+x,6+x,22+x,21+x),(6+x,7+x,23+x,22+x),(7+x,8+x,24+x,23+x),(8+x,1+x,17+x,24+x))
    ob1 = createMesh('Solid', origin, crb, [], faces)
    return

def base(origin):
    side=8
    verts=[[0,0,0],[side,side,0],[side,-side,0],[-side,-side,0],[-side,side,0],[side,side,-0.2],[side,-side,-0.2],[-side,-side,-0.2],[-side,side,-0.2]]
    faces=[[1,2,3,4],[5,6,7,8],[1,2,6,5],[2,3,7,6],[3,4,8,7],[4,1,5,8]]
    ob1 = createMesh('Solid', origin, verts, [], faces)
    return


if __name__ == "__main__":
    bpy.ops.screen.new()
    bpy.ops.object.delete(use_global=False)
    #run((0,0,0))
    courtyard((0,0,0))
    innerwall((0,0,0))
    base((0,0,0))
    outerwall((0,0,0))
