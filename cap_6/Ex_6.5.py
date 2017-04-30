string = "X-DSPAM-Confidence: 0.8475"
posicao = string.find(":")
parte_numerica =  float(string[posicao +1:].strip())
print(parte_numerica,end='\t')
print(type(parte_numerica))