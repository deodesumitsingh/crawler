import unittest
import sys
sys.path.append('../..')

from utils import validators

VALID_URL = 'https://github.com'
INVALID_URL = 'xyz.com'

VALID_DEPTH = 1
INVALID_DEPTH = 0


class TestValidators(unittest.TestCase):

    def test_validate_cmd_args_with_invalid_url_exit(self):
        """Test if we have given invalid URL in arguments"""
        with self.assertRaises(SystemExit):
            validators.validate_cmd_args(INVALID_URL, VALID_DEPTH)

    def test_validate_cmd_args_with_invalid_depth_exit(self):
        """Test if we have given invalid Depth in arguments"""
        with self.assertRaises(SystemExit):
            validators.validate_cmd_args(VALID_URL, INVALID_DEPTH)

    def test_validate_cmd_args_without_exit(self):
        """Test if not arguments are invalid"""
        try:
            validators.validate_cmd_args(VALID_URL, VALID_DEPTH)
        except Exception as e:
            fail_msg = ("test_validate_cmd_args_without_exit() raise"
                        "unexpected expception. Error {}")
            self.fail(fail_msg.format(str(e)))

    def test_validate_cmd_args_with_type_error(self):
        """Test for arguments if any one missing"""
        with self.assertRaises(TypeError):
            validators.validate_cmd_args()
        with self.assertRaises(TypeError):
            validators.validate_cmd_args(INVALID_DEPTH)
        with self.assertRaises(TypeError):
            validators.validate_cmd_args(INVALID_URL)
        with self.assertRaises(TypeError):
            validators.validate_cmd_args(VALID_DEPTH, VALID_URL)

if __name__ == '__main__':
    unittest.main()