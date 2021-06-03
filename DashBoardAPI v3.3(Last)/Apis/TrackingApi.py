from Depend import *
from BackendFiles.TrackingGraph_2 import TrackingGraphs


class TrackingApi(Resource):

    def post(self):
        data = json.loads(request.data.decode())
        self.TrackObj = TrackingGraphs(data["filesList"])
        Institute_List = data["instituteList"]
        Filter_Type = data["filterType"]
        # Pass Type: Gr 11 Graph Method
        if data["flag"] == 1: # {"filesList":["2016.xlsx", "2017.xlsx"],"instituteList":["Makhaza","Nyanga"],"filterType":"Branch", "flag":1,"yearslist":["2016"]}
            return self.TrackObj.GenerateGraphPassTypeGr11(Institute_List,Filter_Type,data["yearslist"])

        # Pass Type Most Recent Graph Method
        elif data["flag"] == 2:
            return self.TrackObj.GenerateGraphPassTypeMostRecent(Institute_List,Filter_Type,data["yearslist"])

        # Applied to Graph Methods
        elif data["flag"] == 3:
            return self.TrackObj.GenerateGraphAppliedTo(Institute_List,Filter_Type,data["yearslist"])

        # Applied Status Graph Method
        elif data["flag"] == 4:
            return self.TrackObj.GenerateAppliedStatusGraph(Institute_List,Filter_Type,data["yearslist"])

        # Funding Application Graph Method
        elif data["flag"] == 5:
            return self.TrackObj.GenerateFundigAppGraph(Institute_List,Filter_Type,data["yearslist"])

        # Funding Application Status Graph Methods
        elif data["flag"] == 6:
            return self.TrackObj.GenerateFundingStatusGraph(Institute_List,Filter_Type,data["yearslist"])

        # Final Results Gr 12 Graph
        elif data["flag"] == 7:
            return self.TrackObj.GenerateFinaResultGr12Graph(Institute_List,Filter_Type,data["yearslist"])

        # Placement Type Graph
        elif data["flag"] == 8:
            return self.TrackObj.GeneratePlacementTypeGraph(Institute_List,Filter_Type,data["yearslist"])

        # Trend Graphs
        elif data["flag"] == 9:  # {"filesList":["2016.xlsx", "2017.xlsx"],"instituteList":["Makhaza","Nyanga"],"filterType":"Branch", "flag":9,"YearFrom":2015,"YearTo":2017}
            return self.TrackObj.GenerateTrendGraphPassTypeGr11(Institute_List,Filter_Type,data["YearFrom"],data["YearTo"])
        elif data["flag"] == 10:
            return self.TrackObj.GenerateTrendGraphFinaResultGr12(Institute_List,Filter_Type,data["YearFrom"],data["YearTo"])
        elif data["flag"] == 11:
            return self.TrackObj.GenerateTrendGraphAppliedTo(Institute_List,Filter_Type,data["YearFrom"],data["YearTo"])
        elif data["flag"] == 12:
            return self.TrackObj.GenerateTrendGraphPlacementType(Institute_List,Filter_Type,data["YearFrom"],data["YearTo"])
        elif data["flag"] == 13:
            return self.TrackObj.GetSchools()
        elif data["flag"] == 14:
            return self.TrackObj.GetNumberOfStdAppliedNoWhere(Institute_List, Filter_Type, data["yearslist"])
        elif data["flag"] == 15:
            return self.TrackObj.AvgNumberOfAppPerStd(Institute_List, Filter_Type, data["yearslist"])
        elif data["flag"] == 16:
            return self.TrackObj.GetBranches()


















