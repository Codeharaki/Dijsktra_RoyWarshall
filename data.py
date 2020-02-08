from collections import defaultdict
d = defaultdict(dict)
d = dict(d)

#nombre de nœuds du graphe
keys = 7
#nom de chaque sommet
sommets = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#nombre de lieux de rendez-vous
rdv = 3
#nom de chaque sommet étant un lieu de rendez-vous
spot_rdv = ['b', 'g', 'd']
#deux noms des sommets initiaux
Initials=['e','d']
#liste de triplets (SommetInitial, SommetTerminal, Durée), rep
d[('e', 'a')] = 1
d[('a', 'e')] = 1
d[('a', 'b')] = 1
d[('b', 'a')] = 1
d[('b', 'c')] = 1

d[('c', 'b')] = 1
d[('c', 'd')] = 1
d[('d', 'c')] = 1
d[('d', 'g')] = 10
d[('g', 'd')] = 5
d[('g', 'f')] = 5

d[('f', 'g')] = 3
d[('f', 'c')] = 3
d[('c', 'f')] = 10
d[('f', 'e')] = 10
d[('e', 'f')] = 5
