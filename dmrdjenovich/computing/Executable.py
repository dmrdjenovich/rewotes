from abc import ABC, abstractmethod

class Executable(ABC):
    """
    Class representing a chunk of computational work.
    
    Has time and node / cpu requirements, specified
    by a Resources object.
    """
    
    @abstractmethod
    def get_resources():
        """
        Returns the required resources for this
        computational task.
        """
        pass
        
    @abstractmethod
    def exec(envr):
        """
        Given a Resource object representing the
        available computational resources, runs
        this computational task.
        """
        pass
