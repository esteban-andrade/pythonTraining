#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while(x<5):
    print(x)
    x=x+1


  # define a for loop # its like an iterator. starts on the first
  for x in range(5,10):
    print (x)

  # use a for loop over a collection'
  days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  for d in days:
    print(d)

  
  # use the break and continue statements
  for x in range(5, 10):
    if (x == 7): break
    print(x)

  for x in range(5, 10):
      #if (x == 7): break
   if (x % 2 == 0): continue # to skip the elements in the condition but iterate the other ones
   print(x)


  #using the enumerate() function to get index 
  days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  for i, d in enumerate(days): #enumerate will return the number of the index number in question
    print(i, d)
  
if __name__ == "__main__":
  main()
