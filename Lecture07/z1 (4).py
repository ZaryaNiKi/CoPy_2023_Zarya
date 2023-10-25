import math

class Dual:
    """
        Класс дуальных чисел.
        Пусть x = a + eps*b -- дуальное число,
              где a,b -- вещественные числа,
                  theta -- элемет типа: theta**2 = 0
        Удобное обозначение числа x := (a,b).
    """
    ############################################################################
    ######### Конструктор
    ############################################################################
    def __init__(self):
        """
        __init__ -- "конструктор". Создаёт тривиальное дуальное число.
        """
        self.a, self.b = 0, 0

    ############################################################################
    ######### Ввод и вывод дуальных чисел.
    ############################################################################
    def Dual_Input(self):
        """
        Dual_Input -- метод, который вводите число.
        """
        while True:
              try:
                  a = int(input("Ведите первое число a (x = a + eps*b): "))
                  b = int(input("Ведите первое число b (x = a + eps*b): "))
                  self.a, self.b = a, b
                  break
              except ValueError:
                  print("Что-то нето введли")
    def Dual_Print(self):
        """
        Dual_Input -- метод, который выводит дуальное число.
        """
        if (self.a != 0):
            if   (self.b > 0):
              print(f"Dual number = {self.a} + eps {self.b}")
            elif (self.b < 0):
              print(f"Dual number = {self.a} - eps {abs(self.b)}")
            elif (self.b == 0):
              print(f"Dual number = {self.a}")
        else:
            if   (self.b > 0):
              print(f"Dual number =  eps {self.b}")
            elif (self.b < 0):
              print(f"Dual number = - eps {abs(self.b)}")
            elif (self.b == 0):
              print(f"Dual number = 0 ")

    def Dual_Print_MatrixForm(self):
        """
        Dual_Print_MatrixForm -- метод, который выводит дуальное число в представлении матрицы.

        """
        matrix = [[self.a,self.b],[0,self.a]]
        for row in matrix:
            for element in row:
                print(element, end = ' ')
            print()
    ############################################################################
    ###### Линейные методы
    ############################################################################

    def Dual_Plus(self, other: Dual):#->Новое Dual число
        """
        Dual_Plus -- метод, который иницеализирует новый объект.
                     Складывает два числа.
        """
        var = Dual()
        (var.a, var.b) = (self.a + other.a, self.b + other.b)
        return var

    def Dual_Times_Const (self, const):#->Новое Dual число
        """
        Dual_Times_Const -- метод, который иницеализирует новый объект.
                            Домнажает на константу.
        """
        var = Dual()
        (var.a, var.b) = (const*self.a , const*self.b)
        return var


    def Dual_Minus(self, other):#->Новое Dual число
        """
        Dual_Minus -- метод, который иницеализирует новый объект.
                      Вычитает два числа.
        """
        var = Dual()
        var = self.Dual_Plus(other.Dual_Times_Const(-1))
        return var

    def Dual_Plus_Eq (self, other):#->Редактирует self, на новое Dual число
        """
        Dual_Plus_Eq -- метод, который иницеализирует новый объект.
                        Редактирует self на сумму self и other.
                        Складывает два дуальных числа.
        """
        (self.a, self.b) = (self.a + other.a, self.b + other.b)
        return self

    def Dual_Times_Const_Eq (self, const):#->Редактирует self, на новое Dual число
        """
        Dual_Times_Const_Eq -- метод, который иницеализирует новый объект.
                            Редактирует self на домнажение self и const.
                            Домнажает на константу.
        """
        (self.a, self.b) = (const*self.a , const*self.b)
        return self

    def Dual_Minus_Eq (self, other):#->Редактирует self, на новое Dual число
        """
        Dual_Minus_Eq -- метод, который иницеализирует новый объект.
                        Редактирует self на сумму self и other.
        """
        self = self.Dual_Plus(other.Dual_Times_Const(-1))
        return self
    ############################################################################
    ####### Умнажение и деление
    ############################################################################


    def Dual_Times(self, other):#->Новое Dual число
        """
        Dual_Times -- метод, который иницеализирует новый объект.
                      Умнажает два числа.
        """
        var = Dual()
        (var.a, var.b) = (self.a*other.a, self.b*other.a + self.a*other.b)
        return var

    def Dual_Divide(self, other):#->Новое Dual число
        """
        Dual_Divide -- метод, который иницеализирует новый объект.
                     Делит два числа.
        """
        var = Dual()
        (var.a, var.b) = (self.a/other.a, (self.b*other.a - self.a*other.b)/other.a**2)
        return var
    def Dual_Times_Eq(self, other):#->Новое Dual число
        """
        Dual_Times_Eq -- метод, который иницеализирует новый объект.
                      Умнажает два числа.
        """
        (self.a, self.b) = (self.a*other.a, self.b*other.a + self.a*other.b)
        return self

    def Dual_Divide_Eq(self, other):#->Новое Dual число
        """
        Dual_Divide_Eq -- метод, который иницеализирует новый объект.
                     Делит два числа.
        """
        (self.a, self.b) = (self.a/other.a, (self.b*other.a - self.a*other.b)/other.a**2)
        return self
