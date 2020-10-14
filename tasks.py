import time
import os
from config import cfg
from ipdb import set_trace


class OccupyTask(): 
    def __init__(self,id,cfg=cfg): 
        self._running = True
        self.id = id # gpu编号
        self.t = cfg.sleep_time # 运行时间间隔
        self.is_occupied = False
        self.oc_print = TriggerOnce(self.occuping_print)
        self.pd_print = TriggerOnce(self.pending_print)
      
    def terminate(self): 
        self._running = False
        
    def run(self): 
        while self._running: 
            try:
                os.chdir(cfg.script_path)
                os.system(cfg.cmd_list[self.id]) # do something cost gpu
                print('operating!!!!!:',cfg.cmd_list[self.id])
                self.oc_print()
                self.is_occupied = True
                self.pd_print.reset()
            except:
                self.is_occupied = False
                self.pd_print()
                self.oc_print.reset()
            time.sleep(self.t) 

    def occuping_print(self):
        print('occuping gpu {}'.format(self.id))

    def pending_print(self):
        print('trying to occuping gpu {}'.format(self.id))

class TriggerOnce():
    available = True

    def __init__(self, func):
        """
        trigger function once
        """
        self.func = func

    def reset(self):
        """
        function can be trigger again
        """
        self.available = True
    
    def __call__(self):
        if self.available==True:
            self.func()
            self.available=False