import verificaLE
le = verificaLE.LE()
le.leitorLendo(1)
le.leitorLendo(3)
le.leitorLendo(2)
le.leitorLendo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é par: {0}'.format(0))
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(0))
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(0))
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(0))
print('Thread Leitor - O inteiro lido é par: {0}'.format(0))
le.leitorSaindo(1)
le.escritorBloqueado(3)
le.escritorBloqueado(2)
le.escritorBloqueado(1)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é par: {0}'.format(0))
le.leitorSaindo(2)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é par: {0}'.format(0))
le.leitorSaindo(4)
le.leitorSaindo(1)
le.leitorSaindo(2)
le.leitorSaindo(3)
le.leitorSaindo(3)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorBloqueado(1)
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(2)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(3)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.escritorEscrevendo(1)
le.escritorBloqueado(3)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.escritorEscrevendo(3)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.escritorBloqueado(3)
le.escritorBloqueado(2)
le.leitorSaindo(3)
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorBloqueado(1)
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorBloqueado(1)
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.leitorLendo(1)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorLendo(3)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(1)
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.escritorEscrevendo(1)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorBloqueado(3)
le.escritorSaindo(1)
le.escritorEscrevendo(3)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.leitorLendo(1)
le.leitorLendo(3)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(3)
le.leitorSaindo(1)
le.leitorLendo(2)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.escritorEscrevendo(3)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(3)
le.escritorEscrevendo(1)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(1)
le.escritorEscrevendo(2)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.leitorLendo(3)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorLendo(1)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(3)
le.leitorSaindo(1)
le.leitorLendo(2)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(3)
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.escritorEscrevendo(3)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(3)
le.escritorEscrevendo(1)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(1)
le.escritorEscrevendo(2)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorBloqueado(1)
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.leitorLendo(3)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorLendo(1)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(3)
le.leitorSaindo(1)
le.leitorLendo(2)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.escritorEscrevendo(3)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorBloqueado(1)
le.escritorSaindo(3)
le.escritorEscrevendo(1)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(1)
le.escritorEscrevendo(2)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.leitorLendo(3)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorLendo(1)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(1)
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.escritorEscrevendo(1)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(1)
le.escritorEscrevendo(3)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.leitorLendo(1)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(3)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.escritorEscrevendo(1)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(1)
le.escritorEscrevendo(3)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.leitorLendo(1)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorLendo(3)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(3)
le.leitorSaindo(1)
le.leitorLendo(2)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.escritorEscrevendo(3)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorBloqueado(1)
le.escritorSaindo(3)
le.escritorEscrevendo(1)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(1)
le.escritorEscrevendo(2)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.leitorLendo(3)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorLendo(1)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(3)
le.leitorSaindo(1)
le.leitorLendo(2)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.escritorEscrevendo(3)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(3)
le.escritorEscrevendo(1)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(1)
le.escritorEscrevendo(2)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.leitorLendo(3)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(1)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(2)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.escritorEscrevendo(3)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(3)
le.escritorEscrevendo(1)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(1)
le.escritorEscrevendo(2)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.leitorLendo(3)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(1)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(2)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.escritorEscrevendo(3)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(3)
le.escritorEscrevendo(1)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(1)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(2)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(1)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.leitorLendo(2)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(2))
le.leitorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.escritorEscrevendo(3)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(3)
le.escritorEscrevendo(1)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(1)
le.escritorEscrevendo(2)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(3))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(3))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(3))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(3))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.leitorLendo(3)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(1)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(2)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.escritorEscrevendo(3)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(3)
le.escritorEscrevendo(1)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(1)
le.escritorEscrevendo(2)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.leitorLendo(3)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(1)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(2)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.escritorEscrevendo(3)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(3)
le.escritorEscrevendo(1)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(1)
le.escritorEscrevendo(2)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é par: {0}'.format(2))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.leitorLendo(3)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(1)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(2)
print('Thread LeitorEscritor - O inteiro lido é: {0}'.format(1))
le.leitorSaindo(2)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.leitorLendo(1)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(1)
le.leitorLendo(4)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(4)
le.leitorLendo(3)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(3)
le.leitorLendo(2)
print('Thread Leitor - O inteiro lido é impar: {0}'.format(1))
le.leitorSaindo(2)
le.escritorEscrevendo(3)
print('Thread Escritor - Novo valor atribuído: {0}'.format(3))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print('Thread Escritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
le.escritorEscrevendo(1)
print('Thread Escritor - Novo valor atribuído: {0}'.format(1))
le.escritorSaindo(1)
le.escritorEscrevendo(1)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(1)
le.escritorEscrevendo(3)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(3)
le.escritorEscrevendo(2)
print(' Thread LeitorEscritor - Novo valor atribuído: {0}'.format(2))
le.escritorSaindo(2)
