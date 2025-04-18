def positives_sum(ls):
    #Condition for positive sum:=
    return sum(num for num in ls if num > 0)

# Testing some cases are for positive sums
print(positives_sum([1, 21, 3, 40, 5]))  
print(positives_sum([1, -2, 3]))         
print(positives_sum([-1, -2, -3]))       