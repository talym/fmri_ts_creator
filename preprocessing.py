# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 18:17:09 2023

@author: marko
"""
import os
import pandas as pd
from parameters import PrepParameters
from preprocessing_tools import PrepTools
from visualizer import Visualizer as vs

test = 'KET_INJ'
atlas = 'Schaefer2018_7Networks'
project_root = r'E:\ptsd_ketamine'

if __name__ == '__main__':
    prep_params = PrepParameters(data = test, atlas = atlas,project_root = project_root)
    STANDARTIZE, SMOOTHING_FWHM, DETREND, LOW_PASS, HIGH_PASS, T_R, NUM_VOL_TO_REMOVE = prep_params.GetPrepParam()
    DEBUG, RESULTS, changable_TR = prep_params.GetGeneralParam()
    
    sets_of_files, labels, atlas_img = PrepTools.LoadData(prep_params)
    
    for set_of_files_i in range(len(sets_of_files)):
        set_of_files = sets_of_files[set_of_files_i]
        #Step 1 - remove first NUM_VOL_TO_REMOVE volumes 
        nifti_sliced = PrepTools.RemoveFirstNVolumes(nifti = set_of_files['NIFTI'], num_vol_to_remove = NUM_VOL_TO_REMOVE)            

        conf_, continue_ = PrepTools.handleConf(set_of_files, prep_params)
        if continue_: continue
        if changable_TR: T_R = PrepTools.GetTR(set_of_files['NIFTI'])
        if T_R == None: continue
                
        time_series = PrepTools.CreatTimeSeries(nifti_img = nifti_sliced, atlas = atlas_img, labels = labels,
                                                standardize = STANDARTIZE, smoothing_fwhm = SMOOTHING_FWHM, detrend = DETREND,
                                                low_pass = LOW_PASS, high_pass = HIGH_PASS,  t_r = T_R,
                                                confounds = conf_)
        if DEBUG: vs.PlotSeries(series= time_series[:,:], title = set_of_files['NIFTI'].split('\\')[-1].split('.')[0][:30], xlabel = 'TR', ylabel = 'zscore')
                    
        df = pd.DataFrame(time_series)
        if not os.path.exists(RESULTS):
            # Create the directory
            os.makedirs(RESULTS)
        df.to_csv(os.path.join(RESULTS, set_of_files['NIFTI'].split('\\')[-1].split('.')[0]+'.csv'),index=False)
            

            
    
    
    
                                             
                                         
 