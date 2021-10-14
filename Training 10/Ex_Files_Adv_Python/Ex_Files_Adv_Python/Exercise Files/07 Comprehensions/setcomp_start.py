# Demonstrate how to use set comprehensions


def main():
    # define a list of temperature data points
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    # TODO: build a set of unique Fahrenheit temperatures
    fare_temps_list = [(t*9/5)+32 for t in ctemps]  # list
    fare_temps_set = {(t*9/5)+32 for t in ctemps}

    print(fare_temps_list)
    print(fare_temps_set)

    # TODO: build a set from an input source
    sTemp = "The quick brown fox jumped over the lazy dog"
    chars = {c.upper() for c in sTemp if not c.isspace()}
    print(chars)


if __name__ == "__main__":
    main()
