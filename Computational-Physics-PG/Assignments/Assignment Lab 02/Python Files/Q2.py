#Question 2
#Check if 3 points are collinear or not

x1,y1=eval(input("Enter the first point (x,y): "))
x2,y2=eval(input("Enter the second point (x,y): "))
x3,y3=eval(input("Enter the third point (x,y): "))

if (y2-y1)/(x2-x1) == (y3-y2)/(x3-x2):
    print("The three points are collinear")
else:
    print("The three points are not collinear")
