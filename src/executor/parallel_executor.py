from concurrent.futures import ThreadPoolExecutor


class ParallelExecutor:

    def __init__(self, workers=4):
        self.workers = workers

    def execute(self, func, files):

        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            executor.map(func, files)