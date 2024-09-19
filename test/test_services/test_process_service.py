import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from services.process_service import get_audio_done_service, create_process_service, split_audio_done_service, transcript_done_service, create_audio_done_service, unify_audio_done_service, get_process_by_user_id_service
from repository.database import create_table_process

relative_path = "/teste"

class TestSegmentRepository(unittest.TestCase):

    def test_create_databases_and_table(self):
        create_table_process()

    def test_start_process(self):
        user_id = 1
        process = create_process_service(user_id, relative_path, "en", "pt")
        all_process = get_process_by_user_id_service(1)
        self.assertGreaterEqual(len(all_process), 1)

    def test_get_audio_process (self):
        get_audio_done_service(relative_path)

    def test_split_audio_done(self):
        split_audio_done_service(relative_path, 22, 11)
    
    def test_transcript_audio_done(self):
        transcript_done_service(relative_path, 22, 11)

    def test_create_audio_done(self):
        create_audio_done_service(relative_path, 22, 11)

    def test_unify_audio_done(self):
        unify_audio_done_service(relative_path)

    def test_get_process_by_user(self):
        get_process_by_user_id_service(1)

if __name__ == '__main__':
    unittest.main()