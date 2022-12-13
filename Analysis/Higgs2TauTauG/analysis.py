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
    'ElectronPt':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('ElectronPt', 'electron pt(GeV)', binning(20,100,10))),
    'MuonPt':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('MuonPt', 'muon pt(GeV)', binning(20,100,10))),
    'TauPt_eh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('TauPt_eh', 'tau pt eh(GeV)', binning(30,100,10))),
    'TauPt_uh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('TauPt_uh', 'tau pt uh(GeV)', binning(30,100,10))),

    'Electroneta':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('Electroneta', 'electron eta', binning(-4,4,0.1))),
    'Muoneta':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('Muoneta', 'muon eta', binning(-4,4,0.1))),
    'Taueta_eh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('Taueta_eh', 'tau eta eh', binning(-4,4,0.1))),
    'Taueta_uh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('Taueta_uh', 'tau eta uh', binning(-4,4,0.1))),

    'Electronphi':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('Electronphi', 'electron phi', binning(-4,4,0.1))),
    'Muonphi':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('Muonphi', 'muon phi', binning(-4,4,0.1))),
    'Tauphi_eh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('Tauphi_eh', 'tau phi eh', binning(-4,4,0.1))),
    'Tauphi_uh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('Tauphi_uh', 'tau phi uh', binning(-4,4,0.1))),

    'drlt_eh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('drlt_eh', 'drlt eh', binning(0,4,0.1))),
    'drlt_uh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('drlt_uh', 'drlt uh', binning(0,4,0.1))),

    'drgt_eh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('drgt_eh', 'drgt eh', binning(0,4,0.1))),
    'drgt_uh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('drgt_uh', 'drgt uh', binning(0,4,0.1))),

    'drlg_eh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('drlg_eh', 'drlg eh', binning(0,4,0.1))),
    'drlg_uh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('drlg_uh', 'drlg uh', binning(0,4,0.1))),

    'dphilg_eh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('dphilg_eh', 'dphilg eh', binning(-4,4,0.1))),
    'dphilg_uh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('dphilg_uh', 'dphilg uh', binning(-4,4,0.1))),

    'dphilt_eh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('dphilt_eh', 'dphilt eh', binning(-4,4,0.1))),
    'dphilt_uh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('dphilt_uh', 'dphilt uh', binning(-4,4,0.1))),

    'dphigt_eh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('dphigt_eh', 'dphigt eh', binning(-4,4,0.1))),
    'dphigt_uh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('dphigt_uh', 'dphigt uh', binning(-4,4,0.1))),

    'invarmass_eh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('invarmass_eh', 'invarmasslt eh', binning(0,70,1))),
    'invarmass_uh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('invarmass_uh', 'invarmasslt uh', binning(0,70,1))),

    'MET':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('MET', '$MET$', binning(0,100,1))),

    'PhotonPt_eh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('PhotonPt_eh', 'Photon pt(GeV)', binning(4,50,1))),
    'Photoneta_eh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('Photoneta_eh', 'Photon eta eh', binning(-4,4,0.1))),
    'Photonphi_eh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('Photonphi_eh', 'Photon phi eh', binning(-4,4,0.1))),

    'PhotonPt_uh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('PhotonPt_uh', 'Photon pt uh(GeV)', binning(4,50,0.1))),
    'Photoneta_uh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('Photoneta_uh', 'Photon eta uh', binning(-4,4,0.1))),
    'Photonphi_uh':hist.Hist('Events',hist.Cat('process', 'process'),hist.Bin('Photonphi_uh', 'Photon phi uh', binning(-4,4,0.1)))
}


