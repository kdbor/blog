
from datetime import datetime

# Create your tests here.
class Data:
    def __init__(self,xcors,ycors,created = None):
        self.xcors = xcors
        self.ycors = ycors
        self.created = created or datetime.now()
      
        