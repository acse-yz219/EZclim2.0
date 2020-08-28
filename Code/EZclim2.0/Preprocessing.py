"""
Created by Yusen Zhou Created by Yusen Zhou (Github acse-yz219)
"""
from user_entry import user_entry
import time
from Nco import *
from file_entry import file_entry_preprocessing


if __name__ == "__main__":
    filepath,pieces,num_year,num_time,variable,output_unit,model_grid,prefix,start_year,output_folder,regrid = file_entry_preprocessing()
    nco = Nco(filepath,pieces,num_year,num_time,variable,output_unit,model_grid,prefix,start_year,output_folder,regrid)
    nco.preprocessing()