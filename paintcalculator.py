

#some have windows door sockets ...
#different paint types
#different paint can size 1,2.5 5 10
#10% margin
#save/load

import json

walls=[]

paints=[]

paintpermetre=1/6

defaultcoatcount=1

class area:
	def __init__(self,width,height):
		self.width=width
		self.height=height
	
	def setwidth(self,width):
		self.width=width
	def setheight(self,height):
		self.height=height
	
	def getwidth(self):
		return self.width
	def getheight(self):
		return self.height
	def getarea(self):
		return self.width*self.height

class hole(area):
	def __init__(self,width,height):
		super().__init__(width,height)
	def getarea(self):
		return super().getarea()

class wall(area):
	
	def __init__(self,width,height):
		super().__init__(width,height)
		self.coats=-1 #use global value for -1
		self.name=""
		self.paintname=""
		self.holes=[]
	
	def savelist(self):
		listholes=[]
		for hole in self.holes:
			listholes.append((hole.width,hole.height))
		return [self.name,self.paintname,self.coats,listholes]
	def setcoats(self,coats):
		self.coats=coats
	
	def getcoats(self):
		return self.coats
	
	def calculatepaint(self):
		if self.coats==-1: coats=defaultcoatcount
		else: coats=self.coats
		area=getarea(self.width,self.height)
		for wallhole in self.holes:
			area=area-wallhole.getarea()
		wallpaint=area*coats
		wallpaint=wallpaint*paintpermetre
		return wallpaint

def getarea(x,y):
	return x*y

def removewall(index):
	walls.pop(index)

def clearholes(index):
	selectedwall=walls[index]
	selectedwall.holes=[]

def addhole(index):
	selectedwall=walls[index]
	width=int(input("Enter width of hole: "))
	height=int(input("Enter height of hole: "))
	selectedwall.holes.append(hole(width,height))

def editwall(index):
	selectedwall=walls[index]
	
	while True:
		print("Enter one of: width, height, name, coats, add hole, clear holes. back")
		print("How do you want to edit the wall?")
		intent=input("-> ")
		match intent:
			case "width":
				selectedwall.width=int(input("Input new width: "))
			case "height":
				selectedwall.height=int(input("Input new height: "))
			case "name":
				selectedwall.name=input("Input name: ")
			case "coats":
				selectedwall.coats=int(input("Input number of coats: "))
			case "add hole":
				addhole(index)
			case "clear holes":
				clearholes(index)
			case "back":
				break
			case _:
				print("Command not understood")

def addwall():
	width=int(input("Enter wall width in Meters: "))
	height=int(input("Enter wall height in Meters: "))
	newwall=wall(width,height)

	newwall.name=input("Set an optional name for this wall or leave blank: ")
	newwall.paintname=input("Set an optional name for the paint to be used or leave blank: ")
	numcoats=input("Choose the number of coats of paint or leave blank for default ("+str(defaultcoatcount)+"): ")
	if(numcoats==""): numcoats=-1
	else: numcoats=int(numcoats)
	newwall.coats=numcoats
	print("Adding Wall with id "+str(len(walls)))
	walls.append(newwall)



def initializewalls(wallcount):
	index=0
	while index<wallcount:
		addwall()
		index=index+1

def printwallinfo(index):
	selectedwall=walls[index]
	print("Name: "+selectedwall.name)
	print("Width: "+selectedwall.width)
	print("Height: "+selectedwall.height)
	print("coats: "+selectedwall.coats)
	print("Paint Name: "+selectedwall.paintname)
def printstatus():
	totalpaint=0
	for w in walls:
		totalpaint=totalpaint+w.calculatepaint()
	print("There are "+str(len(walls))+" walls")
	print("Total paint needed: "+str(totalpaint))

def printpaintstatus():
	pass

def save():
#	try:
		fp=open("save.txt","w")
		serialwalls=[]
		for wall in walls:
			serialwalls.append(wall.savelist())
		json.dump(serialwalls,fp)
		fp.close()
#	except:
		pass
def load():
	try:
		fp=open("save.txt","r")
		
		fp.close()
	except:
		pass
def paintmenu():
	while True:
		printpaintstatus()

		print("Type one of the following commands:")
		print("add")
		print("back")

		intent=input("-> ")
		match intent:
			case "add":
				pass
			case "back":
				break
def main():
	initializewalls(int(input("How many walls do you need to paint? ")))
	while True:
		printstatus()
		
		print("Type one of the following commands:")
		print("add")
		print("init")
		print("edit")
		print("remove")
		print("paint")
		print("save")
		print("load")
		print("status")
		print("help")
		print("exit")
		
		intent=input("-> ")
		match intent:
			case "add":
				addwall()
			case "init":
				initializewalls(int(input("How many walls do you need to paint? ")))
			case "edit":
				editwall(int(input("Select wall to be edited: ")))
			case "remove":
				removewall(int(input("Select wall to be removed: ")))
			case "paint":
				paintmenu()
			case "save":
				save()
			case "load":
				load()
			case "status":
				printstatus()
			case "help":
				pass
			case "exit":
				break


if __name__=="__main__":
	main()


#print(int(input("Enter wall height: "))*int(input("Enter wall width: "))/6)
