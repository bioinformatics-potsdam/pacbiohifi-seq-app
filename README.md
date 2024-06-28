# pacbiohifi-seq-app
- **a single page shiny express pacbiohifi-seq-app for sequencing facility or startups.**
- generating a complete profiling of the pacbiohifi reads post sequencing at any sequencing center.
- complete API reference is located at [pythonapi](https://shiny.posit.co/py/api/).
- **parameters to set**: fastq file path, readfiltercutoff, provide the name and the address of the sequencing facility, provide the name and the person responsible for sequencing.
- installation dependencies
```
# First install htmltools, then shiny
pip install https://github.com/posit-dev/py-htmltools/tarball/main
pip install https://github.com/posit-dev/py-shiny/tarball/main
pip install shiny
pip install shinywidgets
pip install shinylive
pip install shinyswatch
```
- to use
```
git clone https://github.com/gauravcodepro/pacbiohifi-seq-app.git
cd pacbiohifi-seq-app
# put the fastq reads files there. provide the parameters and run as 
shiny run pacbiohifi-seq-app.py app.py --reload
- a dashboard will be build for the complete analysis including the
                  name of the sequencing facility or center and the person
```
- You can also host on tapyr template [template](https://github.com/Appsilon/tapyr-template)
- **To do tomorrow: add the path declaration, parameters settings, add the bins and check for the release version.**

Gaurav \
Academic Staff Member \
Bioinformatics \
Institute for Biochemistry and Biology \
University of Potsdam \
Potsdam,Germany

