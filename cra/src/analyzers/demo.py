import os  # Unused import
import sys  # Unused import

def badFunctionName():  # Incorrect function name (not snake_case)
    VAR = "Hello"  # Variable name should be lowercase (PEP 8)
    print(VAR)

class Myclass:  # Class name should be PascalCase
    def __init__(self, val):
        self.VAL = val  # Variable should be lowercase
        if self.VAL > 0:
            if self.VAL > 10:
                if self.VAL > 20:
                    print("Too deep nesting!")  # Too many nested blocks

    def unused_method(self):
        pass  # Unused method (should be removed or implemented)

def isPositive(num):
    if num > 0:
        return True
    else:
        return False  # Can be simplified
    
def very_complex_function(x):
    if x > 0:
        if x > 5:
            if x > 10:
                if x > 15:
                    if x > 20:
                        return True
    return False

user_input = "os.system('rm -rf /')"  # Security risk: eval injection
eval(user_input)  # Dangerous function usage
very_complex_function(29)
