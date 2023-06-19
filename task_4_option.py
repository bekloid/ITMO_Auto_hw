class Car():


    def __init__(self,color,type,year):
        self.color = color
        self.type = type
        self.year= year

    def start_car(self):
        return 'Автомобиль заведен'

    def stop_car(self):
        return'Автомобиль заглушен'


    def y(self):
        return(self.year)

    def t(self):
        return(self.type)

    def c(self):
        return(self.color)