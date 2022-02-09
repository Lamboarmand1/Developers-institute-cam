class Dog:
    def __init__(self,name, heigth):
        self.name = name
        self.height = heigth
    def __bark__(self):
        print( self.name +'ce chien fait woof' )
    def __jump__(self):
        print(self.name +'jumps'+ self.height*2)
davids_dog = Dog('Rex', 50)
davids_dog.__bark__()
davids_dog.__jump__()

sarahs_dog = Dog('Teacup', 20)
sarahs_dog.__bark__()
sarahs_dog.__jump__()
       