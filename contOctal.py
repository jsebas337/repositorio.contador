class Octal:
 def contar_en_octal(numero):
    for i in range(1, numero + 1):
        print(f'{i} en octal: {oct(i)}')
