
# Менеджер который перенаправляет полученные данне в указанные менеджеры
import threading
from core.parser.wb_parse import wb_parse
from core.ai.image_processing import analyze_photo

class TasksPool:
    def __init__(self, size):
        self.semaphores = [threading.Semaphore(1) for _ in range(size)]
        self.lock = threading.Lock()

    def acquire(self):
        with self.lock:
            print("Locked self")
            for i, semaphore in enumerate(self.semaphores):
                if semaphore.acquire(blocking=False):
                    return semaphore
        return None
    
    def handle(self, path):
        semaphore = self.acquire()
        if semaphore == None:
            return None

       
        result = wb_parse(analyze_photo(path))

        semaphore.release()
        
        return result

pool = TasksPool(10)
