from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

#from handler.my_time import add_block



# Creating main kv file class
class main_kv(GridLayout):
    def __init__(self, **kwargs):
        super(main_kv, self).__init__(**kwargs)
        self.border_lines = []     

class Body(GridLayout):
    def __init__(self, **kwargs):
        super(Body, self).__init__(**kwargs)
        self.border_lines = []     
        print("Body: initiated")

class My_Time(BoxLayout):
    def __init__(self, **kwargs):
        super(My_Time, self).__init__(**kwargs)
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
        
        
        

'''            
            Button:
            text: "(add +)"
            size_hint_y: None
            height: "10dp"
            on_press: "..handler.my_time.add_block(self)"  
'''
            

class My_Clock(BoxLayout):
    def __init__(self, **kwargs):
        super(My_Clock, self).__init__(**kwargs)
        self.container = []     
        print("My_Clock: initiated")     