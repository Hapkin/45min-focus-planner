import kivy as k
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle,Line

def my_callback(obj):
    #print('renew settings of self canvas: (borders)!')
    toggle_borders(obj, True)
    return True

def toggle_borders(obj, enable=True):
    if enable:
        for line in obj.border_lines:
            obj.canvas.after.remove(line)
            obj.border_lines.clear()
        prev_rowheight=0
        with obj.canvas.after:
            #for i in range((obj.rows-1),-1,-1):
            for i in range(0,(obj.rows)):
                if(i<3):#red + -> green
                    Color(1, i*0.3, 0)
                elif(i<6):#green + ->blue
                    Color(0,1,((i-3)*0.3))
                else: #blue + ->red
                    Color(((i-6)*0.3),0,1)
                # Black color for the border
                my_row= obj.children[i]
                ##line_menu = Line(points=[0, menu_height, self.width, menu_height], width=2)
                if(i==1):
                    pass
                    ##Body no attribute 'border_lines'
                    #toggle_borders(my_row,True)

                #print(f"#bottom:{i}: obj.children[i]: {obj.children[i]} || {prev_rowheight}\n")
                line_under=Line(points=[0, prev_rowheight, obj.width,prev_rowheight], width=1)
                prev_rowheight+=my_row.height
                #print(f"#upper:{i}: obj.children[i]: {obj.children[i]} || {prev_rowheight}\n")
                line_up=Line(points=[0, prev_rowheight-2, obj.width,prev_rowheight-2], width=1)
                #myline=Line(points=[0, prev_rowheight, obj.width,prev_rowheight], width=3)
                obj.border_lines.append(line_under)
                obj.border_lines.append(line_up)