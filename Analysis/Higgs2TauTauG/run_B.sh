d=$3
if [ $d == '1' ]; then
    python expresso.py --Samples $1  --NumberOfTasks $2 --Analysis Higgs2TauTauG  --PreProcessor Analysis/Higgs2TauTauG/preprocessor_B.py  --PreSelector Analysis/Higgs2TauTauG/preselection_B.py --AnalysisScript Analysis/Higgs2TauTauG/analysis_B.py --Debug --PassOptions $4  --OutputFolder $5
    
else
    python expresso.py --Samples $1  --NumberOfTasks $2 --Analysis Higgs2TauTauG  --PreProcessor Analysis/Higgs2TauTauG/preprocessor_B.py  --PreSelector Analysis/Higgs2TauTauG/preselection_B.py --AnalysisScript Analysis/Higgs2TauTauG/analysis_B.py --PassOptions $4  --OutputFolder $5
fi