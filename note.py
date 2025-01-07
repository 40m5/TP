Nombre = int(input("Combien d'étudiants souhaitez-vous saisir ?"))


etudiants = []
notes = []

for i in range (Nombre) :
    print("Nom de l'étudiant: "+str(i))
    nom = input("Entrez le nom de l'étudiant : ")
    etudiants.append(nom)
    notes.append(int(input("Note de l'étudiant" + etudiants[i] + " : ")))
    
def moyenne(n):
    somme = 0
    for i in n :
        somme = somme + i
    moyenne = somme / len(n)
    
    print(f"La moyenne de la classe est {moyenne:.2f}")
    
moyenne(notes) 
    
def repartition(noms, notes):
        reussite = []
        echec = []
        
        for i in range (len(notes)):
            if notes[i] >= 10:
         
                reussite.append(etudiants[i])
            else : 
                echec.append(etudiants[i])
        print("reussite", reussite)
        print("echec", echec)
        
repartition(etudiants,notes)

def meilleur_note(noms, notes):
    notemax = 0
    posmax=0
    for i in range (len(notes)):
        if notes[i] >= notemax:
            notemax= notes[i]
            posmax=i
    print(notemax, " appartient a ", noms[posmax])

meilleur_note(etudiants, notes)

    
    
    
    
    
    
    
    
    
    

