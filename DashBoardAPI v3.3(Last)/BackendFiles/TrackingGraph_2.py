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
        filesList.sort()
        tempList = []

        for x in filesList:
            baseFileName = ntpath.basename(x)
            baseFileName = int(baseFileName[:4])
            tempList.append(baseFileName)
        tempList2 = []
        for x in range(tempList[0], tempList[-1] + 1):
            tempList2.append(str(x)+'.xlsx')
        filesList = tempList2
        fileNames = [self.homePath + x for x in filesList]
        self.dataList = []
        self.dataDict = OrderedDict()

        for x in fileNames:
            pdDF = pd.read_excel(x, sheetname=self.sheetName)
            pdDF['School Attending'] = [str(y).capitalize() for y in list(pdDF['School Attending'])]

            self.dataList.append(pdDF)
            baseFileName = ntpath.basename(x)

            baseFileName = baseFileName[:4]
            self.dataDict[baseFileName] = pdDF

        self.data = pd.concat(self.dataList, ignore_index=True)

    def GetSchools(self):
        branchList = list(self.data['School Attending'].unique())
        try:
            branchList.remove(np.nan)
        except:
            pass
        try:
            branchList.remove(np.NaN)
        except:
            pass
        try:
            branchList.remove("0")
        except:
            pass
        branchList.sort()
        return branchList

    def GetBranches(self):
        branchList = list(self.data['Branch'].unique())
        try:
            branchList.remove(np.nan)
        except:
            pass
        try:
            branchList.remove(np.NaN)
        except:
            pass
        branchList.sort()
        return branchList

    #Pass Type: Gr 11 Graph Method
    def GenerateGraphPassTypeGr11(self, instituteList, filterType, yearsList=None, data=None):
        if yearsList is not None:
            yearwiseData = []
            for year in yearsList:
                if year in self.dataDict:
                    yearwiseData.append(self.dataDict[year])
            graphData = pd.concat(yearwiseData, ignore_index=True)
        if data is not None:
            graphData = data
        graphData = graphData.replace(0, 'Missing').drop_duplicates()
        graphData = graphData.replace(np.NaN, 'Missing').drop_duplicates()
        graphData = graphData.replace(np.nan, 'Missing').drop_duplicates()
        passTypeValuesList = graphData['Pass Type: Gr 11'].replace(0, "Missing").dropna().unique()
        instituteFilteredDF = {x: graphData[graphData[filterType] == x] for x in instituteList}
        passTypeByInstitute = {}
        for institute, df in instituteFilteredDF.items():
            passTypeByValue = {}
            for value in passTypeValuesList:
                availableData = len(df[df['Pass Type: Gr 11'] == value])
                totalData = len(df)
                if totalData > 0:
                    passTypeByValue[value] = round((availableData / totalData) * 100, 2)

            passTypeByInstitute[institute] = passTypeByValue
        reasons = []
        for x in list(passTypeByInstitute.values()):
            reasons += list(x.keys())
        reasons = list(set(reasons))
        di = {}
        for x in reasons:
            temp = {}
            for y in passTypeByInstitute.keys():
                if x in passTypeByInstitute[y]:
                    temp[y] = passTypeByInstitute[y][x]
            di[x] = temp
        return di

    def GenerateGraphPassTypeGr11_copy(self, instituteList, filterType, yearsList=None, data=None):
        if yearsList is not None:
            yearwiseData = []
            for year in yearsList:
                if year in self.dataDict:
                    yearwiseData.append(self.dataDict[year])
            graphData = pd.concat(yearwiseData, ignore_index=True)
        if data is not None:
            graphData = data
        passTypeValuesList = graphData['Pass Type: Gr 11'].replace(0, np.NaN).dropna().unique()
        instituteFilteredDF = {x: graphData[graphData[filterType] == x] for x in instituteList}
        passTypeByInstitute = {}
        passTypeByValue = {}
        for institute, df in instituteFilteredDF.items():
            for value in passTypeValuesList:
                availableData = len(df[df['Pass Type: Gr 11'] == value])
                if value in passTypeByValue:
                    passTypeByValue[value] += availableData
                else:
                    passTypeByValue[value] = availableData
            # passTypeByInstitute[institute] = passTypeByValue
        # return passTypeByInstitute
        return passTypeByValue
    #Pass Type Most Recent Graph Method
    def GenerateGraphPassTypeMostRecent(self, instituteList, filterType, yearsList):

        yearwiseData = []
        for year in yearsList:
            if year in self.dataDict:
                yearwiseData.append(self.dataDict[year])
        graphData = pd.concat(yearwiseData, ignore_index=True)

        termsList = [x for x in graphData.columns if 'Pass Type: Term' in x]
        recentTerm = max([int(str(x).replace('Pass Type: Term ', '')) for x in termsList])
        passTypeMostRecent = 'Pass Type: Term ' + str(recentTerm)
        graphData = graphData.replace(0, 'Missing').drop_duplicates()
        graphData = graphData.replace(np.NaN, 'Missing').drop_duplicates()
        graphData = graphData.replace(np.nan, 'Missing').drop_duplicates()
        graphData[passTypeMostRecent] = graphData[passTypeMostRecent].replace(0, 'Missing')
        passTypeValues = ['HC', 'Fail (Promoted)', 'Diploma', 'Bachelor', 'Missing']
        temp = graphData[passTypeMostRecent].unique()
        graphData[passTypeMostRecent] = pd.Series([x for x in graphData[passTypeMostRecent].values.tolist() if x in passTypeValues])
        passTypeValuesList = graphData[passTypeMostRecent].replace(0, np.NaN).dropna().unique()

        instituteFilteredDF = {x: graphData[graphData[filterType] == x] for x in instituteList}
        passTypeByInstitute = {}
        for institute, df in instituteFilteredDF.items():
            passTypeByValue = {}
            for value in passTypeValuesList:
                availableData = len(df[df[passTypeMostRecent] == value])
                totalData = len(df)
                if totalData > 0:
                    passTypeByValue[value] = round((availableData / totalData) * 100)
            passTypeByInstitute[institute] = passTypeByValue

        reasons = []
        for x in list(passTypeByInstitute.values()):
            reasons += list(x.keys())
        reasons = list(set(reasons))
        di = {}
        for x in reasons:
            temp = {}
            for y in passTypeByInstitute.keys():
                if x in passTypeByInstitute[y]:
                    temp[y] = passTypeByInstitute[y][x]
            di[x] = temp
        return di

    #Applied to Graph Methods
    def CreateApplicationDF_2(self, data=None):
        if data is None:
            data = self.data

        colNames = list(data.columns.values)

        df = data[['Branch', 'School Attending', 'Option 1', 'Option 2', 'Option 3']]
        dfStatus = data[['Status', 'Status.1', 'Status.2', 'TSiBA Applications']]
        df = df.dropna()
        dfStatus = dfStatus.dropna()
        df.replace(to_replace=0, value='Missing', inplace=True)
        dfStatus.replace(to_replace=0, value='Missing', inplace=True)
        statusList = dfStatus.values.tolist()
        finalStatus = []
        for x in statusList:
            finalStatus.append(self.StatusPriority(x))

        df['Final Status'] = pd.Series(finalStatus)
        df.dropna(inplace=True)
        return df


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




    def GenerateGraphAppliedTo(self, instituteList, filterType, yearsList=None, data=None):

        if yearsList is not None:
            yearwiseData = []
            for year in yearsList:
                if year in self.dataDict:
                    yearwiseData.append(self.dataDict[year])
            graphData = pd.concat(yearwiseData, ignore_index=True)
        if data is not None:
            graphData = data
        graphData = graphData.replace(0, 'Missing').drop_duplicates()
        graphData = graphData.replace(np.NaN, 'Missing').drop_duplicates()
        graphData = graphData.replace(np.nan, 'Missing').drop_duplicates()

        dfTemp = self.CreateApplicationDF(graphData)#[['Option 1', 'Option 2', 'Option 3']]
        optionColumns = [x for x in dfTemp.columns if 'option' in x.lower()]
        appliedTo_Final = dfTemp[optionColumns]

        count = pd.Series(appliedTo_Final.squeeze().values.ravel()).value_counts()
        appliedToCountDF = pd.DataFrame({'Measure': count.index, 'Count': count.values})
        appliedToValuesList = appliedToCountDF['Measure'].values.tolist()

        instituteFilteredDF = {x: graphData[graphData[filterType] == x] for x in instituteList}
        appliedToByInstitute = {}
        # count = sum(appliedToCountDF['Count'].values.tolist())
        count2 = len(appliedTo_Final)


        for institute, df in instituteFilteredDF.items():
            appliedTempValue = {}
            for value in appliedToValuesList:
                appliedTempOption = {}
                for option in optionColumns:
                    appliedTempOption[option] = len(df[df[option] == value])

                sum1 = sum(list(appliedTempOption.values())) / (len(optionColumns))
                if sum1 > 0:
                    appliedTempValue[value] = round((float(sum1) / float(len(df))) * 100, 0)
            appliedToByInstitute[institute] = appliedTempValue

        reasons = []
        for x in list(appliedToByInstitute.values()):
            reasons += list(x.keys())
        reasons = list(set(reasons))
        di = {}
        for x in reasons:
            temp = {}
            for y in appliedToByInstitute.keys():
                if x in appliedToByInstitute[y]:
                    temp[y] = appliedToByInstitute[y][x]
            di[x] = temp
        return di

    def GenerateGraphAppliedTo_copy(self, instituteList, filterType, yearsList=None, data=None):
        if yearsList is not None:
            yearwiseData = []
            for year in yearsList:
                if year in self.dataDict:
                    yearwiseData.append(self.dataDict[year])
            graphData = pd.concat(yearwiseData, ignore_index=True)
        if data is not None:
            graphData = data
        graphData = graphData.replace(0, 'Missing').drop_duplicates()
        dfTemp = self.CreateApplicationDF(graphData)#[['Option 1', 'Option 2', 'Option 3']]
        optionColumns = [x for x in dfTemp.columns if 'option' in x.lower()]
        appliedTo_Final = dfTemp[optionColumns]
        count = pd.Series(appliedTo_Final.squeeze().values.ravel()).value_counts()
        appliedToCountDF = pd.DataFrame({'Measure': count.index, 'Count': count.values})
        appliedToValuesList = appliedToCountDF['Measure'].values.tolist()

        instituteFilteredDF = {x: graphData[graphData[filterType] == x] for x in instituteList}
        appliedToByInstitute = {}
        appliedTempValue = {}

        for institute, df in instituteFilteredDF.items():
            for value in appliedToValuesList:
                appliedTempOption = {}
                for option in optionColumns:
                    appliedTempOption[option] = len(df[df[option] == value])

                sum1 = round(sum(list(appliedTempOption.values())) / len(optionColumns), 0)
                if sum1 > 0:
                    if value in appliedTempValue:
                        appliedTempValue[value] += sum1#round((float(sum1) / float(len(df))) * 100, 0)
                    else:
                        appliedTempValue[value] = sum1#round((float(sum1) / float(len(df))) * 100, 0)
        return appliedTempValue

    #Applied Status Graph Method
    def GenerateAppliedStatusGraph(self, instituteList, filterType, yearsList):

        yearwiseData = []
        for year in yearsList:
            if year in self.dataDict:
                yearwiseData.append(self.dataDict[year])
        graphData = pd.concat(yearwiseData, ignore_index=True)

        appliedTo_and_Status_Final = self.CreateApplicationDF(graphData)
        instituteFilteredDF = {x: appliedTo_and_Status_Final[appliedTo_and_Status_Final[filterType] == x]
                               for x in instituteList}
        appliedStatusValues = appliedTo_and_Status_Final['Final Status'].unique()
        statusByInstitute = {}

        for institute, df in instituteFilteredDF.items():
            statusByValues = {}
            for value in appliedStatusValues:
                valueLength = len(df[df['Final Status'] == value])
                totalLength = len(df['Final Status'])
                if float(totalLength) > 0:
                    statusByValues[value] = round((float(valueLength) / float(totalLength)) * 100,0)
                else:
                    statusByValues[value] = 0
            statusByInstitute[institute] = statusByValues

        reasons = []
        for x in list(statusByInstitute.values()):
            reasons += list(x.keys())
        reasons = list(set(reasons))
        di = {}
        for x in reasons:
            temp = {}
            for y in statusByInstitute.keys():
                if x in statusByInstitute[y]:
                    temp[y] = statusByInstitute[y][x]
            di[x] = temp
        return di

    #Funding Application Graph Method
    def GenerateFundigAppGraph(self, instituteList, filterType, yearsList):

        yearwiseData = []
        for year in yearsList:
            if year in self.dataDict:
                yearwiseData.append(self.dataDict[year])
        self.data = pd.concat(yearwiseData, ignore_index=True)

        data = self.data[['Branch', 'School Attending', 'NSFAS', 'Studietrust', 'HCI', 'Other applications', 'Moshal Scholarship']]
        data = data.replace(0, 'Missing').drop_duplicates()
        data = data.replace(np.NaN, 'Missing').drop_duplicates()
        data = data.replace(np.nan, 'Missing').drop_duplicates()
        data = data.replace(' ', 'Missing').drop_duplicates()
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
                totalDF = len(tempDF[fi])
                lenDF = len(tempDF[tempDF[fi] != 'Missing'])
                # totalDF = len(tempDF[fi])

                if lenDF > 0:
                    fiRatio[fi] = round((lenDF / totalDF) * 100, 0)

            for fi in fundingInstitutesOther:
                tempDF = df[df['Other applications'] == fi]
                lenDF = len(tempDF[tempDF['Other applications'] != 'Missing'])
                totalDF = len(df['Other applications'])

                if lenDF > 0:
                    fiRatio[fi] = round((lenDF / totalDF) * 100, 0)

            fundingApplicationByInst[institute] = fiRatio


        reasons = []
        for x in list(fundingApplicationByInst.values()):
            reasons += list(x.keys())
        reasons = list(set(reasons))
        di = {}
        for x in reasons:
            temp = {}
            for y in fundingApplicationByInst.keys():
                if x in fundingApplicationByInst[y]:
                    temp[y] = fundingApplicationByInst[y][x]
            di[x] = temp
        return di

    #Funding Application Status Graph Methods
    def CreateFundingDF(self, graphData = None):
        if graphData is None:
            graphData = self.data
        df = graphData[['Branch', 'School Attending']]
        dfStatus = graphData[['NSFAS', 'Studietrust', 'HCI', 'Moshal Scholarship', 'Funding Other Status']]
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

    def GenerateFundingStatusGraph(self, instituteList, filterType, yearsList):

        yearwiseData = []
        for year in yearsList:
            if year in self.dataDict:
                yearwiseData.append(self.dataDict[year])
        graphData = pd.concat(yearwiseData, ignore_index=True)

        fundingDF = self.CreateFundingDF(graphData)
        instituteFilteredDF = {x: fundingDF[fundingDF[filterType] == x]
                               for x in instituteList}
        statusValues = fundingDF['Final Status'].unique()

        statusByInstitute = {}
        for institute, df in instituteFilteredDF.items():
            statusByValue = {}
            for value in statusValues:
                finalStatus = len(df[df['Final Status'] == value])
                totalStatus = len(df['Final Status'])
                if totalStatus > 0:
                    statusByValue[value] = round((finalStatus / totalStatus) * 100, 0)
                else:
                    statusByValue[value] = 0

            statusByInstitute[institute] = statusByValue
        reasons = []
        for x in list(statusByInstitute.values()):
            reasons += list(x.keys())
        reasons = list(set(reasons))
        di = {}
        for x in reasons:
            temp = {}
            for y in statusByInstitute.keys():
                if x in statusByInstitute[y]:
                    temp[y] = statusByInstitute[y][x]
            di[x] = temp
        return di

    #Final Results Gr 12 Graph
    def GenerateFinaResultGr12Graph(self, instituteList, filterType, yearsList=None, data=None):
        if yearsList is not None:
            yearwiseData = []
            for year in yearsList:
                if year in self.dataDict:
                    yearwiseData.append(self.dataDict[year])
            graphData = pd.concat(yearwiseData, ignore_index=True)

        if data is not None:
            graphData = data
        graphData = graphData.replace(0, 'Missing').drop_duplicates()
        instituteFilteredDF = {x: graphData[graphData[filterType] == x]
                               for x in instituteList}
        passTypeValues = ['HC', 'Fail (Promoted)', 'Diploma', 'Bachelor', 'Missing']

        resultByInstitute = {}
        for institute, df in instituteFilteredDF.items():
            resultByPassType = {}
            for passType in passTypeValues:
                passTypeLength = len(df[df['Pass type'] == passType])
                totalLength = len(df['Pass type'])
                if totalLength > 0:
                    resultByPassType[passType] = round((passTypeLength / totalLength) * 100, 0)
                else:
                    resultByPassType[passType] = 0

            resultByInstitute[institute] = resultByPassType
        reasons = []
        for x in list(resultByInstitute.values()):
            reasons += list(x.keys())
        reasons = list(set(reasons))
        di = {}
        for x in reasons:
            temp = {}
            for y in resultByInstitute.keys():
                if x in resultByInstitute[y]:
                    temp[y] = resultByInstitute[y][x]
            di[x] = temp
        return di

    def GenerateFinaResultGr12Graph_copy(self, instituteList, filterType, yearsList=None, data=None):
        if yearsList is not None:
            yearwiseData = []
            for year in yearsList:
                if year in self.dataDict:
                    yearwiseData.append(self.dataDict[year])
            graphData = pd.concat(yearwiseData, ignore_index=True)

        if data is not None:
            graphData = data
        graphData = graphData.replace(0, 'Missing').drop_duplicates()
        instituteFilteredDF = {x: graphData[graphData[filterType] == x]
                               for x in instituteList}
        passTypeValues = ['HC', 'Fail (Promoted)', 'Diploma', 'Bachelor', 'Missing']
        passTypeValues = list(graphData['Pass type'].unique())
        resultByInstitute = {}
        resultByPassType = {}

        for institute, df in instituteFilteredDF.items():
            for passType in passTypeValues:
                availableData = len(df[df['Pass type'] == passType])
                if passType in resultByPassType:
                    resultByPassType[passType] += availableData
                else:
                    resultByPassType[passType] = availableData
            #resultByInstitute[institute] = resultByPassType
        #return resultByInstitute
        return resultByPassType

    #Placement Type Graph
    def GeneratePlacementTypeGraph(self, instituteList, filterType, yearsList=None, data=None):
        if yearsList is not None:
            yearwiseData = []
            for year in yearsList:
                if year in self.dataDict:
                    yearwiseData.append(self.dataDict[year])
            graphData = pd.concat(yearwiseData, ignore_index=True)

        if data is not None:
            graphData = data
        graphData = graphData.replace(0, 'Missing').drop_duplicates()
        instituteFilteredDF = {x: graphData[graphData[filterType] == x]
                               for x in instituteList}
        placementValues = list(graphData['Placement Type'].replace(0, 'Missing').dropna().unique())
        #placementValues.remove('Missing')
        placementByInstitute = {}

        for institute, df in instituteFilteredDF.items():
            placementByValues = {}
            for value in placementValues:
                totalLength = len(df['Placement Type'])
                givenLength = len(df[df['Placement Type'] == value])

                if totalLength > 0:
                    placementByValues[value] = round((givenLength / totalLength) * 100, 0)
                else:
                    placementByValues[value] = 0
            placementByInstitute[institute] = placementByValues
        reasons = []
        for x in list(placementByInstitute.values()):
            reasons += list(x.keys())
        reasons = list(set(reasons))
        di = {}
        for x in reasons:
            temp = {}
            for y in placementByInstitute.keys():
                if x in placementByInstitute[y]:
                    temp[y] = placementByInstitute[y][x]
            di[x] = temp
        return di

    def GeneratePlacementTypeGraph_copy(self, instituteList, filterType, yearsList=None, data=None):
        if yearsList is not None:
            yearwiseData = []
            for year in yearsList:
                if year in self.dataDict:
                    yearwiseData.append(self.dataDict[year])
            graphData = pd.concat(yearwiseData, ignore_index=True)

        if data is not None:
            graphData = data
        graphData = graphData.replace(0, 'Missing').drop_duplicates()
        graphData = graphData.replace(np.nan, 'Missing').drop_duplicates()
        graphData = graphData.replace(np.NaN, 'Missing').drop_duplicates()
        instituteFilteredDF = {x: graphData[graphData[filterType] == x]
                               for x in instituteList}
        placementValues = list(graphData['Placement Type'].replace(0, 'Missing').dropna().unique())
        #placementValues.remove('Missing')
        placementByInstitute = {}

        placementByValues = {}
        for institute, df in instituteFilteredDF.items():
            for value in placementValues:
                availableData = len(df[df['Placement Type'] == value])
                if value in placementByValues:
                    placementByValues[value] += availableData
                else:
                    placementByValues[value] = availableData
            placementByInstitute[institute] = placementByValues
        return placementByValues

    #Trend Graphs
    def GenerateTrendGraphPassTypeGr11(self, instituteList, filterType, yearFrom, yearTo):
        resultDict = OrderedDict()
        for year, df in self.dataDict.items():
            if int(year) >= yearFrom and int(year) <= yearTo:
                resultDict[year] = self.GenerateGraphPassTypeGr11_copy(data=df, filterType=filterType, instituteList=instituteList)


        reasons = []
        for x in list(resultDict.values()):
            reasons += list(x.keys())
        reasons = list(set(reasons))
        di = OrderedDict()
        for x in reasons:
            temp = OrderedDict()
            for y in resultDict.keys():
                if x in resultDict[y]:
                    temp[y] = resultDict[y][x]
            di[str(x)] = temp
        return di

    def GenerateTrendGraphFinaResultGr12(self, instituteList, filterType, yearFrom, yearTo):
        resultDict = OrderedDict()
        for year, df in self.dataDict.items():
            if int(year) >= yearFrom and int(year) <= yearTo:
                temp = self.GenerateFinaResultGr12Graph_copy(data=df, filterType=filterType, instituteList=instituteList)
                resultDict[year] = temp


                # resultDict[year] = dict(
                #     list(self.GenerateFinaResultGr12Graph_copy(data=df, filterType=filterType, instituteList=instituteList).values())[0])


        reasons = []
        for x in list(resultDict.values()):
            reasons += list(x.keys())
        reasons = list(set(reasons))
        di = OrderedDict()
        for x in reasons:
            temp = OrderedDict()
            for y in resultDict.keys():
                if x in resultDict[y]:
                    temp[y] = resultDict[y][x]
            di[x] = temp
        return di

    def GenerateTrendGraphAppliedTo(self, instituteList, filterType, yearFrom, yearTo):
        resultDict = OrderedDict()
        for year, df in self.dataDict.items():
            if int(year) >= yearFrom and int(year) <= yearTo:
                resultDict[year] = self.GenerateGraphAppliedTo_copy(data=df, filterType=filterType,
                                                               instituteList=instituteList)
        reasons = []
        for x in list(resultDict.values()):
            reasons += list(x.keys())
        reasons = list(set(reasons))
        di = OrderedDict()
        for x in reasons:
            temp = OrderedDict()
            for y in resultDict.keys():
                if x in resultDict[y]:
                    temp[y] = resultDict[y][x]
            di[x] = temp
        return di

    def GenerateTrendGraphPlacementType(self, instituteList, filterType, yearFrom, yearTo):

        resultDict = OrderedDict()
        for year, df in self.dataDict.items():
            if int(year) >= yearFrom and int(year) <= yearTo:
                resultDict[year] = self.GeneratePlacementTypeGraph_copy(data=df, filterType=filterType, instituteList=instituteList)

        reasons = []
        for x in list(resultDict.values()):
            reasons += list(x.keys())
        reasons = list(set(reasons))
        di = OrderedDict()
        for x in reasons:
            temp = OrderedDict()
            for y in resultDict.keys():
                if x in resultDict[y]:
                    temp[y] = resultDict[y][x]
            di[x] = temp
        return di

    def GetNumberOfStdAppliedNoWhere(self, instituteList, filterType, yearsList=None, data=None):
        if yearsList is not None:
            yearwiseData = []
            for year in yearsList:
                if year in self.dataDict:
                    yearwiseData.append(self.dataDict[year])
            graphData = pd.concat(yearwiseData, ignore_index=True)
        if data is not None:
            graphData = data
        graphData = graphData.replace(0, 'Missing').drop_duplicates()
        graphData = graphData.replace(np.NaN, 'Missing')
        graphData = graphData.replace(np.nan, 'Missing')

        dfTemp = self.CreateApplicationDF(graphData)#[['Option 1', 'Option 2', 'Option 3']]
        optionColumns = [x for x in dfTemp.columns if 'option' in x.lower()]
        instituteFilteredDF = {x: graphData[graphData[filterType] == x] for x in instituteList}
        appliedNoWByInst = {}
        for institute, df in instituteFilteredDF.items():
            df2 = df[optionColumns]
            appliedNoWByInst[institute] = len(df2[df2.apply(lambda x: len(set(x)) == 1 and x == 'Missing', 1)].dropna())
        return appliedNoWByInst

    def AvgNumberOfAppPerStd(self, instituteList, filterType, yearsList=None, data=None):
        if yearsList is not None:
            yearwiseData = []
            for year in yearsList:
                if year in self.dataDict:
                    yearwiseData.append(self.dataDict[year])
            graphData = pd.concat(yearwiseData, ignore_index=True)
        if data is not None:
            graphData = data
        graphData = graphData.replace(0, 'Missing').drop_duplicates()
        graphData = graphData.replace(np.NaN, 'Missing')
        graphData = graphData.replace(np.nan, 'Missing')

        dfTemp = self.CreateApplicationDF(graphData)#[['Option 1', 'Option 2', 'Option 3']]
        optionColumns = [x for x in dfTemp.columns if 'option' in x.lower()]
        instituteFilteredDF = {x: graphData[graphData[filterType] == x] for x in instituteList}
        avgAppInst = {}

        for institute, df in instituteFilteredDF.items():
            if len(df) > 0:
                df.to_csv('test.csv', header=1)
                df2 = pd.read_csv('test.csv', header=0)
                df2 = df2[optionColumns]
                df3 = df2.transpose()
                missing_count = list(df3.applymap(lambda x: str.count(x, 'Missing')).sum())
                len(df.columns)
                appPerStd = []
                for x in missing_count:
                    appPerStd.append(len(df2.columns) - x)
                avg_app = round(sum(appPerStd) / len(appPerStd), 2)
                avgAppInst[institute] = avg_app
            else:
                avgAppInst[institute] = 0
        return avgAppInst
#
tg = TrackingGraphs(['2016.xlsx'])
branches = tg.GetBranches()
print(tg.GenerateFundingStatusGraph(branches, 'Branch', ['2016']))
# print(tg.GenerateTrendGraphPlacementType(branches, 'Branch', 2015,2015))