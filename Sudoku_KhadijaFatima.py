import random
matriz=[]
renglon=[]
juego_fac1=[
    [0,0,6,0,0,2,3,0,4],
    [9,0,4,7,5,0,0,8,2],
    [0,0,8,0,0,6,0,0,5],
    [0,0,3,0,0,0,0,4,0],
    [2,0,0,4,0,0,8,3,0],
    [4,0,7,5,0,0,0,0,0],
    [0,0,0,6,0,0,0,0,8],
    [7,0,0,0,2,0,4,5,3],
    [0,0,0,3,7,0,0,6,9]
    ]
sol_fac1=[
    [5,7,6,8,1,2,3,9,4],
    [9,1,4,7,5,3,6,8,2],
    [3,2,8,9,4,6,7,1,5],
    [6,9,3,2,8,7,5,4,1],
    [2,5,1,4,6,9,8,3,7],
    [4,8,7,5,3,1,9,2,6],
    [1,3,5,6,9,4,2,7,8],
    [7,6,9,1,2,8,4,5,3],
    [8,4,2,3,7,5,1,6,9]
    ]
juego_fac2=[
    [0,0,2,8,0,0,0,7,0],
    [6,0,9,0,7,4,0,2,3],
    [4,0,8,0,0,3,0,5,0],
    [0,0,5,0,8,0,0,3,0],
    [0,0,0,0,0,0,7,4,0],
    [0,2,7,0,3,0,0,8,5],
    [0,0,0,3,6,0,0,0,0],
    [0,0,0,5,1,7,4,0,8],
    [0,0,0,2,0,8,0,9,0]
    ]
sol_fac2=[
    [3,1,2,8,9,5,6,7,4],
    [6,5,9,1,7,4,8,2,3],
    [4,7,8,6,2,3,1,5,9],
    [9,4,5,7,8,1,2,3,6],
    [8,3,6,9,5,2,7,4,1],
    [1,2,7,4,3,6,9,8,5],
    [7,8,4,3,6,9,5,1,2],
    [2,9,3,5,1,7,4,6,8],
    [5,6,1,2,4,8,3,9,7]
    ]
juego_med1=[
    [0,0,0,0,0,0,0,8,4],
    [5,0,0,0,4,2,6,0,0],
    [0,0,4,0,0,0,0,2,0],
    [0,4,0,0,6,3,7,0,0],
    [0,0,0,0,0,1,0,0,3],
    [6,3,0,9,5,7,2,0,0],
    [0,5,0,0,0,9,0,0,6],
    [3,2,0,8,0,0,1,0,9],
    [0,0,9,5,0,0,8,0,0]
    ]
sol_med1=[
    [7,9,2,6,1,5,3,8,4],
    [5,8,3,7,4,2,6,9,1],
    [1,6,4,3,9,8,5,2,7],
    [9,4,8,2,6,3,7,1,5],
    [2,7,5,4,8,1,9,6,3],
    [6,3,1,9,5,7,2,4,8],
    [8,5,7,1,2,9,4,3,6],
    [3,2,6,8,7,4,1,5,9],
    [4,1,9,5,3,6,8,7,2]
    ]
juego_med2=[
    [6,8,0,2,5,0,0,0,7],
    [5,7,1,6,9,0,0,0,0],
    [0,0,0,0,0,0,4,0,0],
    [3,1,0,7,8,0,0,0,6],
    [0,4,0,0,0,5,1,9,8],
    [8,6,5,0,0,0,0,0,3],
    [0,3,2,9,1,8,6,5,0],
    [0,9,0,5,0,7,8,2,0],
    [0,0,0,4,2,0,7,3,9]
    ]
sol_med2=[
    [6,8,4,2,5,3,9,1,7],
    [5,7,1,6,9,4,3,8,2],
    [9,2,3,8,7,1,4,6,5],
    [3,1,9,7,8,2,5,4,6],
    [2,4,7,3,6,5,1,9,8],
    [8,6,5,1,4,9,2,7,3],
    [7,3,2,9,1,8,6,5,4],
    [4,9,6,5,3,7,8,2,1],
    [1,5,8,4,2,6,7,3,9]
    ]
juego_dif1=[
    [0,7,0,0,9,0,0,5,2],
    [0,0,0,0,0,0,0,0,0],
    [3,0,9,0,8,0,0,0,0],
    [0,0,0,7,0,9,4,0,0],
    [0,5,0,0,3,0,9,0,0],
    [0,0,8,6,5,0,0,3,7],
    [0,8,2,0,0,0,5,7,0],
    [0,4,0,0,2,0,6,0,8],
    [6,0,0,1,0,0,3,0,4]
    ]
sol_dif1=[
    [8,7,4,3,9,6,1,5,2],
    [5,6,1,2,4,7,8,9,3],
    [3,2,9,5,8,1,7,4,6],
    [2,3,6,7,1,9,4,8,5],
    [4,5,7,8,3,2,9,6,1],
    [9,1,8,6,5,4,2,3,7],
    [1,8,2,4,6,3,5,7,9],
    [7,4,3,9,2,5,6,1,8],
    [6,9,5,1,7,8,3,2,4]
    ]
juego_dif2=[
    [0,5,0,0,0,1,0,0,0],
    [0,0,0,0,0,6,0,7,0],
    [3,0,9,0,4,0,0,6,5],
    [0,0,8,9,1,4,0,0,0],
    [0,0,0,0,6,7,8,2,9],
    [0,9,7,0,0,0,0,0,4],
    [0,0,4,1,0,0,0,0,0],
    [0,7,0,0,0,0,6,9,1],
    [0,3,5,0,0,0,2,0,0]
    ]
