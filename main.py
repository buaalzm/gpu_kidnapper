import fire
from config import cfg
from tasks import *
from worker_manager import WorkerManager
import time


wm = WorkerManager()

def print_task():
    '''
    暂时没啥用，留了接口
    '''
    wm.show_occupied()

def start():
    wm.occupy_start()

if __name__ == '__main__':
    fire.Fire()
    