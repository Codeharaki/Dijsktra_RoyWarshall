from data import *
import numpy as np


def InitDijkstra(arr, s_r):
    N = len(arr)
    d = np.full(N, np.inf)
    pi = np.zeros(N)
    d[s_r] = 0
    pi[s_r] = s_r
    return d, pi


def Relacher(d, pi, arr, u, v):
    if d[v] > (d[u] + arr[u][v]):
        d[v] = d[u] + arr[u][v]
        pi[v] = u
    return d, pi


def minDistance(O, F, d, sommets):
    N = len(arr)
    temp = np.full((keys), np.inf)
    temp = list(temp)
    for u in sommets:
        i = sommets.index(u)
        if O[i] == 0 and F[i] == 1:
            temp[i] = d[i]
    return temp.index(min(temp))


def Dijkstra(arr, s, sommets, choix):
    N = len(arr)
    F = np.ones((N))
    O = np.ones((N))
    s_r = sommets.index(s)
    d, pi = InitDijkstra(arr, s_r)
    O[sommets.index(s)] = 0
    for i in range(0, N):
        u = minDistance(O, F, d, sommets)
        for v in range(0, N):
            if arr[u][v] < np.inf and F[v] == 1:
                O[v] = 0
                if choix == 1:
                    d, pi = Relacher(d, pi, arr, u, v)
                if choix == 2:
                    d, pi = Relacher2(d, pi, arr, u, v)
        F[u] = 0
    return d, pi


def Relacher2(d, pi, arr, u, v):
    if arr[u][v] != 0:
        if d[v] > (d[u] + 1):
            d[v] = d[u] + 1
            pi[v] = u
    return d, pi


def compare(d1, d2, spot_rdv, sommets):
    N = len(d1)
    temp = np.inf
    for fin in spot_rdv:
        if (d1[sommets.index(fin)] != 0 or d2[sommets.index(fin)] != 0):
            if (temp > d1[sommets.index(fin)] + d2[sommets.index(fin)]):
                l_fin = fin
                temp = d1[sommets.index(fin)] + d2[sommets.index(fin)]
    return l_fin


def minimal_s(pi1, pi2, d1, d2, s_i1, s_i2, arr, sommets):
    N = len(d1)
    l_fin = 0
    temp_arr = np.full(len(d1), np.inf)
    for fin in spot_rdv:
        i = sommets.index(fin)
        if d1[i] != 0 or d2[i] != 0:
            temp_arr[i] = d1[i] + d2[i]
    temp = np.inf
    for k in range(0, len(np.where(temp_arr == temp_arr.min())) + 1):
        temp1 = 0
        temp2 = 0
        save = 0
        j = np.where(temp_arr == temp_arr.min())[0][k]
        if d1[j] != 0:
            while True:
                save = int(j)
                j = pi1[int(j)]
                temp1 += arr[int(j)][save]
                if int(pi1[int(j)]) == sommets.index(s_i1):
                    save = int(j)
                    j = pi1[int(j)]
                    if save != j:
                        temp1 += arr[int(j)][save]
                    break
        else:
            temp1 = 0
        save = 0
        j = np.where(temp_arr == temp_arr.min())[0][k]
        if (d2[j] != 0):
            while True:
                save = int(j)
                j = pi2[int(j)]
                temp2 += arr[int(j)][save]
                if int(pi2[int(j)]) == sommets.index(s_i2):
                    save = int(j)
                    j = pi2[int(j)]
                    if save != j:
                        temp2 += arr[int(j)][save]
                    break
        else:
            temp2 = 0
        if temp > (temp1 + temp2):
            temp = temp1 + temp2
            l_fin = np.where(temp_arr == temp_arr.min())[0][k]

    return sommets[l_fin]


z = 0
k = 0
axis = list(d.keys())
Values = list(d.values())
arr = np.full((keys, keys), np.inf)
for i in sommets:
    for j in sommets:
        if (i, j) in axis:
            arr[sommets.index(i), sommets.index(j)] = Values[axis.index((i, j))]

item = 1
if len(sommets) != keys:
    print("Nombre des sommets données est different du nombre de nœuds du graphe ")
    exit(-1)

for item in d.values():
    if item < 0:
        print("Le graphe ne peut pas possede un circuit absorbant")
        exit(-1)

sommet_d1 = Initials[0]
sommet_d2 = Initials[1]

userChoice = 1

while userChoice == 1 or userChoice == 2:
    userChoice = int(input("Veuillez choisir l'algorithm 1 ou 2 ou les deux 3> "))
    if userChoice == 1 or userChoice==3:
        d1, pi1 = Dijkstra(arr, sommet_d1, sommets, 1)
        d2, pi2 = Dijkstra(arr, sommet_d2, sommets, 1)
        l_fin = compare(d1, d2, spot_rdv, sommets)
        print("Le sommet minimisant la somme des temps de parcours des deux amis: ", l_fin)
    if userChoice == 2 or userChoice==3:
        d1, pi1 = Dijkstra(arr, sommet_d1, sommets, 2)
        d2, pi2 = Dijkstra(arr, sommet_d2, sommets, 2)
        l_f = minimal_s(pi1, pi2, d1, d2, sommet_d1, sommet_d2, arr, sommets)
        print("Le sommet minimisant la somme du nombre de chemins/arcs parcourus par les deux amis: ", l_f)
