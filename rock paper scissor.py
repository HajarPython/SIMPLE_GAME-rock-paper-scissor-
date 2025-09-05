import random
import turtle

def jouer_turtle():
    screen = turtle.Screen()
    screen.title("Pierre-Papier-Ciseaux")
    screen.bgcolor("lightblue")
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(0, 100)
    pen.speed(0)
    turtle.tracer(1, 80)  # السرعة بلا تأخير


    choix_possibles = ["pierre", "papier", "ciseaux"]
    pen.write("Bienvenue au jeu Pierre-Papier-Ciseaux !\nClique sur la fenêtre pour commencer.",
              align="center", font=("Arial", 18, "bold"))

    screen.onclick(lambda x, y: None)

    while True:
        pen.clear()
        choix = "Choisissez: pierre, papier ou ciseaux (ou 'q' pour quitter)"
        joueur = screen.textinput("Votre choix", choix)

        if joueur is None or joueur.lower() == 'q':
            pen.clear()
            pen.write("Merci d'avoir joué ! À bientôt.", align="center", font=("Arial", 18, "normal"))
            break

        joueur = joueur.lower()
        if joueur not in choix_possibles:
            pen.clear()
            pen.write("Choix invalide, essayez encore.", align="center", font=("Arial", 18, "normal"))
            continue

        ordinateur = random.choice(choix_possibles)
        pen.clear()
        pen.goto(0, 100)
        pen.write(f"Vous avez choisi : {joueur}\nL'ordinateur a choisi : {ordinateur}",
                  align="center", font=("Arial", 18, "normal"))

        if joueur == ordinateur:
            resultat = "C'est une égalité !"
        elif (joueur == "pierre" and ordinateur == "ciseaux") or \
             (joueur == "papier" and ordinateur == "pierre") or \
             (joueur == "ciseaux" and ordinateur == "papier"):
            resultat = "Vous avez gagné ! 🎉"
        else:
            resultat = "Vous avez perdu... 😢"

        pen.goto(0, -20)
        pen.write(resultat, align="center", font=("Arial", 22, "bold"))
        pen.goto(0, -80)
        pen.write("Cliquez sur OK pour continuer ou 'q' pour quitter.",
                  align="center", font=("Arial", 14, "normal"))



    screen.mainloop()

jouer_turtle()
