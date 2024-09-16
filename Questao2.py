def contagem(texto):
   
    quantidade = texto.lower().count('a')

    if quantidade > 0:
        return f"A letra 'a' ocorre {quantidade} vezes na string."
    else:
        return "A letra 'a' não foi encontrada na string."


entrada = input("Informe uma string: ")
resultado = contagem(entrada)
print(resultado)