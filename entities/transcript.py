
class Transcript:
    def __init__(self, transcript_id, process_id, user_id):
        self.transcipt_id = transcript_id
        self.process_id = process_id
        self.user_id = user_id
        
    def __repr__(self):
        return f"(transcript_id={self.transcipt_id}, process_id={self.process_id}, user_id={self.user_id})"
