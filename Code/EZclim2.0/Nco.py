"""
Created by Yusen Zhou Created by Yusen Zhou (Github acse-yz219)
"""
import os
import directories
import shutil
from utils import *
from ProgressBar import *
import subprocess

class Nco:
    def __init__(self,filepath,pieces,num_year,num_time,variable,output_unit,model_grid,prefix,start_year,output_folder,regrid):
        self.filepath = filepath
        self.pieces = pieces
        self.num_year = num_year
        self.num_time = num_time
        self.variable = variable
        self.output_unit = output_unit
        self.model_grid = model_grid
        self.prefix = prefix
        self.start_year = start_year
        self.output_folder = output_folder
        self.regrid = regrid
        self.local_file_path = "local.nc"
        self.local_temp_file_path = "temp_local.nc"
    def chunk(self):
        """
        chunk the dataset into small pieces

        """
        if not os.path.isdir(self.output_folder):
            os.makedirs(self.output_folder)
        interval  = int(self.num_time/self.pieces[0])
        year_interval = int(self.num_year/self.pieces[0]) 
        # command_list=[]
        progress = ProgressBar(n_iter=self.pieces[0], total_width= 30 , description='Chunk Process')
        for i in range(self.pieces[0]):
            current_start = interval*i
            current_end = interval*(i+1)-1
            current_str = 'time,'+str(current_start)+','+str(current_end)
            current_list =  ['ncks','-d',current_str]
            output_file_path = self.variable+'_'+str(year_interval*i+self.start_year[0])+'_'+str(year_interval*(i+1)+self.start_year[0]-1)+'.nc'
            current_command = current_list+ [self.filepath] + [output_file_path]
            # print(current_command)
            # command_list.append(current_command)
            subprocess.run(current_command)
            shutil.move(output_file_path,self.output_folder)
            progress.update()
        print("")
        progress.finish()
        print("")


    def change_unit(self):
        """
        Chage the unit of the dataset
        
        """
        progress = ProgressBar(n_iter=1, total_width= 30 , description='Change Unit')
        string1 = 'units,'+self.variable+',o,c,'+self.output_unit
        list = ['ncatted','-O','-a',string1,'-o',self.local_file_path]
        command = list + [self.filepath]
        subprocess.run(command)
        self.filepath = self.local_file_path
        progress.update()
        print("")

    def regrid_file(self):
        """
        regrid the file 
        """
        progress = ProgressBar(n_iter=1 , total_width= 30 , description='regrid_file')
        list = ['ncremap','-i',self.filepath,'-d',self.model_grid,'-o',self.local_temp_file_path]
        command = list
        subprocess.run(command)
        self.filepath = self.local_temp_file_path
        progress.update()
        print("")

    def delete(self):
        """
        Delete the file
        
        """
        if self.regrid == True :
          if os.path.exists(self.local_temp_file_path):
              os.remove(self.local_temp_file_path)
        if os.path.exists(self.local_file_path):
          os.remove(self.local_file_path)
    def preprocessing(self):
        """
        combine the step of preprocessing
        """
        self.change_unit()
        if(self.regrid == True):
            self.regrid_file()
        self.chunk()
        self.delete()

    
    