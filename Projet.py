#!/usr/bin/python
import pygtk
pygtk.require("2.0")
import gtk
from PIL import Image
import numpy
from random import randrange
from math import sin, cos, pi

class Main:
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
		
		self.balle1=interface.get_object("balle1")
		self.balle2=interface.get_object("balle2")
		
		self.image1 = Image.open("canon1.png")
		self.image2 = Image.open("canon2.png")
		
		self.pane = interface.get_object("pane")
		
		self.image1.rotate(self.cursor1.get_value()).save("canon1_rot.png")
		self.gtk_image1.set_from_file("canon1_rot.png")
		
		self.image2.rotate(self.cursor2.get_value()).save("canon2_rot.png")
		self.gtk_image2.set_from_file("canon2_rot.png")
		
		self.posY1 =randrange(0 ,self.pane.get_allocation().height-self.gtk_image1.get_allocation().height)
		self.posY2=randrange(0 ,self.pane.get_allocation().height-self.gtk_image2.get_allocation().height)
		
		self.posX1 = 10
		self.posX2=self.pane.get_allocation().width-10-self.gtk_image2.get_allocation().width
		
		self.pane.move(self.gtk_image1,self.posX1,self.posY1)
		self.pane.move(self.gtk_image2,self.posX2,self.posY2)
		
		self.xb1=self.gtk_image1.get_allocation().width-35
		self.yb1=self.posY1+35
		
		self.xb2=self.pane.get_allocation().width-self.gtk_image2.get_allocation().width-10
		self.yb2=self.posY2+30
		
		self.pane.move(self.balle1, self.xb1, self.yb1)
		self.pane.move(self.balle2,self.xb2,self.yb2)
		
		
		#self.image2 = Image.open("canon1.png")
		#self.image2.rotate(45)
		
		interface.connect_signals(self)

	def on_mainWindow_destroy(self, widget):
		gtk.main_quit()
		
	def on_button1_clicked(self,widget):
		nb=randrange(0 ,self.pane.get_allocation().height-self.gtk_image1.get_allocation().height)
		diff=nb-self.posY1;
		self.posY1=nb
		self.pane.move(self.gtk_image1,self.posX1,self.posY1)
		self.yb1=self.yb1+diff
		self.pane.move(self.balle1,self.xb1,self.yb1)
		self.rotateBalle1(-self.cursor1.get_value())

	def on_button2_clicked(self,widget):
		nb=randrange(0 ,self.pane.get_allocation().height-self.gtk_image2.get_allocation().height)
		diff=nb-self.posY2;
		self.posY2=nb
		self.posX2=self.pane.get_allocation().width-10-self.gtk_image2.get_allocation().width
		self.pane.move(self.gtk_image2,self.posX2,self.posY2)
		self.yb2=self.yb2+diff
		self.pane.move(self.balle2,self.xb2,self.yb2)
		self.rotateBalle2(self.cursor2.get_value())
		
	def rotateBalle1(self,angle):
		cosAngle = cos(self.degToRad(angle))
		sinAngle= sin(self.degToRad(angle))
		centerX=self.posX1+55
		centerY=self.posY1+55
		newX = (self.xb1-centerX)*cosAngle-(self.yb1-centerY)*sinAngle
		newY= (self.yb1-centerY)*cosAngle+(self.xb1-centerX)*sinAngle
		self.pane.move(self.balle1,centerX+newX,centerY+newY)
		
	def rotateBalle2(self,angle):
		cosAngle = cos(self.degToRad(angle))
		sinAngle= sin(self.degToRad(angle))
		centerX=self.posX2+55
		centerY=self.posY2+55
		newX = (self.xb2-centerX)*cosAngle-(self.yb2-centerY)*sinAngle
		newY= (self.yb2-centerY)*cosAngle+(self.xb2-centerX)*sinAngle
		self.pane.move(self.balle2,centerX+newX,centerY+newY)	
	
	def on_cursor1_change_value(self,widget,v1,v2):
		self.image1.rotate(self.cursor1.get_value()).save("canon1_rot.png")
		self.gtk_image1.set_from_file("canon1_rot.png")
		self.rotateBalle1(-self.cursor1.get_value())
		
	
	def on_cursor2_change_value(self,widget,v1,v2):
		self.image2.rotate(-self.cursor2.get_value()).save("canon2_rot.png")
		self.gtk_image2.set_from_file("canon2_rot.png")
		self.rotateBalle2(self.cursor2.get_value())
		
	def degToRad(self,deg):
		return float(deg)*pi/180

	
if __name__ == "__main__":
	Main()
	gtk.main()
