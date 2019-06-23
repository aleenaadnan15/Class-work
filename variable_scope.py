# a = 2
# def my_fun():
#     a = 9
#     print(a)

# my_fun()
# print(a)

# ''' inner function '''

# def calculate_taxes(percent):
#     def actual_tax(salary):
#         return salary * percent
#     return actual_tax 


# actual_tax_fn = calculate_taxes(0.30)
# print(actual_tax_fn)
# print(actual_tax_fn(100000))

''' part 2 '''

def calculator(num1 , num2 , op):
    def add(n1 , n2):
        return n1 + n2 

    def sub(n1, n2):
        return n1 - n2

    if op == '+':
        return add(num1 , num2)
    elif op == '-':
        return sub(num1 , num2)

print(calculator(2, 3, '+'))
print(calculator(2, 3, '-'))