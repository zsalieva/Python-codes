#               ()you put parameters
# print("Hello Python")

# def helloWorld():
#     print("Hello Python")


# for i in range(5):

#      helloWorld()    

#------------------------
#              planet is a parameter , Mars is argument
# def helloWorld(planet="Mars"):
#      print("Hello from a " , planet)

# helloWorld()
# helloWorld("Venus")
# helloWorld("Earth")

#-------------------------

# def helloWorld(planet, age):
#      print("Hello from a " , planet  , age)
     
# helloWorld("Mars", 50000)




#------------------

#keyword arguments
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# my_function( "Emil", "Tobias","Linus") #it will go inorder as in def function 

#----------------------

#passing a list as an argument
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
vegs =["potato","tomato","pepper"]
#food =fruits = ["apple", "banana", "cherry"]   --> passes the fruit argument to food

my_function(fruits) 
my_function(vegs)
