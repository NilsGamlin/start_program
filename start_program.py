#FONCTION QUI PERMET DE DETERMINER LES FICHIERS "exe"; D'UN DOSSIER, INCLUANT LES SOUS-DOSSIERS.
import os.path
import os

def list_exe_files(directory):
    path_list = [] #le nom doit être différent que "root",(risque de confusion sinon, à cause de la première boucle "for).
    exe_files_list = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            path_list.append(os.path.join(root, name))
            #root est une liste avec les racins de chaque fichier contenu dans le fichier du programme voulu
    for i in range(len(root)):
        if path_list[i].endswith(".exe"): #"endswith" d'identifiers quel est le type d'un fichier, donc de trier les fichiers "exe", des autres.
            
            exe_files_list += [path_list[i]]
    ##return root
    return exe_files_list

list_exe_files('C:\Program Files (x86)\Google')
