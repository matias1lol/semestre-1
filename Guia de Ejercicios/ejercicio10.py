# Crear el diccionario para el contacto
agenda = {
    'Nombre': 'Juan Pérez',
    'Direccion': 'Calle Falsa 123',
    'Ciudad': 'Osorno',
    'Numero telefonico': '1234567890'
}

# Agregar la clave para redes sociales con una lista de perfiles
agenda['Redes Sociales'] = ['juanperezfb', 'juampi_insta', 'jperez_twitter']

# Imprimir el perfil de Facebook del contacto
print('Perfil de Facebook:', agenda['Redes Sociales'][0])

# Imprimir la agenda completa
print('Agenda:', agenda)
