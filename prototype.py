import numpy
from math import *
import sys
sys.path.insert(0, '/home/rishi/creage-proj/dependencies')
#import voronoi
from voronoi import computeVoronoiDiagram


#class Point:
#    def __init__(self, x, y):
#        self.x = x;
#        self.y = y;

def main():
#    pointslist = [Point(3, 3)] * 10
    #pointslist = [(2,3), (4,5)]
#    mytuple = computeVoronoiDiagram(pointslist)
    coordinates = numpy.random.uniform(-10,10, (1000000, 2))
    coordinates.tofile('points.txt',sep=" ", format="%s")
    fi = open("points.txt","r")
    print "Name of the file: ", fi.name
    words=fi.read().split()
    fo=open("points_sep.txt", "w")
#    fo.write("Puppy kitten")
    counter=0
    for w in words:
        fo.write(w)
        if counter%2==0:
            fo.write(" ")
        if counter%2==1:
            fo.write('\n')
        counter=counter+1    

if __name__ == "__main__":
    main()
