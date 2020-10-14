from config import cfg
from tasks import OccupyTask
from threading import Thread
from time import sleep


class WorkerManager():
    thread_list = [] # {'id':task_id,'task':task}
    def __init__(self,cfg=cfg):
        self.cfg = cfg

    def occupy_start(self):
        for task_id in self.cfg.target_id_list:
            task = OccupyTask(id=task_id)
            self.thread_list.append({'id':task_id,'task':task})
            t = Thread(target = task.run) 
            t.start() 

    def show_thread_list(self):
        print(self.thread_list)

    def kill_task(self,task_id):
        for task in self.thread_list:
            if task['id'] == task_id:
                task['task'].terminate()
                print(task,'has been killed')
                return

    def show_occupied(self):
        result = []
        for task in self.thread_list:
            result.append({'id':task['id'],'occupied':task['task'].is_occupied})
        print(result)



if __name__ == '__main__':
    w = WorkerManager()
    w.occupy_start()
    w.show_thread_list()
    sleep(10)
    w.kill_task(0)
    sleep(10)
    w.kill_task(1)