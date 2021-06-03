from Depend import *
from BackendFiles.AttendanceGraph import Attendance_Graph
from Commons import *

global attOBJ
attOBJ = Attendance_Graph()

class AttendanceApi(Resource):

    def __init__(self):
        self.AttendObj  = globals()['attOBJ']

    def post(self):
        data = json.loads(request.data.decode())
        institutelist = data["BranchList"]
        datefrom = data["datefrom"]
        dateto = data["dateto"]
        gradeList = data["GradesList"]
        if 'filtertype' in data:
            filtertype = data['filtertype']


        if data["flag"] == 1:    #{"BranchList":["Makhaza","Nyanga"],"GradesList":["G09"],"ColorsList":["Green", "Yellow"],"datefrom":"2017-07-24","dateto":"2017-09-29","flag":1, "filtertype":"Branch"}
            if data['filtertype'] == "Branch":
                institutelist = ConvertName(institutelist)
            return self.AttendObj.CreateBranchWiseData(institutelist,gradeList,data['filtertype'],datefrom,dateto)

        if data["flag"] == 4:    #{"BranchList":["Makhaza","Nyanga"],"GradesList":["G09"],"ColorsList":["Green", "Yellow"],"datefrom":"2017-07-24","dateto":"2017-09-29","flag":1, "filtertype":"Branch"}
            if data['filtertype'] == "Branch":
                institutelist = ConvertName(institutelist)
            return self.AttendObj.GetAllBranchData(gradeList,datefrom,dateto)

        elif data["flag"] == 2:  #{"BranchList":["Makhaza","Nyanga"],"GradesList":["G09"],"ColorsList":["Green", "Yellow"],"datefrom":"2017-07-24","dateto":"2017-09-29","flag":2, "filtertype":"Branch"}
            institutelist = ConvertName(institutelist)
            return self.AttendObj.CreateTrendOverTimeGraph_1(institutelist,gradeList,data["ColorsList"],datefrom,dateto)

        elif data["flag"] == 3: #{"BranchList":["Makhaza","Nyanga"],"GradesList":["G09"],"ColorsList":["Green", "Yellow"],"datefrom":"2017-07-24","dateto":"2017-09-29","flag":3, "filtertype":"Branch"}
            institutelist = ConvertName(institutelist)
            return self.AttendObj.CreateTrendOverTimeGraph_2(institutelist,gradeList,data["ColorsList"],datefrom,dateto)
        elif data['flag'] == 5:
            if filtertype is 'Branch':
                institutelist = ConvertName(institutelist)
            return self.AttendObj.GetLatestAvailableAttandanceDate(datefrom, dateto, institutelist, filtertype)


