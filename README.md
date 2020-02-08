# Dijsktra_RoyWarshall
Dijkstra and Roy Warshall's algorithms application in Python

— Le premier algorithme déterminera le sommet minimisant la somme des temps de parcours des deux
amis. Dans l’exemple ci-dessus, le lieu de rendez-vous optimal pour ce critère est le point b, car la première
personne peut l’atteindre par le chemin e→a→b, et la seconde par le chemin d→c→b. Le temps total est
de 4.
— Le second algorithme calculera le sommet minimisant la somme du nombre de chemins/arcs parcourus
par les deux amis. S’il existe plusieurs sommets satisfaisant ce critère, il en choisira un qui minimise la
somme des temps de parcours. Dans l’exemple ci-dessus, le point de rendez-vous minimisant le nombre de
routes parcourues est d (e→f→c→d et d) avec 3 routes parcourues et un temps total de 9. On peut
remarquer que le nœud g offre également un nombre de routes égal à 3 mais le temps total est de
18(e→f→g et d→g). La première solution sera donc choisie.
