# Creating my first function

def calculate():
  print("Hello, Texas!")

calculate()


# With arguments
def combine(fname, lname):
    print(fname + " " + lname)
    
# Calling the function
combine("john", "Doe")


# With Parameters
def combineNames(fname="John", lname="Doe"):
    print(fname + " " + lname)

# Calling the function
combineNames()


def square(number):
  output = number*number
  return output

def display():
  value = square(7)
  print(f"Hello user the square number is {value}")

display()




