import shutil, tempfile
import os
import unittest
from change_prob_chars import change_prob_chars
import mock

class TestChangeProbChars(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    @mock.patch('change_prob_chars.os')
    def test_white_space(self, mock_os):
        # Create a file in the temp dir
        f = open(os.path.join(self.test_dir, 'test file 1.txt'), 'w')
        # Write something in it
        f.write('the owls are not what they seem')
        # close the file
        f.close()
        # run the change_prob_chars() function 
        change_prob_chars(self.test_dir)
        # check if the white space in the file name has been changed to
        # underscores
        self.assertEqual(os.path.basename(f.name), 'test_file_1.txt') 

if __name__ == '__main__':
    unittest.main
