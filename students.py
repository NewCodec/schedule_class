

class Student():
    def __init__(self):
        self.number = -1
        self.name = None 

        self.wish_time=[]
        self.wish_matched=[[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]]

        
        self.wish_courses_each_week = -1
        self.scheduled_courses=[]
        self.scheduled_course_count = 0

        self.done_times = 0 
        self.priority = 0
        self.conflict = 0

        self.arranged_course = 0
    
    def info_print(self):
        infoStr = "n="+str(self.number)+" name="+str(self.name)
        for i in range(7):
            infoStr = infoStr + " ["+str(i)+"]="+str(self.wish_time[i])
        infoStr = infoStr + " pri="+str(self.priority)
        print(infoStr)
