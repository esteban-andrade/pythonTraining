# Use lambdas as in-place functions


def CelsisusToFahrenheit(temp):
    return (temp * 9/5) + 32


def FahrenheitToCelsisus(temp):
    return (temp-32) * 5/9


def main():
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    # TODO: Use regular functions to convert temps
    print(list(map(FahrenheitToCelsisus, ftemps)))
    print(list(map(CelsisusToFahrenheit,ctemps)))

    # TODO: Use lambdas to accomplish the same thing
    print(list(map(lambda x: (x * 9/5) + 32, ctemps)))
    print(list(map(lambda y: (y-32) * 5/9, ftemps)))


if __name__ == "__main__":
    main()
