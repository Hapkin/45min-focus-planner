import kivy as k
from kivy.uix.widget import Widget

def toggle_borders(obj, enable):
        obj.canvas.clear()
        print(type(obj))
        mine=Widget()
        mine.canvas
        if enable:
            with obj.canvas.after:
                for i in range(obj.rows):
                    Color(0, 0, 1)  
                    # Black color for the border
                    # Top border
                    Line(points=[obj.x, obj.y + (i * 40), obj.x + obj.width, obj.y + (i * 40)], width=2)
                    # Left border
                    Line(points=[obj.x, obj.y + (i * 40), obj.x, obj.y + (i * 40 + 40)], width=2)
                    # Right border
                    Line(points=[obj.x + obj.width, obj.y + (i * 40), obj.x + obj.width, obj.y + (i * 40 + 40)], width=2)
                    # Bottom border
                    Line(points=[obj.x, obj.y + (i * 40 + 40), obj.x + obj.width, obj.y + (i * 40 + 40)], width=2)

                    