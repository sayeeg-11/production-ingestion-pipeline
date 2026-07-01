from dataclasses import dataclass
from threading import Lock


@dataclass
class PipelineStats:

    files_processed: int = 0
    files_skipped: int = 0
    chunks_created: int = 0
    chunks_filtered: int = 0
    failures: int = 0

    def __post_init__(self):
        self.lock = Lock()

    def reset(self):
        with self.lock:
            self.files_processed = 0
            self.files_skipped = 0
            self.chunks_created = 0
            self.chunks_filtered = 0
            self.failures = 0
            
    def increment_processed(self):
        with self.lock:
            self.files_processed += 1


    def increment_skipped(self):
        with self.lock:
            self.files_skipped += 1


    def increment_failures(self):
        with self.lock:
            self.failures += 1


    def add_created_chunks(self, count):
        with self.lock:
            self.chunks_created += count


    def add_filtered_chunks(self, count):
        with self.lock:
            self.chunks_filtered += count