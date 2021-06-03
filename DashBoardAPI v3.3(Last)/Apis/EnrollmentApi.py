from Depend import *
from BackendFiles.EnrollmentGraph import EnrollmentGraph
from Commons import *

global enrollOBJ
enrollOBJ = EnrollmentGraph()
class EnrollmentApi(Resource):

    def __init__(self):
        self.EnrollObj  = globals()['enrollOBJ']

    def post(self):
        data = json.loads(request.data.decode())
        institutelist = data["branches"]
        filtertype = data["filtertype"]
        datefrom = data["datefrom"]
        dateto = data["dateto"]
        gradeList = data["grades"]
        flag = data['flag']
        print(data)
        if 'Branch' in filtertype:
            institutelist = ConvertName(institutelist)

        #{"datefrom":"2017-07-24","dateto":"2017-09-29","branches":["Makhaza","Nyanga"],"grades":["G08","G09","G10","G11"],"filtertype":"Branch"}
        if flag == 1:
            return self.EnrollObj.GenerateEnrollmentGraph(datefrom,dateto,institutelist,gradeList,filtertype)
        elif flag == 2:
            return self.EnrollObj.GetLatestDatesBranchWise(datefrom, dateto, institutelist, filtertype)
        else:
            return self.EnrollObj.GenerateAllBranch(datefrom, dateto, gradeList)



