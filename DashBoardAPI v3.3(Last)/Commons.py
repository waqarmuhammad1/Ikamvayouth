import numpy as np
from dateutil.parser import parse
import pandas as pd
from datetime import datetime as dt
from collections import OrderedDict

filePath = "/home/codexnow/Desktop/DataFiles_9jan/"
dic = {"Makhaza":"MAK", "Nyanga":"NYA", "Masiphumelele":"MAS", "Chesterville":"CHE", "Umlazi":"UML", "Ebony Park":"EBO", "Ivory Park":"IVO",
     "Mamelodi":"MAM", "Ikageng":"IKA", "Joza":"JOZ", "Mahikeng":"MAH", "Gugs Comp & Yebo":"GUG", "Kuyasa":"KUY", "Atlantis":"ATL", "ID Mkize":"IDM", "Leiden":"LEI",
     "Diepsloot":"DIP"}

def GetDateFrom(dateFrom):

    if is_date(dateFrom) == True:
        date = np.datetime64(dateFrom)
        return date
    else:
        term = dateFrom.split('|')[0]
        year = dateFrom.split('|')[1]
        date = GetDateByTermLowerBound(int(term), int(year))
        return date

def GetDateTo(dateTo):
    if is_date(dateTo) == True:
        date = np.datetime64(dateTo)
        return date
    else:
        term = dateTo.split('|')[0]
        year = dateTo.split('|')[1]
        date = GetDateByTermUpperBound(int(term), int(year))
        return date

def GetDateByTermLowerBound(termFrom, termYearFrom):
    termDates = pd.read_csv(filePath + 'TermDates.csv', header=0)
    termDates.StartDate = pd.Series([dt.strptime(str(x).split('T')[0], "%Y-%m-%d").date()
                                     for x in list(termDates['StartDate'])], index=termDates.index)

    termDates.EndDate = pd.Series([dt.strptime(str(x).split('T')[0], "%Y-%m-%d").date()
                                   for x in list(termDates['EndDate'])], index=termDates.index)
    termDates = termDates[(termDates['Term'] == int(termFrom)) & (termDates['TermYear'] == int(termYearFrom))]
    lowerDate = list(termDates.StartDate)[0]
    return np.datetime64(lowerDate)

def GetDateByTermUpperBound(termTo, termYearTo):
    termDates = pd.read_csv(filePath + 'TermDates.csv', header=0)
    termDates.StartDate = pd.Series([dt.strptime(str(x).split('T')[0], "%Y-%m-%d").date()
                                     for x in list(termDates['StartDate'])], index=termDates.index)

    termDates.EndDate = pd.Series([dt.strptime(str(x).split('T')[0], "%Y-%m-%d").date()
                                   for x in list(termDates['EndDate'])], index=termDates.index)
    termDates = termDates[(termDates['Term'] == int(termTo)) & (termDates['TermYear'] == int(termYearTo))]
    upperDate = list(termDates.EndDate)[0]
    return np.datetime64(upperDate)

def FilterDF(dateFrom, dateTo, dfToFilter):

    if is_date(dateFrom) == True:
        dfToFilter = FilterDFByDates(dateFrom, dateTo, dfToFilter)
    else:
        termFrom = int(dateFrom.split('|')[0])
        yearFrom = int(dateFrom.split('|')[1])

        termTo = int(dateTo.split('|')[0])
        yearTo = int(dateTo.split('|')[1])
        dfToFilter = FilterByTermYearTerm(int(termFrom), int(yearFrom), int(termTo), int(yearTo), dfToFilter)

    return dfToFilter

def FilterDFByDates(dateFrom, dateTo, dfToFilter):
    termDates = pd.read_csv(filePath+'TermDates.csv', header=0)

    termDates.StartDate = pd.Series([dt.strptime(str(x).split('T')[0], "%Y-%m-%d").date()
                                     for x in list(termDates['StartDate'])], index=termDates.index)

    termDates.EndDate = pd.Series([dt.strptime(str(x).split('T')[0], "%Y-%m-%d").date()
                                   for x in list(termDates['EndDate'])], index=termDates.index)
    # print(termDates.EndDate)
    termDates.StartDate = pd.to_datetime(termDates.StartDate)
    termDates.EndDate = pd.to_datetime(termDates.EndDate)

    temp = termDates[(termDates.StartDate >= dateFrom) | (termDates.EndDate >= dateFrom)]

    temp['Day_Diff'] = temp.EndDate - pd.to_datetime(dateTo)
    temp3 = temp[temp.Day_Diff >= pd.to_timedelta(0)]
    minDayDiff = min(list(temp3['Day_Diff']))

    temp3 = temp[temp['Day_Diff'] == (minDayDiff)]
    newDateTo = list(temp3.EndDate)[0]

    temp = temp[temp.EndDate <= newDateTo]

    termYears = temp['TermYear'].unique()
    li = {}
    for x in termYears:
        li[x] = list(temp[temp.TermYear == x]['Term'].unique())

    termYearFiltered = {year: dfToFilter[(dfToFilter.TermYear == year) &
                                       (dfToFilter.Term.isin(values))]
                        for year, values in li.items()}
    if len(termYearFiltered.values()) > 0:
        newDF = pd.concat(list(termYearFiltered.values()))
    else:
        newDF = termYearFiltered.values()
    return newDF

def FilterByTermYearTerm(termFrom, yearFrom, termTo, yearTo, dfToFilter):
    if yearFrom != yearTo:
        dfToFilter = dfToFilter[(dfToFilter['TermYear'] >= yearFrom) & (dfToFilter['TermYear'] <= yearTo)]
        lowerBound = dfToFilter[dfToFilter['TermYear'] == yearFrom]
        lowerBound = lowerBound[lowerBound['Term'] >= termFrom]
        midBound = dfToFilter[(dfToFilter['TermYear'] > yearFrom) & (dfToFilter['TermYear'] < yearTo)]
        upperBound = dfToFilter[(dfToFilter['TermYear'] == yearTo)]
        upperBound = upperBound[upperBound['Term'] <= termTo]
        dfToFilter = pd.concat([lowerBound, midBound, upperBound])
        return dfToFilter
    else:
        dfToFilter = dfToFilter[(dfToFilter['TermYear'] == yearFrom)]
        dfToFilter = dfToFilter[(dfToFilter['Term'] >= termFrom) & (dfToFilter['Term'] <= termTo)]
        return dfToFilter


def GetTermDates(termDic, termYear):
    termDates = pd.read_csv(filePath + 'TermDates.csv', header=0)

    dateDict = OrderedDict()

    termList = list(termDic.keys())
    termList.sort()
    for term in termList:
        endDate = str(list(termDates[(termDates.TermYear == int(termYear)) & (termDates.Term == int(term))]["EndDate"])[0])
        endDate = endDate.split('T')[0]

        dateDict[endDate] = termDic[term]

    return dateDict

def ConvertName(nameList):
    return [dic[x] for x in nameList]

def is_date(string):
    try:
        parse(string)
        return True
    except ValueError:
        return False
