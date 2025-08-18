### script to test individual functions()
from handler.convert_images import calculate_newsizes
import os
from configuration import PROJECT_DIR


def main():
    imagename="test.svg"
    #size(width,height)
    size=(160,80)
    PROJECT_DIR=os.path.abspath(os.path.dirname(__file__))
    breakpoint()
    calculate_newsizes(imagename,size)



main()