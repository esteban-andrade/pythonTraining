# Use standard library functions to search strings for content


sampleStr = "The quick brown fox jumps over the lazy dog"

# startsWith and endsWith functions
print(sampleStr.startswith("The"))
print(sampleStr.startswith("the"))
print(sampleStr.endswith("dog"))


# the find and rfind functions
# Starts searching from left Returns index value of where the element is located
print(sampleStr.find("the"))
print(sampleStr.rfind("the"))  # starts searching from the right


# returns true or false whether things are located in the right order
print("the" in sampleStr)


# using replace
newStr = sampleStr.replace("lazy", "tired")  # replaces lazy with tired
print(newStr)


# counting instances of substrings
print(sampleStr.count("over"))
