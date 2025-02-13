M1=float(input("Nota 01:"))
M2=float(input("Nota 02:"))
M3=float(input("Nota 03:"))
M4=float(input("Nota 04:"))
M5=float(input("Nota 05:"))

media=(( M1 + M2 + M3 + M4 + M5 )/5)

if media <= 4:
    print("O aluno está reprovado")
elif media <=6:
    print("O aluno pegou exame")
    exame = float(input("Adicione a nota do  exame:"))
elif media > 6:
    print("O aluno esta aprovado")

print(f"Essa é sua media: {media}")