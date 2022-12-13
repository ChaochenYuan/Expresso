import awkward as ak
from modules.paths import IHEP_path,golden_json_path
from coffea.lumi_tools import LumiMask

def preselection(pars,events,selections):
    #-----------Add your pre selection here----------------------#
    year,isData,analysispoint=pars['year'],pars['isData'],pars['analysispoint']
    histAxisName=pars['histAxisName']
    if isData:
        lumi_mask = LumiMask(golden_json_path(year))(events.run,events.luminosityBlock)
        selections.add("is_good_lumi",lumi_mask)

    selections.add("delta R between electron and tau should larger than 0.0", events.drgt >= 0)

    return events,selections