sol_dif2=[
    [8,7,4,3,9,6,1,5,2],
    [5,6,1,2,4,7,8,9,3],
    [3,2,9,5,8,1,7,4,6],
    [2,3,6,7,1,9,4,8,5],
    [4,5,7,8,3,2,9,6,1],
    [9,1,8,6,5,4,2,3,7],
    [1,8,2,4,6,3,5,7,9],
    [7,4,3,9,2,5,6,1,8],
    [6,9,5,1,7,8,3,2,4]
    ]
nivel_facil=[juego_fac1,juego_fac2]
nivel_med=[juego_med1,juego_med2]
nivel_dif=[juego_dif1,juego_dif2]
sol_facil=[sol_fac1,sol_fac2]
sol_med=[sol_med1,sol_med2]
sol_dif=[sol_dif1,sol_dif2]
def crea_matriz():
    global juego_grid
    random_grid=random.randint(0,1)
    if menu=='F':
        juego_grid=nivel_facil[random_grid]
    elif menu=='M':
        juego_grid=nivel_med[random_grid]
    elif menu=='D':
        juego_grid=nivel_dif[random_grid]
    else:
        print('Sólo podrás ingresar \'F\' para nivel fácil, \'M\' para medio y \'D\' para difícil.')
    for columna in range(1):
        for fila in range(9):
            renglon.append(juego_grid[fila])
    matriz.append(renglon)
    return matriz
def vinculo_randomsol(juego_grid):
    global sol_grid
    if juego_grid==juego_fac1:
        sol_grid=sol_fac1
    elif juego_grid==juego_fac2:
        sol_grid=sol_fac2
    elif juego_grid==juego_med1:
        sol_grid=sol_med1
    elif juego_grid==juego_med2:
        sol_grid=sol_med2
    elif juego_grid==juego_dif1:
        sol_grid=sol_dif1
    elif juego_grid==juego_dif2:
        sol_grid=sol_dif2
    return sol_grid
def tablero_bonito(matriz):
    r=len(matriz)
    c=len(matriz[0])
    for renglon in range (r):
        for col in range(c):
            print(matriz[renglon][col],end="\n")
        print()
def continua_juego():
    global jugada,selecc
    for columna in range(9):
        while 0 in juego_grid[columna]:
            selecc=(input('¿Qué casilla quiere cambiar?: ')).split(',')
            jugada=int(input('Número: '))
            if jugada<1 or jugada>9:
                print('Los únicos valores validos del 1 al 9')
            transforma_coord(selecc)
    print('¡Has ganado!')
    print("")
    print("-------------------------------------------------------------")
    print("")  
    print("----------------¡GRACIAS POR USAR MI PROGRAMA!---------------")
    print("--------------Programa hecho por Khadija Fatima--------------")
    print("")
    print("-------------------------------------------------------------")
def coord_posible():
    if juego_grid[coord_fila][coord_col]==0:
        for renglon in range(0,9):
            if juego_grid[coord_fila][renglon]==jugada:
                print('El número seleccionado no está disponible en su fila')
                return False
        for columna in range(0,9):
            if juego_grid[columna][coord_col]==jugada:
                print('El número seleccionado no está disponible en su columna')
                return False
        modulo_fila=coord_fila//3*3
        modulo_col=coord_col//3*3
        for i in range(3):
            for j in range(3):
                if juego_grid[modulo_fila+i][modulo_col+j]==jugada:
                    print('El número seleccionado no está disponible en su recuadro')
                    return False
        if jugada!=sol_grid[coord_fila][coord_col]:
            print('El número seleccionado no va en esa celda, intenta de nuevo')
            return False
    else:
        print('La celda seleccionada ya cuenta con un valor diferente de \'0\'')
        return False
    return True
def transforma_coord(selecc):
    global coord_fila,coord_col
    if selecc[0].isdecimal() and selecc[1].isdecimal():
        coord_fila=(int(selecc[0]))-1
        coord_col=(int(selecc[1]))-1
        if coord_posible():
            juego_grid[coord_fila][coord_col]=jugada
            tablero_bonito(matriz)
        else:
            termina_juego(coord_posible)
    else:
        print('Únicamente deben ingresarse valores numéricos separados por una coma (a,b)')
        tablero_bonito(matriz)
def termina_juego(coord_posible):
    global contador
    contador+=1
    if contador==3:
        print('-----------------------------------------------')
        print('¡¡¡Has tenido 3 errores!!!')
        print('')
        print('----------------------¡SIGUE PRACTICANDO!--------------------')
        print('----------------¡GRACIAS POR USAR MI PROGRAMA!---------------')
        print('')
        print("--------------Programa hecho por Khadija Fatima--------------")
        print('')
        print("-------------------------------------------------------------")
        exit()
    return contador
def main():
    global menu
    print('')
    print('-------------------------------------------------------------')
    print('------------------------¡BIENVENIDO!-------------------------')
    print('-------------------------------------------------------------')
    print('Este programa es el clásico juego de Sudoku. Nota que algunas\ncasillas contienen ceros \'0\', son estas las que debes modificar.\nEl formato para ingresar el número de casilla será de a,b siendo\n\'a\' el número de renglón y \'b\' el número de columna.')
    print('-------------------------------------------------------------')
    print('-------------------------------------------------------------')
    print('')
    menu=input('Hay tres diferentes niveles de juego. ¿Cuál jugarás?\nInserte \'F\' para fácil, \'M\' para medio y \'D\' para difícil: ')
    crea_matriz()
    vinculo_randomsol(juego_grid)
    tablero_bonito(matriz)
    continua_juego()
contador=0
if __name__ == '__main__':
    main()