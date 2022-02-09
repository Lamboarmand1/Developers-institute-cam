from .models import Animals

new_animal = Animals(name= 'Chien',
                                legs= 4,
                                weight= 30,
                                height= 41,
                                speed= 12.4)
new_animal.save()