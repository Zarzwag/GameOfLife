# GameOfLife
Juego de la Vida de Conway. Con multiples tamaños de arreglo, generación de gráfica y mapa de calor.


# Inicio
El juego esta programado en Python 3, utilizando la librerıa Pygame como
motor grafico. Para iniciar el programa escribimos ”python3 GameOfUltimate.py" en
la consola, mientras nos encontramos en la carpeta que contiene dicho pro-
grama. Presionamos Enter y comienza el programa.

Al iniciar la consola nos preguntara el color en RGB de las celulas vivas
y muertas, con el fin de que el usuario pueda decidirse por el color que mas
le convenga o guste. Despues de esto la consola preguntara el tamaño de la
pantalla en pixeles. Una vez tecleado este dato, solo falta decidir el tamaño
de la celula en pixeles. Cabe destacar que si elegimos por ejemplo, un tamano
de ventana de 800x600 pixeles, y un tama ̃no de celula de 20 pixeles, entonces
el programa automaticamente generara el arreglo bidimensional de tama ̃no
40x20 celulas.
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
-Una vez querramos que el juego inicie, presionamos la tecla ”P”(de
”Pausa”) para que el juego comience a evolucionar.
-También podemos presionar la tecla "G" (de Gráfica), para generar en una ventana aparte,
la gráfica de densidad poblacional a través de las generaciones.
-En este estado podemos tambien presionar la tecla "H"(de Heat) para activar y desactivar
la vista de "calor". Que nos muestra qué células han estado vivas más tiempo.
-Por último, podemos presionar la tecla "C"(de Clear) para reiniciar el tablero, conteo de generación, gráfica poblacional y mapa de calor.

# Estado de Evolucion
Una vez iniciado el juego,  ́este comenzara la evolucion de las celulas de
forma interminable. Al mismo tiempo, en la consola se imprime
la cantidad de celulas vivas y la generacion en la que nos encontramos desde
que quitamos la pausa.
Si queremos generar algun cambio en el juego, o pausarlo en cualquier
momento, presionamos la tecla ”P”para que el juego se detenga inme-
diatamente y regresemos al estado de Pausa.

El espacio celular esta programado como un toroide, de manera que
si una celula esta en el borde superior, tomara en cuenta las celulas
del borde inferior y viceversa. Esto pasa de igual manera con los dos
costados.
