# GameOfLife
Juego de la Vida de Conway. Con multiples tamaños de arreglo, generación de gráfica y calculo de atractores en arreglos 2x2 hasta 4x4.


# Inicio
El juego está programado en Python 3, utilizando la librería Pygame como motor gráfico, NetworkX para manejar los Diagramas de Ciclos y MatPlotLib para imprimir en pantalla éstos. Hay que estar seguros de tener instaladas estas Librerías en la computadora.
Para iniciar el programa escribimos 'python3 GameOfUltimate.py' en la consola, mientras nos encontramos en la carpeta que contiene dicho programa. Presionamos Enter y comienza el programa.

Al iniciar la consola nos preguntará el color en RGB de las celulas vivas y muertas, con el fin de que el usuario pueda decidirse por el color que más le convenga o guste. Después de esto la consola preguntará el tamaño de la pantalla en pixeles. Una vez tecleado este dato, solo falta decidir el tamaño de la célula en pixeles. Cabe destacar que si elegimos por ejemplo, un tamaño de ventana de 800x600 pixeles, y un tamaño de célula de 20 pixeles, entonces el programa automáticamente generará el arreglo bidimensional de tamaño 40x20 células.
Después de esto, el programa nos preguntará cómo queremos tratar las orillas del arreglo: Como un toroide o como células muertas.
Por último hay que elegir con cuál de las tres reglas programadas queremos jugar.
# Estado de Pausa

Una vez iniciado el Juego, todas las celulas estaran en estado ”Muer-
to”, y el Juego Pausado. Basta con dar click en cualquier punto de la
pantalla, para generar una celula Viva. O bien, convertir una que ya lo
este al estado ”Muerto”. Este proceso se puede realizar cuantas veces
se quiera.

-De igual manera, en este estado podemos presionar la tecla ”S”(de
”Save”) para guardar el estado actual del Juego a un archivo ”.txt”.
La consola nos preguntara el nombre que queremos asignarle a este
archivo, guardandolo en la misma carpeta donde se encuentra el archivo
del Juego.

-En este estado de Pausa, tambien podemos presionar la tecla ”L”(de
Load) para cargar un Juego antes guardado. La consola nos preguntara
el nombre del archivo ”.txt.a cargar, el cual se tiene que encontrar en
la misma carpeta que el archivo del Juego. Hasta el momento, solo
podemos cargar archivos que se hayan creado con el mismo tamaño
de Pantalla y Celula, pues de otra manera se genera un error.

-Si queremos reiniciar por completo el juego (Matar a todas las células, reinciar contadores de Generación y Células Vivas), presionamos la tecla 'C' (de Clear)

-Al presionar la tecla 'G' (de Graph), generamos una gráfica que muestra la densidad poblacional del juego, con respecto al tiempo. Si queremos regresar al juego, hay que cerrar la ventana de la gráfica.

-Si presionamos la tecla '2', el programa comienza a calcular los diagramas de ciclos para un arreglo 2x2. (Se recomienda hacerlo en un arreglo de 4x4 células, y jugando con las orillas 'Muertas', con la finalidad de que haya una capa exterior de células muertas). El progreso de este cálculo se va mostrando en la consola. Una vez terminado, automáticamente se abre una ventana con los diagramas de ciclos. Así pues, es fácil detectar los Atractores.

-Si presionamos la tecla '3', el programa comienza a calcular los diagramas de ciclos para un arreglo 3x3. (Se recomienda hacerlo en un arreglo de 5x5 células, y jugando con las orillas 'Muertas', con la finalidad de que haya una capa exterior de células muertas). El progreso de este cálculo se va mostrando en la consola. Una vez terminado, automáticamente se abre una ventana con los diagramas de ciclos. Así pues, es fácil detectar los Atractores.

-Si presionamos la tecla '4', el programa comienza a calcular los diagramas de ciclos para un arreglo 4x4. (Se recomienda hacerlo en un arreglo de 6x6 células, y jugando con las orillas 'Muertas', con la finalidad de que haya una capa exterior de células muertas). El progreso de este cálculo se va mostrando en la consola. Una vez terminado, automáticamente se abre una ventana con los diagramas de ciclos. Así pues, es fácil detectar los Atractores.

-Una vez querramos que el juego inicie, presionamos la tecla 'P' (de 'Play') para que el juego comience a evolucionar.

# Estado de Evolucion
Una vez iniciado el juego,  ́este comenzara la evolucion de las celulas de
forma interminable. Al mismo tiempo, en la consola se imprime
la cantidad de celulas vivas y la generacion en la que nos encontramos desde
que quitamos la pausa.

-Si queremos generar algun cambio en el juego, o pausarlo en cualquier
momento, presionamos la tecla ”P”para que el juego se detenga inme-
diatamente y regresemos al estado de Pausa.

El espacio celular esta programado como un toroide, de manera que
si una celula esta en el borde superior, tomara en cuenta las celulas
del borde inferior y viceversa. Esto pasa de igual manera con los dos
costados.
