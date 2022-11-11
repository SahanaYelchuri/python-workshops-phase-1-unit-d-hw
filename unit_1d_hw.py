'''
In this file you will fill in each function.

Only edit where it says it is okay to edit. Altering the rest 
of the code may result in false failures. If you have trouble please
reach out to your instructor. :)
'''

'''

For Unit 1D you will practice what you learned below:

- Functions 
    - Creating a function
    - Returning a value (including void)
    - Creating parameters for function
    - Default arguments
    - Multiple returns

- Classes
    - Creating an object 
    - Creating the init function
    - setting attributes with the init function
    - Creating more functions in the same class

'''

#### Create a Function Below! ####
'''
Create a function called useless_function(), have it return None

Hint: Syntax to create a function:
'''

def useless_function():
    return None



##################################

#### Create a Function Below ####
'''
Create a function called integer_return_5() that returns the integer 5

'''
def integer_return_5():
    return 5

##################################

#### Create a Function Below ####
'''
Create a function called string_return_I_am_a_string() that returns the string "I am a string!"

'''
def string_return_I_am_a_string():
    return "I am a string!"
##################################

#### Create a Function Below ####
'''
Create a function called add_one(), that takes in a parameter x, adds 1 then returns the value

'''
def add_one(x):
    return x+1
##################################


#### Create a Function Below ####
'''
Create a function called add_x_y, that takes in a parameter x, and a parameter y, adds x and y then returns that value

'''
def add_x_y(x,y):
    return x+y
##################################


#### Create a Function Below ####
'''
Create a function called slope_intercept_function, that takes in parameters, m, x and b. Where:

:param m: (float) The slope to scale the the list x
:param x: (list) The list of values we want to scale and shift based on m and b
:param b: (float) The intercept to shift the values of x

Have the function scale each value of x then add b and store the result back into x.

Have the function return x

Hint: Use a for loop to iterate through the list
'''
def slope_intercept_function(m:float,x:list,b:float):
    y=[]
    i=0
    while i<len(x):
        q=x[i]*m+b
        i=i+1
        y.append(q)
    return y


##################################



#### Create a Function Below ####
'''
Create a function called multi_return, that takes in parameters, x and y

:param x: (int) Integer passed in, scaled by 5 and returned
:param y: (int) Integer passed in, incremented by 2 and returned

Have the function scale the of x by 5 and add 2 to y. 

Have the function return x and y in that order. 

'''
def multi_return(x,y):
    x=5*x
    y=y+2
    return x,y
##################################


#### Create a Function Below ####
'''
Create a function called default_args, that takes in a list x, and a parameter pre_pend


:param x: (list) List we want to prepend onto
:param pre_pend = 5: (int) Integer we would like to prepend to the list x
:return x: (list) List after prepend

Have the default value for pre_pend be 5. Have the function prepend the value pre_pend to the list x.

Return the list x.

Hint: Look up some methods you can use with a list to help you!
'''

##################################
def default_args(x, pre_pend=5):
    x=[pre_pend]+x
    return x

##### Create a Class Below #######
'''
Create a class called Car, create an __init__ method (constructor) that takes in 
miles_per_gallon, and assigns it to the attribute `mpg`.

'''
class Car:
    def __init__(self,miles_per_gallon):
        self.mpg=miles_per_gallon
        
##################################

##### Create a Class Below #######
'''
Create a class called Dog, create an __init__ method (constructor) that takes in breed, and assigns
it to the attribute `breed`. Have __init__ also take in weight, an assign it to the attribute `weight`.

Then create a method (aka class function) called `get_breed`. It should return the
`breed` attribute. 

Then create a method called `get_weight`. It should return the `weight` attribute.

Note: The get_x functions should not have an input. Ex: def get_weight(self):

'''

##################################
class Dog:
    def __init__(self,breed,weight):
        self.breed=breed
        self.weight=weight  
    def get_breed(self):
        return self.breed 
    def get_weight(self):
        return self.weight
        
##### Create a Class Below #######
'''
Create a class called Math_Operations

Create a method called add, that takes in a and b, adds them together (a+b) and returns the value. 

Create a method called sub, that takes in a and b, then subtracts b from a (a-b), and returns the value.

Create a method called slope_intercept, that takes in an m, x, and b. Then 
returns the output based on the slope equation (y = m * x + b)

Create a method called pythagorean, which takes in a and b, squares a and b, takes the sum then returns 
the square roots the summed values. (output = sqrt(a^2 + b^2))

HINT: Use ** instead of ^ for python exponents.
HINT HINT: You can raise variable and numbers to a fractional (or decimal) exponent for roots!
Note: Even though we will not be using self in this class, dont forget to include it as the first
argument in the method definitions. 
'''
class Math_Operations:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
            return a-b
    def slope_intercept(self,m,x,b):
        return m*x+b
    def pythagorean(self,a,b):
        return(a**2 + b**2)**(1/2)
 
if __name__ == "__main__":
    print("Test your functions at the bottom of this file!")
    pass