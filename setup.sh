echo "########### Setting up env for expresso ##############"

system=$(uname --all)
if [[ "$system" == *"WSL2"* ]]; then
   echo "In wsl2"
   conda activate py37_coffea_hep
elif [[ "$system" == *"lxslc"* ]]; then
    echo "In lxslc"
    conda activate expresso
elif [[ "$system" == *"lxplus"* ]]; then
    echo "In lxplus"
    conda activate expresso
else
    echo "Are you in supported node?"
fi      

chmod +x plot+.py
chmod +x expresso.py
pip install -e .
chmod +x modules/createJSON.py


ehelp () {
    python expresso.py --help
}


phelp () {
    python plot+.py --help
}

ana () {
    ls Analysis/
}

testana () {
    ./expresso.py --Samples Analysis/testAnalysis/test_samples.txt --Analysis testAnalysis --NumberOfTasks 2 --Debug --SaveRoot
}
testplot () {
    python plot+.py --PlotterScript Analysis/testAnalysis/allplots.yaml --HistoFolder Output/Analysis/testAnalysis/output/analysis/ --SaveLocation Output/Analysis/testAnalysis/output/analysis/
    }
