import math #Importing Math laibrary.

# Informed the user to choose their desire numbers with conditions.
print("please input variables")

Hypotenuse = float(input("Hypotenuse: ")) # Input for hypotenuse of the triangle.
One_side = float(input("One Side: ")) # input for one side of the triangle.

# Giving sutuable conditions
if ((Hypotenuse > One_side) and (Hypotenuse>0 and One_side >0)) :
    print("Another Side is ", math.sqrt(Hypotenuse**2 - One_side**2)) #Condition for correct input.
                  
elif (Hypotenuse<0 or One_side <0):
    print("input error! Side does not in negative") #Condition for Wrong Input : Length as a Negative.
    
elif(Hypotenuse < One_side):
    #Condition For Wrong Input:Side length is greater then Hypotenuse.
    print("input error!  hypotenuse must be greather then side length! ")  

    

                 
    