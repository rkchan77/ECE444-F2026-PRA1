import typing

class utils: 
    def __init__(self):
        pass

    def reversed(num: int):
        num_str = str(num)
        num_str = num_str[::-1]
        
        return int(num_str)
    
    def formatter(num: int):
        return bin(num), oct(num)
        