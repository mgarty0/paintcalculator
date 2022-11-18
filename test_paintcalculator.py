
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

