from entity.resources import Resources
from pydantic.typing import List

class DataCenter:
    def __init__(self,location):
        self.location = location
        self.__resource_list :List[Resources] = []

    def get_resource_list(self):
        return self.__resource_list
    
    def add_resource(self,new_resource):
        for resource in self.__resource_list:
            if resource.id == new_resource.id:
                print("Resource already exists ")
                return
        self.__resource_list.append(new_resource)
        print(f"resource {new_resource.id} successfully added")

    def remove_resource(self,resource_id):
        for resource in self.__resource_list:
            if resource.id == resource_id:
                del resource
                print(f"resource {resource_id} successfully removed")
                return
        print("Resource not found")

data_center = DataCenter("mumbai") # following singlton design pattern to fix concurrency