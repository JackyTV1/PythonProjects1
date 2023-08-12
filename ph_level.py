#PARA SABER EL NIVEL DE PH
ph= int (input("enter a number between 0-14: "))

if ph == 7:
    print ("PH is neutral")
    
elif ph >7 & ph <=14:  #falta limitar a 14
    
     print ("PH i basic")

elif ph >0 & ph < 7:
    print ("PH ia ACIDIC")       
    
else :
    print ("the number given is not valid, try again")      