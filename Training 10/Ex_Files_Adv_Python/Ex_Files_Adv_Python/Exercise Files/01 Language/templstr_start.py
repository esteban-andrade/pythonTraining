# demonstrate template string functions

from string import Template


def main():
    # Usual string formatting with format()
    str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)
    
    # TODO: create a template with placeholders
    template_ = Template(" YOu are lol ${first} and ${second}")
    
    # TODO: use the substitute method with keyword arguments
    subs = template_.substitute(first="Lmao",second = "meme")

    print(subs)
    
    # TODO: use the substitute method with a dictionary

    data = {

        "first":"Lmao",
        "second":"meme"
    }

    string3 = template_.substitute(data)
    print(string3)

    
if __name__ == "__main__":
    main()
    