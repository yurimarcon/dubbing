import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from services.process_service import get_audio_done_service, create_process_service, split_audio_done_service, transcript_done_service, create_audio_done_service, unify_audio_done_service
from repository.database import create_table_process

relative_path = "/teste"

class TestSegmentRepository(unittest.TestCase):

    def test_create_databases_and_table(self):
        create_table_process()

    def test_start_process(self):
        user_id = 1
        process = create_process_service(user_id, relative_path)
        print(process)
        self.assertEqual(process.process_id, 1)

    def test_get_audio_process (self):
        get_audio_done_service(relative_path)

    def test_split_audio_done(self):
        split_audio_done_service(relative_path, 22, 11)
    
    def test_transcript_audio_done(self):
        transcript_done_service(relative_path)

    def test_create_audio_done(self):
        create_audio_done_service(relative_path)

    def test_unify_audio_done(self):
        unify_audio_done_service(relative_path)

if __name__ == '__main__':
    unittest.main()