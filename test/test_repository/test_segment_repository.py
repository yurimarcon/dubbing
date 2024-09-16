import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from repository.segment_repository import create_segment, get_segment, get_all_segments, update_segment
from repository.database import create_table_segments

class TestSegmentRepository(unittest.TestCase):

    def test_create_databases_and_table(self):
        create_table_segments()

    def test_create_segment (self):
        create_segment(1, 1, 1, 1, "The test description segment", 10.0, 15.0)
        segment = get_segment(1)
        self.assertEqual(segment.user_id, 1)

    def test_get_all_segment(self):
        segment = get_all_segments()
        self.assertEqual(len(segment), 1)

    def test_update_segment(self):
        segment = get_segment(1)
        segment_to_update = {
            "segment_id" : 1,
            "user_id" : 2
        }
        update_segment(segment_to_update) 
        segment_updated = get_segment(1)
        self.assertEqual(segment_updated.user_id, 2)

    def test_z_remove_database(self):
        os.remove("database.db")

if __name__ == '__main__':
    unittest.main()