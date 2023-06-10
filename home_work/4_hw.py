# задача 1
#
# class Rectangle():
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#
#     def sq(self):
#         return int(self.width) * int(self.height)
#     def per(self):
#         return (self.width + self.height) * 2
#
# # я все еще не понимаю, как это работает
# p_1 = Rectangle(5, 7)
# p_2 = Rectangle(9, 3)
# p_3 = Rectangle(35,4)
# print(p_1.sq())
# print(p_1.per())
# print(p_2.sq())
# print(p_2.per())
# print(p_3.sq())
# print(p_3.per())

# Задача 2

class Math():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(int(self.a) + int(self.b))


    def multiplication(self):
        print(int(self.a) * int(self.b))


    def division(self):
        print(int(self.a) / int(self.b))

    def subtraction(self):
        print(int(self.a) - int(self.b))


