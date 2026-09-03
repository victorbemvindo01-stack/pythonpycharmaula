

nome_produto = input("iphone: ")
custo_fabrica = float(input("900.00 (R$): "))
preco_venda = float(input("4.000 (R$): "))

lucro = preco_venda - custo_fabrica

lucro_bom = lucro > 20.00

print(f"\nProduto: {nome_produto}")
print(f"Lucro obtido: R$ {lucro:.2f}")
print(f"Lucro bom (maior que R$ 20.00)?: {lucro_bom}")
