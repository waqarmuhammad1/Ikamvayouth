# -*- coding: utf-8 -*-
from Apis.TrackingApi import TrackingApi
from Apis.AttendanceApi import AttendanceApi
from Apis.AcademicApi import AcademicApi
from Apis.KickoutApi import KickoutApi
from BackendFiles.TutorGraph import TutorGraph
from Commons import *
from Apis.TutorApi import TutorApi
from Apis.EnrollmentApi import EnrollmentApi
from Depend import *
import os

app = Flask(__name__)
CORS(app)
api = Api(app)


class Branch(Resource):

    def post(self):
        list = ["Makhaza","Nyanga","Masiphumelele",
                "Chesterville","Umlazi","Ebony Park","Ivory Park",
                "Mamelodi","Ikageng","Joza","Mahikeng","Gugs Comp & Yebo", "Kuyasa","Atlantis","ID Mkize","Leiden","Diepsloot"]
        list.sort()
        return list

class School(Resource):

    def post(self):
        stdSchoolData = pd.read_csv(filePath + 'StudCustField.csv', header=0)
        stdSchoolData = stdSchoolData[['StudentID', 'T12', 'T13']]
        stdSchoolData['School'] = pd.concat([stdSchoolData['T12'].dropna(), stdSchoolData['T13'].dropna()]).reindex_like(stdSchoolData)
        stdSchoolData = stdSchoolData[['StudentID', 'School']].dropna()
        stdSchoolData = stdSchoolData.drop_duplicates()
        stdSchoolData['School'] = [x.capitalize() for x in list(stdSchoolData['School'])]
        school_list = list(stdSchoolData['School'].unique())
        school_list.sort()
        # data = pd.read_csv(filePath+ 'StudCustField.csv')
        # data = (data[['T21']]).dropna()
        # data = (data[['T21']]).drop_duplicates()
        # school_list = list(data['T21'])
        # school_list.sort()
        return school_list


class Subject(Resource):

    def post(self):
        data = pd.read_csv(filePath+ 'vSubjects.csv')
        data = (data[['Subject']]).drop_duplicates()
        subject_list = list(data['Subject'])
        subject_list.sort()
        return subject_list

class GetYears(Resource):

    def post(self):
        lis = []
        for file in os.listdir(filePath):
            if file.endswith(".xlsx"):
                lis.append(file.replace('.xlsx', ''))
        return lis

class GetTimeYears(Resource):

    def post(self):
        data = pd.read_csv(filePath + 'TermDates.csv')
        data = list(data['TermYear'].unique())
        data = [str(x) for x in data]
        data.sort()
        return data

api.add_resource(TrackingApi, '/TrackingGraph')
api.add_resource(AttendanceApi, '/AttendanceGraph')
api.add_resource(AcademicApi, '/AcademicGraph')
api.add_resource(KickoutApi, '/KickoutGraph')
api.add_resource(TutorApi, '/TutorGraph')
api.add_resource(EnrollmentApi,'/EnrollmentGraph')
api.add_resource(Branch,'/Branches')
api.add_resource(School,'/GetSchools')
api.add_resource(Subject,'/GetSubjects')
api.add_resource(GetYears,'/GetYears')
api.add_resource(GetTimeYears,'/GetTimeYears')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000,threaded = True)
