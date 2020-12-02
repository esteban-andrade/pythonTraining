#
# Example file for working with conditional statements
#


def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else
    if(x<y):
        result = "x is less than y"
    elif(x==y):
        result = "x is same as y"
    else:
        result="x is greater than y"

    print(result)


    # conditional statements let you use "a if C else b"

    result = "x is less than y" if (x < y) else "x is greater or same as y"
    print (result)


if __name__ == "__main__":
    main()
