# Менеджер который перенаправляет полученные данне в указанные менеджеры

import queue
import threading

class Router:
    def __init__(self, tasks_count, user_callback):
        self.queue = queue.Queue()
        self.tasks = [threading.Thread(target=self.handle) for i in range(0, tasks_count)]
        self.callback = user_callback
        self.run = True

        for task in self.tasks:
            task.start()
    
    def handle(self):
        while self.run:
            (photo, user_context) = self.queue.get()

            # обработали фотку .... и получили несколько продуктов

            self.callback(response, user_context)
    
    def scan_photo(self, photo, user_context):
        self.queue.put((photo, user_context))

    def end(self):
        self.run = False

        for task in self.tasks:
            task.join()