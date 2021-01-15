import os, pygame
import matplotlib
import matplotlib.pyplot as plt

def crearArreglo(cols, rows):
    arreglo=[]
    i, j=0, 0
    while i<cols:
        columnas=[]
        while j<rows:
            columnas.append(0)
            j+=1
        arreglo.append(columnas)
        j=0
        i+=1
    return arreglo

def toDecimal(binario):
    binarioString=str(binario)
    numero_decimal = 0 #aquí iremos sumando el resultado de cada multiplicación
    for posicion, digito_string in enumerate(binarioString[::-1]):
	       numero_decimal += int(digito_string) * 2 ** posicion
    return numero_decimal

def toBinario(decimal):
    binario=bin(int(decimal))
    binary=str(binario)
    binary=binary[2:]
    return binary

def save(arreglo):
    name=input("Nombre del Archivo: ")
    f = open("output.txt",'w')
    for line in arreglo:
        f.write(str(line)+ "\n") # works with any number of elements in a line
    f.close()
    f = open("output.txt",'r')
    data = f.read()
    data = data.replace("[", "")
    f.close()
    fo = open(name+'.txt', "w")
    fo.write(data)
    fo.close()
    fo = open(name+'.txt', "r")
    data = fo.read()
    data = data.replace("]", "")
    fo.close()
    fo = open(name+'.txt', "w")
    fo.write(data)
    fo.close()
    fo = open(name+'.txt', "r")
    data = fo.read()
    data = data.replace("\n", ", ")
    fo.close()
    fo = open(name+'.txt', "w")
    fo.write(data)
    fo.close()
    os.remove("output.txt")
    print("Guardado terminado")
def load():
    name=input("Nombre del Archivo: ")
    f = open (name+'.txt','r')
    arreglo=[]
    elemento=f.read().split(', ')
    elemento=elemento[:-1]
    i, j, k=0, 0, 0
    while i<cols:
        columnas=[]
        while j<rows:
            columnas.append(int(elemento[k]))
            k+=1
            j+=1
        arreglo.append(columnas)
        j=0
        i+=1
    f.close()
    return arreglo
def pintarPantalla(arreglo):
    i=0
    j=0
    total=0
    while i<cols:
        while j<rows:
            x=i*resolution
            y=j*resolution
            if arreglo[i][j]==1:
                pygame.draw.rect(screen, colorVivo, (x,y, resolution, resolution))
                total+=1
            elif arreglo[i][j]==0:
                pygame.draw.rect(screen, colorMuerto, (x,y, resolution, resolution))
            j+=1
        j=0
        i+=1
    pygame.display.flip()
    return total

def pintarCalor(arregloCalor, screenCalor):
    i=0
    j=0
    total=0
    multiplicador=255/arregloGeneracion[-1]
    while i<cols:
        while j<rows:
            x=i*resolution
            y=j*resolution
            pygame.draw.rect(screenCalor, (255,int(255-(arregloCalor[i][j]*multiplicador)),int(255-(arregloCalor[i][j]*multiplicador))), (x,y, resolution, resolution))
            j+=1
        j=0
        i+=1
    pygame.display.flip()
    calor=True
    while calor==True:
        for event in pygame.event.get():
            #Si el evento es salir de la ventana, terminamos
            if event.type == pygame.QUIT:
                calor = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    calor=False

def reglas(arreglo, arregloCalor):
    arreglo2=crearArreglo(cols,rows)
    i=0
    j=0
    #1+0=1 MUERTO
    #1+1=2 MUERTO
    #1+2=3 VIVO
    #1+3=4 VIVO
    #1+4=5 MUERTO
    #1+5=6 MUERTO
    #1+6=7 MUERTO
    #1+8=9 MUERTO
    #0+0=0 MUERTO
    #0+1=1 MUERTO
    #0+2=2 MUERTO
    #0+3=3 VIVO
    #0+4=4 MUERTO
    #0+5=5 MUERTO
    #0+6=6 MUERTO
    #0+7=7 MUERTO
    #0+8=8 MUERTO
    while i<cols:
        while j<rows:
            state = arreglo[i][j]
            if state!=0:
                arreglo2=sumarVecinos(arreglo2, i, j)
            j+=1
        j=0
        i+=1
    i=0
    j=0
    while i<cols:
        while j<rows:
            state=arreglo2[i][j]
            if state == 3:
                arreglo2[i][j]=1
                arregloCalor[i][j]+=1
            elif state == 4 and arreglo[i][j] == 1:
                arreglo2[i][j]=1
                arregloCalor[i][j]+=1
            else:
                arreglo2[i][j]=0
            j+=1
        j=0
        i+=1
    arreglo = arreglo2
    return arreglo

