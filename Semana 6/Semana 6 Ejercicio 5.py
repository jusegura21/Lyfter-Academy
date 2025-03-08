def upper_and_lower_cases(value):
    upper_counter=0
    lower_counter=0
    for n in range(len(value)):
        if value[n].isupper():
            upper_counter+=1
        elif value[n]==" ":
            continue
        else:
            lower_counter+=1
    return upper_counter, lower_counter


text="Mamma Mia is Mario and Luigi"
print(f"There are {upper_and_lower_cases(text)[0]} upper cases and {upper_and_lower_cases(text)[1]} lower cases")