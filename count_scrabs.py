# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:06:41 2023

@author: marko
"""
from preprocessing_tools import PrepTools


import glob
import pandas as pd
from parameters import PrepParameters


test = 'REST_RAMA'
if test == 'PAIN':
    logs_path = r'E:\ketamine\pain\Results_Schaefer2018\log'
elif test == 'JOY':
    logs_path = r'E:\joy\log'
elif test =='REST_RAMA':
     logs_path = r'\\fmri-maayan\PTSD_IPMP\Subjects\ActiveSubjects_Return\fmriprep\log'


atlas = 'Schaefer2018_7Networks'
#project_root = r'E:\ptsd_ketamine'
project_root = r'\\fmri-maayan\PTSD_IPMP\Subjects\ActiveSubjects_Return\fmriprep'
TSV = True

if __name__ == '__main__':

    prep_params = PrepParameters(data = test, atlas = atlas,project_root = project_root)
    list_of_log_files = glob.glob(logs_path + "\sub*")

    if TSV:
        sets_of_files, labels, atlas_img = PrepTools.LoadData(prep_params)
        for set_of_files in sets_of_files:
            tsv = set_of_files['CONFOUND']
            if len(tsv) == 0:
                print(set_of_files['NIFTI'])
                continue
            id = tsv.split('\\')[-1][:10]
            indices = [index for index, string in enumerate(list_of_log_files) if id in string]
            if len(indices) != 1:
                # print(tsv.split('\\')[-1], len(indices), '+++++++++++++++++++++')
                if len(indices) == 0:
                    print(tsv.split('\\')[-1], len(indices), '+++++++++++++++++++++')
                    continue
            log_file = list_of_log_files[indices[0]]
            with open(log_file, 'r') as file:
                lines = file.readlines()
            indices = [index for index, string in enumerate(lines) if 'FD_motion_outlier' in string]
            try:
                conf = pd.read_table(tsv)
            except:
                print(tsv)
                print(len(indices), ',', int((len(indices) / 442) * 100), ',', 442, log_file)
            else:
                print(len(indices), ',', int((len(indices) / conf.shape[0]) * 100), ',', conf.shape[0], ',', log_file)
    else:
        for log_file in list_of_log_files:
            with open(log_file, 'r') as file:
                lines = file.readlines()
            indices = [index for index, string in enumerate(lines) if 'FD_motion_outlier' in string]
            print(len(indices), ',', int((len(indices) / 442) * 100), ',', 442, log_file)
