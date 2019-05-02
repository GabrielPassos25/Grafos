caminhos1=[]
caminhos2=[]
distancias=[]
def criar_grafo():
    print("=-"*30)
    print("Para adicionar grafos, digite 1 quando solicitado!\nCaso não deseje mais adicionar grafos, digite 0!")
    print("Escreva primeiro o nome do primeiro caminho, logo em seguida, o destino e a distancia")
    i =1
    caminho1 = input("Digite o nome do seu {}° caminho:".format(i))
    caminho2 = input("Digite o nome do caminho que se conecta ao vértice {}:".format(caminho1))
    distancia = int(input("Digite a distância ente os caminhos {} e {}:".format(caminho1,caminho2)))
    print("=-"*50)
    adicionar = int(input("Deseja adicionar mais algum vértice?[1/0]"))
    caminhos1.append(caminho1)
    caminhos2.append(caminho2)
    distancias.append(distancia)
    print("=-"*50)
    todos_caminhos =[caminho1]
    for z in range(0,len(caminhos2)):
        todos_caminhos.append(caminhos2[z]) 
    caminhos_sem_rep=sorted(set(todos_caminhos))
    if adicionar ==1:
        v=1
        x=3
        while v==1:
            conector=input("Digite o nome do {} vértice:".format(x))
            caminhos2.append(conector)
            local_conector = input("Vértices disponíveis: {}.\nDeseja adicionar o vértice {} em qual vértice(s) já existente(s)?".format(sorted(set(caminhos_sem_rep)),conector))
            caminhos1.append(local_conector)
            while local_conector not in caminhos_sem_rep:
                local_conector = input("Vértices disponíveis: {}.\nDeseja adicionar o vértice {} em qual vértice já existente?".format(caminhos_sem_rep,conector))
            caminhos_sem_rep.append(conector)
            distancia = int(input("Digite a distância ente os caminhos {} e {}:".format(local_conector,conector)))
            distancias.append(distancia)
            x+=1
            print("=-"*50)
            adicionar = int(input("Deseja adicionar mais algum vértice?[1/0]"))
            if adicionar ==0:
                v=0
criar_grafo()
print("=-"*50)
#Mostra a distância entre todos os pontos
for i in range(0,len(caminhos1)):
    print("Distância entre",caminhos1[i],"e",caminhos2[i],":",distancias[i])
print("=-"*50)


    


