# PODRÁS SABER LA CASA DE HOWARDS A LA QUE PERTENECES

#CASAS

Gryffindor=0
Ravenclaw=0
Hufflepuff=0
Slytherin=0
Result=""

#PREGUNTA 1

Result = int (input ("Q1. Do you like 1) Dawn or 2) Dusk?  "))
if Result ==1:
    Gryffindor=Gryffindor+1
    Ravenclaw=Ravenclaw+1
   # print (f"el puntaje va Gr= {Gryffindor} , rav = {Ravenclaw} , huf = {Hufflepuff} Y sLY = {Slytherin}" )
elif Result==2:
    Hufflepuff=Hufflepuff+1
    Slytherin=Slytherin+1
    #print (f"el puntaje va Gr2= {Gryffindor} , rav2 = {Ravenclaw} , huf2= {Hufflepuff} Y sLY2 = {Slytherin}" )
else: print ("Wrong input.")


#PREGUNTA 2

Result = int (input ("Q2) When Im dead, I want people to remember me as: 1)The Good  | 2)The Great  | 3)The Wise  | 4)The Bold  "))
if Result ==1:
    Hufflepuff=Hufflepuff+2
   # print (f"el puntaje va Gr3= {Gryffindor} , rav3 = {Ravenclaw} , huf3 = {Hufflepuff} Y SLY3= {Slytherin}" )

elif Result==2:
        Slytherin=Slytherin+2
     #   print (f"el puntaje va Gr4= {Gryffindor} , rav4 = {Ravenclaw} , huf4= {Hufflepuff} Y sLY4 = {Slytherin}" )

elif Result==3:
      Ravenclaw=Ravenclaw+2
    #  print (f"el puntaje va Gr5= {Gryffindor} , rav5 = {Ravenclaw} , huf5= {Hufflepuff} Y sLY5 = {Slytherin}" )

elif Result==4:
        Gryffindor=Gryffindor+2
     #   print (f"el puntaje va Gr26= {Gryffindor} , rav6 = {Ravenclaw} , huf6= {Hufflepuff} Y sLY6 = {Slytherin}" )

else: print ("Wrong input.")


#PREGUNTA 3
Result = int (input ("Q3) Which kind of instrument most pleases your ear? 1)The violin  ||  2)The trumpet  || 3)The piano  || 4)The drum  "))
if Result ==1:
    Slytherin=Slytherin+4
   # print (f"el puntaje va final Gr= {Gryffindor} , rav = {Ravenclaw} , huf = {Hufflepuff} Y sLY = {Slytherin}" )

elif Result==2:
    Hufflepuff=Hufflepuff+4
   # print (f"el puntaje final va Gr2= {Gryffindor} , rav2 = {Ravenclaw} , huf2= {Hufflepuff} Y sLY2 = {Slytherin}" )

elif Result==3:
    Ravenclaw=Ravenclaw+4
   # print (f"el puntaje final va Gr2= {Gryffindor} , rav2 = {Ravenclaw} , huf2= {Hufflepuff} Y sLY2 = {Slytherin}" )

elif Result==4:
    Gryffindor=Gryffindor+4
   # print (f"el puntaje final va Gr2= {Gryffindor} , rav2 = {Ravenclaw} , huf2= {Hufflepuff} Y sLY2 = {Slytherin}" )


else: print ("Wrong input.")


if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor>= Slytherin:
    print(f"Tu casa de Howards es ˜”*°•.˜”*°• GRIFFINDOR •°*”˜.•°*”˜ con {Gryffindor} puntos ¡Felicidades!")

elif Ravenclaw>= Gryffindor  and Ravenclaw>= Hufflepuff and Ravenclaw>= Slytherin:
    print(f"Tu casa de Howards es (っ◔◡◔)っ ♥ Ravenclaw ♥ con {Ravenclaw} puntos  ¡Felicidades!")

elif Hufflepuff >= Gryffindor  and Hufflepuff>= Ravenclaw and Hufflepuff >= Slytherin:
    print(f"Tu casa de Howards es  ◦•●◉✿ 🅷🆄🅵🅵🅻🅴🅿🆄🅵🅵✿◉●•◦ con {Hufflepuff} puntos  ¡Felicidades!")
else :    print(f"Tu casa de Howards es ๑۞๑ø¤º°`°๑۩ Slytherin ๑۩ø¤º°`°๑۞๑ con {Slytherin} puntos  ¡Felicidades!") 