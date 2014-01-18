#!/usr/bin/python

import os,gtk, math, cairo, rsvg

PENGUIN_X = 507.0
PENGUIN_Y = 650.0
SPEECH_X = 434.0
SPEECH_Y = 394.0
TEXT_X = 336.0
TEXT_Y = 280.0
CORNER = 20.0

class Penguin(gtk.Window):
    def __init__(self):
        super(Penguin, self).__init__()
        self.resize(int(PENGUIN_X/6), int(PENGUIN_Y/6))
        self.set_gravity(gtk.gdk.GRAVITY_SOUTH_EAST)
        self.width, self.height = self.get_size()
        self.move(gtk.gdk.screen_width() - self.width, gtk.gdk.screen_height() - self.height)
        screen = self.get_screen()
        rgba = screen.get_rgba_colormap()
        self.set_colormap(rgba)
        self.set_app_paintable(True)
        self.connect('expose-event', self.draw_penguin)
        self.set_decorated(False)
        self.connect("destroy", gtk.main_quit)
        self.add_events(gtk.gdk.BUTTON_PRESS_MASK)
        self.connect("button-press-event", self.click_handler)
        self.connect('window-state-event', self.window_state_event_handler)
        self.show_all()
        self.create_options()
        
    def draw_penguin(self, widget, event):
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
        scalef = widget.get_size()[0]/PENGUIN_X
        cr.scale(scalef, scalef)
        svg.render_cairo(cr)
       
    def draw_options(self, widget, event):
        cr = widget.window.cairo_create()
        cr.set_operator(cairo.OPERATOR_CLEAR)
        cr.rectangle(0.0,0.0, *widget.get_size())
        cr.fill()
        cr.set_operator(cairo.OPERATOR_OVER)
        svg = rsvg.Handle(file="assets/speech.svg")
        scalef = widget.get_size()[0]/SPEECH_X
        cr.scale(scalef, scalef)
        svg.render_cairo(cr)
   
    def create_options(self):
        self.options = gtk.Window(gtk.WINDOW_POPUP)
        self.options.resize(int(SPEECH_X/2), int(SPEECH_Y/2))
        self.options.set_gravity(gtk.gdk.GRAVITY_SOUTH_EAST)
        width, height = self.options.get_size()
        self.options.move(gtk.gdk.screen_width() - width - self.width, gtk.gdk.screen_height() - height -self.height) 
        screen = self.options.get_screen()
        rgba = screen.get_rgba_colormap()
        self.options.set_colormap(rgba)
        self.options.set_app_paintable(True)
        self.options.connect('expose-event', self.draw_options)
        self.options.set_decorated(False)
        self.optionsbox = gtk.Window(gtk.WINDOW_POPUP)
        self.optionsbox.resize(int(TEXT_X/2), int(TEXT_Y/2))
        self.optionsbox.move(gtk.gdk.screen_width() - width - self.width+int(CORNER/2), gtk.gdk.screen_height() - height -self.height+int(CORNER/2))
        self.optionsbox.set_app_paintable(True)
        self.optionsbox.set_colormap(rgba)
        self.optionsbox.set_decorated(False)
        
        text = gtk.TextView()
        text.set_size_request(50,50)
        text.get_buffer().set_text("Hello World!")
        self.optionsbox.add(text)
        self.options.show_all()
        self.optionsbox.show_all()
        
    def click_handler(self, widget, event):
        if self.options:
            self.options.destroy()
            self.options = None
        else:
            self.create_options()

    def window_state_event_handler(self, widget, event):
        if event.changed_mask & gtk.gdk.WINDOW_STATE_ICONIFIED:
            if event.new_window_state & gtk.gdk.WINDOW_STATE_ICONIFIED and self.options:
                self.options.hide()
                self.optionsbox.hide()
            elif self.options:
                self.options.show()
                self.optionsbox.show()
    
if os.geteuid() != 0:
    exit("I need root permissions!")

penguin = Penguin() #create_penguin()
gtk.main()

