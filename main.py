import kivy 
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window

import configuration as c
from handler.gui_classes import main_kv
from handler.gui_def import toggle_borders, my_callback


# Loading Multiple .kv files 
Builder.load_file('view/menu.kv')
Builder.load_file('view/body.kv')
Builder.load_file('view/bottom.kv')
Builder.load_file('view/_main.kv')


Window.size = (c.SIZE_WINDOW_X,c.SIZE_WINDOW_Y)


# Create App class
class MainApp(App):
    def build(self):
        layout=main_kv()
        Clock.schedule_once(lambda dt: toggle_borders(layout, True), 1)
        Clock.schedule_interval(lambda dt:my_callback(layout), 60)
        return layout
    
    def on_exit(self):
        print("clean exit.")
        self.stop()


# run the App.
if __name__=='__main__':
    MainApp().run()