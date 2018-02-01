import os.path #import veut donc dire qu'il faut avoir une connection internet, je vais donc devoir "installer" os.path non ?

folder_list = [d for d in os.listdir('C:\Program Files (x86)') if os.path.isdir(os.path.join('C:\Program Files (x86)', d))] # ca j'ai pompé d'internet en gros ca créer une liste avec le nom de tout les dossiers. 
#print(dirs)

user_input = input("Which program do you want to start ?")

for i in range(len(folder_list)):
    if user_input == str.lower(folder_list[i]):
        #print(directory[i])
        wanted_folder = "C:\Program Files (x86)\%s"%folder_list[i]
        print(wanted_folder)
        for file in os.listdir(wanted_folder):
            if file.endswith(".exe"):
                print(1)
