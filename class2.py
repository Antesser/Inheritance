from class3 import Verification
# from tkinter import Tk, Button

class V2(Verification): #создаём новый класс, в скобках указываем имя наследуемого класса.
    #pass #pass нужен, когда требуется оператор ради синтаксиса, но что-то новое исполнять не нужно.

    def __init__(self, login, password, age):
        super().__init__(login, password) #super() метод, осуществляющий автоматический поиск методов в родительских классах, не нужно указывать имя метода родительского класса
        self.save()
        self.age = age
    
    def __save(self):#переопределили существующий метод, инкапсулируем двумя нижними подчёркиваниями методы, которые не используются(вызываются) извне
        with open("users") as r:
            for i in r:
                if f"{self.login, self.password}" + "\n" == i:
                    raise ValueError("Такой пользователь уже есть")
        super().save() #принудительно вызываем метод save из родительского класса Verification для сохранения пользователя из переопределённого метода выше 
    
    def show(self): #добавили новый метод
        return self.login, self.password

x = V2("Bob","124123432243",44)        



# class My_app(Tk): #композиция - когда мы запускаем в нашем классе другой класс

#     def __init__(self): #переопределяем метод init
#         Tk.__init__(self) #принудительно вызываем конструктор из класса Tk
#         self.geometry("400x400")
#         self.setUI()

#     def setUI(self):
#         Button(self, text = "OK").pack()    


# root = My_app()
# root.mainloop() 
