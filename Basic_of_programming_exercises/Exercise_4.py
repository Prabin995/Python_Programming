def y_intersect(x1, y1, x2, y2):
    if x1 == x2:
        # In this case The line is gone vertical and does not intersect the y-axis
        return None

    # Calculating the slope of the line
    slope = (y2 - y1) / (x2 - x1)

    # Calculating the y-intercept using y = mx + c
    y_intercept = y1 - slope * x1

    return  y_intercept

# Testing some cases 
print(y_intersect(x1=1, y1=3, x2=5, y2=4))  
print(y_intersect(x1=3, y1=0, x2=5, y2=4))  
print(y_intersect(x1=3, y1=0, x2=3, y2=4))

#Founding result from testiong :2.75,-6.0,None for above cases
