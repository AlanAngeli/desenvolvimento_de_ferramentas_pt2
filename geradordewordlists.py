'''

                                O que são wordlists?

- Wordlists são arquivos contendo uma palavra por linha. São tulizadas em ataques
de força bruta como quebra de autenticação, pode ser por usada para testar a
autenticação e confidencialidade de um sistema


'''

import itertools

resultado = itertools.permutations('abc', 3) #fará 3 permutações (3 caracteres)

for i in resultado: #para cada caractere(i) no resultado(resultado):
    print(''.join(i))