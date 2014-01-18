#!/usr/bin/python

import gtk, math

class Penguin(gtk.DrawingArea):
    def __init__(self):
        gtk.DrawingArea.__init__(self)
        self.connect("expose_event", self.expose)

    def expose(self, widget, event):
        self.context = widget.window.cairo_create()

        # set a clip region for the expose event
        self.context.rectangle(event.area.x, event.area.y,
                               event.area.width, event.area.height)
        self.context.clip()

        rect = self.get_allocation()
        x = rect.x + rect.width/2
        y = rect.y+rect.height / 2
        radius = min(rect.width / 2, rect.height / 2)-5
        self.context.arc_negative(x,y,radius, 0, math.pi)
        self.context.set_source_rgb(1,1,1)
        self.context.fill_preserve()
        self.context.set_source_rgb(0,0,0)
        self.context.stroke()

        self.draw(self.context)
        return False

if __name__ == "__main__":
    window = gtk.Window()
    penguin = Penguin()
    
    window.add(penguin)
    window.connect("destroy", gtk.main_quit)
    window.show_all()

    gtk.main()

