# Use special methods to compare objects to each other


class Employee():
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsService

    # TODO: implement comparison functions by emp level
    def __ge__(self, other): # greater or equal to

        if self.level ==other.level:
            return self.seniority >= other.seniority
        return self.level >=other.level
        

    def __gt__(self, other): # greater than
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.level > other.level

    def __lt__(self, other): # less than
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.level < other.level

    def __le__(self, other): # less or equal
        if self.level == other.level:
            return self.seniority <= other.seniority
        return self.level <= other.level

    def __eq__(self, other): # equal
        return self.level == other.level


def main():
    # define some employees
    dept = []
    dept.append(Employee("Tim", "Sims", 5, 9))
    dept.append(Employee("John", "Doe", 4, 12))
    dept.append(Employee("Jane", "Smith", 6, 6))
    dept.append(Employee("Rebecca", "Robinson", 5, 13))
    dept.append(Employee("Tyler", "Durden", 5, 12))

    # TODO: Who's more senior?
    print(bool(dept[0] > dept[2]))
    print(bool(dept[4] < dept[3]))

    # TODO: sort the items
    employees = sorted(dept)
    for employee in employees:
        print(employee.lname)


if __name__ == "__main__":
    main()
