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

    selections.add("atleast 1tau,1lep,1pho (out of the box)",(ak.num(events.Tau)>=1) & (ak.num(events.Photon)>=1) & ak.num(events.l)>=1)

    
    if 'tight_tau' in analysispoint:
        selections.add("tight tau", ak.num(events.Tau[events.Tau.istight])== 1)
    if 'med_tau' in analysispoint:
        selections.add("med tau", ak.num(events.Tau[events.Tau.ismed])== 1)
    if 'loose_tau' in analysispoint:
        selections.add("loose tau", ak.num(events.Tau[events.Tau.isloose])== 1)

    if 'tight_l' in analysispoint:
        selections.add("tight l", ak.num(events.l[events.l.istight])== 1)
    if 'med_l' in analysispoint:
        selections.add("med l", ak.num(events.l[events.l.ismed])== 1)
    if 'loose_l' in analysispoint:
        selections.add("loose l", ak.num(events.l[events.l.isloose])== 1)
    
    if 'tight_pho' in analysispoint:
        selections.add("tight photon", ak.num(events.Photon[events.Photon.istight])== 1)
    if 'med_pho' in analysispoint:
        selections.add("med photon", ak.num(events.Photon[events.Photon.ismed])== 1)
    if 'loose_pho' in analysispoint:
        selections.add("loose photon", ak.num(events.Photon[events.Photon.isloose])== 1)

    if histAxisName=="H2TTTG":
        selections.add("should be ttg events at gen level", ak.num(events.photonswithcut)==1)
    if histAxisName=="H2TTT":
        selections.add("should not be ttg events at gen level", ak.num(events.photonswithcut)==0)

    #selections.add("delta R between electron and tau should larger than 0.4", events.drlt > 0.4)
    #selections.add("charge shoule be oppsite for electron and tau", events.chargelt == -1)
    #selections.add("Invarmass for e-tau should less than 60GeV", events.invarmass < 60)
    #selections.add("delta R between photon and electron should larger than 0.4", events.drlg > 0.4)

    

    return events,selections


