def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print ("I’m a lumberjack, and I’m okay.")
    print ("I sleep all night and I work all day.")

repeat_lyrics()

"""
Reposta:  A execução do da função print lyrics ocorre normalmente pois quando ela é chamada já houve a definição,
na linha anterior ela estava dentro da declaração de repeat_lyrics, mais não havia ocorrido a tentativa de execução
"""