
import paintcalculator as pc


def test_getarea_1():
	assert pc.getarea(5,6)==30
	assert pc.getarea(0,0)==0

#def test_addwall_1():
#	pc.walls=[]

def test_wall_class_1():
	wall=pc.wall(4,8)
	assert wall.getwidth()==4
	assert wall.getheight()==8
	assert wall.getarea()==32
	assert wall.getcoats()==-1


def test_paintamounttocans_1():
	paintamount=pc.paintamounttocans(30.4)
	assert paintamount[10]==3
	assert paintamount[5]==0
	assert paintamount[2.5]==0
	assert paintamount[1]==1

def test_paintamounttocans_2():
	paintamount=pc.paintamounttocans(2.4)
	assert paintamount[10]==0
	assert paintamount[5]==0
	assert paintamount[2.5]==1
	assert paintamount[1]==0


