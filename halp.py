#!/usr/bin/python

import os,gtk, math, cairo, rsvg

IMG_X = 507.0
IMG_Y = 650.0

if os.geteuid() != 0:
    exit("I need root permissions!")

def expose(widget, event):
    cr = widget.window.cairo_create()

    # Sets the operator to clear which deletes everything below where an object is drawn
    cr.set_operator(cairo.OPERATOR_CLEAR)
    # Makes the mask fill the entire window
    cr.rectangle(0.0, 0.0, *widget.get_size())
    # Deletes everything in the window (since the compositing operator is clear and mask fills the entire window
    cr.fill()
    # Set the compositing operator back to the default
    cr.set_operator(cairo.OPERATOR_OVER)

    svg = rsvg.Handle(file="assets/penguin.svg")
    scalef = widget.get_size()[0]/IMG_X
    cr.scale(scalef, scalef)
    svg.render_cairo(cr)

if __name__ == "__main__":
    window = gtk.Window()
    window.resize(int(IMG_X/6), int(IMG_Y/6))
    window.set_gravity(gtk.gdk.GRAVITY_SOUTH_EAST)
    width, height = window.get_size()
    window.move(gtk.gdk.screen_width() - width, gtk.gdk.screen_height() - height)
    screen = window.get_screen()
    rgba = screen.get_rgba_colormap()
    window.set_colormap(rgba)
    window.set_app_paintable(True)
    window.connect('expose-event', expose)
    window.set_decorated(False)
    window.connect("destroy", gtk.main_quit)
    window.show_all()

    gtk.main()

