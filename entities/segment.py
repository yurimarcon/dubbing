
class Segment:
    def __init__(self, segment_id, transcript_id, process_id, user_id, text, start, end):
        self.segment_id = segment_id,
        self.transcript_id = transcript_id
        self.process_id = process_id
        self.user_id = user_id
        self.text = text,
        self.start = start,
        self.end = end
        
    def __repr__(self):
        return f"(segment_id={self.segment_id} transcript_id={self.transcript_id}, process_id={self.process_id}, user_id={self.user_id}, text={self.text}, start={self.start}, end={self.end})"
