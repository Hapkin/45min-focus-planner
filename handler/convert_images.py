import xml.etree.ElementTree as ET
import cairosvg
import os
import sys

from configuration import PROJECT_DIR


#path without extension
#size is tuple
def _convert_svg2png(path_SVG,size,different_out=None):
    try:
        if(type(size)==tuple)and(path_SVG[-4:]==".svg"):
            PNG_width=size[0]
            PNG_height=size[1]
        else:
            raise ValueError(f"convert_svg2png::size must be a tuple {size} \nOR\n path is incorrect::{path_SVG[-4:]}")
        
        # Get the width and height attributes of SVG
        tree = ET.parse(path_SVG)
        root = tree.getroot()
        # first remove "mm" => [:-2]
        # convert to float float()
        # convert to int int()
        SVG_width = int(float(root.get('width')[:-2]))
        SVG_height = int(float(root.get('height')[:-2]))
        print(f"SVG x= {SVG_width}:y= {SVG_height}")

        ### Create viewBox: this is to make the SVG large enough to create a good PNG file in return
        #here you chose what is most important width or height comparison;this is using height as difference as most important
        if(PNG_width>SVG_width)and(PNG_height<=SVG_height): 
            aspectratio=(PNG_width/SVG_width)+1  #the +1 I still need to check
        elif(PNG_height>SVG_height):
            aspectratio=(PNG_height/SVG_height)+1  #the +1 I still need to check
        else:
            aspectratio=1
            
        new_SVG_width= SVG_width*aspectratio
        new_SVG_height= SVG_height*aspectratio

        root.set('viewBox',f'0 0 {new_SVG_width} {new_SVG_height}')

        HERE,HERE!



        if(different_out is None):
            #remove .svg add .png
            write_png=f"{path_SVG[:-4]}.png"
        else:
            #remove n*.png but keep the path
            write_png.split("//",-1)
            write_png=f"{path_SVG[:-4]}+{different_out}"

        







        
        #def svg2png(bytestring=None, *, file_obj=None, url=None, dpi=96,
            #parent_width=None, parent_height=None, scale=1, unsafe=False,
            #background_color=None, negate_colors=False, invert_images=False,
            #write_to=None, output_width=None, output_height=None):
        cairosvg.svg2png(url=path_SVG, write_to=write_png, output_width=PNG_width,output_height=PNG_height,dpi=300) #dpi?
        print(f"converted: {path_SVG} :: svg2png || x{PNG_width},y:{PNG_height}")
        return 0
    except Exception as e:
        print(e)



#only this function should be able to recalculate the size of the images
def calculate_newsizes(imagename,size):
    #this is already a change for when it becomse an executable
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = PROJECT_DIR
    
    images_path = os.path.join(application_path, "img", imagename)
    
    #testSVG_path = os.path.join(images_path, )
    
    _convert_svg2png(images_path,size)