# File: Triangle.py

# Description: A basic 2D Triangle class

# Student Name: Abhinav Achuta

# Student UT EID: aa85934

# Course Name: CS 313E

# Unique Number: 86610

import sys
import math

TOL = 0.01

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
      self.x = x
      self.y = y

  # get the distance to another Point object
  def dist (self, other):
      distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
      return distance

class Triangle (object):
    # constructor
    def __init__(self, PointA, PointB, PointC):
        self.PointA = PointA
        self.PointB = PointB
        self.PointC = PointC

        self.AB_length = PointA.dist(self.PointB)
        self.BC_length = PointB.dist(self.PointC)
        self.CA_length = PointC.dist(self.PointA)

    # check congruence of Triangles with equality
    # returns True or False (bolean)
    def __eq__(self, other):

        other_side_lengths = [other.AB_length, other.BC_length, other.CA_length]

        #Comparison
        if (self.AB_length in other_side_lengths and 
            self.BC_length in other_side_lengths and 
            self.CA_length in other_side_lengths):

            return True
        else:
            return False


    # returns whether or not the triangle is valid
    # returns True or False (bolean)
    def is_triangle(self):
        if (self.AB_length + self.BC_length > self.CA_length + TOL and
            self.BC_length + self.CA_length > self.AB_length + TOL and
            self.CA_length + self.AB_length > self.BC_length + TOL):
            
            return True
        else:
            return False

    # return the area of the triangle:
    def area(self):

        part_1 = self.PointA.x *(self.PointB.y - self.PointC.y)
        part_2 = self.PointB.x * (self.PointC.y - self.PointA.y)
        part_3 = self.PointC.x * (self.PointA.y - self.PointB.y)

        area = float((part_1 + part_2 + part_3)/2)

        return abs(area)

######################################################
# The code below is filled out for you, DO NOT EDIT. #
######################################################

# takes a string of coordinates and changes it to a list of Points
def get_points(coords_str):
    coords = [float(c) for c in coords_str.split(" ")]
    return [Point(c[0], c[1]) for c in zip(*[iter(coords)]*2)]

def main():
    # read the two triangles
    pointsA = get_points(sys.stdin.readline().strip())
    pointsB = get_points(sys.stdin.readline().strip())

    triangleA = Triangle(pointsA[0], pointsA[1], pointsA[2])
    triangleB = Triangle(pointsB[0], pointsB[1], pointsB[2])

    # Print final output
    print(triangleA.area())
    print(triangleB.area())
    print(triangleA.is_triangle())
    print(triangleB.is_triangle())
    print(triangleA == triangleB)

if __name__ == "__main__":
    main()
