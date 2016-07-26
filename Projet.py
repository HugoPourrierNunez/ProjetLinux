#!/usr/bin/python
import pygtk
pygtk.require("2.0")
import gtk
from PIL import Image
import numpy
from random import randrange

class HelloWorld:
	def __init__(self):
		interface = gtk.Builder()
		interface.add_from_file('Projet.glade')
		
		self.cursor1=interface.get_object("cursor1")
		self.cursor1.set_range(-75,75)
		self.cursor1.set_value(0)
		
		self.cursor2=interface.get_object("cursor2")
		self.cursor2.set_range(-75,75)
		self.cursor2.set_value(0)
		
		self.button1=interface.get_object("button1")
		self.button2=interface.get_object("button2")
		self.name1=interface.get_object("name1")
		self.name2=interface.get_object("name2")
		self.score1=interface.get_object("score1")
		self.score2=interface.get_object("score2")
		
		self.gtk_image1=interface.get_object("image1")
		self.gtk_image2=interface.get_object("image2")
		
		self.image1 = Image.open("canon1.png")
		self.image2 = Image.open("canon2.png")
		
		self.pane = interface.get_object("pane")
		
		self.image1.rotate(self.cursor1.get_value()).save("canon1_rot.png")
		self.gtk_image1.set_from_file("canon1_rot.png")
		
		self.image2.rotate(self.cursor2.get_value()).save("canon2_rot.png")
		self.gtk_image2.set_from_file("canon2_rot.png")
		
		#self.image2 = Image.open("canon1.png")
		#self.image2.rotate(45)
		
		
		
		interface.connect_signals(self)

	def on_mainWindow_destroy(self, widget):
		gtk.main_quit()
		
	def on_button1_clicked(self,widget):
		self.pane.move(self.gtk_image1,10,randrange(0 ,self.pane.get_allocation().height-self.gtk_image1.get_allocation().height))

	def on_button2_clicked(self,widget):
		self.pane.move(self.gtk_image2,self.pane.get_allocation().width-10-self.gtk_image2.get_allocation().width,randrange(0 ,self.pane.get_allocation().height-self.gtk_image2.get_allocation().height))
	
	def on_cursor1_change_value(self,widget,v1,v2):
		self.image1.rotate(self.cursor1.get_value()).save("canon1_rot.png")
		self.gtk_image1.set_from_file("canon1_rot.png")
		
	
	def on_cursor2_change_value(self,widget,v1,v2):
		self.image2.rotate(-self.cursor2.get_value()).save("canon2_rot.png")
		self.gtk_image2.set_from_file("canon2_rot.png")

	
if __name__ == "__main__":
	HelloWorld()
	gtk.main()
