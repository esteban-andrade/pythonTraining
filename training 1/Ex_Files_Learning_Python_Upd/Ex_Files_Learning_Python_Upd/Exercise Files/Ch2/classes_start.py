#
# Example file for working with classes
#

class myClass():
    def method1(self):
        print("myClass method 1")
    
    def method2(self,someString):
        print ("myClass Method 2 "+ someString)


class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("Another Class")

    def method2(self,someString):
        print("Another class method 2 " + someString)
    

def main():
    c = myClass()
    c.method1()
    c.method2("test")

    c2=anotherClass()
    c2.method1()
    c2.method2( "test")


if __name__ == "__main__":
    main()
