def create_list(string): #funcion que crea la lista a partir del string
    concatenate=""
    words_list=[]
    for n in range(len(string)):
        if string[n]=="-":
            words_list.append(concatenate)
            concatenate=""
            continue
        elif n==len(string)-1:
            concatenate = concatenate+string[n]
            words_list.append(concatenate)
        else:
            concatenate = concatenate+string[n]
    return words_list

def sorteador(value): #funcion que realiza una iteracion a la lista y realiza un acomodo
    sorted_words=value
    storage=""
    contador=0
    for n in range(len(value)-1):
        if sorted_words[n][0]<sorted_words[n+1][0]:
            contador+=1
            continue
        else:
            storage=sorted_words[n+1]
            sorted_words[n+1]=sorted_words[n]
            sorted_words[n]=storage
    return sorted_words, contador

def main(value):
    words_list=create_list(value)
    new_string=""
    while True: #funcion que llama a "sorteador" N veces hasta que la lista se encuentre acomodada. 
        if sorteador(words_list)[1]==len(words_list)-1:
            break
        else:
            words_list=sorteador(words_list)[0]
    for index in range(len(words_list)): #funcion que convierte la lista a string
        if index ==len(words_list)-1:
            new_string=new_string+words_list[index]
        else:
            new_string=new_string+words_list[index]+"-"
    return new_string
        

text='zapayo-manzana-uva-fresa-limon-sandia'
print(main(text))



