#FONCTION QUI PERMET DE DETERMINER LES FICHIERS "exe"; D'UN DOSSIER, INCLUANT LES SOUS-DOSSIERS.
import os

def list_exe_files(directory):
    path_list = [] #le nom doit être différent que "root",(risque de confusion sinon, à cause de la première boucle "for).
    exe_files_list = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            path_list.append(os.path.join(root, name))
            #root est une liste avec les racines de chaque fichier contenu dans le dossier du programme voulu
    for i in range(len(root)):
        if path_list[i].endswith(".exe"): #"endswith" permet d'identifier quel est le type d'un fichier, donc de trier les fichiers "exe", des autres.
            
            exe_files_list += [path_list[i]]
    ##return root
    return exe_files_list

list_exe_files('C:\Program Files (x86)\Google')

#-------------------------------------------------------------------------------------------------------------------------------------------

#FONCTION QUI DOIT PERMETTRE DE CHOISIR LE FICHIER "exe", D'UNE LISTE, POUR ÉXÉCUTER LE PROGRAMME VOULU.

import os

def find_correct_exe_file(list_of_all_exe_files, application_name):
    for i in range(len(list_of_all_exe_files)):
        if list_of_all_exe_files[i][- (len(application_name) + 4):] == "%s.exe" %application_name: # le "+ 4" est pour ajouter le nombre de caractères dans ".exe", car len(".exe") = 4.
            return os.startfile(list_of_all_exe_files[i])
        
        
#------------------------------------------------Prototype 1--------------------------------------------------------------------------------
import os.path
import os

def list_exe_files(directory):
    path_list = [] #le nom doit être différent que "root",(risque de confusion sinon, à cause de la première boucle "for).
    exe_files_list = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            path_list.append(os.path.join(root, name))
            #root est une liste avec les racines de chaque fichier contenu dans le dossier du programme voulu
    for i in range(len(root)):
        if path_list[i].endswith(".exe"): #"endswith" permet d'identifier quel est le type d'un fichier, donc de trier les fichiers "exe", des autres.
            
            exe_files_list += [path_list[i]]
    ##return root
    return exe_files_list

def find_correct_exe_file(list_exe_files, application_name):
    for i in range(len(list_exe_files)):
        if list_exe_files[i][- (len(application_name) + 4):] == "%s.exe" %application_name: # le "+ 4" est pour ajouter le nombre de caractères dans ".exe", car len(".exe") = 4.
            return os.startfile(list_exe_files[i])

while True:        
    wanted_directory = input("Which directory ?")
    wanted_program = input("Which program do you want to start ?")
    directory = "C:\Program Files (x86)\%s\%s" %(wanted_directory, wanted_program)
    exe_files = list_exe_files(directory)
    find_correct_exe_file(exe_files, wanted_program)
    
    #works only with Google chrome at the moment
