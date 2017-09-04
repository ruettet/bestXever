import unittest
from rules import BestClassEver


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.bce = BestClassEver()

    def test_prune_left_context(self):
        self.assertEqual(self.bce._prune_left_context("dit is een van"), "dit is")

    def test_rule_1_1(self):
        data = {
            "targetconstructie": "beste ajax ooit",
            "left_context": "@brouwertje ben het nu aan het terugkijken.",
            "right_context": ", genieten. gaan we niet meer zien, zo’n team of dit voetbal in nederland.."
        }
        self.assertTrue(self.bce.rule_1_1(data))

    def test_rule_1_2(self):
        data = {
            "targetconstructie": "fast as ever",
            "left_context": "o wat een pech, het sint kado is nog onderweg #royalmail trustworthy and",
            "right_context": "."
        }
        self.assertTrue(self.bce.rule_1_2(data))

    def test_rule_1_3(self):
        data = {
            "targetconstructie": "beste voetballers ooit",
            "left_context": "",
            "right_context": ": johan cruijff#rtl7"
        }
        self.assertTrue(self.bce.rule_1_3(data))
        data = {
            "targetconstructie": "slechtste map ooit",
            "left_context": "",
            "right_context": ""
        }
        self.assertTrue(self.bce.rule_1_3(data))

    def test_rule_1_4(self):
        data = {
            "targetconstructie": "stomste pleio &#39;feature&#39; ooit",
            "left_context": "@nellyspanjer zal je wat vertellen (",
            "right_context": ") als je wel ingelogd bent, maar geen lid van groep mag je openbare..."
        }
        self.assertTrue(self.bce.rule_1_4(data))

    def test_rule_2_1(self):
        data = {
            "targetconstructie": "de beste fiets ooit kopen",
            "left_context": "nu nog meer belgen die",
            "right_context": "! “@tulpfietsen: tulpfietsen doet mee aan de orangebikedays in belgië: http://t.co/fj7rm82”"
        }
        self.assertTrue(self.bce.rule_2_1(data))

    def test_rule_2_2(self):
        data = {
            "targetconstructie": "de beste stunt ooit",
            "left_context": "rt @wouter_gk: dit wordt",
            "right_context": ". #rutte komt in #sotsji uit de kast. alle zure reacties zijn voorbarig. trots op zo&#39;n dappere …"
        }
        self.assertTrue(self.bce.rule_2_2(data))

    def test_rule_2_3(self):
        data = {
            "targetconstructie": "de beste sex ooit",
            "left_context": "sinds ik bij sexplanner.be ben ingeschreven heb ik",
            "right_context": ". schrijf jij je ook in? esmee van sexplanner.be"
        }
        self.assertTrue(self.bce.rule_2_3(data))

    def test_rule_2_4(self):
        data = {
            "targetconstructie": "het beste jaar ooit",
            "left_context": "2012 is begonnen mensen. veel geluk, liefde en inspiratie voor het komende jaar! maak er",
            "right_context": "van!"
        }
        self.assertTrue(self.bce.rule_2_4(data))

    def test_rule_2_5(self):
        data = {
            "targetconstructie": "mijn (hopelijk) laatste tentamen ever",
            "left_context": "oké ik mag nog een half uurtje leuke dingen doen en dan echt leren, want maandag",
            "right_context": "!"
        }
        self.assertTrue(self.bce.rule_2_5(data))

    def test_rule_2_6(self):
        data = {
            "targetconstructie": "de meest kalme invasie ooit kunnen worden. zonder ook maar één kogel. we gaan het zien.",
            "left_context": "rt @obk: dit zou trouwens nog wel eens",
            "right_context": "kunnen worden. zonder ook maar één kogel. we gaan het zien."
        }
        self.assertTrue(self.bce.rule_2_6(data))

if __name__ == '__main__':
    unittest.main()