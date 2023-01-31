print("Renamer 2")

import os

path = os.getcwd()
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.json' in file:
            files.append(file)

print("liste des fichiers :")
for f in files:
    print(f)


########################### REGLE 1 ###################################################
files2 = []
for f in files:
    regle1 = f.replace("[","20220501_")
    #print(regle1)
    #os.rename(f,regle1)
    files2.append(regle1)
print("regle 1 :")
for f in files2:
    print(f)

########################### REGLE 2 ###################################################
files3 = []
#TODO deonner le choix HASH ou CONF
for f in files2:
    regle2 = f.replace("] ","_HASH-")

    #print(regle1)
    #os.rename(f,regle1)
    files3.append(regle2)
print("regle 2 :")
for f in files3:
    print(f)

########################### REGLE 3 ###################################################
files4 = []
for f in files3:
    regle3 = f.replace(" ","")
    #print(regle1)
    #os.rename(f,regle1)
    files4.append(regle3)

print("regle 3 :")
for f in files4:
    print(f)

########################### REGLE 3.2 ###################################################
files32 = []
for f in files4:
    #TODO HASH OU CONF (.csv
    regle32 = f.replace(".json","")
    #print(regle1)
    #os.rename(f,regle1)
    files32.append(regle32)

print("regle 3.2 :")
for f in files32:
    print(f)

########################### REGLE 4 ###################################################
files5 = []
for f in files32:
    regle4 = f.split("-")
    #print(regle1)
    #os.rename(f,regle1)
    files5.append(regle4)
print("regle 4 :")
for f in files5:
    #l = len(f)
    print(f)

    date_cla_HASH = []
    date_cla_HASH.append(f[0])
    print(date_cla_HASH)
    f.remove(f[0])

    id_liste = []
    id_liste.append(f[0])
    f.remove(f[0])
    id_liste.append(f[0])
    f.remove(f[0])
    id_liste.append(f[0])
    f.remove(f[0])

    id = '-'.join(id_liste)
    print(id)
    blabla = '-'.join(f)
    print(blabla)
    date_cla_HASH.append(blabla)
    date_cla_HASH.append(id)
    ok = '_'.join(date_cla_HASH)
    print(ok)
    #TODO RECUPERER LE CHOIX HASH OU CONF
    ok2 = ok + ".json"
    print(ok2)
    f.clear()
    f.append(ok2)
    print(" ")

print(" rename :")
for f in files5:
    f2 = ''.join(f)
    print(f2)


print(files5)
print(files)
########################### REGLE 5 ###################################################


i=0
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.json' in file:
            os.rename(file,''.join(files5[i]))
            i += 1

print("Tous les fichiers ont été renommés avec succés...")