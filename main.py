import time 
from collections import deque

class Graph:
    def __init__(self, nodes):
        
        """
    Esta é a função construtora e recebe os vertíces como parâmetros.    

        """

        self.nodes = nodes
        self.adj = list()
        
        for i in range(nodes):
            self.adj.append(list())
        
        self.visited = [0]*nodes
        self.q = deque()
    
    def add_edge(self, v, u):
        """
    
    Esta função conecta os vertices formando as arestas e recebe dois vertíces.
        
        """
        for i in self.adj[u]:
            if i == v:
                return False
        
        self.adj[u].append(v)
        self.adj[v].append(u)

        return True
        
    def dfs(self, node):
        """
    Essa função realiza a busca em profundidade e recebe como parâmetro o vertice atual do dfs e verifica se ja o visitou.   
        """


        self.visited[node] = 1
        
        for to in self.adj[node]:
         
            if self.visited[to] == 0:
                self.dfs(to)
        
        
    def bfs(self, node):

        """
    Essa função realiza a busca em largura e recebe como parâmetro o vertice atual do bfs e verifica se ja o visitou.   
        """
        
        self.q.append(node)
        self.visited[node]=1
        
        while (len(self.q) > 0):
           
            u = self.q.popleft()
              
            for to in self.adj[u]:
                if self.visited[to] == 0:
                    self.visited[to] = 1
                    self.q.append(to)
        
    def clear_vis(self):
        """
    Essa função reinicializa o vetor de visitados e não possuí parâmetro.    
        """
        for i in range(len(self.visited)):
            self.visited[i] = 0
        
    def play(self):
        """
    Esta função utiliza as funções anteriores e retorna o tempo gasto no dfs e no bfs
        """

        self.clear_vis()
        self.time_dfs = time.time() 
        
        for i in range(self.nodes):
            if self.visited[i] == 0:
                self.dfs(i)
        
        self.time_dfs = time.time() - self.time_dfs
        
        self.q.clear()
        self.clear_vis()
        self.time_bfs = time.time()
        
        for i in range(self.nodes):
            if self.visited[i] == 0:
                self.bfs(i)
        
        self.time_bfs = time.time() - self.time_bfs
        
        return self.time_dfs, self.time_bfs


class Player:
    """
    Essa classe descreve um jogador 
    """
    def __init__(self, n, m, nome):
        
        self.nome = nome
        self.n = n
        self.m = m
        self.g = Graph(n)
        self.time = [0, 0]
    
    def add_edge(self, u, v):
        return self.g.add_edge(u, v)
    
    def play(self):
        
        a, b = self.g.play()
        self.time[0] += a
        self.time[1] += b



class Game:
    """
   Essa classe possuí todos os prints e o menu do jogo 
    """

    def input_num(self, msg, min, max):
        
        num = input(msg + ' ')
        while True:

            if not num.isdigit():
                num = input("Digite um número válido ")
                continue

            num = int(num)

            if num > max or num < min:
                msg = "Digite um numero entre" + str(min) + "e" + str(max) + ' '
                num = input(msg)
                continue

            return num

    def input_pair(self, msg, min, max):
        t = input(msg).split()

        while True:
            if len(t) != 2:
                t = input("Insira um par de numeros ").split()
                continue

            a, b = t

            if not a.isdigit() or not b.isdigit():
                t = input("Digite um par de números válidos separados por um espaço ").split()
                continue

            a = int(a)
            b = int(b)

            if a > max or a < min or b < min or b > max or a == b:
                msg = "Digite um par de numeros diferentes entre " + str(min) + " e " + str(max) + ' '
                t = input(msg).split()
                continue
    
            return a, b
    
    def play(self):
        n = self.input_num("Insira o numero de vértices", 0, 100)
        m = self.input_num("Insira o numero de arestas", n-1, n*(n-1)//2)
        
        nome1 = input("Jogador 1 insira o seu nome: ")
        p1 = Player(n, m, nome1)
        print("Bem vindo", p1.nome)
        
        nome2 = input("Jogador 2 insira o seu nome: ")
        p2 = Player(n, m, nome2)
        print("Bem vindo", p2.nome)

        print(p1.nome, "escolha suas arestas")
        for _ in range(m):
            while True:
                u, v = self.input_pair('', 0, n-1)
                if p1.add_edge(u, v):
                    break
                print("Insira uma aresta diferente")
        
        print(p2.nome, "escolha suas arestas")
        for _ in range(m):
            while True:
                u, v = self.input_pair('', 0, n-1)
                if p2.add_edge(u, v):
                    break
                print("Insira uma aresta diferente")
        
        for _ in range(100):
            p1.play()
            p2.play()

        tipo = input("Selecione o modo de jogo:\n0 para decidir no BFS\n1 para decidir no DFS\n2 para decidir em ambos\n")

        if tipo == '0':
            t1 = p1.time[1]
            t2 = p2.time[1]
        elif tipo == '1':
            t1 = p1.time[0]
            t2 = p1.time[0]
        else:
            t1 = p1.time[1] + p1.time[0]
            t2 = p2.time[1] + p2.time[0]
        
        winner = ''
        
        if t1 < t2:
            winner = p1.nome
        else:
            winner = p2.nome

        
        print("Parabens", winner, "ganhou")
        print("Margem:", t1, t2)


game = Game()
game.play()