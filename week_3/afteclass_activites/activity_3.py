# use static method to rewrite Factorial class
class Factorial:
  @staticmethod
  # Define a method to calculate factorial of given number
  def factorial(num1): 
    result = 1  # Initialized before the loop to store the product.
    for i in range(1, num1 + 1):
        result *= i
    return result
  
  @staticmethod
  # Define a method to check prime
  def check_Prime(num1): 
    if num1 < 2:  # 0 and 1 are not prime numbers
        return False
    for i in range(2, int(num1 ** 0.5) + 1): # Check up to the square root of num1 and int to make it not show decimal values
        # Check if num1 is divisible by i 
        if num1 % i == 0:
            return False
    return True
  
  @staticmethod
  # define a method to show the factorial result and the check prime result
  def display(num1):  
    print("Factorial of", num1, "is", Factorial.factorial(num1)) # show factorial result
    # show check prime result
    if Factorial.check_Prime(num1):
        print(f"{num1} is a prime number.")
    else:
        print(f"{num1} is not a prime number.")

 
# Call the display method to call show the result
Factorial.display(2)
Factorial.display(10)