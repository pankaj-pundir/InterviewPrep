
from queue import Queue
import time
from typing import List
from entity.resources import Resources
from entity.data_center import data_center
from entity.data_center import DataCenter
from entity.task import Task
from enums.resource_manager_enums import AllocationStrategyType, ResourceType

class ResourceManager:
    def __init__(self):
        self.data_center:DataCenter = data_center
        self.fifo_queue:Queue = Queue()
        self.task_list: List[Task] = []
    
    def add_resource(self,resource_id,price,number_of_cpu):
        self.data_center.add_resource(Resources(resource_id,price,number_of_cpu))

    def is_resource_available(self):
        if len(self.data_center.get_resource_list()) == 0:
            raise RuntimeError("No resource added")
        
    def show_task_status(self,):
        print("#----- Task status -----")
        for _task in self.task_list:
            _task.show_status()
    
    def remove_resource(self,resource_id):
        self.data_center.remove_resource(resource_id)

    def show_resources(self,resource_type,number_of_cpu): # number of cpu resources greater
        for resource in self.data_center.get_resource_list():
            if resource.resource_type == resource_type and resource.number_of_cpu >= number_of_cpu and resource.is_allocated == False:
                resource.show_stats()
    
    def show_resources_source_type(self,resource_type): # number of cpu resources greater
        for resource in self.data_center.get_resource_list():
            if resource.resource_type == resource_type:
                resource.show_stats()
        
    def allocate_task(self,task:Task):
        self.fifo_queue.put(task)
        self.task_list.append(task)

    def allocation_engine(self,engine_type = AllocationStrategyType.LEAST_PRICE): # strategy pattern
        task = self.fifo_queue.get()
        if engine_type == AllocationStrategyType.LEAST_PRICE:
            self.least_price_allocation(task)
        elif engine_type == AllocationStrategyType.BEST_EXECUTION_TIME:
            self.best_execution_time(task)
        else:
            raise Exception("Unknown strategy")

    def least_price_allocation(self,task:Task):
        self.is_resource_available()
        li = []
        for resource in self.data_center.get_resource_list():
            if resource.number_of_cpu >= task.min_cpu_required:
                li.append((resource.price,resource))

        # checks
        if len(li) == 0:
            print("No resource available with the requested number of processors")
            return
        
        min_price_resource = sorted(li)[0][1]
        while min_price_resource.is_available() ==False:
            time.sleep(1) # sleep for 1 second and wait for resource to be free.

            
        if min_price_resource.is_available():
            min_price_resource.allocate_task(task)
        
        print(f"Task allocated successfully with task id {task.task_id} to resource {min_price_resource.id}")

    def best_execution_time(self,task:Task):
        self.is_resource_available()
        li = []
        for resource in self.data_center.get_resource_list():
            if resource.number_of_cpu >= task.min_cpu_required:
                li.append((resource.number_of_cpu,resource))

        # checks
        if len(li) == 0:
            print("No resource available with the requested number of processors")
            return
        best_exec = sorted(li)[::-1][0][1]
        while best_exec.is_available() ==False:
            time.sleep(1) # sleep for 1 second and wait for resource to be free.

            
        if best_exec.is_available():
            best_exec.allocate_task(task)
        
        print(f"Task allocated successfully with task id {task.task_id} to resource {best_exec.id}")


        
        
        


rm = ResourceManager()

#------------------------- P0 Task ---------------------------------------
# add resources
# Resource ->  resource id, price, nunmber of cpu
rm.add_resource("R123",10,4)
rm.add_resource("R124",4,10)
rm.add_resource("R125",15,80) # best execution time allocation

# remove resources
rm.remove_resource("R125")

# show resource
rm.show_resources(ResourceType.SERVER_INSTANCE,8) 

# show resource
rm.show_resources_source_type(ResourceType.SERVER_INSTANCE) 


# create and execute task

# TASK -> task id, task time, task min cpu code
rm.allocate_task(Task("T123",1,10)) # 2 cpu req, single resource default, add to queue
rm.allocation_engine()

rm.allocate_task(Task("T123",2,2)) # 2 cpu req, single resource default, add to queue
rm.allocation_engine()

rm.allocate_task(Task("T123",1,4)) # 2 cpu req, single resource default, add to queue
rm.allocation_engine(engine_type = AllocationStrategyType.BEST_EXECUTION_TIME)


rm.allocate_task(Task("T123",2,1)) # 2 cpu req, single resource default, add to queue
rm.allocation_engine()

# show task statistics
rm.show_task_status()

