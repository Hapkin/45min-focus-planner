import os
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))


#fixed global variables
#will be editable via menu->settings

SIZE_WINDOW_X=300
SIZE_WINDOW_Y=450

#categories:
## work -> programming, actually_@_work
## fun -> friends, sports, ...
## void (empty block for anything outside of normal categories or you forgot what it was?)
## house -> coocking, cleaning, ...
## inner peace -> meditation, reading, ...
class Categories():
    def __init__(self, color, name, list_children=[]):
        self.name= name
        self.color= "#000000"
        if(type(list_children)==list):
            self.children=list_children
        else:
            raise ValueError("")


########body -> My_Clock

#normal layout 8.00 should be point 0 for the first label that is added
#if you start before 8.00 let's say 7.00 the block should be above 8...
CLOCK_START=8 
CLOCK_END=20
#you should be able to go over 20.00 but just the graphic ends there
#12h in total

# zoom is a zoomed in version of the program, to see more details of the last 3 houres +1h in future
CLOCK_ZOOM=4


########body -> My_Time
#12h total/vs 4h ZOOM = 15min*3 (min and hour dont matter; only link between the 2 numbers)
#use with dp but keep as number as you need to calculate the results
SIZE_15MIN=30 
SIZE_15MIN_ZOOM=90

#this is the begin number and should adjust if blocks are added out-bound 
TOTAL_SIZE_MYBODY=400 #still static in the code!
TOTAL_SIZE_PROG=450
#top=30; bottom 20;
#===> ToDo switch the static numbers with these configuration CONSTANTS