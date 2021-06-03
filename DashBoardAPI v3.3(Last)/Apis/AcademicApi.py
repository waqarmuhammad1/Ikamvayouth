from Depend import *
from BackendFiles.AcademicGraph import AcademicGraph
from Commons import *

class AcademicApi(Resource):

    def __init__(self):
        self.AcadObj  = AcademicGraph()

    def post(self):
        data = json.loads(request.data.decode())
        self.comparison = []
        subjectlist = data["subjectList"]
        institutelist = data["instituteList"]
        gradelist = data["gradeList"]
        dateFrom = data["DateFrom"]
        dateTo = data["DateTo"]
        if 'filtertype' in data:
            filterType = data['filtertype']

            if filterType == 'Branch':
                institutelist = ConvertName(institutelist)

        if "comparisonList" in data:
            self.comparison = data["comparisonList"]


        if data["flag"] == 1:   # {"subjectList":["Geography", "Visual Arts", "Economics", "English"],"instituteList":["Makhaza","Nyanga"],"gradeList":["G11","G10", "G09"],"DateFrom":"2016-07-24","DateTo":"2017-09-29","flag":1}
            return self.AcadObj.GetAvgAllMarks(subjectList=subjectlist,instituteList=institutelist,gradeList=gradelist,dateFrom=dateFrom,dateTo=dateTo,comparisonList=self.comparison, filterType=filterType)

        elif data["flag"] == 2:
            return self.AcadObj.GetPercentOfStudentsPass(subjectList=subjectlist,instituteList=institutelist,gradeList=gradelist,dateFrom=dateFrom,dateTo=dateTo,comparisonList=self.comparison, filterType=filterType)

        elif data["flag"] == 3:
            return self.AcadObj.GetNumberOfDistinctions(subjectList=subjectlist,instituteList=institutelist,gradeList=gradelist,dateFrom=dateFrom,dateTo=dateTo,comparisonList=self.comparison, filterType=filterType)

        elif data["flag"] == 4:
            return self.AcadObj.GetNumberTakingSubjects(subjectList=subjectlist,instituteList=institutelist,gradeList=gradelist,dateFrom=dateFrom,dateTo=dateTo,comparisonList=self.comparison, filterType=filterType)

        elif data["flag"] == 5: # {"subjectList":["Geography", "Visual Arts", "Economics", "English"],"instituteList":["Makhaza","Nyanga"],"gradeList":["G11","G10", "G09"],"DateFrom":"2016-07-24","DateTo":"2017-09-29","flag":5}
            return self.AcadObj.GetTrendGraph(gradeList=gradelist, instituteList=institutelist,
                                              subjectList=subjectlist, dateFrom=dateFrom, dateTo=dateTo)

        elif data["flag"] == 6: # {"subjectList":["Geography", "Visual Arts", "Economics", "English"],"instituteList":["Makhaza","Nyanga"],"gradeList":["G11","G10", "G09"],"DateFrom":"2016-07-24","DateTo":"2017-09-29","flag":5}
            return self.AcadObj.GetSubjectsByBranchGrade(gradeList=gradelist, instituteList=institutelist,filterType=filterType, dateFrom=dateFrom, dateTo=dateTo)






