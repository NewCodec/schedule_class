
weeks_name = ["星期一","星期二","星期三","星期四","星期五","星期六","星期天",]
choice_options=["None","上午早些","上午晚些","上午早些","上午早些","晚上"]
choice_num = ['1','2','3','4','5','6','7','8','9','10']

class Courses() :
    def __init__(self,week,number,config):
        self.week = week
        self.number = number
        self.is_full = False
        self.students = []
        self.students_count = 0
        self.config = config
    
    def add_student(self,student):
        if self.is_full == True:
            return False
        else:
            self.students.append(student)
            if len(self.students) == self.config.max_students_each_course:
                self.is_full = True
            return True
            
    def is_full(self):
        return self.is_full
    
    def info_print(self):
        print("week=%s,nu=%s,is_full=%s,count=%s" % (weeks[self.week],
        str(self.number),str(self.is_full),str(self.students_count)))
        stuStr = "students:"
        for stu in self.students :
            stuStr = stuStr+str(stu.name)
        print(stuStr)



        