# 
# Example file for variables
#

# Declare a variable and initialize it
f = 0
print(f)


# re-declaring the variable works
f= "ABC"
print(f)

# ERROR: variables of different types cannot be combined
print ("This is a string " + str(123))


# Global vs. local variables in functions
def somefunction():
    global f #makes the variable global in the entire code 
    f = "def" # inside local copy of value f is diff than first one
    print (f)

somefunction()
print(f)

#to
del f #use to undefine the variable
print(f)
