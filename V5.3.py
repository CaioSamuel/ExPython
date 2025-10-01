# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V5.3


#begin_inputs
hab_Taipu = 12000
crescimento = hab_Taipu + (0.10 * hab_Taipu)

hab_cm = 73000
crescimento_cm = hab_cm + (0.03 * hab_cm)

hab_Parnamirim = 250000
crescimento_parnamirim = hab_Parnamirim + (0.01 * hab_Parnamirim)
#end_inputs
meses = 1
while (crescimento + crescimento_cm <= crescimento_parnamirim):
    hab_Taipu += (0.10 * hab_Taipu)
    hab_cm += (0.03 * hab_cm)
    hab_Parnamirim += (0.01 * hab_Parnamirim)
    if (hab_Taipu + hab_cm) >= hab_Parnamirim:
        print(meses)
        break
    meses += 1
	