def myanalysis(pars,logger, h, ev, doweight=True):
    dataset,isData,histAxisName,year=pars['dataset'],pars['isData'],pars['histAxisName'],pars['year']
    xsec,sow,pass_options,analysis_point=pars['xsec'],pars['sow'],pars['passoptions'],pars['analysispoint']
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
         if 'Xsecweight' in pass_options:
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
    if 'tight_tau' in analysis_point: ev["mytau"]=ev.Tau[ev.Tau["istight"]][:,0]
    if 'tight_pho' in analysis_point: ev["myphoton"]=ev.Photon[ev.Photon["istight"]][:,0]
    if 'tight_l' in analysis_point: ev["mylep"]=ev.l[ev.l["istight"]][:,0]

    if 'loose_tau' in analysis_point: ev["mytau"]=ev.Tau[ev.Tau["isloose"]][:,0]
    if 'loose_pho' in analysis_point: ev["myphoton"]=ev.Photon[ev.Photon["isloose"]][:,0]
    if 'loose_l' in analysis_point: ev["mylep"]=ev.l[ev.l["isloose"]][:,0]

    if 'med_tau' in analysis_point: ev["mytau"]=ev.Tau[ev.Tau["ismed"]][:,0]
    if 'med_pho' in analysis_point: ev["myphoton"]=ev.Photon[ev.Photon["ismed"]][:,0]
    if 'med_l' in analysis_point: ev["mylep"]=ev.l[ev.l["ismed"]][:,0]
    # Fill histograms

    ev["drlg"]=ev.myphoton.delta_r(ev.mylep)
    ev["ltobject"]= ev.mytau + ev.mylep
    ev["ltgobject"]=ev.mytau + ev.mylep + ev.myphoton
    ev["drlt"]=ev.mylep.delta_r(ev.mytau)
    ev["drgt"]=ev.myphoton.delta_r(ev.mytau)
    ev["dphilt"]=ev.mylep.delta_phi(ev.mytau)
    ev["dphigt"]=ev.myphoton.delta_phi(ev.mytau)
    ev["dphilg"]=ev.mylep.delta_phi(ev.myphoton)
    ev["chargelt"]=ev.mylep.charge*ev.mytau.charge
    ev["invarmass"]=ev.ltobject.mass
    
    hists.fill('ElectronPt',ev.weight_norm, (abs(ev.mylep.pdgId) ==11), ev.mylep, ElectronPt='pt')
    hists.fill('Electroneta',ev.weight_norm, (abs(ev.mylep.pdgId) ==11), ev.mylep, Electroneta='eta')
    hists.fill('Electronphi',ev.weight_norm, (abs(ev.mylep.pdgId) ==11), ev.mylep, Electronphi='phi')

    hists.fill('MuonPt',ev.weight_norm, (abs(ev.mylep.pdgId) ==13), ev.mylep, MuonPt='pt')
    hists.fill('Muoneta',ev.weight_norm, (abs(ev.mylep.pdgId) ==13), ev.mylep, Muoneta='eta')
    hists.fill('Muonphi',ev.weight_norm, (abs(ev.mylep.pdgId) ==13), ev.mylep, Muonphi='phi')

    hists.fill('TauPt_eh',ev.weight_norm, (abs(ev.mylep.pdgId) ==11), ev.mytau, TauPt_eh='pt')
    hists.fill('Taueta_eh',ev.weight_norm, (abs(ev.mylep.pdgId) ==11), ev.mytau, Taueta_eh='eta')
    hists.fill('Tauphi_eh',ev.weight_norm, (abs(ev.mylep.pdgId) ==11), ev.mytau, Tauphi_eh='phi')

    hists.fill('TauPt_uh',ev.weight_norm, (abs(ev.mylep.pdgId) ==13), ev.mytau, TauPt_uh='pt')
    hists.fill('Taueta_uh',ev.weight_norm, (abs(ev.mylep.pdgId) ==13), ev.mytau, Taueta_uh='eta')
    hists.fill('Tauphi_uh',ev.weight_norm, (abs(ev.mylep.pdgId) ==13), ev.mytau, Tauphi_uh='phi')

    hists.fill('PhotonPt_eh',ev.weight_norm, (abs(ev.mylep.pdgId) ==11), ev.myphoton, PhotonPt_eh='pt')
    hists.fill('Photoneta_eh',ev.weight_norm, (abs(ev.mylep.pdgId) ==11), ev.myphoton, Photoneta_eh='eta')
    hists.fill('Photonphi_eh',ev.weight_norm, (abs(ev.mylep.pdgId) ==11), ev.myphoton, Photonphi_eh='phi')

    hists.fill('PhotonPt_uh',ev.weight_norm, (abs(ev.mylep.pdgId) ==13), ev.myphoton, PhotonPt_uh='pt')
    hists.fill('Photoneta_uh',ev.weight_norm, (abs(ev.mylep.pdgId) ==13), ev.myphoton, Photoneta_uh='eta')
    hists.fill('Photonphi_uh',ev.weight_norm, (abs(ev.mylep.pdgId) ==13), ev.myphoton, Photonphi_uh='phi')

    hists.fill('drlt_eh',ev.weight_norm, (abs(ev.mylep.pdgId) ==11), ev, drlt_eh='drlt')
    hists.fill('drlt_uh',ev.weight_norm, (abs(ev.mylep.pdgId) ==13), ev, drlt_uh='drlt')

    hists.fill('drgt_eh',ev.weight_norm, (abs(ev.mylep.pdgId) ==11), ev, drgt_eh='drgt')
    hists.fill('drgt_uh',ev.weight_norm, (abs(ev.mylep.pdgId) ==13), ev, drgt_uh='drgt')

    hists.fill('drlg_eh',ev.weight_norm, (abs(ev.mylep.pdgId) ==11), ev, drlg_eh='drlg')
    hists.fill('drlg_uh',ev.weight_norm, (abs(ev.mylep.pdgId) ==13), ev, drlg_uh='drlg')

    hists.fill('dphilg_eh',ev.weight_norm, (abs(ev.mylep.pdgId) ==11), ev, dphilg_eh='dphilg')
    hists.fill('dphilg_uh',ev.weight_norm, (abs(ev.mylep.pdgId) ==13), ev, dphilg_uh='dphilg')

    hists.fill('dphilt_eh',ev.weight_norm, (abs(ev.mylep.pdgId) ==11), ev, dphilt_eh='dphilt')
    hists.fill('dphilt_uh',ev.weight_norm, (abs(ev.mylep.pdgId) ==13), ev, dphilt_uh='dphilt')

    hists.fill('dphigt_eh',ev.weight_norm, (abs(ev.mylep.pdgId) ==11), ev, dphigt_eh='dphigt')
    hists.fill('dphigt_uh',ev.weight_norm, (abs(ev.mylep.pdgId) ==13), ev, dphigt_uh='dphigt')


    hists.fill('invarmass_eh',ev.weight_norm, (abs(ev.mylep.pdgId) ==11), ev, invarmass_eh='invarmass')
    hists.fill('invarmass_uh',ev.weight_norm, (abs(ev.mylep.pdgId) ==13), ev, invarmass_uh='invarmass')
    hists.fill('MET',ev.weight_norm, ((abs(ev.mylep.pdgId) ==13)|(abs(ev.mylep.pdgId) ==11)),ev.MET, MET='pt')
    #-------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------
    #End your analysis
    #-------------------------------------------------------------------------------------------------------
    ET.autolog(f"{len(ev)} Events at the end of your analysis", logger, 'i')
    return hists.get()
