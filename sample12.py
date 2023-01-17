# single inheritance example:

class Father:
    def __init__(self):
        print('father class constructor execution')
    def show(self):
        print("father class method execution")
class Son(Father):
    def __init__(self):
        print('child class constructor execution')
    def disp(self):
        print('child class method execution')
s=Son()
s.show()
s.disp()

print("|||  above example is single inheritance example")

print()

# multilevel inheritance:

class Father:
    def __init__(self):
        print("parent class constructor execute")
    def show(self):
        print("parent class method execute")
class Son(Father):
    def __init__(self):
        super().__init__()
        print("son class constructor execute")
    def sho(self):
        print("son method execute")
class Grandson(Son):
    def __init__(self):
        super().__init__()
        print("grandson class constructor execute")
    def sh(self):
        print("grandson method execute")
g=Grandson()
g.show()
g.sho()
g.sh()

print("|||  above example is multilevel inheritance example")
print()
# hierarchical inheritance:

class Father:
    def __init__(self):
        print("parent class constructor execute")
    def show(self):
        print("parent class method execute")
class Son(Father):
    def __init__(self):
        super().__init__()
        print("son class constructor execute")
    def sho(self):
        print("son method execute")
class Daughter(Father):
    def __init__(self):
        super().__init__()
        print("daughter class constructor execute")
    def sh(self):
        print("daughter method execute")
d=Daughter()
d.show()
d.sh()

s=Son()
s.show()
s.sho()

print("|||  above example is hierarchical inheritance example")
print()

# multiple inheritance:

class Father:
    def __init__(self):
        super().__init__()
        print("father class constructor execution")
    def sh(self):
        print("father class method execution")
class Mother:

    def __init__(self):
        super().__init__()
        print("Mother class constructor execution")
    def sho(self):
        print("Mother class method execution")
class Son(Father,Mother):
    def __init__(self):
        super().__init__()
        print("son class constructor execution")
    def show(self):
        print("son class method execution")
s=Son()
s.sh()
s.sho()
s.show()

print("|||  above example is multiple inheritance example")
print()


