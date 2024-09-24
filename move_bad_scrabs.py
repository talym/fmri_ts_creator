# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:49:26 2023

@author: marko
"""
import os
import shutil

if __name__ == '__main__':

    scans = r'E:\joy\fmri_scans'
    bad_scans_path = r'E:\joy\bad scans'
    if not os.path.exists(bad_scans_path):
        # Create the directory
        os.makedirs(bad_scans_path)
    bad_files = [
        'sub-1151_ses-4_task-fmrirest_desc-confounds_regressors.txt',
        'sub-1197_ses-4_task-fmrirest_desc-confounds_regressors.txt',
        'sub-1177_ses-1_task-fmrirest_run-1_desc-confounds_regressors.txt',
        'sub-1308_task-rest_run-1_desc-confounds_timeseries.txt',
        'sub-1151_ses-1_task-fmrirest_desc-confounds_regressors.txt',
        'sub-1161_ses-1_task-fmrirest_desc-confounds_regressors.txt',
        'sub-1211_ses-1_task-fmrirest_desc-confounds_regressors.txt'
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