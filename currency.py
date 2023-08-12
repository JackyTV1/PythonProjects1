#TIPO DE CAMBIO DE UN TURISTA

cn= float (input ("cuantos yuanes chino tienes: "))
kr= float (input ("cuantos wones coreanos tienes: ")) 
sol= float (input ("cuantos soles tienes: "))

dllToSoles= sol/3.72
dllToKR= kr/13.38
dllTocn= cn/6.93

totalDLL= dllToKR+dllTocn+dllToSoles

print (f"tienes  {totalDLL}  dolares")