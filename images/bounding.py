import os
from skimage import io
import xml.etree.cElementTree as ET

lookup = ['cola_can','orange','banana','apple']
num_objects = len(lookup)

def displayImg(image,ub,lb,hb,vb):
	for i in range(ub,lb):
		image[i][hb] = [255,255,255,255]
		image[i][vb] = [255,255,255,255]
	for j in range(hb,vb):
		image[ub][j] = [255,255,255,255]
		image[lb][j] = [255,255,255,255]
	io.imshow(image)
	io.show()
	#io.imsave('test.png',image)

def obtainBox(image,xml):
	#First threshold
	
	w = len(image[0])
	h = len(image) #Verified to be correct

	found = False
	for i in range(0,h):
		for j in range(0,w):
			if image[i][j][1] > 80:
				image[i][j] = [0,255,0,255]
				found = True
			else:
				image[i][j] = [0,0,0,255]
	if found!=True:
		return ((0,0,0,0),found)	

	ub,lb,hb,vb = (0,0,0,0)
	flag = False
	for i in range(0,h):
		if flag:
			flag = False
			break
		else:
			for j in range(0,w):
				if image[i][j][1] == 255:
					ub = i
					flag = True
	for i in range(h-1,-1,-1):
		if flag:
			flag = False
			break
		else:
			for j in range(0,w):
				if image[i][j][1] == 255:
					lb = i
					flag = True
	for i in range(0,w):
		if flag:
			flag = False
			break
		else:
			for j in range(0,h):
				if image[j][i][1] == 255:
					vb = i
					flag = True
	for i in range(w-1,-1,-1):
		if flag:
			flag = False
			break
		else:
			for j in range(0,h):
				if image[j][i][1] == 255:
					hb = i
					flag = True
	#Basic sanity check
	try:
		assert ub < lb
		assert vb < hb
		assert (lb-ub)<250
		assert (hb-vb)<250
	except:
		displayImg(image,ub,lb,hb,vb)
	
	#Now add data to this...
	return ((ub,lb,hb,vb),found)
def writeXML(box,xml,objstr):
	ub,lb,hb,vb = box
	obj = ET.SubElement(xml,'object')
	ET.SubElement(obj,'name').text = objstr
	ET.SubElement(obj,'pose').text = 'left'
	ET.SubElement(obj,'truncated').text = '%d' % 1 
	ET.SubElement(obj,'difficult').text = '%d' % 0

	bndbox = ET.SubElement(obj,'bndbox')
	ET.SubElement(bndbox,'xmin').text = '%d' % (vb+1) #Make indices 1-based for Pascal-format
	ET.SubElement(bndbox,'ymin').text = '%d' % (ub+1)
	ET.SubElement(bndbox,'xmax').text = '%d' % (hb+1)
	ET.SubElement(bndbox,'ymax').text = '%d' % (lb+1)
	return xml

img = os.listdir('raw_images')
for i,im in enumerate(img):
	#Initiate the resulting xml file
	xml = ET.Element('annotation')
	ET.SubElement(xml,'folder').text = 'OAK2017'
	ET.SubElement(xml,'filename').text = im

	source = ET.SubElement(xml,'source')
	ET.SubElement(source,'database').text = 'The OAK2017 Database'
	ET.SubElement(source,'annotation').text = 'ERIK OAK2017'

	ET.SubElement(xml,'owner').text = 'Erik Ryden'

	size = ET.SubElement(xml,'size')
	ET.SubElement(xml,'segmented').text = '%d' % 0	

	ET.SubElement(size,'width').text = '%d' % 960 #Make general later
	ET.SubElement(size,'height').text = '%d' % 540 #Make general later
	ET.SubElement(size,'depth').text = '%d' % 3 #Make general later

	imginfo = im.split('.')
	prefix = imginfo[0]
	indx = prefix.split('_')[2]
	thres_images = []
	for annot in os.listdir('annotated_images'):
		info = annot.split('_')
		if info[2] != indx:
			continue
		else:
			thres_images.append(annot)

	for path in thres_images:
		info = path.split('_')
		try:
			annot = io.imread('annotated_images/'+path)
		except:
			print 'Some error loading annotation set!'
		box,flag = obtainBox(annot,size)
		print box
		if flag:
			xml = writeXML(box,xml,lookup[int(info[4].split('.')[0])])
			print path
			print info
			print info[4]
			print info[4].split('.')
			print lookup[int(info[4].split('.')[0])]
		else:
			continue
	tree = ET.ElementTree(xml)
	tree.write("xml_out/"+prefix+'.xml')
