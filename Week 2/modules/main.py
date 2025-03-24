"""
1. Code reusability
2. Modularity 
3. Maintainability
4. Collaborate

"""

import my_module
# Import specific items
from my_module import greet
# renaming calling the module
import my_module as mm

print(my_module.greet("Alice"))
print(my_module.PI)
print(greet("Bob"))
print(mm.greet("Charlie"))

# Inbuilt modules:
from math import *
import random
print(sqrt(16))
