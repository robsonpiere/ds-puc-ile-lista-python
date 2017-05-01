arquivo = input("informe um arquivo para abrir: ")

try:
    fhand = open(arquivo)
    for line in fhand:
        posicao_linha_procurada = line.find("X-DSPAM-Confidence:")
        if posicao_linha_procurada >= 0:
            posicao_float = line.find(":")
            parte_numerica =  float(line[posicao_float +1:].strip())
            print(parte_numerica,end='\t')
            print(parte_numerica.__class__.__name__)
except:
    print("Deu ruim ao tentar abrir o arquivo")