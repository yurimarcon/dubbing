
class Process:
    def __init__(self, process_id, user_id, start_time, end_time, get_audio_done, split_audio_done, transcript_done, create_audio_done, unify_audio_done):
        self.process_id = process_id
        self.user_id = user_id
        self.start_time = start_time
        self.end_time = end_time
        self.get_audito_done = get_audio_done
        self.split_audio_done = split_audio_done
        self.transcript_done = transcript_done
        self.create_audio_done = create_audio_done
        self.unify_audio_done = unify_audio_done

    def __repr__(self):
        return f"(process_id={self.process_id}, user_id={self.user_id}, start_time='{self.start_time}', end_time='{self.end_time}', get_audio_done='{self.get_audito_done}', split_audio_done={self.split_audio_done}, transcipt_done={self.transcript_done},  create_audio_done={self.create_audio_done},  unify_audio_done={self.unify_audio_done})"
