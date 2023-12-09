import enum

class ResourceType(str, enum.Enum):
    SERVER_INSTANCE = "SERVER_INSTANCE"  
    

class AllocationStrategyType(str, enum.Enum):
    LEAST_PRICE = "LEAST_PRICE"  
    BEST_EXECUTION_TIME = "BEST_EXECUTION_TIME"  
    
    