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
    from coffea.nanoevents.methods import vector
    ak.behavior.update(vector.behavior)
    

    ###################################
    dataset,isData,histAxisName,year,xsec,sow=pars['dataset'],pars['isData'],pars['histAxisName'],pars['year'],pars['xsec'],pars['sow']
    ###################################
    events["GenPart"]=ak.Array({'pt':events['Particle/Particle.PT'], 'eta':events['Particle/Particle.Eta'], 'phi':events['Particle/Particle.Phi'], 'mass':events['Particle/Particle.M']})
    varlist=[(v.split('/')[1]).split('.')[1] for v in events.fields if 'Particle/' in v]
    for v in varlist:
        events["GenPart",v]=events['Particle/Particle.'+v]
    
    
    istau=(abs(events.GenPart.PID)==15)
    events["gentau"]=events.GenPart[istau]
    isphoton=events.GenPart.PID==22
    events["genphoton"]=events.GenPart[isphoton]

    events["propertau"] = ak.zip(
            {
                "pt": events.gentau.pt,
                "eta": events.gentau.eta,
                "phi": events.gentau.phi,
                "mass": events.gentau.mass
            },
            with_name="PtEtaPhiMLorentzVector",
        )

    events["properphotons"] = ak.zip(
            {
                "pt": events.genphoton.pt,
                "eta": events.genphoton.eta,
                "phi": events.genphoton.phi,
                "mass": events.genphoton.mass
            },
            with_name="PtEtaPhiMLorentzVector",
        )

    events["ttgevents"]=((ak.num(events.properphotons) >= 1) & (ak.num(events.propertau)==2))


    events=events[(events.ttgevents ==1)]
    
    events["drgt"]=ak.min(events.propertau.delta_r(events.properphotons[:,0]),axis=-1)
    events["drtt"]=events.propertau[:,0].delta_r(events.propertau[:,1])
    events["dphitt"]=events.propertau[:,0].delta_phi(events.propertau[:,1])
    events["ttobjectmass"]=(events.propertau[:,0]+events.propertau[:,1]).mass
    events["ttgobjectmass"]= (events.propertau[:,0] + events.propertau[:,1]+ events.properphotons[:,0]).mass

    return events
