def cal(diasXmes, nombreMes, diaSemana):
    dias = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
    for mes in range(12):
        print(nombreMes[mes])
        print(' '.join(dias))
        print('   ' * (diaSemana - 1), end='')
        for dia in range(1, diasXmes[mes] + 1):
            print(f'{dia:2}', end=' ')
            if diaSemana == 7:
                print()
                diaSemana = 0
            diaSemana += 1
        print('\n')
nombreMes = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
diasXmes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
diaSemana = 1  
cal(diasXmes, nombreMes, diaSemana)
