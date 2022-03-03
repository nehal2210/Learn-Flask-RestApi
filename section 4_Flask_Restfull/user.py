class User:
    def __init__(self, _id: int, username: str, password: str) -> None:
        '''Initialize the object setting arguments into properties'''
        
        self.id: int = _id
        self.username: str = username
        self.password: str = password
