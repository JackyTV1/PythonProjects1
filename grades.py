#PARA SABER SI UN ESTUDIANTE DESAPROBÓ O APROBÓ

import random

grade = random.randint (0,100)


if grade >= 55:
   print (f"you´ve passed with {grade}")
   
else:
    print (f"you failed with {grade}")   