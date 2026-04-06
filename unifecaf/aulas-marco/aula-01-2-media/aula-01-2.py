nota_prova = float(input("Digite sua nota da prova: "))
nota_trabalho = float(input("Digite a sua nota do trabalho: "))

media = (nota_prova + nota_trabalho) / 2

if media >= 7:
    print("APROVADO")

else:
    if media >= 5:
       print("RECUPERAÇÃO")
    
    else:
       print("REPROVADO")