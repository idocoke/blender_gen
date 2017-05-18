import bpy
import time
from numpy.random import randint
from numpy.random import uniform
from numpy.random import normal
import math
import bmesh
from mathutils.bvhtree import BVHTree

def checkIntersect(relevant_objects):
    flag = True
    for obj_now in relevant_objects:
        while(flag):
            flag = False
            for obj_next in relevant_objects:
                if obj_now == obj_next:
                    continue
                #create bmesh objects
                bm1 = bmesh.new()
                bm2 = bmesh.new()

                #fill bmesh data from objects
                bm1.from_mesh(obj_now.data)
                bm2.from_mesh(obj_next.data)
                bm1.transform(obj_now.matrix_world)
                bm2.transform(obj_next.matrix_world) 

                #make BVH tree from BMesh of objects
                obj_now_BVHtree = BVHTree.FromBMesh(bm1)
                obj_next_BVHtree = BVHTree.FromBMesh(bm2)           

                #get intersecting pairs
                inter = obj_now_BVHtree.overlap(obj_next_BVHtree)
                #if list is empty, no objects are touching
                if inter != []:
                    f = open('out.txt','a')
                    flag = True
                    randx = uniform(-10,10)
                    randy = uniform(-10,10)
                    obj_now.location.x = 100*randx
                    obj_now.location.y = 100*randy
                    f.write('objects moved: %f %f' % (randx,randy))
                    f.write(obj_now)
                    break
def randomizeObjects():
    max_num = 5
    coke_num = randint(0,max_num)
    banana_num = randint(0,max_num)
    orange_num = randint(0,max_num)
    apple_num = randint(0,max_num)
    
    relevant_objects = []
    object_types = []
    #Shuffle away
    for i in range(0,max_num):
        bpy.data.objects['Cola_Can.00{}'.format(i)].location.x = 50
        bpy.data.objects['Cola_Can.00{}'.format(i)].location.y = 50
        bpy.data.objects['Orange.00{}'.format(i)].location.x = 50
        bpy.data.objects['Orange.00{}'.format(i)].location.y = 50
        bpy.data.objects['Apple.00{}'.format(i)].location.x = 50
        bpy.data.objects['Apple.00{}'.format(i)].location.y = 50
        bpy.data.objects['Banana.00{}'.format(i)].location.x = 50
        bpy.data.objects['Banana.00{}'.format(i)].location.y = 50
    for i in range(0,coke_num):
        randx = randint(-15,15)
        randy = randint(-15,15)
        obj = bpy.data.objects['Cola_Can.00{}'.format(i)]
        obj.location.x = randx
        obj.location.y = randy
        relevant_objects.append(obj)
        object_types.append(0)
    for i in range(0,orange_num):
        randx = randint(-15,15)
        randy = randint(-15,15)
        obj = bpy.data.objects['Orange.00{}'.format(i)]
        obj.location.x = randx
        obj.location.y = randy
        relevant_objects.append(obj)
        object_types.append(1)
    for i in range(0,banana_num):
        randx = randint(-15,15)
        randy = randint(-15,15)
        obj = bpy.data.objects['Banana.00{}'.format(i)]
        obj.location.x = randx
        obj.location.y = randy
        relevant_objects.append(obj)
        object_types.append(2)
    for i in range(0,apple_num):
        randx = randint(-15,15)
        randy = randint(-15,15)
        obj = bpy.data.objects['Apple.00{}'.format(i)]
        obj.location.x = randx
        obj.location.y = randy
        relevant_objects.append(obj)
        object_types.append(3)
    ########################################################################
    for i in range(0,coke_num):
        rot = randint(0,360)
        item = bpy.data.objects['Cola_Can.00{}'.format(i)]
        item.rotation_mode = 'XYZ'
        item.rotation_euler = (math.radians(90),0,math.radians(rot))
    for i in range(0,apple_num):
        rot = randint(0,360)
        item = bpy.data.objects['Apple.00{}'.format(i)]
        item.rotation_mode = 'XYZ'
        item.rotation_euler = (math.radians(255),math.radians(-129),math.radians(rot))
    for i in range(0,coke_num):
        rot = randint(0,360)
        item = bpy.data.objects['Orange.00{}'.format(i)]
        item.rotation_mode = 'XYZ'
        item.rotation_euler = (math.radians(90),math.radians(8),math.radians(rot))
    for i in range(0,coke_num):
        rot = randint(0,360)
        item = bpy.data.objects['Banana.00{}'.format(i)]
        item.rotation_mode = 'XYZ'
        item.rotation_euler = (math.radians(-5),math.radians(2),math.radians(rot))
    ###Check for intersection####
    #f = open('out.txt','a')
    #f.write('Running checkIntersect...')
    #checkIntersect(relevant_objects)
    #flag = checkIntersect(relevant_objects)
    #while flag:
    #    checkIntersect(relevant_objects)

    return relevant_objects,object_types
def randomizeLightning():
    lamp = bpy.data.objects['Lamp']
    lamp.data.energy = uniform(2,5)
    lamp = bpy.data.objects['Lamp.001']
    lamp.data.energy = uniform(2,5)
