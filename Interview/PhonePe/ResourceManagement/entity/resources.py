from datetime import timedelta
from datetime import datetime
from entity.task import Task
from enums.resource_manager_enums import ResourceType


class Resources:

    def __init__(self,id,price,number_of_cpu,resource_type = ResourceType.SERVER_INSTANCE,config = None):
        self.id = id
        self.price = price
        self.number_of_cpu = number_of_cpu
        self.config = config # other config
        self.resource_type = resource_type
        self.is_allocated = False
        self.allocated_time = None
        self.task:Task = None

    def is_available(self):
        if self.is_allocated == False:
            return True
        if self.allocated_time + timedelta(seconds = self.task.task_time) <= datetime.now():
            self.is_allocated = False
            self.task.is_completed = True
            self.task.completed_at = self.allocated_time + timedelta(seconds = self.task.task_time)
            return True
        else:
            return False
    
    def allocate_task(self, task:Task):
        self.task = task
        self.task.is_completed = False
        self.is_allocated = True
        self.allocated_time = datetime.now()
        self.task.initiated_at = datetime.now()


    def show_stats(self):
        print(f"Resource id: {self.id} cpu cores: {self.number_of_cpu}")