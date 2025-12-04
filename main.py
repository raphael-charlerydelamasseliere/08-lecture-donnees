#### Imports et définition des variables globales
"""
    Lecture de listes d'entiers depuis un fichier CSV
"""
import csv
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode='r',encoding='utf8') as f:
        r = csv.reader(f, delimiter=';')
        lstring = list(r)
        l = []
        for i in lstring:
            lint = [int(x) for x in i]
            l.append(lint)
    return l

def get_list_k(data, k):
    """
    retourne la liste d'index k dans data
    """
    l = data[k]
    return l

def get_first(l):
    """
    retourne le premier élément de la liste l
    """
    return l[0]

def get_last(l):
    """
    retourne le dernier élément de la liste l
    """
    return l[-1]

def get_max(l):
    """
    retourne le maximum des éléments de la liste l
    """
    lmax1 = max(l)
    return lmax1

def get_min(l):
    """
    retourne le minimum des éléments de la liste l
    """
    lmin1 = min(l)
    return lmin1

def get_sum(l):
    """
    retourne la somme des éléments de la liste l
    """
    suml = 0
    for elt in l:
        suml = suml + elt
    return suml

def main():
    """
    fonction principale effectuant des appels aux fonctions secondaires
    """
    data = read_data(FILENAME)
    print(data)
    print("Liste de 3 : " , get_list_k(data,2))
    print("Premier : " , get_first(data))
    print("Dernier  : " , get_last(data))
    print("Maximum : ", get_max(data))
    print("Minimum : ",get_min(data))
    print("Somme : ", get_sum(get_list_k(data,0)))
    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))

if __name__ == "__main__":
    main()
