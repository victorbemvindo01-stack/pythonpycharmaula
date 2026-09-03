#Questão 7: O Formulário de Doação de Sangue (Múltiplas Condições)

idade = int(input("Digite a idade do doador: "))
peso = float(input("Digite o peso do doador (em kg): "))

pode_doar = (idade >= 16) and (idade <= 69) and (peso > 50)
print(pode_doar)
