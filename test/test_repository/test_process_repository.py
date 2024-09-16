import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from repository.process_repository import create_process, get_process, get_all_process, update_process
from repository.database import create_table_process

class TestProcessRepository(unittest.TestCase):

    def test_create_databases_and_table(self):
        create_table_process()

    def test_create_process (self):
        create_process(1, "", "", 0, 0, 0, 0, 0)
        process = get_process(1)
        self.assertEqual(process.user_id, 1)

    def test_get_all_process(self):
        process = get_all_process()
        self.assertEqual(len(process), 1)

    def test_update_process(self):
        process = get_process(1)
        process_to_update = {
            "process_id" : 1,
            "get_audio_done" : 1
        }
        update_process(process_to_update) 
        process_updated = get_process(1)
        self.assertEqual(process_updated.get_audito_done, 1)

    def test_z_remove_database(self):
        os.remove("database.db")

if __name__ == '__main__':
    unittest.main()