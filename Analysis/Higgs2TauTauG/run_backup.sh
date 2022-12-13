d=$3
if [ $d == '1' ]; then
    python expresso.py --Sample $1  --NumberOfTasks $2 --Analysis Higgs2TauTauG  --PreProcessor Analysis/Higgs2TauTauG/preprocessor.py  --PreSelector Analysis/Higgs2TauTauG/preselection.py --AnalysisScript Analysis/Higgs2TauTauG/analysis.py --Debug --PassOptions $4  --OutputFolder $5 --SaveRoot
    
else
    python expresso.py --Sample $1  --NumberOfTasks $2 --Analysis Higgs2TauTauG  --PreProcessor Analysis/Higgs2TauTauG/preprocessor.py  --PreSelector Analysis/Higgs2TauTauG/preselection.py --AnalysisScript Analysis/Higgs2TauTauG/analysis.py --PassOptions $4  --OutputFolder $5 --SaveRoot
fi