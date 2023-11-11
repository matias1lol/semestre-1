def capitalizaFrases(textoMayusc):
    oraciones = textoMayusc.split('.')
    return '.'.join(oracion.capitalize() for oracion in oraciones)
print(capitalizaFrases("HOLA.QUE BIEN QUE HOY NO LLOVIO TANTO.CUIDATE."))
