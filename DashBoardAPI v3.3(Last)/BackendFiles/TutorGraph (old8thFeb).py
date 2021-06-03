from Commons import *
import math

class TutorGraph():

    def __init__(self):

        self.stdAttandanceFileName = filePath + 'ATDStudAttend.csv'
        self.stdDataFileName = filePath + 'vStudents.csv'


        self.staffDataFileName = filePath + 'StaffCampus.csv'
        self.staffAttandanceFileName = filePath + 'vExt_StaffAttendance.csv'
        # self.staffWorkGroupFileName = filePath + 'vRPWQueryStaff.csv'
        self.staffWorkGroupFileName = filePath + 'vExt_Staff.csv'
        self.stdSchoolDataFileName = filePath + 'StudCustField.csv'

        self.stdDateAttandance = pd.read_csv(self.stdAttandanceFileName, header=0, sep=',')

        self.stdAttData = pd.read_csv(filePath + 'vATDStudAttTerm.csv')
        self.stdData = pd.read_csv(filePath + 'vStudents.csv')
        self.stdReg = pd.read_csv(filePath + 'Registration.csv')

        self.staffData = pd.read_csv(self.staffDataFileName, header=0, sep=',')
        self.staffAttandance = pd.read_csv(self.staffAttandanceFileName, header=0, sep=',')
        self.staffWorkGroup = pd.read_csv(self.staffWorkGroupFileName, header=0, sep=',')
        self.stdSchoolData = pd.read_csv(self.stdSchoolDataFileName, header=0, sep=',')

        self.stdAttandance, self.staffAttandance = self.PreprocessData(self.stdAttData,
                                                                       self.stdReg,
                                                                       self.stdData,
                                                                       self.staffData,
                                                                       self.staffAttandance,
                                                                       self.staffWorkGroup,
                                                                       self.stdSchoolData)

        self.stdDateAttandance = self.PreprocessData2(self.stdDateAttandance, self.stdData, self.staffData,
                                                                       self.staffAttandance, self.staffWorkGroup,
                                                                       self.stdSchoolData)

    def PreprocessData(self, stdAttandance, stdReg, stdData, staffData, staffAttandance, staffWorkGroup, stdSchoolData):

        stdReg = stdReg[['StudentID', 'LeftDate']]
        stdAttandance = stdAttandance[['StudentID', 'Present', 'Term', 'TermYear']]
        stdData = stdData[['StudentID', 'Term', 'TermYear', 'StudYear']]

        stdData = stdData.merge(stdAttandance, on=['StudentID', 'Term', 'TermYear'])
        stdData = stdData.merge(stdReg, on='StudentID', how='left')
        stdData = stdData.replace(np.NaN, 'Missing')

        staffData = staffData.replace(np.NaN, 'Missing')

        staffAttandance = staffAttandance.replace(np.NaN, 'Missing')
        staffWorkGroup = staffWorkGroup.replace(np.NaN, 'Missing')
        #stdSchoolData = stdSchoolData.replace(np.NaN, 'Missing')


        stdSchoolData = stdSchoolData[['StudentID', 'T12', 'T13']]
        stdSchoolData['School'] = pd.concat([stdSchoolData['T12'].dropna(), stdSchoolData['T13'].dropna()]).reindex_like(stdSchoolData)
        stdSchoolData = stdSchoolData[['StudentID', 'School']].dropna()
        stdSchoolData['School'] = [x.capitalize() for x in list(stdSchoolData['School'])]
        # stdSchoolData = stdSchoolData[['StudentID', 'T21']]
        # stdSchoolData = stdSchoolData.rename(columns={'T21': 'School'})

        staffData = staffData.rename(columns={'CampusID': 'Branch'})
        staffData = staffData[['StaffID', 'Branch']]
        staffAttandance = staffAttandance[['StaffID', 'AbsentDate', 'CodeType']]
        staffWorkGroup = staffWorkGroup[['ID', 'WorkGroup', 'StatusName']]
        staffWorkGroup = staffWorkGroup.rename(columns={'WorkGroup':'Position'})
        staffWorkGroup = staffWorkGroup.rename(columns={'ID': 'StaffID'})

        stdData = stdData.merge(stdSchoolData, on='StudentID')
        stdData = stdData.rename(columns={'StudYear':'Branch'})

        staffAttandance = staffAttandance.drop_duplicates()
        staffAttandance['AbsentDate'] = pd.Series([dt.strptime(str(x).split('T')[0], "%Y-%m-%d").date()
                                             for x in list(staffAttandance['AbsentDate'])], index=staffAttandance.index)
        # staffAttandance.AbsentDate = staffAttandance.AbsentDate.dt.date
        staffAttandance = staffAttandance.merge(staffData, on='StaffID', how='left')
        staffAttandance = staffAttandance.merge(staffWorkGroup, on='StaffID', how='left')
        staffAttandance = staffAttandance[staffAttandance['Position'] == 'Tutor']
        staffAttandance = staffAttandance[staffAttandance['StatusName'] == 'Current']

        stdData = stdData.drop_duplicates()
        staffAttandance = staffAttandance.drop_duplicates()
        staffAttandance['day_of_week'] = pd.to_datetime(staffAttandance.AbsentDate).dt.weekday_name


        stdData = stdData.replace('GUGYB', 'GUG')
        staffAttandance = staffAttandance.replace('GUGYB', 'GUG')

        return stdData, staffAttandance

    def PreprocessData2(self, stdAttandance, stdData, staffData, staffAttandance, staffWorkGroup, stdSchoolData):
        stdAttandance = stdAttandance.replace(np.NaN, 'Missing')
        stdData = stdData.replace(np.NaN, 'Missing')


        stdAttandance = stdAttandance[['StudentID', 'AttDate', 'AttCode']]
        stdData = stdData[['StudentID', 'CampusID']]
        stdData = stdData.rename(columns={'CampusID': 'Branch'})

        stdSchoolData = stdSchoolData[['StudentID', 'T12', 'T13']]
        stdSchoolData['School'] = pd.concat(
            [stdSchoolData['T12'].dropna(), stdSchoolData['T13'].dropna()]).reindex_like(stdSchoolData)
        stdSchoolData = stdSchoolData[['StudentID', 'School']].dropna()
        stdSchoolData['School'] = [x.capitalize() for x in list(stdSchoolData['School'])]
        # stdSchoolData = stdSchoolData[['StudentID', 'T21']]
        # stdSchoolData = stdSchoolData.rename(columns={'T21': 'School'})

        try:
            stdAttandance = stdAttandance[stdAttandance['AttCode'] != 'Missing']
        except:
            pass

        stdAttandance = stdAttandance.query('(AttCode != 4) and (AttCode != 10)')
        stdAttandance['AttDate'] = pd.to_datetime(stdAttandance['AttDate'])
        stdAttandance.AttDate = stdAttandance.AttDate.dt.date
        stdAttandance = stdAttandance.drop_duplicates()
        stdAttandance = stdAttandance.merge(stdData, on='StudentID')
        stdAttandance = stdAttandance.merge(stdSchoolData, on='StudentID')

        stdAttandance = stdAttandance.drop_duplicates()
        return stdAttandance

    def GetTotalStudentByInstitute(self, stdAttandance, instituteList, filterType, dateFrom, dateTo):

        # totalDF = mergedDF[(mergedDF.StudYear.str.contains('LEI')) & (mergedDF.Term == 3) & (mergedDF.TermYear == 2017)]
        # withDateDF = totalDF[totalDF.LeftDate != 'Missing']
        # finalDF = totalDF[(totalDF.LeftDate == 'Missing')]
        # withDateDF.LeftDate = pd.Series([dt.strptime(str(x).split('T')[0], "%Y-%m-%d").date()
        #                                  for x in list(withDateDF['LeftDate'])], index=withDateDF.index)
        # count = finalDF.Present.sum()
        # count += withDateDF[((withDateDF.LeftDate == 'Missing') |
        #                      (withDateDF.LeftDate > np.datetime64('2017-09-30')))].drop_duplicates().Present.sum()


        filteredDF = FilterDF(dateFrom, dateTo, stdAttandance)
        instituteFilteredDF = {x: filteredDF[filteredDF[filterType].str.contains(x)] for x in instituteList}
        lowerDate = GetDateFrom(dateFrom)#np.datetime64(dateFrom)
        upperDate = GetDateTo(dateTo)#np.datetime64(dateTo)
        totalStudentsByInstitute = {}
        for institute, df in instituteFilteredDF.items():
            withDateDF = df[df.LeftDate != 'Missing']
            finalDF = df[(df.LeftDate == 'Missing')]
            withDateDF.LeftDate = pd.Series([dt.strptime(str(x).split('T')[0], "%Y-%m-%d").date()
                                                                              for x in list(withDateDF['LeftDate'])], index=withDateDF.index)
            count = finalDF.Present.sum()
            if math.isnan(count):
                count = 0
            if len(withDateDF) > 0:
                tempCount =withDateDF[((withDateDF.LeftDate == 'Missing') |
                                 (withDateDF.LeftDate > upperDate))].drop_duplicates().Present.sum()
                if math.isnan(tempCount) == False:
                    count += tempCount


            # totalStudentsByInstitute[institute] = len(df[(df['AttDate'] >= lowerDate) &
            #                                              (df['AttDate'] <= upperDate)])
            totalStudentsByInstitute[institute] = count

        return totalStudentsByInstitute

    def GetTotalTutorsByInstitute(self, staffAttandance, instituteList, filterType, dateFrom, dateTo, weekDay='False'):

        if weekDay == 'False':
            tempstaffAttandance = staffAttandance[(staffAttandance.day_of_week == 'Saturday') | (staffAttandance.day_of_week == 'Sunday')]
        elif weekDay == 'True':
            tempstaffAttandance = staffAttandance[(staffAttandance.day_of_week != 'Saturday') & (staffAttandance.day_of_week != 'Sunday')]
        else:
            tempstaffAttandance = staffAttandance


        instituteFilteredDF = {x: tempstaffAttandance[tempstaffAttandance[filterType] == x] for x in instituteList}



        lowerDate = GetDateFrom(dateFrom)#np.datetime64(dateFrom)
        upperDate = GetDateTo(dateTo)#np.datetime64(dateTo)

        totalTutorsByInstitute = {}
        for institute, df in instituteFilteredDF.items():
            tempDF = df[(df['AbsentDate'] >= lowerDate) &
                        (df['AbsentDate'] <= upperDate) &
                        ((df['CodeType'] == 'P') | (df['CodeType'] == 'LE') | (df['CodeType'] == 'LN') |(df['CodeType'] == 'LR')| (df['CodeType'] == 'PH')  )]

            tempDF2 = len(df[df[filterType] == institute]['StaffID'].unique())
            totalTutorsByInstitute[institute] = [len(tempDF), len(tempDF['StaffID'].unique()), tempDF2]
        return totalTutorsByInstitute

    def GetNumberOfPupilPerTutorByInstitute(self, instituteList, filterType, dateFrom, dateTo, weekDay='False'):

        tutorsByInstitute = self.GetTotalTutorsByInstitute(self.staffAttandance, instituteList, filterType, dateFrom, dateTo, weekDay)
        studentsByInstitute = self.GetTotalStudentByInstitute(self.stdAttandance, instituteList, filterType, dateFrom, dateTo)
        print(tutorsByInstitute)
        print(studentsByInstitute)
        pupilPerTutorByInstitute = {}
        for key in studentsByInstitute.keys():
            stdNum = float(studentsByInstitute[key])
            totalNum = float(tutorsByInstitute[key][0])
            if totalNum > 0:
                val = stdNum / totalNum
                if math.isnan(val):
                    pupilPerTutorByInstitute[key] = 0
                else:
                    pupilPerTutorByInstitute[key] = math.floor(val)
            else:
                pupilPerTutorByInstitute[key] = 0

        return pupilPerTutorByInstitute

    def GetNumberOfPupilPerTutorAllBranch(self, instituteList, filterType, dateFrom, dateTo, weekDay='False'):

        tutorsByInstitute = self.GetTotalTutorsByInstitute(self.staffAttandance, instituteList, filterType, dateFrom, dateTo, weekDay)
        studentsByInstitute = self.GetTotalStudentByInstitute(self.stdAttandance, instituteList, filterType, dateFrom, dateTo)

        pupilPerTutorByInstitute = {}
        for key in studentsByInstitute.keys():
            stdNum = float(studentsByInstitute[key])
            totalNum = float(tutorsByInstitute[key][0])
            if totalNum > 0:
                val = stdNum / totalNum
                if math.isnan(val):
                    pupilPerTutorByInstitute[key] = 0
                else:
                    pupilPerTutorByInstitute[key] = math.floor(val)
            else:
                pupilPerTutorByInstitute[key] = 0

        return pupilPerTutorByInstitute

    def GetActiveTutorsByInstitute(self, instituteList, filterType, dateFrom, dateTo, weekDay='False'):
        tutorsByInstitute = self.GetTotalTutorsByInstitute(self.staffAttandance, instituteList, filterType, dateFrom, dateTo, weekDay)

        activeTutorsByInstitute = {}
        for key in tutorsByInstitute.keys():
            if tutorsByInstitute[key][2] > 0:
                tem = (float(tutorsByInstitute[key][1]) / float(tutorsByInstitute[key][2])) * 100
                activeTutorsByInstitute[key] = round(tem, 0)
            else:
                activeTutorsByInstitute[key] = 0
        return activeTutorsByInstitute

    def GenerateHighestToLowestPupilGraph(self, instituteList, filterType, dateFrom, dateTo, weekDay='False'):

        lowerDate = GetDateFrom(dateFrom)#np.datetime64(dateFrom)
        upperDate = GetDateTo(dateTo)#np.datetime64(dateTo)

        instituteFilteredStaffDF = {x: self.staffAttandance[self.staffAttandance[filterType] == x]
                                    for x in instituteList}
        instituteFilteredStaffDF = {k: v[(v.AbsentDate >= lowerDate) & (v.AbsentDate <= upperDate)]
                                    for k, v in instituteFilteredStaffDF.items()}
        if weekDay == 'False':

            instituteFilteredStaffDF = {k: v[(v.day_of_week == 'Saturday') | (v.day_of_week == 'Sunday')]
                                        for k, v in instituteFilteredStaffDF.items()}
        elif weekDay == 'True':
            instituteFilteredStaffDF = {k: v[(v.day_of_week != 'Saturday') & (v.day_of_week != 'Sunday')]
                                        for k, v in instituteFilteredStaffDF.items()}
        filterType2 = filterType

        filteredDF = self.stdDateAttandance[self.stdDateAttandance.AttDate >= lowerDate]
        filteredDF = filteredDF[filteredDF.AttDate <= upperDate]

        #instituteFilteredStdDF = {x:self.stdDateAttandance[self.stdDateAttandance[filterType2] == x] for x in instituteList}
        instituteFilteredStdDF = {x: filteredDF[filteredDF[filterType2] == x] for x in
                                  instituteList}
        #instituteFilteredStdDF = {k: v[(v.AttDate >= lowerDate) & (v.AttDate <= upperDate)] for k, v in instituteFilteredStdDF.items()}

        dateValues = self.staffAttandance[(self.staffAttandance.AbsentDate >= lowerDate) &
                                     (self.staffAttandance.AbsentDate <= upperDate)].AbsentDate.unique()

        totalTutorByInstitute = {}
        for institute, df in instituteFilteredStaffDF.items():
            totalTutorByDate = {}
            for value in dateValues:
                totalTutorByDate[value] = len(df[df.AbsentDate == value])
            totalTutorByInstitute[institute] = totalTutorByDate

        totalStdByInstitute = {}
        for institute, df in instituteFilteredStdDF.items():
            totalStdByDate = {}
            for value in dateValues:
                totalStdByDate[value] = len(df[df.AttDate == value])
            totalStdByInstitute[institute] = totalStdByDate

        stdTutorRatioByInstitute = {}
        for institute in totalTutorByInstitute.keys():
            stdTutorRatioByDate = {}
            for date in totalTutorByInstitute[institute].keys():
                tutorPresent = totalTutorByInstitute[institute][date]
                stdPresent = totalStdByInstitute[institute][date]
                try:
                    stdTutorRatioByDate[date] = stdPresent / tutorPresent

                except:
                    pass
            if len(stdTutorRatioByDate.values()) > 0:
                minimum = round(min(stdTutorRatioByDate.values()), 0)
                maximum = round(max(stdTutorRatioByDate.values()), 0)
            else:
                minimum = 0
                maximum = 0
            stdTutorRatioByInstitute[institute] = [minimum, maximum]


        return stdTutorRatioByInstitute


    def GetLatestAvailableStdDate(self, dateFrom, dateTo, instituteList, filterType):

        lowerDate = GetDateFrom(dateFrom)#np.datetime64(dateFrom)
        upperDate = GetDateTo(dateTo)#np.datetime64(dateTo)

        filteredDF = self.stdDateAttandance[self.stdDateAttandance.AttDate >= lowerDate]
        filteredDF = filteredDF[filteredDF.AttDate <= upperDate]

        # instituteFilteredStdDF = {x: self.stdDateAttandance[self.stdDateAttandance[filterType] == x] for x in instituteList}

        instituteFilteredStdDF = {x: filteredDF[filteredDF[filterType] == x] for x in
                                  instituteList}

        # instituteFilteredStdDF = {k: v[(v.AttDate >= lowerDate) & (v.AttDate <= upperDate)] for k, v in
        #                           instituteFilteredStdDF.items()}

        finalDates = {}

        for institute, df in instituteFilteredStdDF.items():
            if len(df) > 0:
                finalDates[institute] = str(max(df.AttDate.unique()))

        return finalDates


    def GetLatestAvailableStaffDate(self, dateFrom, dateTo, instituteList, filterType):

        lowerDate = GetDateFrom(dateFrom)#np.datetime64(dateFrom)
        upperDate = GetDateTo(dateTo)#np.datetime64(dateTo)
        filteredDF = self.staffAttandance[self.staffAttandance.AbsentDate >= lowerDate]
        filteredDF = filteredDF[filteredDF.AbsentDate <= upperDate]
        # instituteFilteredStaffDF = {x: self.staffAttandance[self.staffAttandance[filterType] == x]
        #                             for x in instituteList}
        instituteFilteredStaffDF = {x: filteredDF[filteredDF[filterType] == x]
                                                                 for x in instituteList}
        # instituteFilteredStaffDF = {k: v[(v.AbsentDate >= lowerDate) & (v.AbsentDate <= upperDate)]
        #                             for k, v in instituteFilteredStaffDF.items()}

        finalDates = {}

        for institute, df in instituteFilteredStaffDF.items():
            finalDates[institute] = str(max(df.AbsentDate.unique()))

        return finalDates


# tGraph = TutorGraph()
# print(tGraph.GenerateHighestToLowestPupilGraph(list(dic.values()), 'Branch', '2014-01-24', '2017-09-29', 'a'))
# print(tGraph.GetActiveTutorsByInstitute(list(dic.values()), 'Branch', '2014-06-24', '2017-12-08', 'True'))
# print(tGraph.GetLatestAvailableStaffDate('2017-07-24', '2017-09-29',['MAK', 'NYA'], 'Branch'))
# print(tGraph.GetLatestAvailableStdDate('2017-07-24', '2017-09-29',['MAK', 'NYA'], 'Branch'))
