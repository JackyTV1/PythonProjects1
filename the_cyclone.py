# Filtro automatizado para saber si una persona puede subir a un juego mecánico

height = int (input ("whats your height: "))
credi = int (input ("how much credits do you have: "))

if height >=137 and credi >=10:
    print("Enjoy the ride")
elif height < 137: 
    print ("you are not tall anough to ride")
elif credi < 10:
    print ("you dont have enoght credit to ride")
else: 
    print ("invalid data")    
            
            
            
            
            