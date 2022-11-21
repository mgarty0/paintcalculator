
#10% margin

import json

#class paintcan:
#	def __init__(self,size):
#		self.size=size

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
	
	def __init__(self,width=1,height=1):
		super().__init__(width,height)
		self.coats=-1 #use global value for -1
		self.name=""
		self.paintname=""
		self.holes=[]
	
	def savelist(self):
		listholes=[]
		for hole in self.holes:
			listholes.append((hole.width,hole.height))
		return [self.width,self.height,self.name,self.paintname,self.coats,listholes]
	
	def loadlist(self,loadlist):
		self.width=loadlist[0]
		self.height=loadlist[1]
		self.name=loadlist[2]
		self.paintname=loadlist[3]
		self.coats=loadlist[4]
		self.holes=[]
		for currenthole in loadlist[5]:
			self.holes.append(hole(currenthole[0],currenthole[1]))
	
	def setcoats(self,coats):
		self.coats=coats
	def getcoats(self):
		return self.coats
	def setpaintname(self,name):
		self.paintname=name
	def getpaintname(self):
		return self.paintname
	
	def calculatepaint(self):
		if self.coats==-1: coats=defaultcoatcount
		else: coats=self.coats
		area=getarea(self.width,self.height)
		for wallhole in self.holes:
			area=area-wallhole.getarea()
		wallpaint=area*coats
		wallpaint=wallpaint*paintpermetre
		return wallpaint


walls=[]

paintcans=(paintcan(1),paintcan(2.5),paintcan(5),paintcan(10))

paintpermetre=1/6

defaultcoatcount=1

savefilename="save"

def getarea(x,y):
	return x*y

def removewall(index):
	walls.pop(index)

def clearholes(index):
	selectedwall=walls[index]
	selectedwall.holes=[]

def addhole(index):
	try:

		selectedwall=walls[index]
		width=int(input("Enter width of hole: "))
		height=int(input("Enter height of hole: "))
		selectedwall.holes.append(hole(width,height))
	except:
		print("Error adding hole")
def editwall(index):
	selectedwall=walls[index]
	
	while True:
		try:
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
		except:
			print("Error: Input not recognised")
def addwall():
	try:
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
		print("Enter Edit menu to adjust wall or add obstructions")
	except:
		print("Error adding wall, Try again")


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

def paintamounttocans(paintamount):
	#least waste
	localpaintamount=paintamount
	paintcanlist={10:0,5:0,2.5:0,1:0}
	for can in paintcanlist:
		while can<localpaintamount:
			paintcanlist[can]=paintcanlist[can]+1
			localpaintamount=localpaintamount-can
	if(paintamount>0): paintcanlist[1]=paintcanlist[1]+1
	if(paintcanlist[1]>=3):
		paintcanlist[1]=paintcanlist[1]-3
		paintcanlist[2.5]=paintcanlist[2.5]+1
	return paintcanlist

def printpaintstatus():
	paintamount={}
	for currentwall in walls:
		currentpaint=currentwall.getpaintname()
		if not currentpaint in paintamount:
			paintamount[currentpaint]=0

		paintamount[currentpaint]=paintamount[currentpaint]+currentwall.calculatepaint()
	print("You will need:")
	for paintname in paintamount:
		print(paintname+": "+str(paintamount[paintname])+" Litres")
		canoutputstring="Cans: "
		paintcansneeded=paintamounttocans(paintamount[paintname])
		for can in paintcansneeded:
			canoutputstring=canoutputstring+str(paintcansneeded[can])+"X"+str(can)+"L "
		print(canoutputstring)
	pass

#def paintmenu():
#	while True:
#		printpaintstatus()
#
#		print("Type one of the following commands:")
#		print("add")
#		print("back")
#		intent=input("-> ")
#		match intent:
#			case "add":
#				pass
#			case "back":
#				break

def save():
	try:
		fp=open(savefilename+".txt","w")
		serialwalls=[]
		for tmpwall in walls:
			serialwalls.append(tmpwall.savelist())
		json.dump(serialwalls,fp)
		fp.close()
	except:
		print("Error saving to file")
def load():
	try:
		fp=open(savefilename+".txt","r")
		serialwalls=json.load(fp)
		fp.close()
		walls.clear()
		for curwall in serialwalls:
			tmpwall=wall(curwall)
			tmpwall.loadlist(curwall)
			walls.append(tmpwall)

	except:
		print("Error loading from file (Does the file exist?")
def configmenu():
	global defaultcoatcount
	global savefilename
	while True:
		try:
			print("Which setting do you want to change?")
			print("Valid values are:")
			print("default coat count")
			print("savefile")
			print("back")
			intent=input("->")
			match intent:
				case "default coat count":
					defaultcoatcount=int(input("How many coats will be applied to walls by default"))
				case "savefile":
					savefilename=input("Enter new name for save file: ")
				case "back":
					break
				case "":
					break
				case _:
					print("")
		except:
			print("Error: Input not recognised")


def main():
	try:
		initializewalls(int(input("How many walls do you need to paint (or blank to continue)? ")))
	except:
		pass
	while True:
		try:
			printstatus()
			
			print("Type one of the following commands:")
			print("add     --adds a wall")
			print("init    --clears all walls and starts adding a batch of walls")
			print("edit    --edit a wall")
			print("remove  --remove a wall")
			print("config  --access config menu")
#			print("paint   --access paint menu")
			print("save    --save walls to file")
			print("load    --load walls from file")
			print("status  --prints brief report of paint needed")
#			print("help    --NA")
			print("exit    --exits the program with a detailed report on paint needed")
			
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
				case "config":
					configmenu()
#				case "paint":
#					paintmenu()
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
		except:
			print("Error: Input not recognised")
	printpaintstatus()


if __name__=="__main__":
	main()

