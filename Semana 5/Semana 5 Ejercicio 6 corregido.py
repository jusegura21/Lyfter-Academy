
h1={
            'numero': 1,
            'piso': 1,
            'precio': '150$'
        }
h2={
            'numero': 2,
            'piso': 2,
            'precio': '300$'}
h3={
            'numero': 3,
            'piso': 3,
            'precio': '450$'}
habitaciones=[h1,h2,h3]  

my_hotel = {
    "nombre" : 'Hotel Gilton',
    'estrellas': '4',
    'habitaciones': habitaciones,
}
print (my_hotel['habitaciones'][2]['precio'])