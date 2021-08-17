#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:

    # constructor
    def __init__(self, type, name, sound):
        # object variables The underscore does not encourrage users to access this methods
        self._type = type
        self._name = name
        self._sound = sound

        # if we dont know the argumens we can change the values to **Kwartds
        def __init__(self, **kwargs):
            # object variables The underscore does not encourrage users to access this methods and we can give them defould values
            self._type = kwargs["type"] if "type" in kwargs else "kitten"  # this gives default value
            self._name = kwargs["name"]
            self._sound = kwargs["sound"]

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound


def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(
        o.type(), o.name(), o.sound()))


def main():
    a0 = Animal('kitten', 'fluffy', 'rwar')
    a1 = Animal('duck', 'donald', 'quack')
    s2 = Animal(type="animal",name="hjdhd",sound="ghug")
    print_animal(s2)
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal('velociraptor', 'veronica', 'hello'))


if __name__ == '__main__':
    main()
