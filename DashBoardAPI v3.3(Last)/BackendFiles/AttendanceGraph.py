# DataSource -> CSV-Table

from Commons import *

class Attendance_Graph():

    def __init__(self):
        self.StdAttend = pd.read_csv(filePath + 'vATDStudAttTerm.csv')
        self.StdSub = pd.read_csv(filePath + 'vStudents.csv')
        self.StdSchools = pd.read_csv(filePath + 'StudCustField.csv')
        self.attDates = pd.read_csv(filePath + 'ATDStudAttend.csv')
        self.CombinedDF, self.condition = self.FilterData()
        # self.attDates.AttDate = pd.Series([dt.strptime(str(x).split('T')[0], "%Y-%m-%d").date()
        #                                    for x in list(self.attDates.AttDate)], index=self.attDates.index)
        #
        #
        # self.attDates = self.attDates.merge(self.CombinedDF, on='StudentID')
        # self.attDates = self.attDates[['StudentID', 'AttDate', 'AcYear', 'School']]



    def FilterData(self):
        filterStdAttendColumns = self.StdAttend[['TermYear', 'Term', 'Present', 'Absent', 'StudentID']]
        filterStdAttendColumns = filterStdAttendColumns.assign(Percent =((filterStdAttendColumns['Present']) / (filterStdAttendColumns['Present'] + filterStdAttendColumns['Absent'])) * 100)
        filterStdSubjColumns = self.StdSub[["StudYear", "StudentID",'FirstName', 'LastName', 'Term', 'TermYear']]
        filterStdSubjColumns.rename(columns={'StudYear': 'AcYear'}, inplace=True)

        self.StdSchools = self.StdSchools[['StudentID', 'T12', 'T13']]
        self.StdSchools['School'] = pd.concat([self.StdSchools['T12'].dropna(), self.StdSchools['T13'].dropna()]).reindex_like(self.StdSchools)
        self.StdSchools = self.StdSchools[['StudentID', 'School']].dropna()
        self.StdSchools['School'] = [x.capitalize() for x in list(self.StdSchools['School'])]
        #filterSchoolColumns = self.StdSchools[['StudentID','T21']].drop_duplicates()
        #filterSchoolColumns.rename(columns={'T21': 'School'}, inplace=True)

        combineDF = filterStdAttendColumns.merge(filterStdSubjColumns, on=['StudentID', 'TermYear', 'Term'], how='right').drop_duplicates()
        combineDF = combineDF.merge(self.StdSchools, on=['StudentID'], how='left').drop_duplicates()

        condition = OrderedDict([("Black 0-49", ((combineDF['Percent'] >= 0) & (combineDF['Percent'] < 50))),
                                 ("Red 50-69", ((combineDF['Percent'] >= 50) & (combineDF['Percent'] < 70))),
                                 ("Yellow 70-79", ((combineDF['Percent'] >= 70) & (combineDF['Percent'] < 80))),
                                 ("Green 80-100", (combineDF['Percent'] >= 80))])
        self.get_colors=["Black 0-49","Red 50-69","Yellow 70-79", "Green 80-100"]


        return combineDF,condition

    def CreateBranchWiseData(self, Type, grades, filtertype, dateFrom, dateTo):
        grades = '|'.join([x + '' for x in grades])
        CombineDF, condition = self.CombinedDF, self.condition

        CombineDF = FilterDF(dateFrom, dateTo, CombineDF)

        CombineDF = CombineDF.replace(np.nan, 'Missing')
        CombineDF = CombineDF.replace(np.NaN, 'Missing')
        CombineDF = CombineDF[CombineDF.Present != 'Missing']
        CombineDF = CombineDF[CombineDF.Absent != 'Missing']
        CombineDF = CombineDF[CombineDF["AcYear"].str.contains(r'' + grades + '')]
        CombineDF = CombineDF[['StudentID', 'Absent', 'Present', 'AcYear', 'FirstName', 'LastName', 'School']]
        CombineDF[['School']] = CombineDF[['School']].replace(np.nan, 'Missing')
        CombineDF = CombineDF.groupby(['StudentID', 'AcYear', 'FirstName', 'LastName', 'School'], as_index=False).sum()
        CombineDF['Percent'] = round((CombineDF['Present'] / (CombineDF['Present'] + CombineDF['Absent'])) * 100, 0)

        condition = OrderedDict([("Black 0-49", ((CombineDF['Percent'] >= 0) & (CombineDF['Percent'] < 50))),
                                 ("Red 50-69", ((CombineDF['Percent'] >= 50) & (CombineDF['Percent'] < 70))),
                                 ("Yellow 70-79", ((CombineDF['Percent'] >= 70) & (CombineDF['Percent'] < 80))),
                                 ("Green 80-100", (CombineDF['Percent'] >= 80))])
        CombineDic = OrderedDict()
        if filtertype == "School":
            for y in Type:
                IndividualDic = OrderedDict()
                count = 0
                for x in condition:
                    CondCount = len(CombineDF[(CombineDF['School'].str.contains(y)) & (condition[x])].StudentID.unique())
                    IndividualDic[self.get_colors[count]] = CondCount
                    count += 1
                CombineDic[y] = IndividualDic


        else:
            for y in Type:
                IndividualDic = OrderedDict()
                count = 0
                for x in condition:
                    CondCount = len(CombineDF[(CombineDF['AcYear'].str.contains(y)) & (condition[x])].StudentID.unique())
                    IndividualDic[self.get_colors[count]] = CondCount
                    count += 1
                CombineDic[y] = IndividualDic

        reasons = OrderedDict()

        for x in list(CombineDic.values()):
            for y in x.keys():
                if y not in reasons:
                    reasons[y] = 0
            #reasons += list(x.keys())

        #reasons = list(set(reasons))
        reasons = reasons.keys()
        #print(reasons)
        di = OrderedDict()
        for x in reasons:
            temp = OrderedDict()
            for y in CombineDic.keys():
                if x in CombineDic[y]:
                    temp[y] = CombineDic[y][x]
            di[x] = temp
        return di




    def CreateTrendOverTimeGraph_1(self,branches,grades,colors,dateFrom,dateTo):
        grades = '|'.join([x + '' for x in grades])
        CombineDF, condition = self.CombinedDF, self.condition

        CombineDF = FilterDF(dateFrom, dateTo, CombineDF)
        # if is_date(dateFrom) == True:
        #     CombineDF = FilterDFByDates(dateFrom, dateTo, CombineDF)
        # else:
        #     termFrom = dateFrom.split(',')[0]
        #     yearFrom = dateFrom.split(',')[1]
        #
        #     termTo = dateTo.split(',')[0]
        #     yearTo = dateTo.split(',')[1]
        #
        #     CombineDF = FilterByTermYearTerm(termFrom, yearFrom, termTo, yearTo, CombineDF)

        term_unique = list( CombineDF["Term"].unique())

        get_years = list(CombineDF.TermYear.unique())
        get_years.sort()
        CombineDic = OrderedDict()
        for y in branches:
            IndividualDic = OrderedDict()
            for z in get_years:
                IndividualDic_2 = OrderedDict()
                for i in term_unique:
                    val_2 = CombineDF[(CombineDF['AcYear'].str.contains(y)) & (CombineDF['TermYear'].astype(str).str.contains(str(z))) & (CombineDF['AcYear'].str.contains(r'' + grades + ''))]
                    val_2 = val_2.query("Term == "+str(i))
                    if len(val_2) <=0:
                        continue
                    val_3 = val_2.count()
                    val = 0
                    for x in colors:
                        val += len(val_2[(condition[x])].StudentID.unique())
                    IndividualDic_2[str(i)] = val
                newDict = GetTermDates(IndividualDic_2, z)
                IndividualDic[str(z)] = newDict
            finalDict = OrderedDict()
            for year, value in IndividualDic.items():
                for x, v in value.items():
                    finalDict[x] = v
            CombineDic[y] = finalDict
        return CombineDic



    def CreateTrendOverTimeGraph_2(self, branches, grades, colors, dateFrom, dateTo):
        CombineDF, condition = self.CombinedDF, self.condition

        CombineDF = FilterDF(dateFrom, dateTo, CombineDF)

        term_unique = list(CombineDF["Term"].unique())
        term_unique.sort()
        get_years = list(CombineDF.TermYear.unique())
        get_years.sort()
        IndividualDic =OrderedDict()
        instituteDFLis = [CombineDF[CombineDF.AcYear.str.contains(x, na=False)] for x in branches]
        CombineDF = pd.concat(instituteDFLis)
        instituteDFLis = []
        instituteDFLis = [CombineDF[CombineDF.AcYear.str.contains(x, na=False)] for x in grades]
        tempDFLis = CombineDF[CombineDF.AcYear.str.contains('G09')]
        CombineDF = pd.concat(instituteDFLis)
        CombineDic = OrderedDict()
        CombineDF = CombineDF.drop_duplicates()
        for z in get_years:
            dictest = OrderedDict()
            for i in term_unique:
                IndividualDic_2 = OrderedDict()
                val_2 = CombineDF[(CombineDF['TermYear'].astype(str).str.contains(str(z)))]
                val_2 = val_2.query("Term == " + str(i))
                if len(val_2) <= 0:
                    continue
                for x in colors:
                    if x in IndividualDic_2.keys():
                        IndividualDic_2[x] += len(val_2[(condition[x])].StudentID.unique())
                    else:
                        IndividualDic_2[x] = len(val_2[(condition[x])].StudentID.unique())
                dictest[str(i)] = IndividualDic_2

            newDict = GetTermDates(dictest, z)
            IndividualDic[str(z)] = newDict
        finalDict = OrderedDict()
        for year, value in IndividualDic.items():
            for x, v in value.items():
                finalDict[x] = v
        reasons = OrderedDict()
        for x in list(finalDict.values()):
            for y in x.keys():
                if y not in reasons:
                    reasons[y] = 0
            #reasons += list(x.keys())
        #reasons = list(set(reasons))
        reasons = reasons.keys()
        di = OrderedDict()
        for x in reasons:
            temp = OrderedDict()
            for y in finalDict.keys():
                if x in finalDict[y]:
                    temp[y] = finalDict[y][x]
            di[x] = temp
        return di




    def GetAllBranchData(self, gradeList, dateFrom, dateTo):


        branchList = list(set(dic.values()))
        temp = self.CreateBranchWiseData(branchList,gradeList,'Branch',dateFrom, dateTo)
        allBranches = {}
        for k, v in temp.items():
            tempValue = 0
            for k1, v1 in v.items():
                tempValue += v1

            allBranches[k] = tempValue
        return allBranches

    def create_years(self,YearsFrom,YearTo):
        self.list = []
        for x in range(YearsFrom,(YearTo+1)):
            self.list.append(x)
        return self.list

    def GetLatestAvailableAttandanceDate(self, dateFrom, dateTo, instituteList, filterType):

        lowerDate = GetDateFrom(dateFrom)
        upperDate = GetDateTo(dateTo)

        tempDates = FilterDF(dateFrom, dateTo, self.attDates)

        # if is_date(dateFrom):
        #     tempDates = FilterDFByDates(dateFrom, dateTo, self.attDates)
        # else:
        #     termFrom = dateFrom.split(',')[0]
        #     yearFrom = dateFrom.split(',')[1]
        #
        #     termTo = dateTo.split(',')[0]
        #     yearTo = dateTo.split(',')[1]
        #     tempDates = FilterByTermYearTerm(termFrom, yearFrom, termTo, yearTo, self.attDates)
        #self.attDates = self.attDates[(self.attDates.AttDate >= lowerDate) & (self.attDates.AttDate <= upperDate)]
        tempDates = tempDates.dropna()
        if filterType is 'School':
            instituteFilteredStaffDF = {x: tempDates[tempDates.School == x]
                                        for x in instituteList}
            instituteFilteredStaffDF = {k: v[(v.AttDate >= lowerDate) & (v.AttDate <= upperDate)]
                                        for k, v in instituteFilteredStaffDF.items()}

        else:
            instituteFilteredStaffDF = {x: tempDates[tempDates.AcYear.str.contains(x)]
                                        for x in instituteList}
            instituteFilteredStaffDF = {k: v[(v.AttDate >= lowerDate) & (v.AttDate <= upperDate)]
                                        for k, v in instituteFilteredStaffDF.items()}

        finalDates = {}

        for institute, df in instituteFilteredStaffDF.items():
            finalDates[institute] = str(max(df.AttDate.unique()))

        return finalDates


# print(Attendance_Graph().CreateBranchWiseData(["MAM"],["G09"],"Branch","4|2017","4|2017"))
# print(Attendance_Graph().GetLatestAvailableAttandanceDate('2017-07-24', '2017-09-30', ['MAK'], 'Branch'))
# print(Attendance_Graph().CreateTrendOverTimeGraph_2(
#     ["CHE"],
#     ["G10", "G11", "G12"],
#     ["Green 80-100", "Yellow 70-79", "Black 0-49", "Red 50-69"],
#     "2016-01-01",
#     "2017-11-28"))
