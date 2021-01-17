import os, pygame
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx

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

def reglas(arreglo):
    arreglo2=crearArreglo(cols,rows)
    i=0
    j=0
    #1+0=1 muerto//muerto//muerto
    #1+1=2 muerto//muerto//muerto
    #1+2=3 VIVO//muerto//muerto
    #1+3=4 VIVO//VIVO//muerto
    #1+4=5 muerto//muerto//muerto
    #1+5=6 muerto//muerto//muerto
    #1+6=7 muerto//muerto//muerto
    #1+7=8 muerto//muerto//VIVO
    #1+8=9 muerto//muerto//muerto
    #0+0=0 muerto//muerto//muerto
    #0+1=1 muerto//muerto//muerto
    #0+2=2 muerto//VIVO//VIVO
    #0+3=3 VIVO//muerto//muerto
    #0+4=4 muerto//muerto//muerto
    #0+5=5 muerto//muerto//muerto
    #0+6=6 muerto//muerto//muerto
    #0+7=7 muerto//muerto//muerto
    #0+8=8 muerto//muerto//muerto
    if toroide=="M":
        while i<cols:
            while j<rows:
                if i == 0:
                    arreglo[i][j]=0
                if i == cols-1:
                    arreglo[i][j]=0
                if j == 0:
                    arreglo[i][j]=0
                if j == rows-1:
                    arreglo[i][j]=0
                j+=1
            j=0
            i+=1
        i=0
        j=0
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
            if juego == "1":
                if state == 3:
                    arreglo2[i][j]=1
                elif state == 4 and arreglo[i][j] == 1:
                    arreglo2[i][j]=1
                else:
                    arreglo2[i][j]=0
            elif juego == "2":
                if state == 4 and arreglo[i][j] == 1:
                    arreglo2[i][j]=1
                elif state == 2 and arreglo[i][j] == 0:
                    arreglo2[i][j]=1
                else:
                    arreglo2[i][j]=0
            else:
                if state == 8 and arreglo[i][j] == 1:
                    arreglo2[i][j]=1
                elif state == 2 and arreglo[i][j] == 0:
                    arreglo2[i][j]=1
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
    cargando=0
    G=nx.DiGraph()
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
        G.add_node(toDecimal(binario))
        arregloEvoluciones=[toDecimal(binario)]
        for z in range(1, 51):
            arreglo=reglas(arreglo)
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
            G.add_edge(arregloEvoluciones[-2], arregloEvoluciones[-1])

        cargando+=6.25
        os.system("cls")
        print(f'Cargando: {cargando}%...')
        arreglo=crearArreglo(cols, rows)
    print(list(nx.connected_components(G)))
    plt.subplot(111)
    nx.draw_planar(G, arrows=True, with_labels=1, node_color='r')
    plt.show()
    arreglo=crearArreglo(cols, rows)

def atractorTres(arreglo):
    medioArregloX=int(len(arreglo)/2)-1
    medioArregloY=int(len(arreglo[medioArregloX])/2)-1
    cargando=0
    G=nx.DiGraph()
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

        arregloEvoluciones=[]
        G.add_node(toDecimal(binario))
        arregloEvoluciones=[toDecimal(binario)]
        for z in range(1, 51):
            arreglo=reglas(arreglo)
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
            G.add_edge(arregloEvoluciones[-2], arregloEvoluciones[-1])
        cargando+=0.1953125
        os.system("cls")
        print(f'Cargando: {cargando}%...')
        arreglo=crearArreglo(cols, rows)
    #plt.subplot(111)
    #nx.draw_kamada_kawai(G, arrows=True, with_labels=1, node_size=80, node_color='r', font_size=8, arrowsize=5)
    nx.draw(G, pos=nx.planar_layout(G, center=[0,0]), arrows=True, with_labels=1, node_size=80, node_color='r', font_size=8)
    plt.show()
    arreglo=crearArreglo(cols, rows)

def paused(arreglo, arregloGeneracion, arregloVivos):
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
                    start(arreglo, arregloGeneracion, arregloVivos)
                elif event.key == pygame.K_s:
                    save(arreglo)
                elif event.key == pygame.K_l:
                    arreglo=load()
                elif event.key == pygame.K_c:
                    arregloGeneracion=[0]
                    arregloVivos=[0]
                    arreglo=crearArreglo(cols, rows)
                elif event.key == pygame.K_g:
                    graficarGeneraciones(arregloGeneracion, arregloVivos)
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

def start(arreglo, arregloGeneracion, arregloVivos):
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
                    paused(arreglo, arregloGeneracion, arregloVivos)
        arreglo=reglas(arreglo)
        arregloVivos.append(pintarPantalla(arreglo))
        arregloGeneracion.append(arregloGeneracion[-1]+1)
        os.system("clear")
        os.system("cls")
        print("Generacion: "+str(arregloGeneracion[-1]))
        print("Celulas Vivas: "+str(arregloVivos[-1]))
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
toroide="X"
juego="0"

while toroide!="T" and toroide!="M":
    toroide=input("Quieres que las orillas sean tratadas como [T]oroide o [M]uertas: ")
    toroide=toroide.upper()

while juego!="1" and juego!="2" and juego!="3":
    juego=input("Selecciona la regla con la que deseas jugar: \n[1] B3/S23\n[2] B2/S3\n[3] B2/S7\nElección: ")



pygame.init()
size = width, height
cols= width/resolution
rows=height/resolution
screen = pygame.display.set_mode(size)
arreglo=crearArreglo(cols,rows)
arregloGeneracion=[0]
arregloVivos=[0]
paused(arreglo, arregloGeneracion, arregloVivos)
