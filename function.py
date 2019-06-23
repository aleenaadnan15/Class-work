# def greet (): #function definition
#     print("Good morning")
# greet() #function calling
# print("i am outside the function")
# greet()
# print("completed")
# a = int(input("enter num 1 :"))
# b = int(input("enter num 2 :"))
# def add(num1 , num2): #recieving information/data called parameters
#     my_sum = num1 + num2
#     print(my_sum)
# add(a,b) #passing data called arguments


# def my_pet(owner , pet , city = "Karachi"):
#     print(owner , "is an owner of" , pet , " . They are from" , city)
# my_pet(owner = "john" , pet = "rabbit" , city = "lahore")


# def sum(): #takes nothing resturn something
#     a = 2
#     b = 3 
#     #print("sum is" (a+b))
#     return (a+b)
# result = sum()
# print(result)

# a = int(input("enter value 1"))
# b = int(input("enter value 2"))

# def sum(val1, val2):
#     result = val1 + val2
#     return result 
# output_of_function = sum(a,b)
# print(output_of_function)


# '''take an input from the user , pass it in the argument and 
#          return whether it is even or odd '''
         
         
# num = int(input("enter the num"))

# def even_or_odd (num):
#     if num % 2 == 0:
#         result ="it is an even num"
#     else:
#         result = "it is an odd num"
#     return result 
# output_of_function = even_or_odd (num) 
# print(output_of_function)     




# def pizza(crust, *topping):
#     print("you have ordered a pizza with" , crust , "crust and the following topping:")
#     for each in topping:
#         print(each)
# pizza("thick" , "green olive" ,"chicken" , "black olives" , )




def pizza(crust, **topping):
     print("you have ordered a pizza with" , crust , "crust and the following topping:")
     for key,value in topping.items():
        print(key , ":" , value)
pizza("thick" , topping1 = "green olive" , topping2 = "chicken" , topping3 = "black olives" , )


# toppings = {topping1 = "green olives" , topping2 = "chicken" , topping3 = "black olives"}