def sumarVecinos(arreglo, x, y):
    i=-1
    j=-1
    while i<2:
        while j<2:
            col=int((x+i+cols)%cols)
            row=int((y+j+rows)%rows)
            arreglo[col][row]+=1
            j+=1
        j=-1
        i+=1
    return arreglo

def graficarGeneraciones(generacion, vivos):
    plt.plot(generacion, vivos)
    plt.xlabel("Generación")
    plt.ylabel("Células Vivas")
    plt.show()

def atractorDos(arreglo):
    medioArregloX=int(len(arreglo)/2)-1
    medioArregloY=int(len(arreglo[medioArregloX])/2)-1
    arregloAtractores=[]
    cargando=0
    for x in range(0, 16):
        binario=toBinario(x)
        if len(binario)<4:
            binario="000"+binario
            binario=binario[-4:]
        if binario[0]=="1":
            arreglo[medioArregloX][medioArregloY]=1
        if binario[1]=="1":
            arreglo[medioArregloX+1][medioArregloY]=1
        if binario[2]=="1":
            arreglo[medioArregloX][medioArregloY+1]=1
        if binario[3]=="1":
            arreglo[medioArregloX+1][medioArregloY+1]=1

        arregloCalor=crearArreglo(cols, rows)
        arregloEvoluciones=[]
        for z in range(0, 251):
            arreglo=reglas(arreglo, arregloCalor)
            if arreglo[medioArregloX][medioArregloY]==1:
                evolucion="1"
            else:
                evolucion="0"
            if arreglo[medioArregloX+1][medioArregloY]==1:
                evolucion+="1"
            else:
                evolucion+="0"
            if arreglo[medioArregloX][medioArregloY+1]==1:
                evolucion+="1"
            else:
                evolucion+="0"
            if arreglo[medioArregloX+1][medioArregloY+1 ]==1:
                evolucion+="1"
            else:
                evolucion+="0"
            arregloEvoluciones.append(toDecimal(evolucion))
        cargando+=6.25
        os.system("cls")
        print(f'Cargando: {cargando}%...')
        arregloAtractores.append(arregloEvoluciones)
        arreglo=crearArreglo(cols, rows)
        plt.plot(range(0,251), arregloAtractores[x])
    plt.xlabel("Generación")
    plt.ylabel("Estructuras")
    plt.show()
    arreglo=crearArreglo(cols, rows)

def atractorTres(arreglo):
    medioArregloX=int(len(arreglo)/2)-1
    medioArregloY=int(len(arreglo[medioArregloX])/2)-1
    arregloAtractores=[]
    cargando=0
    for x in range(0, 512):
        binario=toBinario(x)
        if len(binario)<9:
            binario="00000000"+binario
            binario=binario[-9:]
        if binario[0]=="1":
            arreglo[medioArregloX][medioArregloY]=1
        if binario[1]=="1":
            arreglo[medioArregloX+1][medioArregloY]=1
        if binario[2]=="1":
            arreglo[medioArregloX+2][medioArregloY]=1
        if binario[3]=="1":
            arreglo[medioArregloX][medioArregloY+1]=1
        if binario[4]=="1":
            arreglo[medioArregloX+1][medioArregloY+1]=1
        if binario[5]=="1":
            arreglo[medioArregloX+2][medioArregloY+1]=1
        if binario[6]=="1":
            arreglo[medioArregloX][medioArregloY+2]=1
        if binario[7]=="1":
            arreglo[medioArregloX+1][medioArregloY+2]=1
        if binario[8]=="1":
            arreglo[medioArregloX+2][medioArregloY+2]=1

        arregloCalor=crearArreglo(cols, rows)
        arregloEvoluciones=[]
        for z in range(0, 251):
            arreglo=reglas(arreglo, arregloCalor)
            if arreglo[medioArregloX][medioArregloY]==1:
                evolucion="1"
            else:
                evolucion="0"
            if arreglo[medioArregloX+1][medioArregloY]==1:
                evolucion+="1"
            else:
                evolucion+="0"
            if arreglo[medioArregloX+2][medioArregloY]==1:
                evolucion+="1"
            else:
                evolucion+="0"
            if arreglo[medioArregloX][medioArregloY+1]==1:
                evolucion+="1"
            else:
                evolucion+="0"
            if arreglo[medioArregloX+1][medioArregloY+1]==1:
                evolucion+="1"
            else:
                evolucion+="0"
            if arreglo[medioArregloX+2][medioArregloY+1]==1:
                evolucion+="1"
            else:
                evolucion+="0"
            if arreglo[medioArregloX][medioArregloY+2]==1:
                evolucion+="1"
            else:
                evolucion+="0"
            if arreglo[medioArregloX+1][medioArregloY+2]==1:
                evolucion+="1"
            else:
                evolucion+="0"
            if arreglo[medioArregloX+2][medioArregloY+2]==1:
                evolucion+="1"
            else:
                evolucion+="0"
            arregloEvoluciones.append(toDecimal(evolucion))
        cargando+=0.1953125
        os.system("cls")
        print(f'Cargando: {cargando}%...')
        arregloAtractores.append(arregloEvoluciones)
        arreglo=crearArreglo(cols, rows)
        plt.plot(range(0,251), arregloAtractores[x])
    plt.xlabel("Generación")
    plt.ylabel("Estructuras")
    plt.show()
    arreglo=crearArreglo(cols, rows)

