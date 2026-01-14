"""
Group Name: SYDNEY-35 (SYD-35)
Authors: Roshan Lamichhane (S399178), Ekraj Ghimire - (S398831), Sudip Sunar (S398629), Shrijan Neupane  (S398335)

Group Members:
Roshan Lamichhane - S399178
Ekraj Ghimire - S398831
Sudip Sunar - S398629
Shrijan Neupane - S398335

############
Question:
Create a program that uses a recursive function to generate a geometric pattern using Python's turtle graphics.
The pattern starts with a regular polygon and recursively modifies each edge to create intricate designs.
Pattern Generation Rules:

For each edge of the shape:
1.Divide the edge into three equal segments
2.Replace the middle segment with two sides of an equilateral triangle pointing inward (creating an indentation)
3.This transforms one straight edge into four smaller edges, each 1/3 the length of the original edge
4.Apply this same process recursively to each of the four new edges based on the specified depth


############
References:
- https://www.geeksforgeeks.org/python/python-turtle-tutorial/
- https://docs.python.org/3/library/turtle.html

"""

import turtle

def draw_edge(length, depth):
    """ draw the edges recrusively"""
    if depth == 0:
        # Draw a straight line
        turtle.forward(length)
    else:
        new_length = length / 3
        # 1. First segment
        draw_edge(new_length, depth - 1)

        # 2. Turn RIGHT to point the triangle inward
        turtle.right(60)
        draw_edge(new_length, depth - 1)

        # 3. Turn LEFT 120 to complete the inward triangle
        turtle.left(120)
        draw_edge(new_length, depth - 1)

        # 4. Turn RIGHT 60 to straighten out
        turtle.right(60)
        draw_edge(new_length, depth - 1)


#### Main Program

 # User inputs for sides, length and depth
sides = int(input("Enter the number of sides: "))
length = float(input("Enter the side length: "))
depth = int(input("Enter the recursion depth: "))

# Set drawing speed
turtle.speed(0)
turtle.delay(0)
