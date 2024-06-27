#!/usr/bin/env python3
# Author Gaurav
# Universitat Potsdam
# Date 2024-6-27
from pathlib import Path
import pandas as pd
from shiny import reactive
from shiny.express import render, ui

ui.tags.link(href="https://www.uni-potsdam.de/typo3conf/ext/up_template/Resources/Public/Images/logos/up_logo_international_2.png", rel="stylesheet")

app_ui = ui.page_fixed(
    ui.h2("a single page application summary post pacbio hifi sequencing runs"),
        ui.markdown(" use the pacbiohifisequencing reads files and generate a single page deploayable summary"),
        ui.markdown("Developed by Gaurav Sablok, Academic Staff Member, Universitat Potsdam, Germany")
        ui.output_table("realengthbeforecutoff"),
        ui.output_plot("readplot")
        ui.output_table("readlengthaftercutoff")
)
def server(input, output, session):
    @output
    @render.table
    def table():
        infile = Path(__file__).parent / "reads.fastq"
        readsfastq = {}
        with open(infile, "r") as readsfile:
            readstore = readsfile.readlines()
            for i in range(len(readsstore)):
                if readstore[i].startswith["@"]:
                    readsfastq[readstore[i].strip().split()[0]] = readstore[i+1]
        fastalength = list(map(len,list(readstore.values())))
        minbins = min(fastalength)
        maxbins = max(fastalength)
        bin25
        bin50
        bin75
        bin100
        ui.text
        combined = pd.concat([bin25, bin50, bin57, bin100], axis = 1)
        return combined 
    @output
    @render.plot
    def plot():
        combined = pd.concat([bin25, bin50, bin57, bin100], axis = 1)
        return combined.bin25.plot.bar(), combined.bin50.plot.bar(), combined.bin75.plot.bar(), combined.bin100.plot.bar()
app = App(app_ui, server)
