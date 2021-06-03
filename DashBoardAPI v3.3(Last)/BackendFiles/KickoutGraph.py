import pandas as pd
import numpy as np
from textacy import preprocess
from datetime import datetime as dt
from Commons import *
import math
class KickOutGraph():

    # def __init__(self):
    #     self.dataFilePath = filePath + 'Registration.csv'
    #     self.stdFilePath = filePath + 'vStudents.csv'
    #     self.data = pd.read_csv(self.dataFilePath, header=0, sep=',', infer_datetime_format=True)
    #     self.studentData = pd.read_csv(self.stdFilePath, header=0, sep=',', infer_datetime_format=True)
    #     self.stdSchoolData = pd.read_csv(filePath + 'StudCustField.csv', header=0)
    #     self.reason = pd.read_csv(filePath + 'RegReason.csv', header=0)
    #     self.mergedDF = self.ProcessDataForKickoutGraph(self.data, self.studentData)
    #
    #
    # def ProcessDataForKickoutGraph(self, data, studentData):
    #     kickoutData = data[['StudentID', 'LeftDate', 'ReasonID']]
    #     kickoutData = kickoutData.merge(self.reason, on='ReasonID', how='left')
    #     kickoutData = kickoutData.replace(np.NaN, 'Missing')
    #     kickoutData = kickoutData[kickoutData['Reason'] != 'Missing']
    #     kickoutData = kickoutData[kickoutData['LeftDate'] != 'Missing']
    #
    #     tempSeries = pd.Series(
    #         [dt.strptime(str(x).split('T')[0], "%Y-%m-%d").date() for x in list(kickoutData['LeftDate'])],
    #         index=kickoutData.index)
    #     #tempSeries = pd.to_datetime(kickoutData.LeftDate)
    #     kickoutData['LeftDate'] = tempSeries
    #     #kickoutData = kickoutData.rename(columns={'ReasonTranfTo': 'Reason'})
    #     studentData = studentData[['StudentID', 'CampusID']]
    #
    #     self.stdSchoolData = self.stdSchoolData[['StudentID', 'T12', 'T13']]
    #     self.stdSchoolData['School'] = pd.concat([self.stdSchoolData['T12'].dropna(), self.stdSchoolData['T13'].dropna()]).reindex_like(self.stdSchoolData)
    #     self.stdSchoolData = self.stdSchoolData[['StudentID', 'School']].dropna()
    #     self.stdSchoolData['School'] = [x.capitalize() for x in list(self.stdSchoolData['School'])]
    #
    #     mergedDF = kickoutData.merge(studentData, on='StudentID')
    #     mergedDF = mergedDF.merge(self.stdSchoolData, on='StudentID')
    #     mergedDF = mergedDF.replace(np.NaN, 'Missing')
    #     mergedDF = mergedDF.drop_duplicates()
    #     mergedDF = mergedDF.rename(columns={'CampusID': 'Branch'})
    #     return mergedDF

    def __init__(self):
        self.studentData = pd.read_csv(filePath + 'vStudents.csv', header=0)
        self.enrollmentData = pd.read_csv(filePath + 'Registration.csv', header=0)
        self.stdSchoolData = pd.read_csv(filePath + 'StudCustField.csv', header=0)
        self.reason = pd.read_csv(filePath + 'RegReason.csv', header=0)
        self.mergedDF = self.ProcessData()

    def ProcessData(self):
        self.studentData = self.studentData[['StudentID', 'CampusID', 'StatusName', 'Term', 'TermYear','StudYear']]
        self.enrollmentData = self.enrollmentData[['EnrollDate', 'LeftDate', 'StudentID', 'EnrollYear', 'ReasonID']]
        mergedData = self.studentData.merge(self.enrollmentData, on='StudentID', how='left')
        mergedData = mergedData.merge(self.reason, on='ReasonID', how='left')
        # mergedData = mergedData.merge(self.ko, on='StudentID', how='left')
        self.stdSchoolData = self.stdSchoolData[['StudentID', 'T12', 'T13']]
        self.stdSchoolData['School'] = pd.concat([self.stdSchoolData['T12'].dropna(), self.stdSchoolData['T13'].dropna()]).reindex_like(self.stdSchoolData)
        self.stdSchoolData = self.stdSchoolData[['StudentID', 'School']].dropna()
        self.stdSchoolData['School'] = [x.capitalize() for x in list(self.stdSchoolData['School'])]

        mergedData = mergedData.merge(self.stdSchoolData, on='StudentID', how='left')
        mergedData = mergedData.replace(np.NaN, 'Missing')
        filteredData = mergedData[(mergedData.LeftDate != 'Missing')]
        filteredData.LeftDate = pd.Series([dt.strptime(str(x).split('T')[0], "%Y-%m-%d").date()
                                             for x in list(filteredData['LeftDate'])], index=filteredData.index)
        filteredData = filteredData.rename(columns={'CampusID' : 'Branch'})

        testData = filteredData[filteredData.School != 'Nan']
        schoolList = list(testData.School.unique())
        schoolCreated = OrderedDict((x, min(testData[testData.School == x].EnrollDate)) for x in schoolList)
        te = OrderedDict()
        te['School'] = list(schoolCreated.keys())
        # te['CreationDate'] = list(schoolCreated.values())
        df = pd.DataFrame.from_dict(te)
        filteredData = filteredData.merge(df, on='School', how='left').drop_duplicates()
        # filteredData['EnrollDiff'] = ((filteredData.EnrollDate - filteredData.CreationDate) / np.timedelta64(1, 'M')).astype(int)

        return filteredData

    def GenerateKickoutGraph(self, data, instituteList, filterType, dateFrom, dateTo):
        filteredData = data[(data.LeftDate != 'Missing')]
        filteredData = FilterDF(dateFrom, dateTo, filteredData)
        filteredData.LeftDate = pd.Series([dt.strptime(str(x).split('T')[0], "%Y-%m-%d").date()
                                           for x in list(filteredData['LeftDate'])], index=filteredData.index)
        instituteFilteredDF = {x: filteredData[filteredData[filterType].str.contains(x)] for x in instituteList}
        reasonValues = list(filteredData['Reason'].unique())
        kickoutByInstitute = {}
        lowerDate = GetDateFrom(dateFrom)#dt.date(dt.strptime(dateFrom, "%Y-%m-%d"))
        upperDate = GetDateTo(dateTo)#dt.date(dt.strptime(dateTo, "%Y-%m-%d"))
        for institute, df in instituteFilteredDF.items():
            kickoutByValue = {}
            for value in reasonValues:
                tempLen = len(df[(df['Reason'] == value) & (df['LeftDate'] >= lowerDate) & (df['LeftDate'] <= upperDate)].StudentID.unique())
                totalLen = len(df[(df['LeftDate'] >= lowerDate) & (df['LeftDate'] <= upperDate)].StudentID.unique())
                myValue = value.replace('Did not meet attendance requirement', 'DNMAR: ')
                if  'dnmar:  because of extracurricular activities (i.e. sports or arts)' in myValue.lower():
                    myValue = 'DNMAR: extracurricular activities (e.g. sports)'
                elif "learner stopped attending - dont know why" in myValue.lower():
                    myValue = 'Learner stopped attending'
                elif "dnmar:  - unsure why the learner was not attending" in myValue.lower():
                    myValue = 'DNMAR: reason unkown'
                elif "dnmar:  because of commitments at home" in myValue.lower():
                    myValue = "DNMAR: commitments at home"
                if tempLen > 0 and totalLen > 0:
                    # myValue = value.replace('Did not meet attendance requirement', 'DNMAR: ')
                    #myValue = preprocess.remove_punct(myValue)
                    #myValue = preprocess.normalize_whitespace(myValue)
                    kickoutByValue[myValue] = round(float(tempLen) / float(totalLen) * 100, 2)
            if len(kickoutByValue) > 0:
                kickoutByInstitute[institute] = kickoutByValue
        return kickoutByInstitute

    def GenerateKickoutGraphByBranch(self, data, dateFrom, dateTo):
        reasonValues = list(data['Reason'].unique())
        lowerDate = GetDateFrom(dateFrom)#dt.date(dt.strptime(dateFrom, "%Y-%m-%d"))
        upperDate = GetDateTo(dateTo)#dt.date(dt.strptime(dateTo, "%Y-%m-%d"))
        kickoutByValue = {}
        totalDF = data[(data['LeftDate'] >= lowerDate) & (data['LeftDate'] <= upperDate)]
        totalLen = len(totalDF)
        for value in reasonValues:
            #tempLen = len(data[(data['Reason'] == value) & (data['LeftDate'] >= lowerDate) & (data['LeftDate'] <= upperDate)])
            tempLen = len(totalDF[totalDF['Reason'] == value])
            if tempLen > 0:
                myValue = value.replace('Did not meet attendance requirement', 'DNMAR: ')
                myValue = preprocess.remove_punct(myValue)
                myValue = preprocess.normalize_whitespace(myValue)
                calcValue = float(tempLen) / float(totalLen)
                kickoutByValue[myValue] = round((calcValue * 100), 0)

    def GenerateGraph(self, branchList, filterType, dateFrom, dateTo):
        graphDict = self.GenerateKickoutGraph(self.mergedDF, branchList, filterType, dateFrom, dateTo)
        reasons = []

        for x in  list(graphDict.values()):
            reasons += list(x.keys())

        reasons = list(set(reasons))

        di = {}
        for x in reasons:
            temp = {}
            for y in graphDict.keys():
                if x in graphDict[y]:
                    temp[y] = graphDict[y][x]
            di[x] = temp

        return di

    def GenerateKickoutGraph2(self, data, instituteList, filterType, dateFrom, dateTo):
        instituteFilteredDF = {x: data[data[filterType].str.contains(x[:3].upper())] for x in instituteList}
        reasonValues = list(data['Reason'].unique())
        kickoutByInstitute = {}
        lowerDate = GetDateFrom(dateFrom)#dt.date(dt.strptime(dateFrom, "%Y-%m-%d"))
        upperDate = GetDateTo(dateTo)#dt.date(dt.strptime(dateTo, "%Y-%m-%d"))
        for institute, df in instituteFilteredDF.items():
            kickoutByValue = {}
            for value in reasonValues:
                if 'Did not meet attendance requirement' in value and 'DNMAR' not in kickoutByValue:
                    kickoutByValue['DNMAR'] = len(
                        df[(df['Reason'] == value) & (df['LeftDate'] >= lowerDate) & (df['LeftDate'] <= upperDate)])
                elif 'Did not meet attendance requirement' in value and 'DNMAR' in kickoutByValue:
                    kickoutByValue['DNMAR'] += len(
                        df[(df['Reason'] == value) & (df['LeftDate'] >= lowerDate) & (df['LeftDate'] <= upperDate)])
                else:
                    kickoutByValue[value] = len(
                        df[(df['Reason'] == value) & (df['LeftDate'] >= lowerDate) & (df['LeftDate'] <= upperDate)])
            kickoutByInstitute[institute] = kickoutByValue

        return kickoutByInstitute

    def GetLatestDatesBranchWise(self, dateFrom, dateTo, instituteList, filterType):
        lowerDate = GetDateFrom(dateFrom)#dt.date(dt.strptime(dateFrom, "%Y-%m-%d"))
        upperDate = GetDateTo(dateTo)#dt.date(dt.strptime(dateTo, "%Y-%m-%d"))
        filteredData = self.mergedDF[(self.mergedDF.LeftDate != 'Missing')]
        filteredData = FilterDF(dateFrom, dateTo, filteredData)
        filteredData.LeftDate = pd.Series([dt.strptime(str(x).split('T')[0], "%Y-%m-%d").date()
                                           for x in list(filteredData['LeftDate'])], index=filteredData.index)
        newDF = filteredData[(filteredData['LeftDate'] >= lowerDate) & (filteredData['LeftDate'] <= upperDate)]
        instituteFilteredDF = {x: newDF[newDF[filterType] == x] for x in instituteList}
        finalDates = {}
        for institute, df in instituteFilteredDF.items():
            if len(df.LeftDate.unique()) > 0:
                finalDates[institute] = str(max(df.LeftDate.unique()))
        return finalDates

# result = KickOutGraph().GenerateGraph(list(dic.values()), 'Branch', '2014-01-09', '2017-02-28')
# print(result)
# d = OrderedDict()
# branchList = []
# for x in result:
#     if x in d:
#         vals = list(result[x].values())
#         if len(vals) > 0:
#             valSum = sum(vals)
#             if valSum > 0:
#                 branchList += list(result[x].keys())
#             d[x]+=sum(vals)
#     else:
#         vals = list(result[x].values())
#         if len(vals) > 0:
#             valSum = sum(vals)
#             if valSum > 0:
#                 branchList += list(result[x].keys())
#             d[x] = sum(vals)
#
# totalB = len(list(dic.values()))
# totalVal = 0
# totalB = len(set(branchList))
# for x in d:
#     totalVal += (d[x] / totalB)
#     d[x] = round((d[x] / totalB), 2)
#
# print(d)
# print(totalVal)

# print(KickOutGraph().GetLatestDatesBranchWise('4|2017', '4|2017', list(dic.values()), 'Branch'))
