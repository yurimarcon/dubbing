import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from repository.transcript_repository import create_transcript, get_transcript, get_all_transcript, update_transcript
from repository.database import create_table_transcripts

class TestTranscriptRepository(unittest.TestCase):

    def test_create_databases_and_table(self):
        create_table_transcripts()

    def test_create_transcript (self):
        create_transcript(1, 1, 1)
        transcript = get_transcript(1)
        self.assertEqual(transcript.user_id, 1)

    def test_get_all_transcript(self):
        transcript = get_all_transcript()
        self.assertEqual(len(transcript), 1)

    def test_update_transcript(self):
        transcript = get_transcript(1)
        transcript_to_update = {
            "transcript_id" : 1,
            "user_id" : 2
        }
        update_transcript(transcript_to_update) 
        transcript_updated = get_transcript(1)
        self.assertEqual(transcript_updated.user_id, 2)

    def test_z_remove_database(self):
        os.remove("database.db")

if __name__ == '__main__':
    unittest.main()