def text_inverter(string_value):
    new_list=""
    
    for index in range(len(string_value)):
        length=len(string_value)-1 
        new_list+=string_value[length-index]
    return new_list

text="Sopa de pollo con arroz y vegetales"
print(text_inverter(text))


