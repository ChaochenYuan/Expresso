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
    source /cvmfs/sft.cern.ch/lcg/views/dev4cuda/latest/x86_64-centos7-gcc8-opt/setup.sh
    pip install objprint
    pip install pprintpp
else
    echo "Are you in supported node?"
fi      

chmod +x plot+.py
chmod +x expresso.py
#pip install -e .
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
    ./expresso.py --Samples Analysis/barebones/samples.txt --Analysis barebones --NumberOfTasks 2 --Debug --SaveRoot
}
testanatight () {
    ./expresso.py --Samples Analysis/barebones/samples.txt --Analysis barebones --NumberOfTasks 2 --Debug --SaveRoot --AnalysisPoint tight_ele_tight_mu
}
testplot () {
    python plot+.py --PlotterScript Analysis/barebones/allplots.yaml --HistoFolder Output/Analysis/barebones/output/analysis/ --SaveLocation Output/Analysis/barebones/output/analysis/
    }
