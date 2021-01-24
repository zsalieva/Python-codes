#Write a Python program which calculates area and perimeter of a rectangle. Length and width are provided by the user. 
length=input("What is the rectable length?")
width=input("What is the rectangle width?")
#casting to convert from a string data type to integer data type
l=int(length)
w=int(width)
area= l * w
perimeter = 2*(l+w)
print('Area = ' , area)
print('Perimeter', perimeter)

