import networkx as nx
import matplotlib.pyplot as plt

def inicializar():
    G = nx.Graph()
    return G

def criarGrafo(G, arquivo):
    print('Montando o grafo...')
    for i in arquivo:
        x = i.split(' ')
        G.add_edge(str(x[0]), str(x[1]).rstrip('\n'))

def plotGrafo(G):
    nx.draw(G, with_labels=1)
    print('Gerando a imagem...')
    plt.savefig('grafo.png', format='png')
    plt.show()
    print('Proceso finalizado!\n')

def listaGrauVertice(G, listaGrafo, listaGrau):
    arquivo = open('facebook_combined.txt', 'r')
    contador = 0
    for i in arquivo:
        x = i.split(' ')
        y = x[0]
        if y not in listaGrafo:
            listaGrafo.append(y)
            contador += 1

    listaGrau = [0]*contador    

    for i in listaGrafo:
        indice = listaGrafo.index(i)
        listaGrau[indice] = int(G.degree[i])

    print('teste')
    Insertionsort(listaGrau, listaGrafo)

    
def Insertionsort(quantificador, identificador):
    for p in range(0, len(quantificador)):
        quantificador_atual = quantificador[p]
        identificador_atual = identificador[p]

        while p > 0 and quantificador[p - 1] > quantificador_atual:
            quantificador[p] = quantificador[p - 1]
            identificador[p] = identificador[p - 1]
            p -= 1

        quantificador[p] = quantificador_atual
        identificador[p] = identificador_atual
    print('finalizado')


def somatoriaCloseness(G, listaGrafo, no):
    soma = 0
    for x in listaGrafo:
        soma += len(list(nx.shortest_path(G, no, x)))
    return soma
        


    


G = inicializar()
arquivo = open('facebook_combined.txt', 'r')
criarGrafo(G, arquivo)
#plotGrafo(G)
listaGrafo = []
listaGrau = []
listaGrauVertice(G, listaGrafo, listaGrau)

'''x = len(listaGrafo) - 1
for i in range(len(listaGrafo)):
    print("Vertice "+str(listaGrafo[i])+ " tem grau "+str(G.degree[str(listaGrafo[i])]))
    '''

#lista = list(G.adj[listaGrafo[3000]])
#print(listaGrafo)
listaClose = [0] * len(listaGrafo)
'''
contador = 0
novoArquivo = open("teste.txt", "w")
for i in listaGrafo:
    listaClose[contador] = somatoriaCloseness(G, listaGrafo, i)
    x = str(listaClose[contador])
    print("soma: "+ x +" vertice:"+ i)
    novoArquivo.write(x+"\n")
    contador += 1
'''
arquivo = open("teste.txt", "r")

contador = 0
for i in arquivo:
    listaClose[contador] = int(i.rstrip("\n"))
    contador += 1

Insertionsort(listaClose, listaGrafo)
x = len(listaGrafo) - 1
for i in range(10):
    print("Vertice "+str(listaGrafo[x-i])+ " tem closeness "+str(1/listaClose[x-i]))
