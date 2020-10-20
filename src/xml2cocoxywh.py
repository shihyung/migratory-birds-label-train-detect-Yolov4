import glob
import os
import shutil
import xml.etree.ElementTree as ET

if os.path.exists('labels'):
    shutil.rmtree('labels')
os.makedirs('labels')

flist=glob.glob('annotations/*.xml')
for fxml in flist:
    xmltree=ET.parse(fxml).getroot()
    fname=xmltree.find('filename').text
    width=xmltree.find('size').find('width').text
    height=xmltree.find('size').find('height').text
    for ETobj in xmltree.findall('object'):
        if not ETobj.find('bndbox'):
            with open('labels/'+fname[:-4]+'.txt','a') as fout:
                pass
            fout.close()
            continue
        bbox_x1=ETobj.find('bndbox').find('xmin').text
        bbox_y1=ETobj.find('bndbox').find('ymin').text
        bbox_x2=ETobj.find('bndbox').find('xmax').text
        bbox_y2=ETobj.find('bndbox').find('ymax').text

        bbox_cx=(int(bbox_x1)+int(bbox_x2))/2./float(width)
        bbox_cy=(int(bbox_y1)+int(bbox_y2))/2./float(height)
        bbox_w=(int(bbox_x2)-int(bbox_x1))/float(width)
        bbox_h=(int(bbox_y2)-int(bbox_y1))/float(height)

        with open('labels/'+fname[:-4]+'.txt','a') as fout:
            fout.write('0 {} {} {} {}\n'.format(bbox_cx,bbox_cy,bbox_w,bbox_h))
        fout.close()