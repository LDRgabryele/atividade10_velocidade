# Exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida
km = int(input("Digite a velocidade do veiculo em km: "))
multa = (km-60)*7
print("O valor da sua multa é: R$", multa)  