from tkinter import filedialog
def open_file_chooser():
    i=0
    global filename
    filename = filedialog.askdirectory()
    print("Vous avez selectionner le dossier : %s" % filename)
    import os

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(filename):
        for file in f:
            if '.json' in file:
                files.append(file)
        break

    print("liste des fichiers :")
    print(files)
    for f in files:
        #ttk.Treeview seems to split a given string by spaces to multiple
        #values.
        #If you don't like this behaviour you have to pass the value as
        #a tuple.
        tE.insert(parent='', index=0,values=(f,))

    ########################### REGLE 1 ###################################################
    files2 = []
    for f in files:
        regle1 = f.replace("[", "20220501_")
        # print(regle1)
        # os.rename(f,regle1)
        files2.append(regle1)

    ########################### REGLE 2 ###################################################
    files3 = []
    for f in files2:
        # TODO deonner le choix HASH ou CONF
        regle2 = f.replace("] ", "_HASH-")
        files3.append(regle2)
    print("regle 2 :")

    ########################### REGLE 3 ###################################################
    files4 = []
    for f in files3:
        regle3 = f.replace(" ", "")
        files4.append(regle3)
    print("regle 3 :")

    ########################### REGLE 4 ###################################################
    files5 = []
    for f in files4:
        # TODO HASH OU CONF (.csv
        regle4 = f.replace(".json", "")
        files5.append(regle4)

    print("regle 4 :")

    ########################### REGLE 5 ###################################################
    global files6
    files6 = []
    for f in files5:
        regle5 = f.split("-")
        files6.append(regle5)
    print("regle 5 :")
    for f in files6:
        date_cla_HASH = []
        date_cla_HASH.append(f[0])
        f.remove(f[0])

        id_liste = []
        id_liste.append(f[0])
        f.remove(f[0])
        id_liste.append(f[0])
        f.remove(f[0])
        id_liste.append(f[0])
        f.remove(f[0])

        id = '-'.join(id_liste)
        blabla = '-'.join(f)
        date_cla_HASH.append(blabla)
        date_cla_HASH.append(id)
        ok = '_'.join(date_cla_HASH)
        # TODO RECUPERER LE CHOIX HASH OU CONF
        ok2 = ok + ".json"

        f.clear()
        f.append(ok2)
        tS.insert(parent='', index=0, values=(f,))
    print(files6)


def renommer():
    import os
    i = 0
    # r=root, d=directories, f = files
    for r, d, f in os.walk(filename):
        for file in f:
            if '.json' in file:
                os.rename(file,''.join(files6[i]))
                i += 1
        break

    print("Tous les fichiers ont été renommés avec succés...")


def resource_path(relative_path):
    import sys
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
print("Renamer 2 est lancé")

from tkinter import *            # On importe tkinter : une librarie graphique
root = Tk()                      # On cree une fenetre appeler root
root.title("The Renamer2")       # On lui donne un titre
root.geometry("500x350")         # On lui donne une certaine dimension

import os
##icon = resource_path("icon.ico")
##root.iconbitmap(icon)



################################ Menue Bar ################################
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

menubar = Menu(root,
               background='white',
               foreground='black',
               activebackground='white',
               activeforeground='black')

file = Menu(menubar,
            tearoff=1,
            background='white',
            foreground='black')

file.add_command(label="Ouvrir", command=open_file_chooser)
#TODO donner la pocibilitée de sauvgarder
file.add_command(label="Enregistrer")
file.add_command(label="Enregistrer sous")
file.add_separator()
file.add_command(label="Quitter", command=root.quit)

menubar.add_cascade(label="Fichier",
                    menu=file)

#TODO mettre un menu "A propos" avec les crdits

################################ Tableau d'entrés ################################
from tkinter import ttk
#TODO sdroll bar
tE = ttk.Treeview(root,height=5, yscrollcommand = scrollbar.set)
tE['columns']=('Nom')
tE.column('#0', width=0, stretch=NO) # On cree la colone
tE.column('Nom', width=500)

tE.heading('#0', text='') # entete de la colone
tE.heading('Nom', text='Fichiers selectionnés', anchor=W)
tE.place(x=0, y=0)

################################ Tableau de sortie ################################
#TODO sdroll bar
tS = ttk.Treeview(root, height=5, yscrollcommand = scrollbar.set)
tS['columns']=('Nom')
tS.column('#0', width=0, stretch=NO) # On cree la colone
tS.column('Nom', width=500)

tS.heading('#0', text='') # entete de la colone
tS.heading('Nom', text='Fichiers Renommés',anchor=W)
tS.place(x=0, y=150)

################################ Bouton de renomage ################################
P = PhotoImage(file = resource_path("img/fichier.png"))
resized = P.subsample(10, 10)
label23 = Label(root,image=resized)
B= Button(root, text='Renommer', command=renommer,image=resized)
B.place(x= 215, y= 290)


#label23.place(x= 215, y= 290)


scrollbar.config( command = tE.yview and tS.yview() )


root.config(menu=menubar)
root.mainloop()