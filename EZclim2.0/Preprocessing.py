"""
Created by Yusen Zhou
"""
from user_entry import user_entry
import time
from Nco import *
from file_entry import file_entry_preprocessing


if __name__ == "__main__":
    filepath,pieces,variable,output_unit,model_grid,prefix,start_year,output_folder,regrid = file_entry_preprocessing()
    nco = Nco(filepath,pieces,variable,output_unit,model_grid,prefix,start_year,output_folder,regrid)
    nco.preprocessing()