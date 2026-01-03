# Verificar se um aluno foi aprovado, considerando que a média para aprovação é 7 e que o aluno
# cursou 2 disciplinas.

print("Cálculo das médias do semestre")

# Entrada dos valores numéricos - notas de cada disciplina naquele semestre
nota1 = float(input("Entre com a nota da primeira disciplina: "))
nota2 = float(input("Entre com a nota da segunda disciplina: "))

# Cálculo da média considerando as notas informadas
media = (nota1 + nota2)/2

# Tomada de decisão - Aprovação ou reprovação
if media >= 7:
  print(f"Você passou no semestre! Sua média é {media:.2f}")
else:
  print(f"Infelizmente você reprovou neste semestre. Sua média é {media:.2f}")