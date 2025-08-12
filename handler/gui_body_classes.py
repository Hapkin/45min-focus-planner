#to create the propper layoutblocks I will need empty wrappers
#adjustability is keen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image


#can be a Label, Button, ....
class Blocks():
    def __init__(self,type, **kwargs):
        if (type==None):
            raise ValueError("No blocks without type allowed!")
        match type:
            case "Button":
                self.my_obj=Button(kwargs)
            case "Label":
                self.my_obj=Label(kwargs)
            case "Image":
                self.my_obj=Image(kwargs)


class TimeBlock(Blocks):
    def __init__(self, **kwargs):
        super(TimeBlock, self).__init__(**kwargs)


class ClockBlock(Blocks):
    def __init__(self, **kwargs):   
        super(ClockBlock, self).__init__(**kwargs)

class WrapperBlock(Blocks):
    def __init__(self, **kwargs):
        super(WrapperBlock, self).__init__(**kwargs)


