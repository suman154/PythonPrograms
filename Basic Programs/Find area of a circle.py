#* Python Program to Find Area of a Circle
def findarea(r):
    PI =3.142
    return PI *(r*r);

print("Area is %.6f" % findarea(10));




#* Python Program to Find Area of a Circle With Math library
import math
def area(r):
    area = math.pi* pow(r,2)
    return print('Area of circle is:', area)
area(10)





