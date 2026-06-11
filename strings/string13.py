import random

palavras = ["python", "programacao", "computador", "desenvolvimento", "algoritmo", "jogo", "palavra", "embaralhada", "tentativas", "adivinhar", "aleatoriamente", "ganhou", "perdeu", "simples", "funcao", "def", "join", "lista", "escolher", "mostrar", "tela", "usuario", "jogador", "palavras", "embaralhadas", "dificil", "facil", "divertido", "desafio", "vitoria", "derrota", "conquista", "frustracao", "persistencia", "estrategia", "inteligencia", "criatividade", "diversao", "entretenimento", "aprendizado", "conhecimento", "habilidade", "desenvolver", "melhorar", "praticar", "jogar", "adivinhar", "palavra", "embaralhada", "tentativas", "ganhou", "perdeu", "simples", "funcao", "def", "join", "lista", "escolher", "mostrar", "tela", "usuario", "jogador", "palavras", "embaralhadas", "dificil", "facil", "divertido", "desafio", "vitoria", "derrota", "conquista", "frustracao", "persistencia", "estrategia", "inteligencia", "criatividade", "diversao", "entretenimento", "aprendizado", "conhecimento", "habilidade", "desenvolver", "melhorar", "praticar"]

palavra_secreta = random.choice(palavras)
palavra_embaralhada = ""
for letra in palavra_secreta:
    palavra_embaralhada += letra
palavra_embaralhada = ''.join(random.sample(palavra_embaralhada, len(palavra_embaralhada)))
tentativas = 6
print("Bem-vindo ao jogo da palavra embaralhada!")
print("A palavra embaralhada é:", palavra_embaralhada)
while tentativas > 0:
    palpite = input("Digite seu palpite: ")
    if palpite == palavra_secreta:
        print("Parabéns! Você adivinhou a palavra secreta:", palavra_secreta)
        break
    else:
        tentativas -= 1
        print("Palpite incorreto. Tentativas restantes:", tentativas)
if tentativas == 0:
    print("Game over! A palavra secreta era:", palavra_secreta)