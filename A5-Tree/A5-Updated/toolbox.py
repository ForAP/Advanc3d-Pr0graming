# File name: toolbox.py
import kivy
kivy.require('1.7.0')
import math
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Line
from turingwidgets import StateRep, DraggableWidget
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Ellipse, Line, Bezier
from state import State

class ToolButton(ToggleButton):
    def on_touch_down(self, touch):
        ds = self.parent.drawing_space
        if self.state == 'down' and ds.collide_point(touch.x, touch.y):
            (x,y) = ds.to_widget(touch.x, touch.y)
            self.draw(ds, x, y)
            return True
        return super(ToolButton, self).on_touch_down(touch)

    def draw(self, ds, x, y):
        pass


class ToolState(ToolButton):
    #This method actaully calls the state class..... Bad Design ahaha
    def draw(self, ds, x, y):
        sm = StateRep(width=48, height=48)
        sm.center = (x,y)
        sm.opacity = 0.9
        state = State()
        print "\nThis is the state that you just created, will you name it?" + str(state)
        print type(ds.children)
        print "ds children is " + str(ds.children)
        print "ds children's length is " + str(len(ds.children))
        self.parent.general_options.add_state(state)
        ds.add_widget(sm)
        ds.children[0].set_state()

class ToolTransition(ToolButton):
    def draw(self, ds, x, y):
        pass

    def on_touch_down(self, touch):
        ds = self.parent.drawing_space
        if touch.is_double_tap and ds.collide_point(touch.x, touch.y):
            (x,y) = ds.to_widget(touch.x, touch.y)
            print (x,y)
            return True
        return super(ToolTransition, self).on_touch_down(touch)

# class ToolFigure(ToolButton):
#     def draw(self, ds, x, y):
#         (self.ix, self.iy) = (x,y)
#         with ds.canvas:
#             self.figure=self.create_figure(x,y,x+1,y+1)
#         ds.bind(on_touch_move=self.update_figure)
#         ds.bind(on_touch_up=self.end_figure)
#
#     def update_figure(self, ds, touch):
#         if ds.collide_point(touch.x, touch.y):
#             (x,y) = ds.to_widget(touch.x, touch.y)
#             ds.canvas.remove(self.figure)
#             with ds.canvas:
#                 self.figure = self.create_figure(self.ix, self.iy,x,y)
#
#     def end_figure(self, ds, touch):
#         ds.unbind(on_touch_move=self.update_figure)
#         ds.unbind(on_touch_up=self.end_figure)
#         ds.canvas.remove(self.figure)
#         (fx,fy) = ds.to_widget(touch.x, touch.y)
#         self.widgetize(ds,self.ix,self.iy,fx,fy)
#
#     def widgetize(self,ds,ix,iy,fx,fy):
#         widget = self.create_widget(ix,iy,fx,fy)
#         (ix,iy) = widget.to_local(ix,iy,relative=True)
#         (fx,fy) = widget.to_local(fx,fy,relative=True)
#         widget.canvas.add(self.create_figure(ix,iy,fx,fy))
#         ds.add_widget(widget)
#
#     def create_figure(self,ix,iy,fx,fy):
#         pass
#
#     def create_widget(self,ix,iy,fx,fy):
#         pass
#
# class ToolLine(ToolFigure):
#     def create_figure(self,ix,iy,fx,fy):
#         return Line(points=[ix, iy, fx, fy])
#
#     def create_widget(self,ix,iy,fx,fy):
#         pos = (min(ix, fx), min(iy, fy))
#         size = (abs(fx-ix), abs(fy-iy))
#         return DraggableWidget(pos = pos, size = size)
#
# class ToolCircle(ToolFigure):
#     # def draw(self, ds, x, y):
#     #     sm = Ellipse(size=(30,30))
#     #     sm.center = (x,y)
#     #     state = State()
#     #     self.parent.general_options.add_state(state)
#     #     ds.add_widget(sm)
#
#     def create_figure(self,ix,iy,fx,fy):
#         return Ellipse(size=(30,30)) #Line(circle=[ix,iy,math.hypot(ix-fx,iy-fy)])
#
#     def create_widget(self,ix,iy,fx,fy):
#         # r = math.hypot(ix-fx, iy-fy)
#         # pos = (ix-r, iy-r)
#         # size = (2*r, 2*r)
#         return DraggableWidget() #pos = pos, size = size
