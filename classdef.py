# class Employee:
#     def __init__(self,first,last,phone):
#         self.first=first
#         self.last=last
#         self.email=first +'.'+last+'@gmail.com'
#         self.phone=phone
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)



# emp1=Employee('ebin','baby','9538117238')
# emp2=Employee('thenu','jose',8606565773)

# print(emp1.fullname())
# print(emp2.fullname())
# print(Employee.fullname(emp1))
# print(Employee.fullname(emp2))
# '''instance variables contains data that is unique to each instance'''

# # print(emp1)
# # print(emp2)
# # emp1.first='Ebin'
# # emp1.last='Baby'
# # emp1.email='ebi.baby92@gmail.com'
# # emp1.phone='9538117238'
# # emp2.first='Thenu'
# # emp2.last='Jose'
# # emp2.email='thenu.jose@gmail.com'
# # emp1.phone='8606565773'
# print(emp1.email)
# print(emp2.email)

# class Jeeps:
#     num_of_jeeps=0
#     depreciation=0.033
#     def __init__(self,manufacturer,year,model,price):
#         self.manufacturer=manufacturer
#         self.year=year
#         self.model=model
#         self.price=price
#         Jeeps.num_of_jeeps+=1

#     def age(self):
#         return '{} is {} years old'.format(self.model,(2020-self.year))
#     def current_value(self):
#         self.price=self.price-(self.price*self.depreciation)
#     @classmethod
#     def set_depreciation(cls,amt):
#         cls.depreciation = amt
#     @classmethod
#     def from_string(cls,jstring):
#         manufacturer,year,model,price = jstring.split('-')
#         return cls(manufacturer,year,model,price)

# jstring1='Mahindra-2010-thar-800000'
# vehicle1=Jeeps('Willys',1969,'CJ3B',300000)
# vehicle2=Jeeps('Willys',1979,'CJ5B',350000)
# vehicle2=Jeeps('Mahindra',1986,'CJ500D',268765)
# vehicle2=Jeeps('Mahindra',1990,'CL500DI',156000)
# vehicle3=Jeeps('Mahindra',1995,'CL500MD',132000)
# vehicle4=Jeeps('Mahindra',1997,'CL500MDI',178000)
# vehicle5=Jeeps('Mahindra',1999,'CL550MDI',400000)
# vehicle6=Jeeps('Mahindra',2000,'Major',550000)
# vehicle7 = Jeeps.from_string(jstring1)
# print(vehicle7.manufacturer)

# # print(vehicle1.price)
# # vehicle1.current_value()
# # print(vehicle1.price)
# # vehicle1.depreciation=0.0599
# print(vehicle1.__dict__)
# # print(Jeeps.__dict__)
# vehicle2.set_depreciation(3722)
# print(Jeeps.depreciation)
# print(vehicle1.depreciation)
# print(vehicle5.depreciation)
# print(vehicle4.depreciation)


# ###### Static Methods #############

# class Companies():
#     def __init__(self,name,incodate,loc,sal):
#         self.name=name
#         self.incodate=incodate
#         self.loc=loc
#         self.sal=sal
#     @staticmethod
#     def isworkday(day):
#         if day.weekday() ==5 or day.weekday() == 6:
#             return False
#         return True
# import datetime as dt
# check_date = dt.date(2020,6,6)
# print(Companies.isworkday(check_date))


############ Class Inheritance #############

#Creating a class to manage the employees for different companies

class Folks():
    hike=1.10
    def __init__(self,first,last,desig,sal):
        self.first=first
        self.last=last
        self.email=first+'.'+last+ '@'+self.__class__.__name__+'.com'
        self.desig=desig
        self.sal=sal
    def salhike(self):
        self.sal=(self.sal*self.hike)

class LTI(Folks):
    pass
class Synup(Folks):
    hike=1.30
    def __init__(self,first,last,desig,sal,place):
        super().__init__(first,last,desig,sal)
        self.place=place

class Manager(Folks):
    def __init__(self,first,last,desig,sal,subordinates=None):
        super().__init__(first,last,desig,sal)
        self.subordinates=subordinates
        if subordinates is None:
            self.subordinates=[]
        else:
            self.subordinates=subordinates
    def hire(self,subordinates):
        if subordinates not in self.subordinates:
            self.subordinates.append(subordinates)

    def fire(self,subordinates):
        if subordinates in self.subordinates:
            self.subordinates.remove(subordinates)

    def print_subs(self):
        for sub in self.subordinates:
            print('-->',sub.email)



e1=Synup('ebin','baby','Data Scientist',150000,'wayanad')
e2=LTI('ebin','baby','software engineer',100000)
su1=Manager('Ebin','Baby','Manager',500000,[e1])

# su1.hire(e2)
# su1.fire(e2)
# su1.print_subs()


# print(e1.email)
# print(e2.email)
# print(e1.sal)
# print(e2.sal)
# e1.salhike()
# e2.salhike()
# print(e1.sal)
# print(e2.sal)


############ isinstance(), issubclass()###############

# print(isinstance(su1,LTI))
print(issubclass(LTI,LTI))


######### Special methods/ Majic Methods ##########
'''
__repr__ --> an unambiguous representation of the oblect and is used for debugging, logging etc..
__str__ --> readable representation of an object. used as a display
'''
class College():
    def __init__(self,dept,name,usn,fees):
        self.dept=dept
        self.name=name
        self.usn=usn
        self.fees=fees
    def fullname(self):
        return self.name+self.dept

    def __repr__(self):
        return "College('{}','{}','{}')".format(self.dept,self.name,self.usn)
    def __str__(self):
        return '{}'.format(self.fullname())
    def __add__(self,other):
        return self.fees + other.fees
    def __len__(self):
        return len(self.name)


s1=College('Aero','Ebin','1NT11AE010',200000)
s2=College('Aero','Midhun','1NT11AE022',150000)
print(s1+s2)
print(len(s2))
print(len(s1))


