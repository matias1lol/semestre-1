def capitalizaFrases(textoMayusc):
    oraciones = textoMayusc.split('.')
    resultado = '.'.join(oracion.capitalize() for oracion in oraciones)
    print(resultado)

capitalizaFrases("HOLA.QUE BIEN QUE HOY NO LLOVIO TANTO.CUIDATE.")
