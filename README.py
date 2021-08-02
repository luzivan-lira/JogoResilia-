# JogoResilia-

# apresentação do jogo
Mario = 1
Luigi = 2
Yoshi = 3

print("Você vivnciará uma grade jornada, boa sorte!")
nome = input("Digite seu nome")
print("Seja bem vido ao jogo", nome)

print("Personagens")

personagem = ("Mario", "Luigi", "Yoshi")
for p in personagem:
    print(p)

personagem = input("Escolha seu personagem")
print(personagem)
print("Ótima escolha")
# primeira fase
print("Bem vindo a primeira fase")
print("Descobrindo o SARS-cov2")

print("Mario vai ao encontro da princessa e descobre que a princesa pegou covid")

Mario = input('Voce pegou covid? ')

if not Mario == "não":
    print('Fim de jogo!')
else:
    print('Passou de fase!')
# SegundaFase
print("Bem vindo a segunda fase")
print("Enfrentando a cloroquina")

print("Mario conhece a cloroquina, porém descobre que não e tratamento correto")

Mario = input('Você tomou cloroquina? ')

if not Mario == "não":
    print('Fim de jogo!')
else:
    print('Passou de fase!')
# TerceiraFase
print("Bem vindo a terceira fase")
print("O tratamento")

print("Mario encontra a vacina e vai levar ela, ate a princesa")

Mario = input('Você tomou a vacina? ')

if not Mario == "não":
    print('Fim de jogo!')
else:
    print('Passou de fase!')
