import random

alunos = ['Hélia', 'Arthur', 'Esther', 'Bernardo', 'Caio Samuel o melhor']

equipe1 = []
equipe2 = []

random.shuffle(alunos)

total_alunos = len(alunos)

for n in range(total_alunos // 2):
    equipe1.append(alunos.pop(0))

for i in range(len(alunos)):
    equipe2.append(alunos.pop(0))

print(f"Equipe 1:, {equipe1[0]} e {equipe1[1]}")
print(f"Equipe 2: {equipe2[0]}, {equipe2[1]} e {equipe2[2]}")