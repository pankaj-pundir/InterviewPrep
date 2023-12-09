class Task:
    def __init__(self,task_id,task_time = 10,min_cpu_required = 1) -> None:
        self.task_id = task_id
        self.task_time = task_time
        self.number_of_resource_required = 1
        self.is_completed = False
        self.min_cpu_required = min_cpu_required
        self.initiated_at = None
        self.completed_at = None
    
    def show_status(self):
        print(f"{self.task_id}: COMPLETED {self.is_completed}, STARTED AT {self.initiated_at}, COMPLETED AT {self.completed_at}  ")