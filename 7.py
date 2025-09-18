def calculate_operations(a, b): 
    sum_result = a + b 
    difference = a - b 
    product = a * b 
    return (sum_result, difference, product) 
num1 = 10 
num2 = 5 
list= calculate_operations(num1, num2)
print(list)
