#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[str.index('obj') : str.index('l')] + str[str.index('with') : str.index('with') + 5]  + str[0:6]
print(str)
