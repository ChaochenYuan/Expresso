def preprocess(pars,events,AttachSF=True):
    ###################################
    import awkward as ak    
    import modules.ExpressoTools as ET
    dataset,isData,histAxisName,year,xsec,sow=pars['dataset'],pars['isData'],pars['histAxisName'],pars['year'],pars['xsec'],pars['sow']
    
    import numpy as np
    import modules.cut as cut
    
    isphoton=(events.GenPart.pdgId==22)
    events["genphotons"]=events.GenPart[isphoton]
    events["halfproperphotons"]=(events["genphotons"][abs(events.GenPart[events["genphotons"].genPartIdxMother].pdgId)==15])
    events["properphotons"]=events["halfproperphotons"][events.halfproperphotons.status==1]
    events["photonswithcut"]=events.properphotons[events.properphotons.pt>5]

    events["Tau","istight"]=(cut.ispresTau(events.Tau.pt, events.Tau.eta, events.Tau.dxy, events.Tau.dz, events.Tau.idDeepTau2017v2p1VSjet, 30) & cut.istightTau(events.Tau.idDeepTau2017v2p1VSjet))
    events["Tau","ismed"]=cut.ispresTau(events.Tau.pt, events.Tau.eta, events.Tau.dxy, events.Tau.dz, events.Tau.idDeepTau2017v2p1VSjet, 30) & cut.ismedTau(events.Tau.idDeepTau2017v2p1VSjet)
    events["Tau","isloose"]=cut.ispresTau(events.Tau.pt, events.Tau.eta, events.Tau.dxy, events.Tau.dz, events.Tau.idDeepTau2017v2p1VSjet, 30) & cut.islooseTau(events.Tau.idDeepTau2017v2p1VSjet)

    events["Electron","istight"]=cut.istightElectron(events.Electron.pt, events.Electron.eta, events.Electron.cutBased, 24)
    events["Electron","ismed"]=cut.ismedElectron(events.Electron.pt, events.Electron.eta, events.Electron.cutBased, 24)
    events["Electron","isloose"]=cut.islooseElectron(events.Electron.pt, events.Electron.eta, events.Electron.cutBased, 24)

    events["Muon","istight"]=cut.istightMuon(events.Muon.pt, events.Muon.eta, events.Muon.tightId, 20)
    events["Muon","ismed"]=cut.ismedMuon(events.Muon.pt, events.Muon.eta, events.Muon.mediumId, 20)
    events["Muon","isloose"]=cut.islooseMuon(events.Muon.pt, events.Muon.eta, events.Muon.looseId, 20)

    events["Photon","istight"]=cut.istightPhoton(events.Photon.pt, events.Photon.eta, events.Photon.cutBased, 5)
    events["Photon","ismed"]=cut.ismedPhoton(events.Photon.pt, events.Photon.eta, events.Photon.cutBased, 5)
    events["Photon","isloose"]=cut.isloosePhoton(events.Photon.pt, events.Photon.eta, events.Photon.cutBased, 5)

    events["NJets"]=ak.num(events.Jet)

    
    events["Electron"]=ET.sortpt(events.Electron)
    events["Muon"]=ET.sortpt(events.Muon)
    events["Tau"]=ET.sortpt(events.Tau)
    events["Photon"]=ET.sortpt(events.Photon)
    events["l"]=ak.with_name(ak.concatenate([events.Electron, events.Muon], axis=1), 'PtEtaPhiMCandidate')
    events["l"]=ET.sortpt(events.l)
    
    return events

   
