

#some have windows door sockets ...
#different paint types
#different paint can size 1,2.5 5 10
#10% margin
#save/load



walls=[]

paintpermetre=1/6

defaultcoatcount=1

class wall:
	
	width=1
	height=1
	coats=-1 #use global value for -1
	name=""
	paintname=""

	def __init__(self,width,height):
		self.width=width
		self.height=height
		self.calculatepaint()
	
	def setcoatcount(self,coats):
		self.coats=coats
	
	def calculatepaint(self):
		if self.coats==-1: coats=defaultcoatcount
		else: coats=self.coats
		area=getarea(self.width,self.height)
		wallpaint=area*paintpermetre*coats
		return wallpaint

def getarea(x,y):
	return x*y

def removewall(index):
	walls.pop(index)

def editwall(index):
	selectedwall=walls[index]
	
	while True:
		print("Enter one of: width, height, name, coats, back")
		intent=input("How do you want to edit the wall")
		match intent:
			case "width":
				selectedwall.width=int(input("Input new width: "))
			case "height":
				selectedwall.height=int(input("Input new height: "))
			case "name":
				selectedwall.name=input("Input name: ")
			case "coats":
				selectedwall.coats=int(input("Input number of coats: "))
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


def main():
	initializewalls(int(input("How many walls do you need to paint? ")))
	while True:
		printstatus()
		
		print("Type one of the following commands:")
		print("init")
		print("add")
		print("status")
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
			case "status":
				printstatus()
			case "help":
				pass
			case "exit":
				break


if __name__=="__main__":
	main()


#print(int(input("Enter wall height: "))*int(input("Enter wall width: "))/6)