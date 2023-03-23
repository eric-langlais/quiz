import json
import sys

# PROJET QUESTIONNAIRE V3 : POO
#
# - Pratiquer sur la POO
# - Travailler sur du code existant
# - Mener un raisonnement
#
# -> Définir les entitées (données, actions)

# quiz = {"categorie":"Animaux",
#         "titre":"Les chats",
#         "questions":
#           [{"titre":"question",
#             "choix": [["choix1", boolean],["choix2", boolean],["choix3", boolean]]}],
#         "difficulte":"debutant"}
#
# Question  (dictionnaire)
#    - titre       - str
#    - questions   - liste de dictionnaire
#           - titre     - str
#           - choix     - liste de liste
#                 - choix     - str
#                 - reponse   - bool
#
#    - difficulte  - str
#
# Questionnaire
#    - questions      - (Question)
#
#    - lancer()
#


class Question:
    def __init__(self, titre, choix, current_question, nb_total_questions):
        self.titre = titre
        self.choix = choix
        self.current_question = current_question
        self.nb_total_questions = nb_total_questions

    # def FromData(data):
    #     # ....
    #     q = Question(data[2], data[0], data[1])
    #     return q

    def poser(self):
        print("Question (" + str(self.current_question) + " de " + str(self.nb_total_questions) + ")")
        print(self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i][0])
        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int-1][1]:
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")

        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") : ")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)
    
class Questionnaire:
    # constructor
    def __init__(self, categorie, titre, questions, difficulte):
        self.categorie = categorie
        self.titre = titre
        self.questions = questions  # liste de dictionnaire
        self.difficulte = difficulte

    def lancer(self):
        score = 0
        current_q = 1
        total_q = len(self.questions)
        print()
        print("--------------------------------------------------------------------")
        print(" Categorie: " + self.categorie)
        print(" Sujet: " + self.titre)
        print(" Nombres de questions: " + str(len(self.questions)))
        print(" Niveau de difficulté: " + self.difficulte)
        print("--------------------------------------------------------------------")
        print()
        for i in range(0, len(self.questions)):
            t = self.questions[i]['titre']
            c = self.questions[i]['choix']
            if Question(t, c, current_q, total_q).poser():
                score += 1
            print("Votre Score: " + str(score) + " sur " + str(current_q))
            print()
            current_q += 1
        print("Score final :", score, "sur", len(self.questions))

        return score

# ouverture et lecture des donnees d'un fichier JSON

file_to_open = sys.argv

f = open(file_to_open[1])
quest = json.load(f)
f.close()

# decomposition du fichier JSON en differents elements

c = quest['categorie']
t = quest['titre']
q = quest['questions']
d = quest['difficulte']

# lancement du programme


Questionnaire(c, t, q, d).lancer()


