# -*- coding: utf-8 -*-
from diff import get_input_files
import unittest
import diff


class DiffTest(unittest.TestCase):

    # テストクラスが初期化される際に一度だけ呼ばれる (python2.7以上)
    @classmethod
    def setUpClass(cls):
        pass

    # テストクラスが解放される際に一度だけ呼ばれる (python2.7以上)
    @classmethod
    def tearDownClass(cls):
        pass

    # テストメソッドを実行するたびに呼ばれる
    def setUp(self):
        pass

    # テストメソッドの実行が終わるたびに呼ばれる
    def tearDown(self):
        pass

    # get_input_fiules seijoukei
    def test_get_input_files_success(self):
        expected1 = "hoge.txt"
        expected2 = "foo.txt"

        actual1, actual2 = get_input_files(["diff.py", "hoge.txt", "foo.txt"])
        self.assertEqual(expected1,actual1)
        self.assertEqual(expected2,actual2)

    # get_input_files error case
    def test_get_input_files_errorCase1(self):
        self.assertRaises(diff.ArgumentsErrors, get_input_files, ["diff.py", "hoge.txt"])
        
    def test_read_file_success(self):
        expected = "file contents\n"
        actual = diff.read_file("hoge.txt")
        self.assertEqual(expected, actual)
        
        expected = "file contents another\n"
        actual = diff.read_file("foo.txt")
        self.assertEqual(expected, actual)

    def test_read_file_error(self):
        self.assertRaises(FileNotFoundError, diff.read_file, "invalid_file.txt")

    def test_parse_text_success(self):
        expected = ["aaaabcd", "taiwannihon", "tonkotsu"]
        actual = diff.parse_text("aaaabcd taiwannihon tonkotsu.\n")
        self.assertEqual(expected, actual)
        expected = ["I'm", "batman", "www!"]
        actual = diff.parse_text("I'm batman www!")
        self.assertEqual(expected, actual)

    def test_diff_case_equal(self):
        expected = "I'm batman www!"
        actual1, actual2 = diff.diff(["I'm", "batman", "www!"],["I'm", "batman", "www!"])
        self.assertEqual(expected, actual1)
        self.assertEqual(expected, actual2)







if __name__ == '__main__':
    # unittestを実行
    unittest.main()