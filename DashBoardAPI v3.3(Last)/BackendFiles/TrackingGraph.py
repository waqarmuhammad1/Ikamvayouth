# DataSource -> ExcelSheet

import ntpath
import numpy as np
import pandas as pd
from collections import Counter
from Commons import *
class TrackingGraphs():

    def __init__(self, filesList):
        self.homePath = filePath
        self.sheetName = 'New Consolidated list'
        fileNames = [self.homePath + x for x in filesList]
        self.dataList = []
        self.dataDict = {}

        for x in fileNames:
            pdDF = pd.read_excel(x, sheetname=self.sheetName)
            self.dataList.append(pdDF)
            baseFileName = ntpath.basename(x)

            baseFileName = baseFileName[:4]
            self.dataDict[baseFileName] = pdDF

        self.data = pd.concat(self.dataList, ignore_index=True)



    #Pass Type: Gr 11 Graph Method
    def GenerateGraphPassTypeGr11(self, instituteList, filterType, data=None):
        graphData = self.data
        if data is not None:
            graphData = data
        passTypeValuesList = graphData['Pass Type: Gr 11'].replace(0, np.NaN).dropna().unique()
        instituteFilteredDF = {x: graphData[graphData[filterType] == x] for x in instituteList}
        passTypeByInstitute = {}
        for institute, df in instituteFilteredDF.items():
            passTypeByValue = {}
            for value in passTypeValuesList:
                passTypeByValue[value] = len(df[df['Pass Type: Gr 11'] == value])
            passTypeByInstitute[institute] = passTypeByValue
        return passTypeByInstitute
        reasons = []
        for x in list(CombineDic.values()):
            reasons += list(x.keys())
        reasons = list(set(reasons))
        di = {}
        for x in reasons:
            temp = {}
            for y in CombineDic.keys():
                if x in CombineDic[y]:
                    temp[y] = CombineDic[y][x]
            di[x] = temp
        return di

    #Pass Type Most Recent Graph Method
    def GenerateGraphPassTypeMostRecent(self, instituteList, filterType):

        termsList = [x for x in self.data.columns if 'Pass Type: Term' in x]
        recentTerm = max([int(str(x).replace('Pass Type: Term ', '')) for x in termsList])
        passTypeMostRecent = 'Pass Type: Term ' + str(recentTerm)
        passTypeValues = ['HC', 'Fail (Promoted)', 'Diploma', 'Bachelor']
        self.data[passTypeMostRecent] = pd.Series(
            [x for x in self.data[passTypeMostRecent].values.tolist() if x in passTypeValues])
        passTypeValuesList = self.data[passTypeMostRecent].replace(0, np.NaN).dropna().unique()

        instituteFilteredDF = {x: self.data[self.data[filterType] == x] for x in instituteList}
        passTypeByInstitute = {}
        for institute, df in instituteFilteredDF.items():
            passTypeByValue = {}
            for value in passTypeValuesList:
                passTypeByValue[value] = len(df[df[passTypeMostRecent] == value])
            passTypeByInstitute[institute] = passTypeByValue
        return passTypeByInstitute

    #Applied to Graph Methods
    def CreateApplicationDF(self, data=None):
        if data is None:
            data = self.data

        optionColumns = [x for x in data.columns if 'option' in x.lower()]
        statusColumns = [x for x in data.columns if 'status' in x.lower()]
        statusColumns = statusColumns[:len(optionColumns)]
        tsibaCols = [x for x in data.columns if 'tsiba' in x.lower()]
        statusColumns += tsibaCols

        filterOptionCol = ['Branch', 'School Attending'] + optionColumns

        df = data[filterOptionCol]
        dfStatus = data[statusColumns]
        df = df.replace(np.NaN, 'Missing')
        dfStatus = dfStatus.replace(np.NaN, 'Missing')
        df.replace(to_replace=0, value=np.NaN, inplace=True)
        dfStatus.replace(to_replace=0, value=np.NaN, inplace=True)
        statusList = dfStatus.values.tolist()
        finalStatus = []
        for x in statusList:
            finalStatus.append(self.StatusPriority(x))

        df['Final Status'] = pd.Series(finalStatus)
        df.dropna(inplace=True)
        return df

    def StatusPriority(self, status):
        if 'Firm Offer' in status:
            return 'Firm Offer'
        elif 'Conditional Offer' in status:
            return 'Conditional Offer'
        elif 'Shortlisted' in status:
            return 'Shortlisted'
        elif 'Assessment' in status:
            return 'Assessment'
        elif 'Interview' in status:
            return 'Interview'
        elif 'Accepted' in status:
            return 'Accepted'
        elif 'Declined' in status:
            return 'Rejected'
        elif 'Applied' in status or 'Applied ' in status:
            return 'Applied'
        else:
            return 'Missing'

    def GenerateGraphAppliedTo(self, instituteList, filterType, data=None):

        graphData = self.data
        if data is not None:
            graphData = data

        dfTemp = self.CreateApplicationDF(graphData)
        optionColumns = [x for x in dfTemp.columns if 'option' in x.lower()]
        appliedTo_Final = dfTemp[optionColumns]
        count = pd.Series(appliedTo_Final.squeeze().values.ravel()).value_counts()
        appliedToCountDF = pd.DataFrame({'Measure': count.index, 'Count': count.values})
        appliedToValuesList = appliedToCountDF['Measure'].values.tolist()

        instituteFilteredDF = {x: dfTemp[dfTemp[filterType] == x] for x in instituteList}
        appliedToByInstitute = {}

        for institute, df in instituteFilteredDF.items():
            appliedTempValue = {}
            for value in appliedToValuesList:
                appliedTempOption = {}
                for option in optionColumns:
                    appliedTempOption[option] = len(df[df[option] == value])

                sum1 = sum(list(appliedTempOption.values()))
                if sum1 > 0:
                    appliedTempValue[value] = round((float(sum1) / float(len(graphData))) * 100, 2)
            appliedToByInstitute[institute] = appliedTempValue
        return appliedToByInstitute

    #Applied Status Graph Method
    def GenerateAppliedStatusGraph(self, instituteList, filterType):
        appliedTo_and_Status_Final = self.CreateApplicationDF()
        instituteFilteredDF = {x: appliedTo_and_Status_Final[appliedTo_and_Status_Final[filterType] == x]
                               for x in instituteList}
        appliedStatusValues = appliedTo_and_Status_Final['Final Status'].unique()
        statusByInstitute = {}
        for institute, df in instituteFilteredDF.items():
            statusByValues = {}
            for value in appliedStatusValues:
                statusByValues[value] = len(df[df['Final Status'] == value])
            statusByInstitute[institute] = statusByValues
        return statusByInstitute

    #Funding Application Graph Method
    def GenerateFundigAppGraph(self, instituteList, filterType):
        data = self.data[['Branch', 'School Attending', 'NSFAS', 'Studietrust', 'HCI', 'Other applications', 'Moshal Scholarship']]
        instituteFilteredDF = {x: data[data[filterType] == x]
                               for x in instituteList}
        fundingInstitutes = ['NSFAS', 'Studietrust', 'HCI', 'Moshal Scholarship']
        fundingInstitutesOther = list(data['Other applications'].replace(0, 'Missing').dropna().unique())

        fundingApplicationByInst = {}
        for institute, df in instituteFilteredDF.items():
            fiRatio = {}
            for fi in fundingInstitutes:
                tempDF = df[[filterType, fi]]
                tempDF = tempDF.replace(0, 'Missing')
                fiRatio[fi] = len(tempDF[tempDF[fi] != 'Missing'])

            for fi in fundingInstitutesOther:
                tempDF = df[df['Other applications'] == fi]
                fiRatio[fi] = len(tempDF[tempDF['Other applications'] != 'Missing'])
            fundingApplicationByInst[institute] = fiRatio

        return fundingApplicationByInst

    #Funding Application Status Graph Methods
    def CreateFundingDF(self):
        df = self.data[['Branch', 'School Attending']]
        dfStatus = self.data[['NSFAS', 'Studietrust', 'HCI', 'Status.3', 'Moshal Scholarship']]
        df = df.dropna()
        # dfStatus = dfStatus.dropna()
        df = df.replace(to_replace=0, value=np.NaN)
        dfStatus = dfStatus.replace(to_replace=0, value=np.NaN)
        statusList = dfStatus.values.tolist()
        finalStatus = []
        for x in statusList:
            finalStatus.append(self.StatusPriority(x))

        df['Final Status'] = pd.Series(finalStatus)
        df = df.dropna()
        return df


    def GenerateFundingStatusGraph(self, instituteList, filterType):
        fundingDF = self.CreateFundingDF()
        instituteFilteredDF = {x: fundingDF[fundingDF[filterType] == x]
                               for x in instituteList}
        statusValues = fundingDF['Final Status'].unique()

        statusByInstitute = {}
        for institute, df in instituteFilteredDF.items():
            statusByValue = {}
            for value in statusValues:
                statusByValue[value] = len(df[df['Final Status'] == value])
            statusByInstitute[institute] = statusByValue
        return statusByInstitute

    #Final Results Gr 12 Graph
    def GenerateFinaResultGr12Graph(self, instituteList, filterType, data=None):

        graphData = self.data
        if data is not None:
            graphData = data

        instituteFilteredDF = {x: graphData[graphData[filterType] == x]
                               for x in instituteList}
        passTypeValues = ['HC', 'Fail (Promoted)', 'Diploma', 'Bachelor']

        resultByInstitute = {}
        for institute, df in instituteFilteredDF.items():
            resultByPassType = {}
            for passType in passTypeValues:
                resultByPassType[passType] = len(df[df['Pass type'] == passType])
            resultByInstitute[institute] = resultByPassType
        return resultByInstitute

    #Placement Type Graph
    def GeneratePlacementTypeGraph(self, instituteList, filterType, data=None):

        graphData = self.data
        if data is not None:
            graphData = data

        instituteFilteredDF = {x: graphData[graphData[filterType] == x]
                               for x in instituteList}
        placementValues = list(graphData['Placement Type'].replace(0, 'Missing').dropna().unique())
        placementValues.remove('Missing')
        placementByInstitute = {}

        for institute, df in instituteFilteredDF.items():
            placementByValues = {}
            for value in placementValues:
                placementByValues[value] = len(df[df['Placement Type'] == value])
            placementByInstitute[institute] = placementByValues
        return placementByInstitute

    #Trend Graphs
    def GenerateTrendGraphPassTypeGr11(self, instituteList, filterType, yearFrom, yearTo):
        resultDict = {}
        for year, df in self.dataDict.items():
            if int(year) >= yearFrom and int(year) <= yearTo:
                resultDict[year] = dict(
                    list(self.GenerateGraphPassTypeGr11(data=df, filterType=filterType, instituteList=instituteList).values())[0])
        return resultDict

    def GenerateTrendGraphFinaResultGr12(self, instituteList, filterType, yearFrom, yearTo):
        resultDict = {}
        for year, df in self.dataDict.items():
            if int(year) >= yearFrom and int(year) <= yearTo:
                resultDict[year] = dict(
                    list(self.GenerateFinaResultGr12Graph(data=df, filterType=filterType, instituteList=instituteList).values())[0])
        return resultDict

    def GenerateTrendGraphAppliedTo(self, instituteList, filterType, yearFrom, yearTo):
        resultDict = {}
        for year, df in self.dataDict.items():
            if int(year) >= yearFrom and int(year) <= yearTo:
                resultDict[year] = dict(
                    list(self.GenerateGraphAppliedTo(data=df, filterType=filterType, instituteList=instituteList).values())[0])
        return resultDict

    def GenerateTrendGraphPlacementType(self, instituteList, filterType, yearFrom, yearTo):
        resultDict = {}
        for year, df in self.dataDict.items():
            if int(year) >= yearFrom and int(year) <= yearTo:
                resultDict[year] = dict(
                    list(self.GeneratePlacementTypeGraph(data=df, filterType=filterType, instituteList=instituteList).values())[0])
        return resultDict

# tGraph = TrackingGraphs(['2015.xlsx', '2016.xlsx', '2017.xlsx'])
# print(tGraph.GenerateGraphAppliedTo(['Makhaza', 'Nyanga'], 'Branch'))