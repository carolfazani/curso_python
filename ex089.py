alunos = []
boletim = []
c = 1

while True:
    nome = str(input('Nome: '))
    p1 = float(input(('Prova 1: ')))
    p2 = float(input('Prova 2: '))
    continua = str(input('Quer continuar? ')).upper().strip()
    alunos.append([c, nome, p1, p2])
    alunos.append(nome)
    alunos.append(p1)
    alunos.append(p2)
    boletim.append(alunos[:])
    alunos.clear()
    c +=+1

    if continua == 'N':
        break
print(f'Nº  nome    média ')
for v in range(0, len(boletim)):
    print(f'{boletim[v][0]}     {boletim[v][1]}    {(boletim[v][2]+ boletim[v][3])/2}')
aluno = 0
while aluno != 999:
    aluno = int(input('Mostrar as notas de qual aluno? (999 interrompe) '))
    print(f' Nome: {boletim[aluno - 1][1]}, P1: {boletim[aluno - 1][2]}, P2 {boletim[aluno - 1][3]}')
    if aluno == 999:
        break