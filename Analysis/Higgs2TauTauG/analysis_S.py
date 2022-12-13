import awkward as ak, coffea, copy
from coffea import hist, analysis_tools
from modules.selection import *
import modules.ExpressoTools as ET
import modules.objects as obj
from coffea.analysis_tools import PackedSelection
import numpy.ma as ma
import numpy as np
from modules.hcoll import binning

histograms = {
    'TauPt_leading':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('TauPt_leading', 'Tau_leadint_pt(GeV)', binning(0,100,10))), 
    'Taueta_leading':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('Taueta_leading', 'Tau_leading_eta', binning(-4,4,1))),
    'Tauphi_leading':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('Tauphi_leading', 'Tau_leading_phi', binning(-4,4,1))),
    'TauPt_subleading':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('TauPt_subleading', 'Tau_subleading_pt(GeV)', binning(0,100,10))), 
    'Taueta_subleading':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('Taueta_subleading', 'Tau_subleading_eta', binning(-4,4,1))),
    'Tauphi_subleading':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('Tauphi_subleading', 'Tau_subleading_phi', binning(-4,4,1))),
    'drgt_V1':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('drgt_V1', 'drgt', binning(0,4,0.1))),
    'drgt_V2':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('drgt_V2', 'drgt', binning(0,1,0.1))),
    'drgt_V3':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('drgt_V3', 'drgt', binning(0,10,0.1))),

    'drtt_V1':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('drtt_V1', 'drtt', binning(0,4,0.1))),
    'drtt_V2':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('drtt_V2', 'drtt', binning(0,1,0.1))),
    'drtt_V3':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('drtt_V3', 'drtt', binning(0,10,0.1))),

    'dphitt':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('dphitt', 'dphitt', binning(-4,4,0.1))),

    'ttobjectmass':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('ttobjectmass', 'invarmasstt', binning(60,150,1))),
    'ttgobjectmass':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('ttgobjectmass', 'invarmassttg', binning(60,150,1))),
    'PhotonPt':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('PhotonPt', 'photon pt(GeV)', binning(4,50,1))),
    'Photoneta':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('Photoneta', 'photon eta', binning(-4,4,1))),
    'Photonphi':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('Photonphi', 'photon phi', binning(-4,4,1))),
}
def myanalysis(pars,logger, h, ev, doweight=True):
    dataset,isData,histAxisName,year=pars['dataset'],pars['isData'],pars['histAxisName'],pars['year']
    xsec,sow,pass_options=pars['xsec'],pars['sow'],pars['passoptions']
    from modules.hcoll import hcoll,binning
    hists = hcoll(h, isData, xsec, sow, doweight, process=histAxisName)
    ET.autolog(f"{len(ev)} Events at the start of your analysis", logger, 'i')
    # Start your analysis``
    #-------------------------------------------------------------------------------------------------------
    # Create any needed branches
    #-------------------------------------------------------------------------------------------------------
    # Define pass options
    #-------------------------------------------------------------------------------------------------------
    # For MC
    if not isData:
         if pass_options=='Xsecweight':
            genw = ev["genWeight"]
            ev["weight_norm"] = (xsec / sow) * genw
         else:
            ev["weight_norm"]=1
    
   
    
    #-------------------------------------------------------------------------------------------------------
    # Masks
    #-------------------------------------------------------------------------------------------------------
    #Dilepton events
    #-------------------------------------------------------------------------------------------------------
    #Special masks
    #-------------------------------------------------------------------------------------------------------
    # Fill histograms
    # plots=["pt","eta","phi"]
    # names=[]
    # objects=[ev.propertau[:,0],]

    # for ob in objects:
    #     for name,plot in zip(names,plots):


    hists.fill('TauPt_leading',ev.weight_norm, (ev.drgt >=0), ev.propertau[:,0], TauPt_leading='pt')
    hists.fill('Taueta_leading',ev.weight_norm, (ev.drgt >= 0), ev.propertau[:,0], Taueta_leading='eta')
    hists.fill('Tauphi_leading',ev.weight_norm, (ev.drgt >= 0), ev.propertau[:,0], Tauphi_leading='phi')

    hists.fill('TauPt_subleading',ev.weight_norm, (ev.drgt >= 0), ev.propertau[:,1], TauPt_subleading='pt')
    hists.fill('Taueta_subleading',ev.weight_norm, (ev.drgt >= 0), ev.propertau[:,1], Taueta_subleading='eta')
    hists.fill('Tauphi_subleading',ev.weight_norm, (ev.drgt >= 0), ev.propertau[:,1], Tauphi_subleading='phi')

    hists.fill('PhotonPt',ev.weight_norm, (ev.drgt >= 0), ev.properphotons[:,0], PhotonPt='pt')
    hists.fill('Photoneta',ev.weight_norm, (ev.drgt >= 0), ev.properphotons[:,0], Photoneta='eta')
    hists.fill('Photonphi',ev.weight_norm, (ev.drgt >= 0), ev.properphotons[:,0], Photonphi='phi')
    hists.fill('drgt_V1',ev.weight_norm, (ev.drgt >= 0), ev, drgt_V1='drgt')
    hists.fill('drgt_V2',ev.weight_norm, (ev.drgt >= 0), ev, drgt_V2='drgt')
    hists.fill('drgt_V3',ev.weight_norm, (ev.drgt >= 0), ev, drgt_V3='drgt')
    hists.fill('drtt_V1',ev.weight_norm, (ev.drgt >= 0), ev, drtt_V1='drtt')
    hists.fill('drtt_V2',ev.weight_norm, (ev.drgt >= 0), ev, drtt_V2='drtt')
    hists.fill('drtt_V3',ev.weight_norm, (ev.drgt >= 0), ev, drtt_V3='drtt')

    hists.fill('dphitt',ev.weight_norm, (ev.drgt >= 0), ev, dphitt='dphitt')
    
    hists.fill('ttobjectmass',ev.weight_norm, (ev.drgt >= 0), ev, ttobjectmass='ttobjectmass')
    hists.fill('ttgobjectmass',ev.weight_norm, (ev.drgt >= 0), ev, ttgobjectmass='ttgobjectmass')
    #-------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------
    #End your analysis
    #-------------------------------------------------------------------------------------------------------
    ET.autolog(f"{len(ev)} Events at the end of your analysis", logger, 'i')
    return hists.get()

