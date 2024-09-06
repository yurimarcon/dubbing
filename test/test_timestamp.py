import unittest
import json


with open(inputTranscriptText, 'r') as file:    
    result = json.load(file)

segments = result['segments']

class TestTimestemp(unittest.TestCase):
    
    def test_generate_segment(self):
        
        self.assertEqual(speed_factor, 0.9)


if __name__ == '__main__':
    unittest.main()