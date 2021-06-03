
from Commons import *

class EnrollmentGraph():

    def __init__(self):
        self.studentData = pd.read_csv(filePath + 'vStudents.csv', header=0)
        self.enrollmentData = pd.read_csv(filePath + 'Registration.csv', header=0)
        self.stdSchoolData = pd.read_csv(filePath + 'StudCustField.csv', header=0)
        self.finalData = self.ProcessData()

    def ProcessData(self):
        self.studentData = self.studentData[['StudentID', 'CampusID', 'StatusName', 'Term', 'TermYear','StudYear']]
        self.enrollmentData = self.enrollmentData[['EnrollDate', 'LeftDate', 'StudentID', 'EnrollYear']]
        mergedData = self.studentData.merge(self.enrollmentData, on='StudentID', how='left')
        # mergedData = mergedData.merge(self.ko, on='StudentID', how='left')
        self.stdSchoolData = self.stdSchoolData[['StudentID', 'T12', 'T13']]
        self.stdSchoolData['School'] = pd.concat([self.stdSchoolData['T12'].dropna(), self.stdSchoolData['T13'].dropna()]).reindex_like(self.stdSchoolData)
        self.stdSchoolData = self.stdSchoolData[['StudentID', 'School']].dropna()
        self.stdSchoolData['School'] = [x.capitalize() for x in list(self.stdSchoolData['School'])]

        mergedData = mergedData.merge(self.stdSchoolData, on='StudentID', how='left')
        mergedData = mergedData.replace(np.NaN, 'Missing')
        filteredData = mergedData[(mergedData.EnrollDate != 'Missing')]
        filteredData.EnrollDate = pd.Series([dt.strptime(str(x).split('T')[0], "%Y-%m-%d").date()
                                             for x in list(filteredData['EnrollDate'])], index=filteredData.index)
        filteredData = filteredData.rename(columns={'CampusID' : 'Branch'})

        testData = filteredData[filteredData.School != 'Nan']
        schoolList = list(testData.School.unique())
        schoolCreated = OrderedDict((x, min(testData[testData.School == x].EnrollDate)) for x in schoolList)
        te = OrderedDict()
        te['School'] = list(schoolCreated.keys())
        te['CreationDate'] = list(schoolCreated.values())
        df = pd.DataFrame.from_dict(te)
        filteredData = filteredData.merge(df, on='School', how='left').drop_duplicates()
        filteredData['EnrollDiff'] = ((filteredData.EnrollDate - filteredData.CreationDate) / np.timedelta64(1, 'M')).astype(int)

        return filteredData


    def GetNewLearners(self, dateFrom, dateTo, instituteList, gradesList, filterType):

        lowerDate = GetDateFrom(dateFrom)
        upperDate = GetDateTo(dateTo)

        instituteFilteredDF = {x: self.finalData[self.finalData[filterType] == x] for x in instituteList}
        newLearnersByInstitute = {}
        for institute, df in instituteFilteredDF.items():
            newLearnersByGrades = {}
            for grade in gradesList:
                df2 = df[(df.EnrollDate >= lowerDate) & (df.EnrollDate <= upperDate)]
                df2 = df2[df2[filterType] == institute]
                df2 = df2[df2.StatusName == 'Current']
                df2 = df2.groupby('StudentID', as_index=False).max()
                df2 = df2[df2.StudYear.str.contains(grade)]
                df3 = df2[df2.EnrollDiff > 3]
                newLearnersByGrades[grade] = len(df3.StudentID.unique())
                # newLearnersByGrades[grade] = len(df3)
            newLearnersByInstitute[institute] = newLearnersByGrades
        # print(newLearnersByInstitute)
        return newLearnersByInstitute

    def GetNewLearners2(self, dateFrom, dateTo, instituteList, gradesList, filterType):

        lowerDate = GetDateFrom(dateFrom)
        upperDate = GetDateTo(dateTo)

        instituteFilteredDF = {x: self.finalData[self.finalData[filterType] == x] for x in instituteList}

        newLearnersByInstitute = {}
        for institute, df in instituteFilteredDF.items():
            newLearnersByGrades = {}
            for grade in gradesList:
                df2 = df[(df.EnrollDate >= lowerDate) & (df.EnrollDate <= upperDate)]
                df2 = df2[df2[filterType] == institute]
                df2 = df2[df2.StatusName == 'Current']
                df2 = df2[df2.StudYear.str.contains(grade)]
                newLearnersByGrades[grade] = len(df2.StudentID.unique())
                # newLearnersByGrades[grade] = len(df[(df.EnrollDate >= lowerDate) & (df.EnrollDate <= upperDate) &
                #                                         (df[filterType] == institute) & (df.StatusName == 'Current') &
                #                                     (df.StudYear.str.contains(grade)) & (df.EnrollDiff > 3)].StudentID.unique())
            newLearnersByInstitute[institute] = newLearnersByGrades
        return newLearnersByInstitute

    def GetNewLearnersAtNewSchool(self, dateFrom, dateTo, instituteList, gradesList, filterType):

        lowerDate = GetDateFrom(dateFrom)
        upperDate = GetDateTo(dateTo)

        instituteFilteredDF = {x: self.finalData[self.finalData[filterType] == x] for x in instituteList}

        newAtNewByInsitute = {}
        for institute, df in instituteFilteredDF.items():
            newAtNewByGrades = {}
            for grade in gradesList:
                df2 = df[(df.EnrollDate >= lowerDate) & (df.EnrollDate <= upperDate)]
                df2 = df2[df2[filterType] == institute]
                df2 = df2[df2.StatusName == 'Current']
                df2 = df2[df2.StudYear.str.contains(grade)]
                df4 = df2[df2.EnrollDiff <= 3]
                newAtNewByGrades[grade] = len(df4.StudentID.unique())
                # newLearnersByGrades[grade] = len(df[(df.EnrollDate >= lowerDate) & (df.EnrollDate <= upperDate) &
                #                                         (df[filterType] == institute) & (df.StatusName == 'Current') &
                #                                     (df.StudYear.str.contains(grade)) & (df.EnrollDiff > 3)].StudentID.unique())
            newAtNewByInsitute[institute] = newAtNewByGrades
        return newAtNewByInsitute

    def GetTotalLearnersByInstitute(self, dateFrom, dateTo, instituteList, gradesList, filterType):

        newDF = FilterDF(dateFrom, dateTo, self.finalData)


        instituteFilteredDF = {x: newDF[newDF[filterType] == x] for x in instituteList}

        totalLearnersByInstitute = {}
        for institute, df in instituteFilteredDF.items():
            totalLearnersByGrade = {}
            for grade in gradesList:
                gradeStr = grade+'-'+institute
                #totalLearnersByGrade[grade] = (len(df[(df[filterType] == institute) & (df.StudYear.str.contains(grade))].StudentID.unique()))
                totalLearnersByGrade[grade] = len(df[df.StudYear.str.contains(gradeStr)].StudentID.unique())
            totalLearnersByInstitute[institute] = totalLearnersByGrade

        return totalLearnersByInstitute

    def GetKickOutByInstitute(self, dateFrom, dateTo, instituteList, gradesList, filterType):

        # newDF = FilterDF(dateFrom, dateTo, self.finalData)
        lowerDate = GetDateFrom(dateFrom)
        upperDate = GetDateTo(dateTo)

        filteredData = self.finalData[(self.finalData.LeftDate != 'Missing')]
        filteredData = FilterDF(dateFrom, dateTo, filteredData)
        filteredData.LeftDate = pd.Series([dt.strptime(str(x).split('T')[0], "%Y-%m-%d").date()
                                           for x in list(filteredData['LeftDate'])], index=filteredData.index)
        filteredData['LeftYear'] = pd.Series([x.year for x in list(filteredData.LeftDate)], index=filteredData.index)
        # filteredData = filteredData.loc[filteredData.groupby('StudentID')['TermYear'].agg(pd.Series.idxmax)]
        #30651
        # instituteFilteredDF = {x: newDF[newDF[filterType] == x] for x in instituteList}
        instituteFilteredDF = {x: filteredData[filteredData[filterType] == x] for x in instituteList}
        kickOutByInstitute = {}

        for institute, df in instituteFilteredDF.items():
            kickOutByGrade = {}
            for grade in gradesList:
                df2 = df[(df.LeftDate >= lowerDate) & (df.LeftDate <= upperDate) & (df.TermYear == df.LeftYear)]
                df2 = df2[df2[filterType] == institute]
                df2 = df2[df2.StudYear.str.contains(grade)]
                df2 = df2[df2.StatusName != 'Deleted']
                kickOutByGrade[grade] = len(df2.StudentID.unique())
                # kickOutByGrade[grade] = len(df[(df[filterType] == institute) & (df.LeftDate != 'Missing') &
                #                                (df.StudYear.str.contains(grade))].StudentID.unique())
            kickOutByInstitute[institute] = kickOutByGrade
        return kickOutByInstitute

    def GenerateEnrollmentGraph(self, dateFrom, dateTo, instituteList, gradesList, filterType):
        learners = self.GetNewLearners(dateFrom, dateTo, instituteList, gradesList, filterType)
        newAtnew = self.GetNewLearnersAtNewSchool(dateFrom, dateTo, instituteList, gradesList, filterType)
        totalReturning = self.CalculateTotalReturning(dateFrom, dateTo, instituteList, gradesList, filterType)
        kickouts = self.GetKickOutByInstitute(dateFrom, dateTo, instituteList, gradesList, filterType)
        enrollmentByReasons = {}

        enrollmentByInstitute = {}
        for key, values in learners.items():
            enrollmentByInstitute[key] = sum([value for x, value in values.items()])
        enrollmentByReasons['New Learners at existing school'] = enrollmentByInstitute

        enrollmentByInstitute = {}
        for key, values in newAtnew.items():
            enrollmentByInstitute[key] = sum([value for x, value in values.items()])
        enrollmentByReasons['New Learners at new school'] = enrollmentByInstitute

        enrollmentByInstitute = {}
        for key, values in totalReturning.items():
            enrollmentByInstitute[key] = sum([value for x, value in values.items()])
        enrollmentByReasons['Total Returning'] = enrollmentByInstitute

        enrollmentByInstitute = {}
        for key, values in kickouts.items():
            enrollmentByInstitute[key] = sum([value for x, value in values.items()])
        enrollmentByReasons['Kickout'] = enrollmentByInstitute

        return enrollmentByReasons

    def CalculateTotalReturning(self, dateFrom, dateTo, instituteList, gradesList, filterType):
        totalLearners = self.GetTotalLearnersByInstitute(dateFrom, dateTo, instituteList, gradesList, filterType)
        kickouts = self.GetKickOutByInstitute(dateFrom, dateTo, instituteList, gradesList, filterType)
        newLearners = self.GetNewLearners2(dateFrom, dateTo, filterType=filterType, gradesList=gradesList, instituteList=instituteList)
        totalReturningByInstitute = {}
        for institute, gradesDic in totalLearners.items():
            totalReturningByGrade = {}
            for grade, totalNumber in gradesDic.items():
                if institute in newLearners:
                    if grade in newLearners[institute]:
                        kickout = newLearners[institute][grade]
                        total = 0
                        if totalNumber > 0:
                            total = totalNumber - kickout
                            if total < 0:
                                total = 0

                        totalReturningByGrade[grade] = total
            totalReturningByInstitute[institute] = totalReturningByGrade
        return  totalReturningByInstitute

    def GetLatestDatesBranchWise(self, dateFrom, dateTo, instituteList, filterType):

        newDF = FilterDF(dateFrom, dateTo, self.finalData)
        instituteFilteredDF = {x: newDF[newDF[filterType] == x] for x in instituteList}
        finalDates = {}
        for institute, df in instituteFilteredDF.items():
            if len(df.EnrollDate.unique()) > 0:
                finalDates[institute] = str(max(df.EnrollDate.unique()))
        return finalDates

print(EnrollmentGraph().GenerateEnrollmentGraph('3|2017', '3|2017', ['ATL'], ['G08', 'G09', 'G10', 'G11', 'G12', 'Gr11'], 'Branch'))
# print(EnrollmentGraph().GetLatestDatesBranchWise('2017-10-12', '2017-12-12', list(dic.values()), 'Branch'))