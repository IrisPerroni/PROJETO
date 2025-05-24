
# Interpolação basica de strings
# s - string
# d e i - int
# f - float 
# x e X - Hexadecimal (ABCDEF0123456789)

nome = 'Iris'
preco = 1000.956318
variavel = '%s, o preço é R$%.2f' % (nome,preco)
print(variavel)
print('o Hexadecimal de %d é %08X' % (1500,1500))

#Formatação basica string 
# (Caractere)(><^)(quantidade)
# >  -Esquerda
# < - Direita
# ^ - Centro

var = 'ABC'
print(f'{var}')
print(f'{var : >10}')
print(f'{var : <10}.')
print(f'{var : ^10}.')
print(f'{1000.00574156846:.1f}')