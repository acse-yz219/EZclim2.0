EZclim2.0
=================================

EZclim2.0 was developed in this project to enhance the scope of application of this EZclim1.0. EZclim1.0 was assessed in many aspects during this project. Various resolutions were provided to address its limitations. This has paved the way for creating EZclim2.0 to improve user experience by working on reasonable suggestions from different feedback. It has eventually attained three goals. It can be ported to JASMIN, it can operate pre-processing before diagnostics, and it can apply parallelization algorithms. This enhanced software version can manage various dataset types and process data faster. It is likewise convenient. Modifications are also possible for pre-processing steps. A progress bar is also provided to display the software’s current status. Overall, creating EZclim2.0 has been successful. For how to use this software please see UserGuide 

You can find all the output in these directories:

- **FinalReport**: [FinalReport](/FinalReport/irp_final_report.pdf)
- **Code**: [Code](/Code/EZclim2.0)
- **UserGuide**: [UserGuide](/Code/Documentation/UserGuide.pdf)
- **Documentation**:[Documentation](/Code/Documentation)

A short instruction will also be provided here but it is highly recommend that you go through the UserGuide

## Getting Started (Quick Setup)
- Download / clone the repository unto your computer
- You must first apply for JASMIN account. 
- Use a ssh server to login the JASMIN and upload the package to the JASMIN 
- load jaspy module to enable python3 on JASMIN
    ```
    module load jaspy
    ```
- CD EZclim2.0
    ```
    cd EZclim2.0
    ```
## Usage

### Input and output folders
The `.nc` data files to be analysed should be stored in the folder `DATA`. The `INPUT` folder stores all input, input masks, input sample points etc. files. The `RESULTS` folder will store the analysis, once computed. 
The file names can be changed in the file `directories.py`

### Do Preprocessing
```
# Created by Yusen Zhou
# Preprocessing Option Input
#
# ----------------- PLEASE FILL IN THE ARGUMENTS LISTED BELOW ------------------
#
# REQUIRED ARGUMENTS
# ------------------------------------------------------------------------------
# File Path: /badc/cmip6/data/CMIP6/CMIP/MOHC/UKESM1-0-LL/historical/r11i1p1f2/Omon/so/gn/latest/so_Omon_UKESM1-0-LL_historical_r11i1p1f2_gn_185001-189912.nc
File Path: DATA\so_Omon_UKESM1-0-LL_historical_r11i1p1f2_gn_185001-189912.nc
Number of pieces: 10
Number of year: 50
Number of time: 600
Variable Name: so
Output Unit: K
Model Grid: /badc/cmip5/data/cmip5/output1/MOHC/HadCM3/decadal1969/mon/ocean/Omon/r1i2p1/latest/so/so_Omon_HadCM3_decadal1969_r1i2p1_196911-197912.nc
Output Prefix: so
Start_year: 1850
output_folder: DATA/temp
regrid: False
#
# ------------------------------------------------------------------------------
# HELP : Found in the UserGuide
# ------------------------------------------------------------------------------
```
### RUN
```
python Preprocessing.py 
```
### Do Diagnostic
```
# User input for Climate Modelling Diagnostics Program: EZclim
#
# ----------------- PLEASE FILL IN THE ARGUMENTS LISTED BELOW ------------------
#
# REQUIRED ARGUMENTS
# ------------------------------------------------------------------------------
Prefix:
Start date of analysis:
Variables:
Number of ensembles: 1
#
# ------------------------------------------------------------------------------
# OPTIONAL ARGUMENTS
# ------------------------------------------------------------------------------
End date of analysis:
Analysis:
Spatial:
Total ensemble stats:
Plot: 1
Monthly:
Grid:
Sample:
Mask file:
Save Output: True
Covary:
Histogram bin selection:
Longitude centre:
User function:
Calculate areas:
Calculate index:
#
# ------------------------------------------------------------------------------
# HELP : Found in the UserGuide
# ------------------------------------------------------------------------------
```
### RUN
```
python main.py
```
## Built With

Python 3

## Author

**Yusen Zhou** (yz219@ic.ac.uk)

Acknowledgement
-----------------
Dr Plancherel, Yves and his PHD student Meuriot, Ophelie
    
