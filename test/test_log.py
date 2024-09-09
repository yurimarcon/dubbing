import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils_loger import log_info


class TestLog(unittest.TestCase):
    
    def test_write_log(self):
           
        log_info("quantity_sliced_audios")


        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()