def randomizeBackground():
    w1 = bpy.data.objects['Plane']
    ind = randint(4,18)
    img = bpy.data.images.load('/home/erik/blender-2.78/textures/Con{}.jpg'.format(ind))
    w1.data.materials[0].texture_slots[0].texture.image = img
    
    w2 = bpy.data.objects['Wall']
    ind = randint(4,18)
    img = bpy.data.images.load('/home/erik/blender-2.78/textures/Con{}.jpg'.format(ind))
    w2.data.materials[0].texture_slots[0].texture.image = img
    
    w3 = bpy.data.objects['Wall.001']
    ind = randint(4,18)
    img = bpy.data.images.load('/home/erik/blender-2.78/textures/Con{}.jpg'.format(ind))
    w3.data.materials[0].texture_slots[0].texture.image = img
    
def randomizeCamera():
    radius = normal(30,5)
    polar = uniform(0,90)
    camera = bpy.data.objects['Camera']
    camera.location.z = math.sin(math.radians(polar))*radius
    camera.location.y = -math.cos(math.radians(polar))*radius
    
    camera.rotation_mode = 'XYZ'
    camera.rotation_euler = (math.radians(normal(90-polar,2)),math.radians(normal(0,2)),math.radians(normal(0,2)))
def annotateImage(path,relevant_objects,object_types):
    #relevant_objects = [bpy.data.objects['Cola_Can'],bpy.data.objects['Cola_Can.005'],bpy.data.objects['Cola_Can.006']]
    for object in relevant_objects:
        object.hide_render = True
    w1 = bpy.data.objects['Plane']
    w2 = bpy.data.objects['Wall']
    w3 = bpy.data.objects['Wall.001']
    w1.hide_render = True
    w2.hide_render = True
    w3.hide_render = True
    
    for i,object in enumerate(relevant_objects):
        object.hide_render = False
        setTexture(object,1)
        bpy.data.scenes['Scene'].render.filepath = "/home/erik/blender-2.78/images/annotated_images/"+path+"_"+"%d_%d" % (i,int(object_types[i]))
        bpy.ops.render.render(write_still=True)
        object_type = object_types[i]+2
        setTexture(object,texture = object_type)
        object.hide_render = True
    
    for object in relevant_objects:
        object.hide_render = False
    w1.hide_render = False
    w2.hide_render = False
    w3.hide_render = False 
def setTexture(object,texture=1):
    if texture==1:
        img = bpy.data.images.load('/home/erik/blender-2.78/textures/green_texture.jpg')
        object.data.materials[0].texture_slots[0].texture.image = img
    if texture==2:
        img = bpy.data.images.load('/home/erik/blender-2.78/models/coke_can_1/Cola_Can_albedo.png')
        object.data.materials[0].texture_slots[0].texture.image = img
    if texture==3:
        img = bpy.data.images.load('/home/erik/blender-2.78/models/orange_1/Color.jpg')
        object.data.materials[0].texture_slots[0].texture.image = img
    if texture==4:
        img = bpy.data.images.load('/home/erik/blender-2.78/models/banana_1/banana texture.png')
        object.data.materials[0].texture_slots[0].texture.image = img
    if texture==5:
        img = bpy.data.images.load('/home/erik/blender-2.78/models/apple_1/TEKSTURA/Fruit.jpg')
        object.data.materials[0].texture_slots[0].texture.image = img
        
    #cTex = bpy.data.textures.new('Green',type='IMAGE')
    #cTex.image = img
    #Create material to hold texture
    #mat = bpy.data.materials.new('TexMat')
    #
    #mtex = mat.texture_slots.add()
    #mtex.texture = cTex
    #object.data.materials.append(mtex)
    
def makeMaterial(name,diffuse,specular,alpha):
    mat = bpy.data.materials.new(name)
    #mat.diffuse_color = diffuse
    #mat.diffuse_shader = 'LAMBERT' 
    #mat.diffuse_intensity = 1.0 
    #mat.specular_color = specular
    #mat.specular_shader = 'COOKTORR'
    #mat.specular_intensity = 0.5
    #mat.alpha = alpha
    #mat.ambient = 1
    #return mat
def setMaterial(ob, mat):
    me = ob.data
    me.materials.append(mat)

def generateAnnotations():
    pass
    #red = makeMaterial('red',(1,0,0),(1,1,1),1)
    #cube = bpy.data.objects['Cube']
    #setMaterial(cube,red)
def generateAnnotatedData(suite_nbr = 1):
    if suite_nbr == 1:
        generateImages()
    else:
        pass
def takeImage(img_nbr):
    bpy.data.scenes['Scene'].render.filepath = '/home/erik/blender-2.78/images/'+'seq1'+str(img_nbr)
    bpy.ops.render.render(write_still=True)
    
#lamp_object.select = True
#scene.objects.active = lamp_object -> it is now the active object
#generateImages()
#suite_nbr = 1
#generateAnnotatedData(suite_nbr)
num_images = 12
img_per_scene = 3.0

f = open('images/raw_images/inx.txt','r')
startindx = int(f.readline())
#startindx = 0
f.close()

for i in range(0,int(num_images/img_per_scene)):
    #Randomize scene
    relevant_objects,object_types = randomizeObjects()
    randomizeLightning()
    randomizeBackground()
    for j in range(0,int(img_per_scene)):
        randomizeCamera()
        img_indx = i*int(img_per_scene)+ j + startindx
        bpy.data.scenes['Scene'].render.filepath = "/home/erik/blender-2.78/images/raw_images/scene_varied_%d" % img_indx
        bpy.ops.render.render(write_still=True)
        annotateImage("scene_varied_%d" % img_indx,relevant_objects,object_types)
f = open('images/raw_images/inx.txt','w')
f.write(str(startindx+num_images))
f.close()
#randomizeImage()
