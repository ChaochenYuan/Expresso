#!/usr/bin/env python
import argparse
parser = argparse.ArgumentParser(description='Expresso Framework Options')
parser.add_argument("--Sample","-s", default='modules/json/background_samples/central_UL/UL18_DY50.json', help = 'path of samples')
#parser.add_argument("--OutputName","-oN"   , default='results', help = 'Name of output file')
parser.add_argument("--OutputFolder","-oF"   , default='./', help = 'Path to the output directory')
parser.add_argument("--ChunkSize","-cs"   , default='./', help = 'chunkSize')
parser.add_argument("--NumberOfTasks","-Tasks"   , default='./', help = 'threads')
parser.add_argument("--Analysis","-ana"   , default='chflip', help = 'Analysis name')
parser.add_argument("--AnalysisScript","-anascr"   , default='Analysis/chflip/analysis.py', help = 'Analysis script')
parser.add_argument("--Schema","-schema"   , default='NanoAODSchema', help = 'schema')
parser.add_argument("--PreProcessor","-pre"   , default='pre.py', help = 'preprocessor path')
parser.add_argument('--SaveRoot', default=False, action='store_true',help = 'save a root tree with branches in varstosave.py')
#parser.add_argument("--PreSelection","-pre"   , default='sel.py', help = 'preselection')
parser.add_argument("--PlotterScript","-plotter"   , default='', help = 'plotterscript')
parser.add_argument("--Xrootd","-xrd"   , default='root://cmsxrootd.fnal.gov//', help = 'xrootd redirector')
parser.add_argument("--Mode","-mode"   , default='local', help = 'mode of running: local, wq')

args = parser.parse_args()

from modules.ExpressoTools import cprint,saveHist
from modules.ExpressoPlotTools import dictplot

if args.PlotterScript:
    cprint(f'Plotter Script given, will just plot hists',"OKCYAN")
    PlotterScript=args.PlotterScript
    PlotterScript=PlotterScript.replace(".py","")
    PlotterScript=PlotterScript.replace("/",".")
    exec(f"from {PlotterScript} import histodict")
    exec('dictplot(histodict,args.OutputFolder)')


else:
    
    cprint(f'#----------------- E X P R E S S O    F R A M E W O R K-------------------#',"HEADER")
    cprint(f'Sample will be picked from: {args.Sample}',"OKCYAN")
    cprint(f'Pre-processor will be picked from: {args.PreProcessor}',"OKCYAN")
    cprint(f'Main-analysis will be picked from: {args.AnalysisScript}','OKCYAN')
    
    cprint(f'#------------------ Performing analysis:','OKBLUE')
    cprint(f'sample->pre-processor->pre-selector->main-analysis->save-plots->draw-plots','OKBLUE')
    cprint(f'#----------------- E X P R E S S O    F R A M E W O R K-------------------#',"HEADER")
    
    
    
    PreProcessor=args.PreProcessor
    PreProcessor=PreProcessor.replace(".py","")
    PreProcessor=PreProcessor.replace("/",".")
    exec(f"from {PreProcessor} import preprocess")
    
    
    PreSelection='Analysis/'+args.Analysis+'/preselection.py'
    PreSelection=PreSelection.replace(".py","")
    PreSelection=PreSelection.replace("/",".")
    exec(f"from {PreSelection} import preselection")
    
    AnalysisPath=args.AnalysisScript
    AnalysisPath=AnalysisPath.replace(".py","")
    AnalysisPath=AnalysisPath.replace("/",".")
    exec(f"from {AnalysisPath} import histograms,myanalysis")

    OutputName=(args.AnalysisScript).split('/')[2].replace(".py","")
    print(OutputName)
    
    #------------------- Initialize an IHEPAnalysis #-------------------###########
    import AnalysisX as AnalysisX
    Ana=AnalysisX.IHEPAnalysis(args.Analysis)
    #------------------- Initialize the hists #-------------------###########
    Ana.hists=histograms
    #------------------- GetTheSamples #-------------------###########
    Ana.SampleList=[args.Sample]
    Ana.GetSamples()
    
    Ana.preprocess(preprocess)
    Ana.preselection(preselection)
    #------------------- SetYourAnalysis #-------------------###########
    Ana.SetAnalysis(myanalysis,args.OutputFolder)
    #------------------- RunYourAnalysis #-------------------###########
    
    Ana.SetVarsToSave(args.Analysis,args.SaveRoot)
    
    result,JobFolder=Ana.run(OutputName=OutputName,xrootd=args.Xrootd,chunksize=int(args.ChunkSize),maxchunks=int(args.NumberOfTasks),
                             mode=args.Mode, schema=args.Schema)
    #------------------- Save the Histograms #-------------------###########
    saveHist(result,JobFolder,"results")
    cprint(f'#---- pkl file with results: {JobFolder}/  ----#',"HEADER")
    #------------------- Save the Histograms #-------------------###########