################################################################################
####### Специальные функции
################################################################################
    def Dual_Sqrt(self, n):#->Новое Dual число
        """
        Dual_Sqrt -- метод, который иницеализирует новый объект.
                     Вычисляет корень n-ой степени.
        """
        if isinstance(n, int) and self.a != 0:
           var = Dual()
           (var.a, var.b) = (self.a**(1/n), n*self.b/(self.a**(n-1/n)))
           return var
        elif self.a  == 0:
           print("Формула при a = 0, не работает")
           var = Dual()
           return var
        else:
           return print("n -- не целое")
           var = Dual()
           return var

    def Dual_Abs(self):#->Новое Dual число
        """
        Dual_Abs -- метод, который иницеализирует новый объект.
                     Вычисляет модуль -- т.е. квадратный корень из квадрата числа.
        """
        return self.Dual_Times(self).Dual_Sqrt(2)
################################################################################
####### Тригонаметрические функции
################################################################################
    def Dual_Exp(self):#->Новое Dual число
        """
        Dual_Exp -- метод, который иницеализирует новый объект.
                     Вычисляет экспоненту.
        """
        var = Dual()
        (var.a, var.b) = (math.exp(self.a), math.exp(self.a)*self.b)
        return var

    def Dual_Sin(self):#->Новое Dual число
        """
        Dual_Exp -- метод, который иницеализирует новый объект.
                     Вычисляет экспоненту.
        """
        var = Dual()
        (var.a, var.b) = (math.sin(self.a), math.cos(self.a)*self.b)
        return var

    def Dual_Cos(self):#->Новое Dual число
        """
        Dual_Cos -- метод, который иницеализирует новый объект.
                     Вычисляет косинус дуального числа.
        """
        var = Dual()
        (var.a, var.b) = (math.cos(self.a), - math.sin(self.a)*self.b)
        return var

    def Dual_Sh(self):#->Новое Dual число
        """
        Dual_Exp -- метод, который иницеализирует новый объект.
                     Вычисляет экспоненту.
        """
        var = Dual()
        (var.a, var.b) = (math.sinh(self.a), math.cosh(self.a)*self.b)
        return var

    def Dual_Ch(self):#->Новое Dual число
        """
        Dual_Cos -- метод, который иницеализирует новый объект.
                     Вычисляет косинус дуального числа.
        """
        var = Dual()
        (var.a, var.b) = (math.cosh(self.a) ,  math.sinh(self.a)*self.b)
        return var

################################################################################
##### Показательное пременение класса
################################################################################
a = Dual()
b = Dual()
c = Dual()

a.Dual_Input()
print("#"*25)
a.Dual_Print()

b.Dual_Input()
print("#"*25)
b.Dual_Print()

c = a.Dual_Plus(b)
print("#"*25)
print(" "*10," a + b")
print("#"*25)
c.Dual_Print()

c = a.Dual_Minus(b)
print("#"*25)
print(" "*10," a - b")
c.Dual_Print()

c = a.Dual_Times(b)
print("#"*25)
print(" "*10," a * b")
print("#"*25)
c.Dual_Print()

c = a.Dual_Times(b)
print("#"*25)
print(" "*10," a / b")
print("#"*25)
c.Dual_Print()

c = a.Dual_Sqrt(2)
print("#"*25)
print(" "*10," a**(1/2)")
print("#"*25)
c.Dual_Print()

c = a.Dual_Abs()
print("#"*25)
print(" "*10," |a|")
print("#"*25)
c.Dual_Print()

print("#"*25)
print(" "*10," Matrix -- a")
print("#"*25)
a.Dual_Print_MatrixForm()

print("#"*25)
print(" "*10," exp(a)")
print("#"*25)
a.Dual_Exp().Dual_Print()

print("#"*25)
print(" "*10," sin(a)")
print("#"*25)
a.Dual_Sin().Dual_Print()

print("#"*25)
print(" "*10," cos(a)")
print("#"*25)
a.Dual_Cos().Dual_Print()

print("#"*25)
print(" "*10," sinh(a)")
print("#"*25)
a.Dual_Sh().Dual_Print()

print("#"*25)
print(" "*10," cosh(a)")
print("#"*25)
a.Dual_Ch().Dual_Print()