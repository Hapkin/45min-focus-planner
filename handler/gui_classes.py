from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.properties import NumericProperty


from configuration import SIZE_WINDOW_Y, SIZE_WINDOW_X
from handler.gui_def import set_property
from handler.gui_all import refresh_layout




# Creating main kv file class
class main_kv(GridLayout):
    def __init__(self, **kwargs):
        super(main_kv, self).__init__(**kwargs)
        self.border_lines = [] 




class Body(GridLayout):
    #height=NumericProperty(0)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.border_lines = []
        # 55 is the size of menu and bottom
        #set_property(self, 'height', SIZE_WINDOW_Y-55)
        #self.height = SIZE_WINDOW_Y - 55
        print(f"Body: initiated height:{self.height}")


class Bottom(BoxLayout):
    #height=NumericProperty(25)
    def __init__(self, **kwargs):
        super(Bottom, self).__init__(**kwargs)
        #set_property(self, 'height', 25)
        print(f"Bottom: initiated height:{self.height}")



class My_Time(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.container = [] => children already exists!
        print("My_Time: initiated")
        self.name="My_Time"
        self.border=(20,20,20,20)
        my_add_button=Button(text="(add +)",size_hint_y=None,height="15dp")
        #my_add_button.on_press = self.add_block_
        my_add_button.bind(on_press=self.add_block_)
        self.add_widget(my_add_button, index=0)
        
    def add_block_(self, instance):
        pass
        print(f"Button: add block is pressed! canvas:{self.name}")
        new_label=Button(text=f"Label{len(self.children)}",size_hint_y=None,height="15dp")
        self.add_widget(new_label, index=1)
        refresh_layout(self)
        
            

class My_Clock(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.container = []     
        print("My_Clock: initiated")
    
    
         