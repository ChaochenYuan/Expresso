from modules.ExpressoPlotter import ExpressoPlotter,normalplot

plotter=ExpressoPlotter("2016")
plotter.histolocation('Signal/Analysis/Higgs2TauTauG/output/analysis_S/')
plotter.savelocation('Analysis/Higgs2TauTauG/gen_level_plots/')
plotter.settings('modules/plotsettings.yaml')

plotter.addfile('H2TTG','H2TTTG_passop_Xsecweight.pkl.gz','red','nostack',-1)
plotter.addfile('DYJTLL','DYJTLL50_passop_Xsecweight.pkl.gz','blue','nostack',-1)
plotter.addfile('ZGTLLG','ZGToLLG01J_passop_Xsecweight.pkl.gz','green','nostack',-1)
plotter.addfile('H2TTGNP','H2TTTGNP_passop_1.pkl.gz','orange','nostack',-1)
plotter.addfile('H2TTGSM','H2TTTGSM_passop_1.pkl.gz','brown','nostack',-1)
plotter.addfile('H2TTGSMNP','H2TTTGSMNP_passop_1.pkl.gz','yellow','nostack',-1)


p=normalplot(plotter,filename="TauPt_leading",hi='TauPt_leading',axis='TauPt_leading',rebin=2)
p=normalplot(plotter,filename="Taueta_leading",hi='Taueta_leading',axis='Taueta_leading',rebin=2)
p=normalplot(plotter,filename="Tauphi_leading",hi='Tauphi_leading',axis='Tauphi_leading',rebin=2)
p=normalplot(plotter,filename="TauPt_subleading",hi='TauPt_subleading',axis='TauPt_subleading',rebin=2)
p=normalplot(plotter,filename="Taueta_subleading",hi='Taueta_subleading',axis='Taueta_subleading',rebin=2)
p=normalplot(plotter,filename="Tauphi_subleading",hi='Tauphi_subleading',axis='Tauphi_subleading',rebin=2)
p=normalplot(plotter,filename="drgt_V1",hi='drgt_V1',axis='drgt_V1',rebin=2)
p=normalplot(plotter,filename="drtt_V1",hi='drtt_V1',axis='drtt_V1',rebin=2)
p=normalplot(plotter,filename="ttobjectmass",hi='ttobjectmass',axis='ttobjectmass',rebin=2)
p=normalplot(plotter,filename="ttgobjectmass",hi='ttgobjectmass',axis='ttgobjectmass',rebin=2)
p=normalplot(plotter,filename="PhotonPt",hi='PhotonPt',axis='PhotonPt',rebin=2)
p=normalplot(plotter,filename="Photoneta",hi='Photoneta',axis='Photoneta',rebin=2)
p=normalplot(plotter,filename="Photonphi",hi='Photonphi',axis='Photonphi',rebin=2)
p=normalplot(plotter,filename="dphitt",hi='dphitt',axis='dphitt',rebin=2)
