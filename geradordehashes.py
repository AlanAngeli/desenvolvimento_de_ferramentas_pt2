import hashlib

resultado = hashlib.md5(b'Python Security')

print('O hash da string é: ', resultado.hexdigest())