from kivy.clock import Clock

import handler.gui_classes as c

#My_Clock or My_Time
def refresh_layout(my_layout):
    try:
        if(isinstance(my_layout,c.My_Clock)):
            Clock.schedule_once(lambda dt: rebuild_My_Clock(my_layout, True), 1)
        elif(isinstance(my_layout,c.My_Time)):
            Clock.schedule_once(lambda dt: rebuild_My_Time(my_layout, True), 1)
        else:
            raise ValueError(f"layout: {my_layout}")
    except Exception as e:
         print(e)

def rebuild_My_Clock(self, dt):
    pass
    print(f"rebuild_My_Clock: {type(self).__name__}")    
        
def rebuild_My_Time(self, dt):
    pass
    print(f"rebuild_My_Time: {type(self).__name__}")    

        
