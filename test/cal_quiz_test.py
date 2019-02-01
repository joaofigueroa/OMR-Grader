import grader as g
import json
import os
import unittest

class CalQuizTest(unittest.TestCase):

    def test_quiz_01(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_01.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['D', 'B', '', '', '', ''])
        self.assertEqual(data['studentId'], '015596200')

    def test_quiz_02(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_02.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['A', 'C', '', '', '', ''])
        self.assertEqual(data['studentId'], '016281261')

    def test_quiz_03(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_03.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['studentId'], '016005570')

    def test_quiz_04(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_04.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['studentId'], '015618079')

    def test_quiz_05(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_05.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['studentId'], '015917963') 

    def test_quiz_06(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_06.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['studentId'], '015852729')

    def test_quiz_07(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_07.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['studentId'], '016117773')

    def test_quiz_08(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_08.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['studentId'], '015951334')

    def test_quiz_09(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_09.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['studentId'], '015949787')

    def test_quiz_10(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_10.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['studentId'], '015764615')

    def test_quiz_11(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_11.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['A', 'A', '', '', '', ''])
        self.assertEqual(data['studentId'], '015685055')

    def test_quiz_12(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_12.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['', '', '', '', '', ''])
        self.assertEqual(data['studentId'], '016382687')

    def test_quiz_13(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_13.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['studentId'], '013776785')

    def test_quiz_14(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_14.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['A', 'B', '', '', '', ''])
        self.assertEqual(data['studentId'], '015374303')

    def test_quiz_15(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_15.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['studentId'], '014125861')

    def test_quiz_16(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_16.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['A', 'B', '', '', '', ''])
        self.assertEqual(data['studentId'], '015149936')

    def test_quiz_17(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_17.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', 'C', 'B', 'B', 'B', 'B'])
        self.assertEqual(data['studentId'], '010911247')

    def test_quiz_18(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_18.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['studentId'], '015584149')

    def test_quiz_19(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_19.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['A', 'B', '', '', '', ''])
        self.assertEqual(data['studentId'], '016187141')

    def test_quiz_20(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_20.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['studentId'], '015664424')

    def test_quiz_2_01(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_01.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'C', 'B', '', '', ''])
        self.assertEqual(data['studentId'], '016042035')

    def test_quiz_2_02(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_02.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', '', 'B', '', '', ''])
        self.assertEqual(data['studentId'], '014528133')

    def test_quiz_2_03(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_03.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['A', 'A', 'B', '', '', ''])
        self.assertEqual(data['studentId'], '015360224')

    def test_quiz_2_04(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_04.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['', '', '', '', '', ''])
        self.assertEqual(data['studentId'], '016315334')

    def test_quiz_2_05(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_05.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', 'A', '', '', '', ''])
        self.assertEqual(data['studentId'], '016040293')

    def test_quiz_2_06(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_06.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', 'A', 'B', '', '', ''])
        self.assertEqual(data['studentId'], '015599372')

    def test_quiz_2_07(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_07.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', 'A', 'C', '', '', ''])
        self.assertEqual(data['studentId'], '015384404')

    def test_quiz_2_08(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_08.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'C', 'B', '', '', ''])
        self.assertEqual(data['studentId'], '015785428')

    def test_quiz_2_09(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_09.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['E', 'E', 'B', '', '', ''])
        self.assertEqual(data['studentId'], '016211087')

    def test_quiz_2_10(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_10.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', 'E', 'B', '', '', ''])
        self.assertEqual(data['studentId'], '012533959')

    def test_quiz_2_11(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_11.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', 'A', 'B', '', '', ''])
        self.assertEqual(data['studentId'], '015988553')

    def test_quiz_2_12(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_12.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['A', '', 'A', '', '', ''])
        self.assertEqual(data['studentId'], '016055815')

    def test_quiz_2_13(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_13.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', 'A', 'B', '', '', ''])
        self.assertEqual(data['studentId'], '015738940')

    def test_quiz_2_14(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_14.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['', '', '', '', '', ''])
        self.assertEqual(data['studentId'], '015964243')

    def test_quiz_2_15(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_15.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', 'C', 'C', '', '', ''])
        self.assertEqual(data['studentId'], '016146750')

    def test_quiz_2_16(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_16.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', 'A', 'B', '', '', ''])
        self.assertEqual(data['studentId'], '105809868')

    def test_quiz_2_17(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_17.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['', '', '', '', '', ''])
        self.assertEqual(data['studentId'], '015359977')

    def test_quiz_2_18(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_18.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', 'E', 'B', '', '', ''])
        self.assertEqual(data['studentId'], '016302347')

    def test_quiz_2_19(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_19.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', 'A', 'B', '', '', ''])
        self.assertEqual(data['studentId'], '015736431')

    def test_quiz_2_20(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_20.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', 'C', 'B', '', '', ''])
        self.assertEqual(data['studentId'], '015294327')

    def test_quiz_2_21(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_21.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', 'A', 'B', '', '', ''])
        self.assertEqual(data['studentId'], '015915714')

    def test_quiz_2_22(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_22.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['A', 'A', 'B', '', '', ''])
        self.assertEqual(data['studentId'], '016162545')

    def test_quiz_2_23(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_23.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', 'A', 'C', '', '', ''])
        self.assertEqual(data['studentId'], '016073196')

    def test_quiz_2_24(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_24.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', 'A', 'B', '', '', ''])
        self.assertEqual(data['studentId'], '015151691')

    def test_quiz_2_25(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_25.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', 'A', 'C', '', '', ''])
        self.assertEqual(data['studentId'], '016172867')

    def test_quiz_2_26(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_26.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', 'A', 'B', '', '', ''])
        self.assertEqual(data['studentId'], '015223802')

    def test_quiz_2_27(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_27.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', 'A', 'B', '', '', ''])
        self.assertEqual(data['studentId'], '015304272')

    def test_quiz_2_28(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_28.png")
        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', 'A', 'B', '', '', ''])
        self.assertEqual(data['studentId'], '016336524')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CalQuizTest)
    unittest.TextTestRunner(verbosity=2).run(suite)