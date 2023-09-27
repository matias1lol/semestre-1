
regiones = {
    14: {
        'nombre': 'los Ríos',
        'superficie': 18429,
        'habitantes': 404432
    },
    12: {
        'nombre': 'magallanes',
        'superficie': 1382291,
        'habitantes': 166533
    }
}
print('diccionario:')
print(regiones)
for region_id in regiones:
    region = regiones[region_id]
    densidad = round(region['habitantes'] / region['superficie'], 1)
    region['densidad'] = densidad
regiones[14]['Capital'] = 'Valdivia'
regiones[12]['Capital'] = 'Punta Arenas'
regiones[14]['Comunas'] = ['Río Bueno', 'La Unión', 'Paillaco']
regiones[12]['Comunas'] = ['Antártica Chilena', 'Magallanes', 'Tierra del Fuego']
regiones[14]['Provincia'] = ('Ranco', 'Valdivia')
regiones[12]['Provincia'] = ('Antártica Chilena', 'Magallanes', 'Tierra del Fuego')
print('\nDiccionario con nuevas claves:')
print(regiones)
