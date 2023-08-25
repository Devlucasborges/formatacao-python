ra = input ("ra :")
nome = input ("nome :")
curso = input ("curso :")
disciplina = input ("disciplina :")
nota_b1 = float(input ("nota da b1 :"))
nota_b2 = float(input ("nota da b2 :"))
nota = nota_b1 + nota_b2
media = nota / 2

if (media >= 7):
    print ("Aluno aprovado, sua nota é {}".format (media))

else:
    print ("Aluno ficou de exame, sua nota é {}".format (media))