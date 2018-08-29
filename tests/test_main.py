
import sys
import unittest

#def assert_test(platform_type, platform):
#    assert platform_type == platform


class test_main(unittest.TestCase):
    """ """

    def test_correct_platform(self):
        """ """

        platform_type = sys.platform

        #assert_test(platform)


if __name__ == '__main__':
    unittest.main()