def paused(arreglo, arregloGeneracion, arregloVivos, arregloCalor):
    pygame.display.set_caption('Game of Life: PAUSADO. P=Jugar, Click=Modificar Celulas, S=Guardar, L=Cargar')
    pause=True
    while pause==True:
        for event in pygame.event.get():
            #Si el evento es salir de la ventana, terminamos
            if event.type == pygame.QUIT:
                pause = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    start(arreglo, arregloGeneracion, arregloVivos, arregloCalor)
                elif event.key == pygame.K_s:
                    save(arreglo)
                elif event.key == pygame.K_l:
                    arreglo=load()
                elif event.key == pygame.K_c:
                    arregloGeneracion=[0]
                    arregloVivos=[0]
                    arreglo=crearArreglo(cols, rows)
                    arregloCalor=crearArreglo(cols, rows)
                elif event.key == pygame.K_g:
                    graficarGeneraciones(arregloGeneracion, arregloVivos)
                elif event.key == pygame.K_h:
                    screenCalor = pygame.display.set_mode(size)
                    pintarCalor(arregloCalor, screenCalor)
                elif event.key == pygame.K_2:
                    arreglo=crearArreglo(cols, rows)
                    atractorDos(arreglo)
                elif event.key == pygame.K_3:
                    arreglo=crearArreglo(cols, rows)
                    atractorTres(arreglo)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if arreglo[int(pos[0]/resolution)][int(pos[1]/resolution)]==0:
                    arreglo[int(pos[0]/resolution)][int(pos[1]/resolution)]=1
                else:
                    arreglo[int(pos[0]/resolution)][int(pos[1]/resolution)]=0
        pintarPantalla(arreglo)

def start(arreglo, arregloGeneracion, arregloVivos, arregloCalor):
    pygame.display.set_caption('Game of Life: JUGANDO. P=Pausar')
    run=True
    while run == True:
        for event in pygame.event.get():
            #Si el evento es salir de la ventana, terminamos
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused(arreglo, arregloGeneracion, arregloVivos, arregloCalor)
        arregloVivos.append(pintarPantalla(arreglo))
        arregloGeneracion.append(arregloGeneracion[-1]+1)
        os.system("clear")
        os.system("cls")
        print("Generacion: "+str(arregloGeneracion[-1]))
        print("Celulas Vivas: "+str(arregloVivos[-1]))

        arreglo=reglas(arreglo, arregloCalor)
        pygame.time.delay(100)


i=0
colorVivo=[]
colorMuerto=[]
while i<3:
    if i==0:
        texto="Color del Vivo(R):"
    elif i==1:
        texto="Color del Vivo(G):"
    else:
        texto="Color del Vivo(B):"
    colorVivo.append(int(input(texto)))
    i+=1
i=0
while i<3:
    if i==0:
        texto="Color del Muerto(R):"
    elif i==1:
        texto="Color del Muerto(G):"
    else:
        texto="Color del Muerto(B):"
    colorMuerto.append(int(input(texto)))
    i+=1
width=int(input("Teclea el ancho de la ventana en pixeles: "))
height=int(input("Teclea el alto de la ventana en pixeles: "))
resolution=int(input("Teclea la dimensión de la célula viva, en pixeles: "))



pygame.init()
size = width, height
cols= width/resolution
rows=height/resolution
screen = pygame.display.set_mode(size)
arreglo=crearArreglo(cols,rows)
arregloCalor=crearArreglo(cols,rows)
arregloGeneracion=[0]
arregloVivos=[0]
paused(arreglo, arregloGeneracion, arregloVivos, arregloCalor)
