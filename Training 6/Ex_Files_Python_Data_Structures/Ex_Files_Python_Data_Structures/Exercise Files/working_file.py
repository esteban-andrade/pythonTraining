def starting():
    dictionary = {"key1": 1, "key2": 2}

    print(dictionary)

    # Assign new Value to key
    dictionary["key1"] = 3
    print(dictionary)

    # Add new Value and Key
    dictionary["key3"] = 4
    print(dictionary)

    # lenght is with lenght
    print(len(dictionary))

    # to eliminate value we use del
    del dictionary["key3"]
    print(dictionary)

    # to clear we use clear
    dictionary.clear()
    print(dictionary)


def iteration():
    diction = dict()
    diction = {"Quito": 123, "guaya": 4456, "cuenca": 890}

    if("Quito" in diction):
        print(diction["Quito"])
    else:
        print("not founf")

    for city in diction:
        print(diction[city])

    for city in diction:
        print(diction)

    if("sydney" not in diction):
        diction["sydney"] = 9875
    else:
        print("already found")

    print(diction)


def methods():
    diction = dict()
    diction = {"Quito": 123, "guaya": 4456, "cuenca": 890, "Sydney": 123456}

    # get is used to access the value from a dicttionary
    print(diction.get("Quito", "not found"))
    print(diction.get("Manta", "not found"))

    # List of all kets
    print(diction.keys())

    # values returns values
    print(diction.values())

    # items returns ketys and values
    print("Key Value pair")

    for i, j in diction.items():
        print("key {}\t  value {}".format(i, j))

    # Max return the key associated with largest value
    print(max(diction, key=diction.get))

    # min returns key with lowest value
    print(min(diction, key=diction.get))

    # pop(key, default) --> Returns  the value associated with the key. (Removed key value pair from the dictionary)
    print(diction)
    print("valued of key {}".format(diction.pop("guaya", "not fount")))
    print(diction)

    # popitem --> access and returns a ramdom key-value pair (removed the key value pair from the dictionary)
    print(diction.popitem())
    print(diction)

    # sorted sorts the element in the dictionary
    print(diction)
    print(sorted(diction.keys()))
    print(sorted(diction.values()))
    # copy makes a shallow copy of the diction COpyes memory not contents


def lists_and_dictionaries():
    eng_di = {}


# Adding lists as value
    eng_di['solitude'] = ['lone', 'lonely',
                          'alone', 'unaccompanied', 'without society']
    eng_di['hope'] = ['aspiration', 'desire',
                      'wish', 'expectation', 'ambition']
    print(eng_di)

 # Creating a dictionary with an empty list
    eng_di.clear()
    eng_di = {'solitude': []}
    eng_words = ['lone', 'lonely', 'alone', 'unaccompanied', 'without society']
    eng_di['solitude'].append(eng_words[0])
    eng_di['solitude'].append(eng_words)
    print(eng_di)

    eng_di['solitude'] = eng_words
    print(eng_di)

    if (eng_di.get('solitude')):
        for list_item in eng_di['solitude']:
            print(list_item)

    else:
        print("word not in dictionary")


def comprenhension():
    sal_data_keys = ["Austin", "Portland", "Dallas", "Atlanta"]

    sal_data_values = [91185, 110123, 89123, 112000]

    sal_info = {}
    print("#### Creating a dictionary without using comprehension")
    for key, value in zip(sal_data_keys, sal_data_values):
        sal_info[key] = value
    print(sal_info)

    #Using Dictionary Comprehension to popultate the dictionary
    print("\n Creating dictionary using comprenhension")

    sal_info={sal_data_keys[index]:sal_data_values[index] for index in range(0,len(sal_data_keys))}
    print(sal_info)

    #alternate to filtering the dictionary using a for loop


    sal_100k = {}
    for k in sal_info:
        if sal_info[k] > 100000:
            sal_100k[k] = sal_info[k]

    print(sal_100k)

    #filtering through the dictionary using comprehension
    sal_100k = {K:V for K,V in sal_info.items() if V >100000}
    print(sal_100k)

def main():

    comprenhension()


if __name__ == "__main__":
    main()
