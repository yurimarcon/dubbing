
class Process:
    def __init__(self, process_id, user_id, start_time, end_time, quantity_split, silence_ranges, get_audio_done, split_audio_done, transcript_done, create_audio_done, unify_audio_done, last_update, relative_path, download_file_name, img, source_lang, target_lang, original_file_name):
        self.process_id = process_id
        self.user_id = user_id
        self.start_time = start_time
        self.end_time = end_time
        self.quantity_split = quantity_split
        self.silence_ranges = silence_ranges
        self.get_audio_done = get_audio_done
        self.split_audio_done = split_audio_done
        self.transcript_done = transcript_done
        self.create_audio_done = create_audio_done
        self.unify_audio_done = unify_audio_done
        self.last_update = last_update
        self.relative_path = relative_path
        self.download_file_name = download_file_name
        self.img = img
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.original_file_name = original_file_name

    def __repr__(self):
        return f"(process_id={self.process_id}, user_id={self.user_id}, start_time='{self.start_time}', end_time='{self.end_time}', quantity_split={self.quantity_split}, silence_ranges={self.silence_ranges}, get_audio_done='{self.get_audio_done}', split_audio_done={self.split_audio_done}, transcipt_done={self.transcript_done},  create_audio_done={self.create_audio_done},  unify_audio_done={self.unify_audio_done}, last_update={self.last_update}, relative_path={self.relative_path}, download_file_name={self.download_file_name}, img={self.img}, source_lang={self.source_lang}, target_lang={self.target_lang}, original_file_name={self.original_file_name})"
