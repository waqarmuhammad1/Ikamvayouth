import pandas as pd
import numpy as np
from Commons import *
import math
from collections import ChainMap
from collections import OrderedDict

class AcademicGraph():

    def __init__(self):
        self.marksFileName = filePath + 'vARSubjAcad.csv'
        self.subjFileName = filePath + 'vSubjects.csv'
        self.stdSchoolData = pd.read_csv(filePath + 'StudCustField.csv', header=0)
        self.stdMarksInfo = pd.read_csv(self.marksFileName, header=0, sep=',')
        self.subjInfo = pd.read_csv(self.subjFileName, header=0, sep=',')

    def PreprocessData(self, subjectList, instituteList, gradeList, dateFrom, dateTo, filterType, comparisonList=[]):

        marksData = self.stdMarksInfo[['TermYear', 'Term', 'AcYear', 'StudID', 'SubjID', 'Mark']]
        marksData = marksData.query('Mark > 0.0')

        self.stdSchoolData = self.stdSchoolData[['StudentID', 'T12', 'T13']]
        self.stdSchoolData['School'] = pd.concat([self.stdSchoolData['T12'].dropna(), self.stdSchoolData['T13'].dropna()]).reindex_like(self.stdSchoolData)
        self.stdSchoolData = self.stdSchoolData[['StudentID', 'School']].dropna()
        self.stdSchoolData = self.stdSchoolData.rename(columns={'StudentID': 'StudID'})
        self.stdSchoolData['School'] = [x.capitalize() for x in list(self.stdSchoolData['School'])]

        subjData = self.subjInfo.replace(np.NaN, 'Missing')
        marksData = marksData.replace(np.NaN, 'Missing')
        subjStr = ' or '.join(['Subject == "' + x + '"' for x in subjectList])

        subjData = subjData.query(subjStr)

        if len(comparisonList) >0:
            comparisonStr = r'|'.join(comparisonList)
            marksData = marksData[marksData.Term.astype(str).str.contains(comparisonStr)]

        marksData = FilterDF(dateFrom, dateTo, marksData)
        # if is_date(dateFrom) == True:
        #     marksData = FilterDFByDates(dateFrom, dateTo, marksData)
        # else:
        #     termFrom = dateFrom.split(',')[0]
        #     yearFrom = dateFrom.split(',')[1]
        #
        #     termTo = dateTo.split(',')[0]
        #     yearTo = dateTo.split(',')[1]
        #
        #     marksData = FilterByTermYearTerm(termFrom, yearFrom, termTo, yearTo, marksData)

        marksData = marksData.merge(subjData, on="SubjID", how='left')
        marksData = marksData.merge(self.stdSchoolData, on='StudID', how='left')

        marksData = marksData.drop(['SubjID', 'SubjCode', 'Seq', 'Lvl'], axis=1)

        if filterType == 'Branch':
            instituteDFLis = [marksData[marksData.AcYear.str.contains(x, na=False)] for x in instituteList]
            marksData = pd.concat(instituteDFLis)
        elif filterType == 'School':
            instituteDFLis = [marksData[marksData.School.str.contains(x, na=False)] for x in instituteList]
            marksData = pd.concat(instituteDFLis)


        instituteDFLis = [marksData[marksData.AcYear.str.contains(x, na=False)] for x in gradeList]
        marksData = pd.concat(instituteDFLis)
        return marksData

    def GetAvgAllMarks(self, subjectList, instituteList, gradeList, dateFrom, dateTo, filterType, comparisonList=[]):
        marksData = self.PreprocessData(subjectList, instituteList, gradeList, dateFrom, dateTo, filterType, comparisonList=comparisonList)

        filteredBySubjectDF = {x: marksData[marksData['Subject'] == x] for x in subjectList}
        if len(comparisonList) <= 0:
            avgMarksBySubject = {}
            for subject, df in filteredBySubjectDF.items():
                val = round(df.Mark.mean(),0)
                if math.isnan(val):
                    avgMarksBySubject[subject] = 0
                else:
                    avgMarksBySubject[subject] = val
            return avgMarksBySubject
        else:
            avgMarksBySubject = {}
            for subject, df in filteredBySubjectDF.items():
                avgMarksByTerm = {}
                for term in comparisonList:
                    val = round(df[df.Term == int(term)].Mark.mean(), 0)
                    if math.isnan(val):
                        avgMarksByTerm['Term '+str(term)] = 0
                    else:
                        avgMarksByTerm['Term ' + str(term)] = val
                avgMarksBySubject[subject] = avgMarksByTerm
            reasons = []
            for x in list(avgMarksBySubject.values()):
                reasons += list(x.keys())
            reasons = list(set(reasons))
            di = {}
            for x in reasons:
                temp = {}
                for y in avgMarksBySubject.keys():
                    if x in avgMarksBySubject[y]:
                        temp[y] = avgMarksBySubject[y][x]
                di[x] = temp

            sorted_dict = OrderedDict(sorted(di.items(), key=lambda t: t[0]))
            return sorted_dict


    def GetPercentOfStudentsPass(self, subjectList, instituteList, gradeList, dateFrom, dateTo, filterType, comparisonList=[]):

        marksData = self.PreprocessData(subjectList, instituteList, gradeList, dateFrom, dateTo, filterType, comparisonList=comparisonList)

        filteredBySubjectDF = {x: marksData[marksData['Subject'] == x] for x in subjectList}

        if len(comparisonList) <=0:
            avgMarksBySubject = {}
            for subject, df in filteredBySubjectDF.items():
                if len(df) > 0:
                    passingStudents = len(df[df.Mark >= 40])
                    totalStudents = len(df)
                    avgMarksBySubject[subject] = round((passingStudents / totalStudents) * 100, 0)
                else:
                    avgMarksBySubject[subject] = 0
            return avgMarksBySubject
        else:
            avgMarksBySubject = {}
            for subject, df in filteredBySubjectDF.items():
                avgMarksByTerm = {}
                for term in comparisonList:
                    if len(df) > 0:
                        firstVal = len(df[(df.Mark >= 40) & (df.Term == int(term))])
                        secondVal = len(df[df.Term == int(term)])
                        if secondVal > 0:
                            avgMarksByTerm['Term '+str(term)] = round((firstVal/ secondVal) * 100, 0)
                        else:
                            avgMarksByTerm['Term ' + str(term)] = 0
                    else:
                        avgMarksByTerm['Term '+str(term)] = 0
                avgMarksBySubject[subject] = avgMarksByTerm

            reasons = []
            for x in list(avgMarksBySubject.values()):
                reasons += list(x.keys())
            reasons = list(set(reasons))
            di = {}
            for x in reasons:
                temp = {}
                for y in avgMarksBySubject.keys():
                    if x in avgMarksBySubject[y]:
                        temp[y] = avgMarksBySubject[y][x]
                di[x] = temp
            return di

    def GetNumberOfDistinctions(self, subjectList, instituteList, gradeList, dateFrom, dateTo, filterType, comparisonList=[]):
        marksData = self.PreprocessData(subjectList, instituteList, gradeList, dateFrom, dateTo, filterType, comparisonList=comparisonList)

        filteredBySubjectDF = {x: marksData[marksData['Subject'] == x] for x in subjectList}

        if len(comparisonList) <=0:
            avgMarksBySubject = {}
            for subject, df in filteredBySubjectDF.items():
                if len(df) > 0:
                    avgMarksBySubject[subject] = len(df[df.Mark >= 80])
                else:
                    avgMarksBySubject[subject] = 0
            return avgMarksBySubject
        else:
            avgMarksBySubject = {}
            for subject, df in filteredBySubjectDF.items():
                avgMarksByTerm = {}
                for term in comparisonList:
                    if len(df) > 0:
                        avgMarksByTerm['Term '+str(term)] = len(df[(df.Mark >= 80) & (df.Term == int(term))])
                    else:
                        avgMarksByTerm['Term '+str(term)] = 0
                avgMarksBySubject[subject] = avgMarksByTerm

            reasons = []
            for x in list(avgMarksBySubject.values()):
                reasons += list(x.keys())
            reasons = list(set(reasons))
            di = {}
            for x in reasons:
                temp = {}
                for y in avgMarksBySubject.keys():
                    if x in avgMarksBySubject[y]:
                        temp[y] = avgMarksBySubject[y][x]
                di[x] = temp
            return di

    def GetNumberTakingSubjects(self, subjectList, instituteList, gradeList, dateFrom, dateTo, filterType, comparisonList=[]):
        marksData = self.PreprocessData(subjectList, instituteList, gradeList, dateFrom, dateTo, filterType, comparisonList=comparisonList)

        if len(comparisonList) <=0:
            filteredBySubjectDF = {x: len(marksData[marksData['Subject'] == x]) for x in subjectList}
            return filteredBySubjectDF
        else:
            filteredBySubjectDF = {x: marksData[marksData['Subject'] == x] for x in subjectList}
            numberTakingSub = {}
            for subject, df in filteredBySubjectDF.items():
                numberTakingSubByTerm = {}
                for term in comparisonList:
                    numberTakingSubByTerm['Term '+str(term)] = len(df[df.Term == int(term)])

                numberTakingSub[subject] = numberTakingSubByTerm
            reasons = []
            for x in list(numberTakingSub.values()):
                reasons += list(x.keys())
            reasons = list(set(reasons))
            di = {}
            for x in reasons:
                temp = {}
                for y in numberTakingSub.keys():
                    if x in numberTakingSub[y]:
                        temp[y] = numberTakingSub[y][x]
                di[x] = temp
            return di

    # def GetTrendGraph(self, subjectList, instituteList, gradeList, dateFrom, dateTo, filterType='Branch'):
    #
    #     marksData = self.PreprocessData(subjectList, instituteList, gradeList, dateFrom, dateTo, filterType)
    #
    #     termYearList = list(marksData.TermYear.unique())
    #
    #     marksDataByTermYear = {x: marksData[marksData.TermYear == x] for x in termYearList}
    #
    #     numberByYear = {}
    #     for year, df in marksDataByTermYear.items():
    #         numberBySubjects = {}
    #         for x in subjectList:
    #             numberBySubjects[x] = len(df[df.Subject == x].StudID.unique())
    #         numberByYear[str(year)] = numberBySubjects
    #     reasons = []
    #     for x in list(numberByYear.values()):
    #         reasons += list(x.keys())
    #     reasons = list(set(reasons))
    #     di = {}
    #     for x in reasons:
    #         temp = {}
    #         for y in numberByYear.keys():
    #             if x in numberByYear[y]:
    #                 temp[y] = numberByYear[y][x]
    #         di[x] = temp
    #     return di

    def GetTrendGraph(self, subjectList, instituteList, gradeList, dateFrom, dateTo, filterType='Branch'):

        marksData = self.PreprocessData(subjectList, instituteList, gradeList, dateFrom, dateTo, filterType)

        termYearList = list(marksData.TermYear.unique())
        termYearList.sort()
        #[OrderedDict((k, d[k](v)) for (k, v) in l.iteritems()) for l in L]
        marksDataByTermYear = [OrderedDict((x, marksData[marksData.TermYear == x]) for x in termYearList)]
        marksDataByTermYear = marksDataByTermYear[0]
        numberByYear = OrderedDict()
        for year, df in marksDataByTermYear.items():

            termList = list(df.Term.unique())
            termList.sort()
            numberByTerm = OrderedDict()
            for term in termList:
                numberBySubjects = OrderedDict()
                tempDF = df[df['Term'] == term]
                for x in subjectList:
                    numberBySubjects[x] = len(tempDF[(tempDF.Subject == x)])
                numberByTerm[str(term)] = numberBySubjects
            newDict = GetTermDates(numberByTerm, year)
            numberByYear[str(year)] = newDict
        try:
            dictValues = list(numberByYear.values())
            newDictValues = OrderedDict()
            for x in dictValues:
                for y in x:
                    newDictValues[y] = x[y]

            dictValues = newDictValues

        except:
            return None



        reasons = []
        for x in list(dictValues.values()):
            reasons += list(x.keys())

        reasons = list(set(reasons))
        di = OrderedDict()
        for x in reasons:
            temp = OrderedDict()
            for k, v in dictValues. items():
                if x in v:
                    temp[k] = v[x]
            di[x] = temp
        return di

    def GetSubjectsByBranchGrade(self, instituteList, gradeList, filterType, dateFrom, dateTo):
        marksData = self.stdMarksInfo[['TermYear', 'Term', 'AcYear', 'StudID', 'SubjID', 'Mark']]
        #marksData = marksData.query('Mark > 0.0')

        stdSchoolData = self.stdSchoolData[['StudentID', 'T12', 'T13']]
        stdSchoolData['School'] = pd.concat([stdSchoolData['T12'].dropna(), stdSchoolData['T13'].dropna()]).reindex_like(stdSchoolData)
        stdSchoolData = stdSchoolData[['StudentID', 'School']].dropna()
        stdSchoolData['School'] = [x.capitalize() for x in list(stdSchoolData['School'])]

        # stdSchoolData = self.stdSchoolData[['StudentID', 'T21']]
        # stdSchoolData = stdSchoolData.rename(columns={'T21': 'School'})
        stdSchoolData = stdSchoolData.rename(columns={'StudentID': 'StudID'})

        subjData = self.subjInfo.replace(np.NaN, 'Missing')
        marksData = marksData.replace(np.NaN, 'Missing')

        marksData = marksData.merge(subjData, on="SubjID", how='left')
        marksData = marksData.merge(stdSchoolData, on='StudID', how='left')

        if filterType == 'Branch':
            instituteDFLis = [marksData[marksData.AcYear.str.contains(x, na=False)] for x in instituteList]
            marksData = pd.concat(instituteDFLis)
        elif filterType == 'School':
            instituteDFLis = [marksData[marksData.School.str.contains(x, na=False)] for x in instituteList]
            marksData = pd.concat(instituteDFLis)
        instituteDFLis = [marksData[marksData.AcYear.str.contains(x, na=False)] for x in gradeList]

        marksData = pd.concat(instituteDFLis)
        marksData = FilterDF(dateFrom, dateTo, marksData)
        # if is_date(dateFrom) == True:
        #     marksData = FilterDFByDates(dateFrom, dateTo, marksData)
        # else:
        #     termFrom = dateFrom.split(',')[0]
        #     yearFrom = dateFrom.split(',')[1]
        #
        #     termTo = dateTo.split(',')[0]
        #     yearTo = dateTo.split(',')[1]
        #
        #     marksData = FilterByTermYearTerm(termFrom, yearFrom, termTo, yearTo, marksData)

        subjectList =list(marksData['Subject'].unique())
        subjectList.remove(np.nan)
        subjectList.sort()
        return subjectList

# print(AcademicGraph().GetNumberTakingSubjects(["Mathematics", "Mathematical Literacy", 'Physical Sciences', 'Life Sciences', 'History', 'Geography', 'Accounting'],
#                                      ["MAK"], ['G12'],'2017-01-01', '2017-03-31', 'Branch'))
# ["Mathematics", "Mathematical Literacy", 'Physical Sciences', 'Life Sciences', 'History', 'Geography', 'Accounting']
# subList = AcademicGraph().GetSubjectsByBranchGrade(['NYA'],['G12'], 'Branch', '1|2016', '1|2017')
# print(len(subList))
# print(AcademicGraph().GetTrendGraph(subList,
#                                      ["NYA"], ['G12'],'1|2016', '1|2017', 'Branch'))


