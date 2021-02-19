import time 
from collections import deque

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj = [list()]*nodes
        self.visited = [0]*nodes
    
    def add_edge(self, v, u):
        for i in self.adj[u]:
            if i == v:
                return False
        
        self.adj[u].append(v)
        self.adj[v].append(u)

        return True
        
    def dfs(self, node):
        self.visited[node] = 1
        
        for to in self.adj[node]:
         
            if self.visited[to] == 0:
                self.dfs(to)
        
        
    def bfs(self, node):
        q = deque()
        q.append(node)
        self.visited[node]=1
        
        while (len(q) > 0):
          
            u = q.popleft()
              
            for to in self.adj[u]:
                if self.visited[to] == 0:
                    self.visited[to] = 1
                    q.append(to)
        
    def clear_vis(self):
        for i in range(len(self.visited)):
            self.visited[i] = 0
        
    def play(self):
      
        self.time_dfs = time.time() 
        self.clear_vis()
        for i in range(self.nodes):
            if self.visited[i] == 0:
                self.dfs(i)
        
        self.time_dfs = time.time() - self.time_dfs
        
        self.time_bfs = time.time()
        self.clear_vis()
        for i in range(self.nodes):
            if self.visited[i] == 0:
                self.bfs(i)
        
        self.time_bfs = time.time() - self.time_bfs
        
        return self.time_dfs, self.time_bfs


class Player:
    def __init__(self, n, m, nome):
        self.nome = nome
        self.n = n
        self.m = m
        self.g = Graph(n)
    
    def add_edge(self, u, v):
        if self.g.add_edge(u, v) == False:
            return False
        return True
    
    def play(self):
        self.time = self.g.play()



class Game:
    def play(self):
        n = int(input("Insira o numero de vertices "))
        m = int(input("Insira o numero de arestas "))
        
        nome1 = input("Jogador 1 insira o seu nome: ")
        p1 = Player(n, m, nome1)
        print("Bem vindo", p1.nome)
        
        nome2 = input("Jogador 2 insira o seu nome: ")
        p2 = Player(n, m, nome2)
        print("Bem vindo", p2.nome)

        print(p1.nome, "escolha suas arestas")
        for _ in range(m):
            u, v = map(int, input().split())
            p1.add_edge(u, v)
        
        print(p2.nome, "escolha suas arestas")
        for _ in range(m):
            u, v = map(int, input().split())
            p2.add_edge(u, v)
        
        p1.play()
        p2.play()

        tipo = input("Selecione o modo de jogo:\n0 para decidir no BFS\n1 para decidir no DFS\n2 para decidir em ambos")

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

game = Game()
game.play()