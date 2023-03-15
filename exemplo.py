# > Parte feita no Google Colab! <
#f-String: mensagem junto com variável

nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))

print(f'Seu nome é {nome} e sua idade é {idade}')

#Para pular linha, você pode fazer vários prints ou utilizar o \n para pular
#linha, como:

print(f'Seu nome é {nome} \n Sua idade é {idade}')
 
print(f'Seu nome é {nome}')
print(f'Sua idade é {idade}')

## Exemplo 

a = int(input('Informe um número: '))
b = a * 2
print(f'O dobro de {a} é {b}')

