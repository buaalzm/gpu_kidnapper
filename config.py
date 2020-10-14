import sys

class Config():
    cmd_list = []
    target_id_list = [2,3]
    sleep_time = 5
    script_path = '/workspace/pyroom/semantic_segmentation/experiment/deeplab_res18/' # train.py所在目录
    script_name = 'train.py' 

    def __init__(self):
        for device in self.target_id_list:
            self.cmd_list.append(self.make_task_cmd(device=device,script_name=self.script_name))
        self.print_info()
    
    def make_task_cmd(self,device,script_name):
        cmd_t = "CUDA_VISIBLE_DEVICES={device} python {script_name} --backbone resnet-18 \
            --lr 0.000080 --workers 4 --epochs 20000 --batch-size 64 --gpu-ids 0 --checkname deeplab-resnet \
            --eval-interval 1 --base-size 256 --crop-size 256 --dataset pascal".format(device=device,script_name=script_name)
        return cmd_t

    def print_info(self):
        print('target gpu id:',self.target_id_list)
        print('scripts',self.cmd_list)

cfg = Config()
