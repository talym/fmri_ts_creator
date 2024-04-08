# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:49:26 2023

@author: marko
"""
import os
import shutil

result = 'HG'

if result == 'NIH_ziv':
    scans = 'E:\\ketamine\\NIH\\Results_Schaefer2018\\Raw' 
    bad_scans_path = 'E:\\ketamine\\NIH\\Results_Schaefer2018\\bad scans' 
    bad_files = [ 
                 'Raw-sub-0727_ses-1_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-0727_ses-2_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-1238_ses-1_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-1306_ses-3_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-1428_ses-2_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-1619_ses-2_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-1716_ses-2_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-1766_ses-1_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-1888_ses-1_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-1888_ses-2_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-1888_ses-3_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-1990_ses-1_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-1990_ses-2_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-1990_ses-3_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-2028_ses-3_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-2099_ses-1_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-2228_ses-1_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-2228_ses-2_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-2236_ses-1_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-2236_ses-3_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-2530_ses-3_task-fcmri_desc-confounds_regressors.txt',
                 'Raw-sub-2645_ses-1_task-fcmri_desc-confounds_regressors.txt']
    str_end=20
    str_start = 4

elif result == 'Guy':

    scans = 'D:\\Guy\\Results\\Raw\\'
    bad_scans_path = 'D:\\Guy\\Results\\bad scans'
    bad_files = [ 'sub-D534C_ses-1_task-nf_run-2_desc-confounds_timeseries.txt',
     'sub-D538T_ses-2_task-nf_run-2_desc-confounds_timeseries.txt',
     'sub-D558T_ses-2_task-nf_run-2_desc-confounds_timeseries.txt',
     'sub-E584T_ses-2_task-nf_run-2_desc-confounds_timeseries.txt',
     'sub-E589C_ses-2_task-nf_run-1_desc-confounds_timeseries.txt',
     'sub-E591C_ses-1_task-nf_run-2_desc-confounds_timeseries.txt',
     'sub-E596T_ses-1_task-nf_run-1_desc-confounds_timeseries.txt',
     'sub-E614T_ses-1_task-nf_run-1_desc-confounds_timeseries.txt',
     'sub-E720T_ses-2_task-nf_run-2_desc-confounds_timeseries.txt',
     'sub-E950T_ses-1_task-nf_run-1_desc-confounds_timeseries.txt',
     'sub-E950T_ses-2_task-nf_run-1_desc-confounds_timeseries.txt',
     'sub-F002T_ses-2_task-nf_run-2_desc-confounds_timeseries.txt',
     'sub-F015T_ses-1_task-nf_run-1_desc-confounds_timeseries.txt',
     'sub-F018C_ses-2_task-nf_run-2_desc-confounds_timeseries.txt',
     'sub-F021T_ses-1_task-nf_run-1_desc-confounds_timeseries.txt',
     'sub-F044T_ses-2_task-nf_run-1_desc-confounds_timeseries.txt',
     'sub-F049T_ses-1_task-nf_run-1_desc-confounds_timeseries.txt',
     'sub-F056T_ses-2_task-nf_run-1_desc-confounds_timeseries.txt',
     'sub-F056T_ses-2_task-nf_run-2_desc-confounds_timeseries.txt',
     'sub-F060T_ses-2_task-nf_run-2_desc-confounds_timeseries.txt'
    ]
    str_end=30
    str_start = 0
elif result == 'Dynamore': 
    scans = 'D:\\Dynamore\\Results\\Raw\\'
    bad_scans_path = 'D:\\Dynamore\\Results\\bad scans'
    if not os.path.exists(bad_scans_path):
        # Create the directory
        os.makedirs(bad_scans_path)
    bad_files = ['sub-14007_task-rest2_desc-confounds_timeseries.txt',
                 'sub-14008_task-rest1_desc-confounds_timeseries.txt',
                 'sub-14017_task-rest1_desc-confounds_timeseries.txt',
                 'sub-14017_task-rest2_desc-confounds_timeseries.txt',
                 'sub-14019_task-rest2_desc-confounds_timeseries.txt',
                 'sub-14021_task-rest1_desc-confounds_timeseries.txt',
                 'sub-14022_task-rest1_desc-confounds_timeseries.txt',
                 'sub-14022_task-rest2_desc-confounds_timeseries.txt',
                 'sub-14030_task-rest1_desc-confounds_timeseries.txt',
                 'sub-14037_task-rest2_desc-confounds_timeseries.txt',
                 'sub-14046_task-rest1_desc-confounds_timeseries.txt',
                 'sub-14048_task-rest2_desc-confounds_timeseries.txt',
                 'sub-14053_task-rest1_desc-confounds_timeseries.txt',
                 '\sub-14053_task-rest2_desc-confounds_timeseries.txt',
                 'sub-14055_task-rest2_desc-confounds_timeseries.txt'
                 ]
    str_end=20
    str_start = 0
elif result == 'NIH': 
    scans = 'D:\\NIH\\Results\\Raw\\'
    bad_scans_path = 'D:\\NIH\\Results\\bad scans'
    if not os.path.exists(bad_scans_path):
        # Create the directory
        os.makedirs(bad_scans_path)
    bad_files = [
        'Raw-sub-1148_task-rest_run-2_desc-confounds_timeseries.txt',
        'Raw-sub-1619_task-rest_run-1_desc-confounds_timeseries.txt',
        'Raw-sub-1619_task-rest_run-2_desc-confounds_timeseries.txt',
        'Raw-sub-2099_task-rest_run-2_desc-confounds_timeseries.txt',
        'Raw-sub-2124_task-rest_run-1_desc-confounds_timeseries.txt',
        'Raw-sub-2124_task-rest_run-2_desc-confounds_timeseries.txt',
        'Raw-sub-2423_task-rest_run-2_desc-confounds_timeseries.txt',
        'Raw-sub-2590_task-rest_run-2_desc-confounds_timeseries.txt',
        'Raw-sub-939_task-rest_run-1_desc-confounds_timeseries.txt',
        'Raw-sub-939_task-rest_run-2_desc-confounds_timeseries.txt']
    str_end=28
    str_start = 4
elif result == 'NIH_sh' : 
    scans = 'C:\\Users\\marko\ketamine\\Results_No_Physio_Schaefer2018\\Raw'
    bad_scans_path = 'C:\\Users\\marko\ketamine\\Results_No_Physio_Schaefer2018\\bad scans'
    if not os.path.exists(bad_scans_path):
        # Create the directory
        os.makedirs(bad_scans_path)
    bad_files = ['Raw-sub-0991_ses-1_task-fmrirestsmstr_desc-confounds_regressors.txt',
                 'Raw-sub-2060_ses-1_task-fmrirestsmstr_desc-confounds_regressors.txt',
                 'Raw-sub-2910_ses-1_task-fmrirestsmstr_desc-confounds_regressors.txt']
    
    str_end=28
    str_start = 4
elif result == 'Naomi_sh' : 
    scans = 'C:\\Users\\marko\ketamine\\Results_naomi_no_pysio_Schaefer2018\\Raw'
    bad_scans_path = 'C:\\Users\\marko\ketamine\\Results_naomi_no_pysio_Schaefer2018\\bad scans'
    if not os.path.exists(bad_scans_path):
        # Create the directory
        os.makedirs(bad_scans_path)
    bad_files = [
         'Raw-sub-015_ses-TP1_task-fmrirest_desc-confounds_regressors.txt',
         'Raw-sub-021_ses-TP1_task-fmrirest_desc-confounds_regressors.txt',
         'Raw-sub-021_ses-TP2_task-fmrirest_desc-confounds_regressors.txt',
         'Raw-sub-041_ses-TP2_task-fmrirest_desc-confounds_regressors.txt',
         ]

    str_end=28
    str_start = 4
elif result == 'Neomi_l':
    scans = 'G:\\neomi_data\\Results_Lausanne\\Raw'
    bad_scans_path = 'G:\\neomi_data\\Results_Lausanne\\bad scans'
    if not os.path.exists(bad_scans_path):
        # Create the directory
        os.makedirs(bad_scans_path)
    bad_files = [
         'Raw-sub-015_ses-TP1_task-fmrirest_desc-confounds_regressors.txt',
         'Raw-sub-021_ses-TP1_task-fmrirest_desc-confounds_regressors.txt',
         'Raw-sub-021_ses-TP2_task-fmrirest_desc-confounds_regressors.txt',
         'Raw-sub-041_ses-TP2_task-fmrirest_desc-confounds_regressors.txt',
         ]

    str_end=28
    str_start = 4
    
elif result == 'PTSD':
    scans = 'E:\\ketamine\\REST_PTSD\\Results_Schaefer2018\\Raw'
    bad_scans_path = 'E:\\ketamine\\REST_PTSD\\Results_Schaefer2018\\bad scans'
    if not os.path.exists(bad_scans_path):
        # Create the directory
        os.makedirs(bad_scans_path)
    bad_files = [
    'Raw-sub-D539C_ses-2_task-rest_run-1_desc-confounds_timeseries.txt',
    'Raw-sub-E720T_ses-1_task-rest_run-1_desc-confounds_timeseries.txt',
    'Raw-sub-F015T_ses-1_task-rest_run-1_desc-confounds_timeseries.txt',
    'Raw-sub-F021T_ses-1_task-rest_run-1_desc-confounds_timeseries.txt',
    'Raw-sub-F021T_ses-2_task-rest_run-1_desc-confounds_timeseries.txt',
    'Raw-sub-F041T_ses-2_task-rest_run-1_desc-confounds_timeseries.txt'
    ]
    str_end=20
    str_start = 4
elif 'HG':
    bad_files = [
    'Raw-sub-010001_ses-02_task-rest_acq-AP_run-01_desc-confounds_timeseries.txt',
    'Raw-sub-010012_ses-01_task-rest_acq-AP_run-01_desc-confounds_timeseries.txt',
    'Raw-sub-010038_ses-01_task-rest_acq-AP_run-01_desc-confounds_timeseries.txt',
    'Raw-sub-010043_ses-01_task-rest_acq-AP_run-01_desc-confounds_timeseries.txt',
    'Raw-sub-010091_ses-01_task-rest_acq-AP_run-01_desc-confounds_timeseries.txt',
    'Raw-sub-010133_ses-02_task-rest_acq-AP_run-01_desc-confounds_timeseries.txt',
    'Raw-sub-010177_ses-02_task-rest_acq-AP_run-01_desc-confounds_timeseries.txt',
    'Raw-sub-010278_ses-01_task-rest_acq-AP_run-01_desc-confounds_timeseries.txt',
    'Raw-sub-010280_ses-01_task-rest_acq-AP_run-01_desc-confounds_timeseries.txt',
    'Raw-sub-010289_ses-01_task-rest_acq-AP_run-01_desc-confounds_timeseries.txt',
    'Raw-sub-010290_ses-01_task-rest_acq-AP_run-01_desc-confounds_timeseries.txt',
    'Raw-sub-010308_ses-01_task-rest_acq-AP_run-01_desc-confounds_timeseries.txt'
    ]
    scans = 'E:\\ketamine\\HG_MPI\\Results_Schaefer2018\\Raw'
    bad_scans_path = 'E:\\ketamine\\HG_MPI\\Results_Schaefer2018\\bad scans'
    if not os.path.exists(bad_scans_path):
        # Create the directory
        os.makedirs(bad_scans_path)
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