from Depend import *
from BackendFiles.TutorGraph import TutorGraph
from Commons import *

global tutorObj
tutorObj = TutorGraph()

class TutorApi(Resource):
    def __init__(self):
        self.TutorObj  = globals()['tutorObj']

    def setOBJ(self, obj):
        self.obj = obj

    def post(self):

        data = json.loads(request.data.decode())
        institutelist = data["instituteList"]
        filtertype = data["filtertype"]
        datefrom = data["datefrom"]
        dateto = data["dateto"]
        weekDay = data['weekDay']
        if filtertype == 'Branch':
            institutelist = ConvertName(institutelist)

        if data["flag"] == 1:  #{"instituteList":["Makhaza","Nyanga"],"filtertype":"Branch", "flag":1,"datefrom":"2017-07-24","dateto": "2017-09-29"}
            return self.TutorObj.GetNumberOfPupilPerTutorByInstitute(institutelist,filtertype,datefrom,dateto, weekDay)

        elif data["flag"] == 2: #{"instituteList":["Makhaza","Nyanga"],"filtertype":"Branch", "flag":2,"datefrom":"2017-07-24","dateto": "2017-09-29"}
            return self.TutorObj.GetActiveTutorsByInstitute(institutelist,filtertype,datefrom,dateto, weekDay)

        elif data["flag"] == 3: #{"instituteList":["Makhaza","Nyanga"],"filtertype":"Branch", "flag":3,"datefrom":"2017-07-24","dateto": "2017-09-29"}
            return self.TutorObj.GenerateHighestToLowestPupilGraph(institutelist,filtertype,datefrom,dateto, weekDay)
        elif data['flag'] == 4:
            return self.TutorObj.GetLatestAvailableStdDate(datefrom, dateto, institutelist, filtertype)
        elif data['flag'] == 5:
            return self.TutorObj.GetLatestAvailableStaffDate(datefrom, dateto, institutelist, filtertype)

