def preprocess(pars,events,AttachSF=True):
    
    import awkward as ak    
    import modules.ExpressoTools as ET
    from modules.corrections import SFevaluator, GetBTagSF, ApplyJetCorrections, GetBtagEff, AttachMuonSF, AttachElectronSF, AttachPerLeptonFR, GetPUSF, ApplyRochesterCorrections, ApplyJetSystematics, AttachPSWeights, AttachPdfWeights, AttachScaleWeights, GetTriggerSF
    #from modules.selection import *
    #from modules.objects import *
    from modules.base_objects.base_electrons import base_electrons
    from modules.base_objects.base_muons import base_muons
    from modules.base_objects.base_leptons import base_leptons
    from modules.base_objects.base_jets import base_jets
    from modules.base_objects.base_met import base_met
    import numpy as np
    

    ###################################
    dataset,isData,histAxisName,year,xsec,sow=pars['dataset'],pars['isData'],pars['histAxisName'],pars['year'],pars['xsec'],pars['sow']
    ###################################
    isphoton=(events.GenPart.pdgId==22)
    istau=(abs(events.GenPart.pdgId)==15)


    events["genphotons"]=events.GenPart[isphoton]
    events["gentau"]=events.GenPart[istau]


    events["halfproperphotons"]=(events["genphotons"][abs(events.GenPart[events["genphotons"].genPartIdxMother].pdgId)==15])
    events["halfpropertau"]=events.gentau[(events.gentau.statusFlags & (1 << 13)== (1<<13))]

    
    
    events["properphotons"]=events["halfproperphotons"][events.halfproperphotons.status==1]
    #events["photonswithcut"]=events.properphotons[events.properphotons.pt>0]
    events["propertau"]=events["halfpropertau"][(abs(events.GenPart[events["halfpropertau"].genPartIdxMother].pdgId)==15) | (abs(events.GenPart[events["halfpropertau"].genPartIdxMother].pdgId)==25)]

    events["ttgevents"]=((ak.num(events.properphotons) >= 1) & (ak.num(events.propertau)==2))


    events=events[(events.ttgevents ==1)]
    
    events["drgt"]=ak.min(events.propertau.delta_r(events.properphotons[:,0]),axis=-1)
    events["drtt"]=events.propertau[:,0].delta_r(events.propertau[:,1])
    events["dphitt"]=events.propertau[:,0].delta_phi(events.propertau[:,1])
    events["ttobjectmass"]=(events.propertau[:,0]+events.propertau[:,1]).mass
    events["ttgobjectmass"]= (events.propertau[:,0] + events.propertau[:,1]+ events.properphotons[:,0]).mass

    return events
