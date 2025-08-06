import kivy 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
# The GridLayout arranges children in a matrix.
# It takes the available space and divides
# it into columns and rows, then adds
# widgets to the resulting “cells”.


# Builder is a global Kivy instance used
# in widgets that you can use to load other
# kv files in addition to the default ones.
from view.borders import toggle_borders


# Loading Multiple .kv files 
Builder.load_file('view/menu.kv')
Builder.load_file('view/body.kv')
Builder.load_file('view/bottom.kv')
Builder.load_file('view/_main.kv')

# Creating main kv file class
class main_kv(GridLayout):
    def __init__(self, **kwargs):
        super(main_kv, self).__init__(**kwargs)
        toggle_borders(self, True)  # show borders for testing



# Create App class
class MainApp(App):
    def build(self):
        self.x = 150
        self.y = 400
        return main_kv()
    def on_exit(self):
        print("clean exit.")
        self.stop()


# run the App.
if __name__=='__main__':
    MainApp().run()