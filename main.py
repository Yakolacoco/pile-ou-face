import random

def PileouFace():
    while True: 
        choix_joueur = input("Choisissez 'Pile' ou 'Face' : ").strip().lower()
        
        if choix_joueur not in ["pile", "face"]:
            print("Veuillez choisir 'Pile' ou 'Face'.")
            continue  
        
        r = random.randint(0, 1)
        resultat = "pile" if r == 1 else "face"

        print(f"Le résultat est : {resultat.capitalize()} !")

        if choix_joueur == resultat:
            print("Bravo, tu as gagné ! 🎉")
        else:
            print("Dommage, tu as perdu. 😢")

        user_input = input("Voulez-vous rejouer ? Tapez 'yes' pour continuer ou 'no' pour quitter : ").strip().lower()

        if user_input == "no":
            print("Merci d'avoir joué. À bientôt !")
            break

PileouFace()
