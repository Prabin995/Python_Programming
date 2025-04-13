def is_rightangled(a, b, c, tol=0.001):
    
    # Checking  if a² + b² is nearly equal to c² or not
    return abs(a**2 + b**2 - c**2) < tol

# Testing some cases
print(is_rightangled(3, 4, 5))  
print(is_rightangled(5, 12, 13))  
print(is_rightangled(1, 1, 1.414))  
print(is_rightangled(2, 2, 3))  


#After excution we find results for these cases are:= True,True,True,False