#1. Analice el algoritmo de bubble_sort usando la Big O Notation.
def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort) - 1):# O(n)
        has_made_changes = False #O(1)
        for index in range(0, len(list_to_sort) - 1 - outer_index):# O(n^2)
            current_element = list_to_sort[index] #O(1)
            next_element = list_to_sort[index + 1]#O(1)

            print(f'-- Iteracion {outer_index}, {index}. Elemento actual: {current_element}, Siguiente elemento: {next_element}')#O(1)

            if current_element > next_element:#O(1)
                print('El elemento actual es mayor al siguiente. Intercambiandolos...')#O(1)
                list_to_sort[index] = next_element#O(1)
                list_to_sort[index + 1] = current_element#O(1)
                has_made_changes = True#O(1)
    if not has_made_changes:
        return#O(1)
#Respuesta: Este programa es O(n^2). Ya que tiene dos ciclos anidados de tamaño variable 'n'.
# 
#2.Analice los siguientes algoritmos usando la Big O Notation:
#----#
def print_numbers_times_2(numbers_list):#O(n)
	for number in numbers_list: #O(n)
		print(number * 2) #O(1)
#Respuesta: Esta funcion es O(n), ya que se ejecuta segun el tamaño de su input y no tiene ciclos anidados. 
#----#
def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:#O(n)
		for element_b in list_b:#O(n^2)
			if element_a == element_b:#O(1)
				return True
				
	return False
#Respuesta: Este programa es O(n^2). Ya que tiene dos ciclos anidados de tamaño variable 'n'.sta funcion es O()
#----#
def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)#O(1)
	for index in range(min(list_len, 10)):#O(1)
		print(list_to_print[index])#O(1)
#Respuesta: Esta función es O(10), porque siempre se va a ejecutar 10 veces. 
#----#
def generate_list_trios(list_a, list_b, list_c):
	result_list = []#O(1)
	for element_a in list_a:#O(n^1)
		for element_b in list_b:#O(n^2)
			for element_c in list_c:#O(n^3)
				result_list.append(f'{element_a} {element_b} {element_c}')#O(1)
				
	return result_list 
#Respuesta: Este programa es O(n^3). Ya que tiene dos ciclos anidados de tamaño variable 'n'.