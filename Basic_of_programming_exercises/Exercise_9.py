def limited_sum(ls, max_sum):
    total_sum = 0.0
    count = 0
""""Condition for after adding new number from list if it cross max_sum it breaks loop and
if it under max_sum count added by 1."""
    for num in ls:
        if total_sum + num > max_sum:
            break
        total_sum += num
        count += 1

return [total_sum, count]

#Testing some cases
print(limited_sum(ls=[1.0, 2.0, 3.0, 4.0], max_sum=3.5))  
print(limited_sum(ls=[1.0, -2.0, 3.0], max_sum=10.0))     
print(limited_sum([20.0, 10.0, 5.0], max_sum=1.0))        