import shutil, tempfile
import os
import unittest
from change_prob_chars2 import change_prob_chars, create_new_filename

class TestChangeProbChars(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_whitespace_filename(self):
        # Create a file in the temp dir
        with open(os.path.join(self.test_dir, 'test file 1.txt'), 'w') as f:
            # Write something in it
            f.write('the owls are not what they seem')
            # close the file
            f.close()
            # run the change_prob_chars() function
            new_filename = change_prob_chars(os.path.basename(f.name))
            # check if the white space in the file name has been changed to
            # underscores
            self.assertEqual(new_filename, 'test_file_1.txt') 

    def test_whitespace_create_new_filename(self):
        # Create a file in the temp dir
        with open(os.path.join(self.test_dir, 'test file 1.txt'), 'w') as f:
            # Write something in it
            f.write('the owls are not what they seem')
            # close the file
            f.close()
            # run create_new_filename with the temp test dir
            create_new_filename(self.test_dir)
            # assert that the original filename 'test file 1.txt' no longer exists
            self.assertFalse(os.path.exists(os.path.join(self.test_dir,'test file 1.txt')))
            # assert that the new filename test_file_1.txt does exist
            self.assertTrue(os.path.exists(os.path.join(self.test_dir,'test_file_1.txt')))

if __name__ == '__main__':
    unittest.main
