#Questão 5: O Sistema de Desconto (Lógica OR)

valor_compra = float(input("200.00 (R$): "))

is_vip = int(input("ja tem o cartao da loja? (1 = Sim, 0 = Não): "))

possui_cartao_vip = bool(is_vip)

tem_frete_gratis = (valor_compra > 200.00) or possui_cartao_vip

print(tem_frete_gratis)

