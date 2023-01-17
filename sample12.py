# single inheritance example:

# class Father:
#     def __init__(self):
#         print('father class constructor execution')
#     def show(self):
#         print("father class method execution")
# class Son(Father):
#     def __init__(self):
#         print('child class constructor execution')
#     def disp(self):
#         print('child class method execution')
# s=Son()
# s.show()
# s.disp()


# multilevel inheritance:

# class Father:
#     def __init__(self):
#         print("perent class constructor execute")
#     def show(self):
#         print("perent class method execute")
# class Son(Father):
#     def __init__(self):
#         super().__init__()
#         print("son class constructor execute")
#     def sho(self):
#         print("son method execute")
# class Grandson(Son):
#     def __init__(self):
#         super().__init__()
#         print("grandson class constructor execute")
#     def sh(self):
#         print("grandson method execute")
# g=Grandson()
# g.show()
# g.sho()
# g.sh()

# hierachical inheritance:

# class Father:
#     def __init__(self):
#         print("perent class constructor execute")
#     def show(self):
#         print("perent class method execute")
# class Son(Father):
#     def __init__(self):
#         super().__init__()
#         print("son class constructor execute")
#     def sho(self):
#         print("son method execute")
# class Daughter(Father):
#     def __init__(self):
#         super().__init__()
#         print("daughter class constructor execute")
#     def sh(self):
#         print("daughter method execute")
# d=Daughter()
# d.show()
# d.sh()
#
# s=Son()
# s.show()
# s.sho()


# multiple inheritance:

# class Father:
#     def __init__(self):
#         super().__init__()
#         print("father class constructor execution")
#     def sh(self):
#         print("father class method execution")
# class Mother:
#
#     def __init__(self):
#         super().__init__()
#         print("Mother class constructor execution")
#     def sho(self):
#         print("Mother class method execution")
# class Son(Father,Mother):
#     def __init__(self):
#         super().__init__()
#         print("son class constructor execution")
#     def show(self):
#         print("son class method execution")
# s=Son()
# s.sh()
# s.sho()
# s.show()

# class P:
#     def __init__(self,ename,eno,esal):
#         self.ename=ename
#         self.eno=eno
#         self.esal=esal
#     def display(self):
#         print(self.ename)
#         print(self.eno)
#         print(self.esal)
# class C:
#     def modify(self):
#         self.esal=self.esal+23000
#         self.display()
# s=P("durga",12,12000)
# C.modify(s)


# inner class ex:

# class Emp:
#     def __init__(self):
#         self.name="vijay"
#         self.db=self.Dob()
#     def display(self):
#         print("name=",self.name)
#     class Dob:
#         def __init__(self):
#             self.date=15
#             self.month=8
#             self.year=1947
#         def shoe(self):
#             print("the dob is:",f"{self.date}/{self.month}/{self.year}")
# e=Emp()
# e.display()
# x=e.db
# x.shoe()


