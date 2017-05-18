import bpy

def generateRawImages():
	scene = bpy.context.scene
	n = 5 #Num coke-cans Name of original object: Cola-can
	for i in range(0,n):
		coke_can_new = bpy.context.active_object.copy() # Or change to whatever the name of cola_can is
		scene.objects.link(bpy.context.active_object.copy())
		coke_can.location = (0,0,0)#(x,y,z)-coordinates
	#Get camera
	
	#Initiate cam somewhere
	m = 5
	cam = bpy.data.objects['Camera']
	bpy.context.scene.objects.active = cam
	for i in range(0,n):
		#Translate camera, render, save
		pass
		#Another thing we can use: bpy.ops.transform.translate(value=(x,y,z))

def generateImages():
	w = 18
	h = 8

    #Select camera as active object
	cam = bpy.data.objects['Camera']
	bpy.context.scene.objects.active = cam
	for i in range(0,h):
            bpy.ops.transform.translate(value=(-18,0,0))
            bpy.ops.transform.translate(value=(0,-1,0))
            for j in range(0,w):
                bpy.ops.transform.translate(value=(1,0,0))
                try:
                    bpy.data.scenes['Scene'].render.filepath = "/home/erik/blender-2.78/images/raw_images/scene_3_%d_%d" % (i,j)
                    bpy.ops.render.render(write_still=True)
                except:
                    print('Some kind of error')
                annotateImage('scene_3_%d_%d' % (i,j))
def annotateImage(path):
    print(path)
    #f = open('/home/erik/blender-2.78/images/annotated_images/'+path,'w')
    #f.write(path)
    quit()
    
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
suite_nbr = 1
generateAnnotatedData(suite_nbr)