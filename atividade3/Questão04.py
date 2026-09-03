#Questão 4: O Boletim Escolar Automático (Aritmética + Lógica AND)

nota1 = float(input("nota 7: "))
nota2 = float(input("nota 8: "))
frequencia = float(input("75): "))
media = (nota1 + nota2) / 2

aprovado = (media >= 6.0) and (frequencia >= 75)

print(f"Média calculada: {media:.1f}")
print(aprovado)

