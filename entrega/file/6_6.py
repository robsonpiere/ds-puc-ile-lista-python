palavra = " teste testando teste "

print("Removendo espaços antes e depois")
print(palavra.strip())

print("Removendo espaços antes")
print(palavra.lstrip())

print("Removendo espaços depois")
print(palavra.rstrip())

print("Substituindo com replace")
print(palavra.replace("teste","testado com sucesso"))