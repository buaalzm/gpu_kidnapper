import sys

class Config():
    cmd_list = []
    target_id_list = [0,1] # 要抢的显卡的id
    sleep_time = 5 # 每次尝试的时间间隔
    script_name = 'train.py' 
    script_workspace_path = '/workspace/pyroom/semantic_segmentation' # 瞎训练的工作目录

    def __init__(self):
        sys.path.append(self.script_workspace_path)
        for device in self.target_id_list:
            self.cmd_list.append(self.make_task_cmd(device=device,script_name=self.script_name))
        self.print_info()
    
    def make_task_cmd(self,device,script_name):
        cmd_t = "CUDA_VISIBLE_DEVICES={device} python {script_name} --backbone resnet-18 \
            --lr 0.000080 --workers 4 --epochs 200 --batch-size 64 --gpu-ids 0 --checkname deeplab-resnet \
            --eval-interval 1 --base-size 256 --crop-size 256 --dataset pascal".format(device=device,script_name=script_name)
        return cmd_t

    def print_info(self):
        print('target gpu id:',self.target_id_list)
        print('scripts',self.cmd_list)

cfg = Config()
