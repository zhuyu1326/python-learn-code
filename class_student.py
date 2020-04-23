#!/usr/bin/python3
# -*- conding: utf-8 -*-

'''
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
'''
class Student(object):
    def __init__(self, name, gender):
        self.__name = name 
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('chenggong')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('shibai')
    else:
        print('chenggong')
