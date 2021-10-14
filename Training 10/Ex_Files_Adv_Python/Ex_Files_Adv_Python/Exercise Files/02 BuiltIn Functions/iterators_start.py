# use iterator functions like enumerate, zip, iter, next


def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # TODO: use iter to create an iterator over a collection
    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))

    # TODO: iterate using a function and a sentinel

    with open("testfile.txt","r") as fp:
        for line in iter(fp.readline,""):
            print(line)

    # TODO: use regular interation over the days

    for j in range(len(days)):
        print(j+1,days[j])

    # TODO: using enumerate reduces code and provides a counter
    for i,j in enumerate(days,start=1):
        print(i,j)


    # TODO: use zip to combine sequences
    for z in zip(days,daysFr):
        print(z) # returns a tuple


    for i,j in enumerate(zip(days,daysFr),start=1):
        print(i,j[0]+" is equal to "+j[1])


if __name__ == "__main__":
    main()
