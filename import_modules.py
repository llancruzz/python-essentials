
# to use a module, we must import it first using the import keyworkd
import random

random.randint(1, 6)
#3


# Use the 'as' keyword to import a module and give it a custom name in your script
import random as rand

rand.randint(1, 6)
#4

# Use the from <module> import <method> syntax to import specific pieces of a module
from random import randint

randint(1, 6)
#2

# we can import all pieces of a module individually using import *
# However this usualy not the best approach to importing Avoid it!

from random import *

randint(1, 6)

#2