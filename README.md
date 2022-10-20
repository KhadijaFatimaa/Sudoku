# Sudoku ##Proyecto Final de la materia Pensamiento Computacional para Ingeniería ###Primer Semestre de la Ingenería en Ciencia de Datos y Matemáticas en el Instituto Tecnológico de Estudios Superiores de Monterrey.

El clásico juego de sudoku en una versión simple de Python. Este código tiene 7 funciones además del main(). Para representar casillas vacías se utilizaron '0' (ceros).
Se empieza por definir una matriz y lista vacía que serán utilizadas más adelante para crear el tablero del juego. En esta primera versión del juego se trabaja con tableros predeterminados, dos por cada nivel: fácil, medio y difícil. Al mismo tiempo, se vinculan los tableros de juego con sus soluciones en la función de vinculo_randomsol(juego_grid). Posteriormente se imprime la matriz de juego en forma de un tablero casi convencional con la función tablero_bonito(matriz).

Ya teniendo el tablero impreso, empiezan a trabajar las funciones relacionadas con el juego que definiré en el mismo orden en el que son llamadas:
continua_juego(): Pregunta al usuario qué casilla cambiará y con qué número lo llenará siempre y cuando aún existan '0' (ceros) en el tablero. Si no se encuentra ningún cero en el tablero imprime un mensaje diciendo que se ganó el juego.
transforma_coord(selecc): Recibe el input de casilla del usuario y lo transforma en una coordenada del tablero. 
coord_posible(): Revisa que la casilla propuesta por el usuario este vacía y que el número propuesto por el usuario vaya acorde con las reglas del sudoku: que éste no esté presente en su misma fila, columna, subrecuadro y que permita resolver el juego con una única solución.
termina_juego(coord_posible): Cuenta cada vez que el usuario comete un error y termina el juego cuando el usuario ha cometido 3 errores. 
