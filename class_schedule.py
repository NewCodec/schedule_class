from openpyxl import workbook
from openpyxl import load_workbook

from students import Student
from config import Config
from courses import Courses
import info_options as inop

students=[]
courses = []

time_options=["上午早些","上午早些","上午早些","上午早些","晚上"]
time_index = []
num = ['1','2','3','4','5','6','7','8','9','10']


if __name__ == "__main__":
    xlsx,info,schedule,configuration = inop.excle_load()
    config = Config(configuration)
    inop.load_students(info,students,config)
    inop.init_courses(courses,config)
    inop.schedule_courses(students,courses,config)
    #print(courses)
    inop.show_courses_to_file(schedule,courses,config)
    xlsx.save("ls.xlsx")
    


