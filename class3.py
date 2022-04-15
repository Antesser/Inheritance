class A:
    def a(self):
        print("A")

class B:
    def a(self):
        print("B")

class C(B):
    def a(self):
        print("C")

class D(C, A):#сначала ищет в C, потом по линии наследования класса C, потом в класс A.
    def a(self):
        super(C, self).a() #super(C, self) - от какого класса искать, те метод а() класса C не используется, мы увидим класс B
        # print(self.__class__.__mro__) #как именно питон будет искать метод наследуемых классов, поиск в глубину.

#полиморфизм - разные способы реализации одного и того же, условный метод a в одном классе может делать что-то другое, чем такой же метод а в другом классе

D().a()







class Verification:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__lenPassword()

    def __lenPassword(self):
        if len(self.password) < 8:
            raise ValueError("weak password")

    def save(self):
        with open("users", "a") as r:
            r.write(f"{self.login, self.password}" + "\n")            