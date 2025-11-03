import inspect

class Debug:
    
    def __init__(self):
        pass
    
    def DBG(self, message='This is a DBG message'):
        
        caller_frame = inspect.stack()[1]
        linenum = caller_frame.lineno
        
        print(f'[Line {linenum}][DBG message]: {message}')
        
    def INFO(self, message='This is a INFO message'):
        
        caller_frame = inspect.stack()[1]
        linenum = caller_frame.lineno
        
        print(f'[Line {linenum}][INFO message]: {message}')