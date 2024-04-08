# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:49:26 2023

@author: marko
"""
import os
import shutil

if __name__ == '__main__':

    scans = r'E:\ptsd_ketamine\Results_Schaefer2018_7Networks'
    bad_scans_path = r'E:\ptsd_ketamine\bad_scans'
    if not os.path.exists(bad_scans_path):
        # Create the directory
        os.makedirs(bad_scans_path)
    bad_files = [
    'sub-D539C_ses-2_task-rest_run-1_desc-confounds_timeseries.txt',
    'sub-E720T_ses-1_task-rest_run-1_desc-confounds_timeseries.txt',
    'sub-F015T_ses-1_task-rest_run-1_desc-confounds_timeseries.txt',
    'sub-F021T_ses-1_task-rest_run-1_desc-confounds_timeseries.txt',
    'sub-F021T_ses-2_task-rest_run-1_desc-confounds_timeseries.txt',
    'sub-F041T_ses-2_task-rest_run-1_desc-confounds_timeseries.txt',
    'sub-F044T_ses-2_task-rest_run-1_desc-confounds_timeseries.txt',
    'sub-K0991_ses-1_task-fmrirestsmstr_desc-confounds_regressors.txt',
    'sub-K2060_ses-1_task-fmrirestsmstr_desc-confounds_regressors.txt',
    'sub-K2910_ses-1_task-fmrirestsmstr_desc-confounds_regressors.txt'
    ]
    str_end=20
    str_start = 4


    
if __name__ == '__main__':
    if not os.path.exists(bad_scans_path):
        os.makedirs(bad_scans_path)
        
    files = os.listdir(scans)
    for bad_file in bad_files:
        matching_files = [file for file in files if bad_file[str_start:str_end] in file]
        for file in matching_files:
            src_path = os.path.join(scans, file)
            dest_path = os.path.join(bad_scans_path, file)
            shutil.move(src_path, dest_path)
            print(f"Moved {file} to {bad_scans_path}")