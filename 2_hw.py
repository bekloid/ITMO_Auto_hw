def task_1():
    a:int = 6
    b: float =134.86
    c: str="fgd"
    d: list=[3,7,"sdj"]
    e:bool= True
    return type(a),type (b), type(c),type(d),type(e)
print(task_1())

task_1()


def task_2():
    a: list = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]
print(task_2())

task_2()   # числа Фибоначчи


def task_3(x:int)-> int:
    return x**2
print(task_3(5))