# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V5.3


#begin_inputs

#end_inputs
hab_Taipu = 12000
crescimento = 1.10

hab_cm = 73000
crescimento_cm = 1.03

hab_Parnamirim = 250000
crescimento_parnamirim = 1.01
ano = 2018

while hab_Parnamirim >= hab_cm or hab_Parnamirim >= hab_Taipu:
    hab_cm = round(hab_cm * crescimento_cm)
    hab_Taipu = round(hab_Taipu * crescimento)
    hab_Parnamirim = round(hab_Parnamirim * crescimento_parnamirim)
    ano += 1

print(f"Parnamirim: {ano}")
print(f"Populaçao Parnamirim: {hab_Parnamirim}")
print(f"Populaçao Ceará mirim: {hab_cm}")
print(f"Populaçao Taipu: {hab_Taipu}")

