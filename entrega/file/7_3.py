def find_easter_egg(arquivo):
    arquivo = arquivo.lower().strip()
    if arquivo == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk’d!")
        exit()

arquivo = input("informe um arquivo para abrir: ")
find_easter_egg(arquivo)

try:
    fhand = open(arquivo)
    for line in fhand:
        posicao_linha_procurada = line.find("X-DSPAM-Confidence:")
        if posicao_linha_procurada >= 0:
            posicao_float = line.find(":")
            parte_numerica =  float(line[posicao_float +1:].strip())
            print(parte_numerica,end='\t')
            print(parte_numerica.__class__.__name__)
except FileNotFoundError:
    print("Deu ruim ao tentar abrir o arquivo")