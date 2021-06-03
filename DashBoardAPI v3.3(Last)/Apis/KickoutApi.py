from Depend import *
from BackendFiles.KickoutGraph import KickOutGraph
from Commons import *

global kickoutOBJ
kickoutOBJ = KickOutGraph()
class KickoutApi(Resource):

    def __init__(self):
        self.KickObj  = globals()['kickoutOBJ']

    def post(self):
        data = json.loads(request.data.decode())
        instituteList = data['branches']



        filterType = data['filtertype']

        if filterType == 'Branch':
            instituteList = ConvertName(instituteList)

        flag = data['flag']
        #{"branches":["Makhaza"],"filtertype":"Branch","datefrom":"2017-07-24","dateto":"2017-09-29", "flag":1}
        if flag == 1:
            return self.KickObj.GenerateGraph(instituteList,filterType,data["datefrom"],data["dateto"])
        elif flag == 2:
            # instituteList = ConvertName(instituteList)
            return self.KickObj.GetLatestDatesBranchWise(data['datefrom'], data['dateto'], instituteList, filterType)
        else:#{"branches":["Makhaza"],"filtertype":"Branch","datefrom":"2017-07-24","dateto":"2017-09-29", "flag":2}
            return self.KickObj.GenerateAllBranch(data["datefrom"], data["dateto"])



