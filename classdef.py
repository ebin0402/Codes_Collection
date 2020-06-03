class Employee:
    def __init__(self,first,last,phone):
        self.first=first
        self.last=last
        self.email=first +'.'+last+'@gmail.com'
        self.phone=phone
    def fullname(self):
        return '{} {}'.format(self.first,self.last)



emp1=Employee('ebin','baby','9538117238')
emp2=Employee('thenu','jose',8606565773)

print(emp1.fullname())
print(emp2.fullname())
print(Employee.fullname(emp1))
print(Employee.fullname(emp2))
'''instance variables contains data that is unique to each instance'''

# print(emp1)
# print(emp2)
# emp1.first='Ebin'
# emp1.last='Baby'
# emp1.email='ebi.baby92@gmail.com'
# emp1.phone='9538117238'
# emp2.first='Thenu'
# emp2.last='Jose'
# emp2.email='thenu.jose@gmail.com'
# emp1.phone='8606565773'
print(emp1.email)
print(emp2.email)

class Jeeps:
    num_of_jeeps=0
    depreciation=0.033
    def __init__(self,manufacturer,year,model,price):
        self.manufacturer=manufacturer
        self.year=year
        self.model=model
        self.price=price
        Jeeps.num_of_jeeps+=1

    def age(self):
        return '{} is {} years old'.format(self.model,(2020-self.year))
    def current_value(self):
        self.price=self.price-(self.price*self.depreciation)
    @classmethod
    def set_depreciation(cls,amt):
        cls.depreciation = amt
    @classmethod
    def from_string(cls,jstring):
        manufacturer,year,model,price = jstring.split('-')
        return cls(manufacturer,year,model,price)

jstring1='Mahindra-2010-thar-800000'
vehicle1=Jeeps('Willys',1969,'CJ3B',300000)
vehicle2=Jeeps('Willys',1979,'CJ5B',350000)
vehicle2=Jeeps('Mahindra',1986,'CJ500D',268765)
vehicle2=Jeeps('Mahindra',1990,'CL500DI',156000)
vehicle3=Jeeps('Mahindra',1995,'CL500MD',132000)
vehicle4=Jeeps('Mahindra',1997,'CL500MDI',178000)
vehicle5=Jeeps('Mahindra',1999,'CL550MDI',400000)
vehicle6=Jeeps('Mahindra',2000,'Major',550000)
vehicle7 = Jeeps.from_string(jstring1)
print(vehicle7.manufacturer)

# print(vehicle1.price)
# vehicle1.current_value()
# print(vehicle1.price)
# vehicle1.depreciation=0.0599
print(vehicle1.__dict__)
# print(Jeeps.__dict__)
vehicle2.set_depreciation(3722)
print(Jeeps.depreciation)
print(vehicle1.depreciation)
print(vehicle5.depreciation)
print(vehicle4.depreciation)


###### Static Methods #############

class Companies():
    def __init__(self,name,incodate,loc,sal):
        self.name=name
        self.incodate=incodate
        self.loc=loc
        self.sal=sal
    @staticmethod
    def isworkday(day):
        if day.weekday() ==5 or day.weekday() == 6:
            return False
        return True
import datetime as dt
check_date = dt.date(2020,6,6)
print(Companies.isworkday(check_date))