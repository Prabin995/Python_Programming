import math

def to_secs(hours, mins, secs):
    # Convertng all parameters to seconds
    total_seconds = math.floor(hours * 3600 + mins * 60 + secs)
    return total_seconds

# testing some cases
print(to_secs(2, 30, 10))       
print(to_secs(2, 0, 0))         
print(to_secs(0, -10, 10))     
print(to_secs(2.5, 0, 10))      
print(to_secs(2.433, 0, 0))     
print(to_secs(0, 0, 1.2))       
 
 #After testing We found results as:= 9010,7200,-590,9010,8758,1 
