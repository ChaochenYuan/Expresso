d=$3
if [ $d == '1' ]; then
    python expresso.py --Samples $1  --NumberOfTasks $2 --Analysis Higgs2TauTauG  --PreProcessor Analysis/Higgs2TauTauG/preprocessor_S.py  --PreSelector Analysis/Higgs2TauTauG/preselection_S.py --AnalysisScript Analysis/Higgs2TauTauG/analysis_S.py --Debug --PassOptions $4  --OutputFolder $5 --Schema $6
    
else
    python expresso.py --Samples $1  --NumberOfTasks $2 --Analysis Higgs2TauTauG  --PreProcessor Analysis/Higgs2TauTauG/preprocessor_S.py  --PreSelector Analysis/Higgs2TauTauG/preselection_S.py --AnalysisScript Analysis/Higgs2TauTauG/analysis_S.py --PassOptions $4  --OutputFolder $5 --Schema $6
fi