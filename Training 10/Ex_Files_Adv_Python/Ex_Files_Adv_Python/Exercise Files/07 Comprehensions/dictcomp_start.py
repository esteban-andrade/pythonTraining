# Demonstrate how to use dictionary comprehensions


def main():
    # define a list of temperature values
    ctemps = [0, 12, 34, 100]

    # TODO: Use a comprehension to build a dictionary
    tempsDictionary = {k:(k*9/5)+32 for k in ctemps}
    print(tempsDictionary)
    tempsDictionary = {k: (k*9/5)+32 for k in ctemps if k <100}
    print(tempsDictionary)
    print(tempsDictionary.get(12))
    print(tempsDictionary[12])


    # TODO: Merge two dictionaries with a comprehension
    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}
    newTeam = {k:v for team in (team1,team2)for k,v in team.items()}
    print(newTeam)


if __name__ == "__main__":
    main()
