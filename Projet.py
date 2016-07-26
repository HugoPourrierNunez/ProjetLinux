#!/usr/bin/python
import pygtk
pygtk.require("2.0")
import gtk

class HelloWorld:
	def __init__(self):
		interface = gtk.Builder()
		interface.add_from_file('Projet.glade')
		
		self.cursor1=interface.get_object("cursor1")
		self.cursor1.set_range(-15,75)
		self.cursor1.set_value(-15)
		
		self.cursor2=interface.get_object("cursor2")
		self.cursor2.set_range(-15,75)
		self.cursor2.set_value(-15)
		
		self.button1=interface.get_object("button1")
		self.button2=interface.get_object("button2")
		self.name1=interface.get_object("name1")
		self.name2=interface.get_object("name2")
		self.score1=interface.get_object("score1")
		self.score2=interface.get_object("score2")
		
		interface.connect_signals(self)

	def on_mainWindow_destroy(self, widget):
		gtk.main_quit()
		
	def on_button1_clicked(self,widget):
		print("on_button1_clicked")

	def on_button2_clicked(self,widget):
		print("on_button2_clicked")
	
	def on_cursor1_change_value(self,widget,v1,v2):
		print("on_cursor1_change_value")
	
	def on_cursor2_change_value(self,widget,v1,v2):
		print("on_cursor2_change_value")

	
if __name__ == "__main__":
	HelloWorld()
	gtk.main()
