print('-='*20)
print('Gerador de PA')
print('-='*20)
primeirotermo = int(input('Insira o primeiro termo: '))
razão = int(input('Insira a razão: '))
print('-='*20)
mais = 10
total = 0
cont = 1
while mais != 0:
    total = total + mais
    while cont < total:
        primeirotermo += + razão
        cont += + 1
        print(f'{primeirotermo} - ', end='')
    print('Pausa' if mais != 0 else '')
    print('-=' * 20 if mais != 0 else '')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
else:
    print(f'Progressão finalizada com {total} termos mostrados')



