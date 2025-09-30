# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V5.2


#begin_inputs
minutos = 0
#end_inputs

distancia_tartaruga = 500

vel_tartaruga = 1
vel_lebre = 10

while True:
    distancia_tartaruga += vel_tartaruga
    distancia_lebre = vel_lebre * minutos

    if distancia_lebre >= distancia_tartaruga:
        break

    minutos += 1

print(minutos)