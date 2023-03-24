import os.path
import unittest
from unittest.mock import patch
import questionnaire
import os
import questionnaire_import
import json
#
# def additionner(a, b):
#     return a + b
#
#
# class TestUnitaireDemo(unittest.TestCase):
#     def test_additionner(self):
#         self.assertEqual(additionner(5, 10), 15)
#
# class TestsQuestion(unittest.TestCase):
#     def test_question_bonne_mauvaise_reponse(self):
#         choix = ("choix1", "choix2", "choix3")
#         q = questionnaire.Question("titre_question", choix, 1, 10)
#         with patch("builtins.input", return_value="1"):
#             self.assertTrue(q.poser())

# class TestsQuestionnaire(unittest.TestCase):
#     def test_questionnaire_lancer_leschats_confirme(self):
#         filename = os.path.join("test_data", "animaux_leschats_confirme.json")
#         questionnaire.Questionnaire

class TestsImportQuestionnaire(unittest.TestCase):
    def test_import_format_json(self):
        questionnaire_import.generate_json_file("Animaux", "Les chats", "https://www.codeavecjonathan.com/res/mission/openquizzdb_50.json")

        filenames = ("animaux_leschats_confirme.json", "animaux_leschats_debutant.json", "animaux_leschats_expert.json")

        for f in filenames:
            self.assertTrue(os.path.isfile(f))
            file = open(f, 'r')
            json_data = file.read()
            file.close()
            try:
                data = json.loads(json_data)
            except:
                self.fail("Probleme de deserialisation pour le fichier: " + f)

            self.assertIsNotNone(data.get("titre"))
            self.assertIsNotNone(data.get("questions"))
            self.assertIsNotNone(data.get("categorie"))
            self.assertIsNotNone(data.get("difficulte"))

            for q in data.get("questions"):
                self.assertIsNotNone(q.get("titre"))
                self.assertIsNotNone(q.get("choix"))
                for c in q.get("choix"):
                    self.assertGreater(len(c[0]), 0)
                    self.assertTrue(isinstance(c[1], bool))
                bonne_reponse = [i[0] for i in q.get("choix") if i[1]]
                self.assertEqual(len(bonne_reponse), 1)



if __name__ == '__main__':
    unittest.main()
