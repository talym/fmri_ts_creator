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

RAW_ONLY = True
test = 'Noam'

if __name__ == '__main__':
    prep_params = PrepParameters(data = test, atlas = 'Lausanne')
    STANDARTIZE, SMOOTHING_FWHM, DETREND, LOW_PASS, HIGH_PASS, T_R, NUM_VOL_TO_REMOVE = prep_params.GetPrepParam()
    DEBUG, RECEPTORS_MAPS, RESULTS, GUY_DATA, changable_TR = prep_params.GetGeneralParam()
    
    sets_of_files, labels, atlas_img = PrepTools.LoadData(prep_params)
    
    for set_of_files_i in range(len(sets_of_files)):
        set_of_files = sets_of_files[set_of_files_i]
        #Step 1 - remove first NUM_VOL_TO_REMOVE volumes 
        nifti_sliced = PrepTools.RemoveFirstNVolumes(nifti = set_of_files['NIFTI'], num_vol_to_remove = NUM_VOL_TO_REMOVE)            
        #Weighed by Receptor maps        
        for receptor in RECEPTORS_MAPS:
            #print(receptor, RECEPTORS_MAPS[receptor])
            if len(RECEPTORS_MAPS[receptor])>0: 
                nifti_sliced = PrepTools.WeightByReceptor(nifti_sliced, RECEPTORS_MAPS[receptor])                        
            #Step 2 - de spiking
            #nifti = PrepTools.Despyke(nifti_sliced)     
            #Step 4, 8, 9, 10, 11, 12, 13, 14 
            conf_, continue_ = PrepTools.handleConf(set_of_files, prep_params, receptor)
            if continue_: continue
            if GUY_DATA or changable_TR: T_R = PrepTools.GetTR(set_of_files['NIFTI'], GUY_DATA)
            if T_R == None: continue
                
            time_series = PrepTools.CreatTimeSeries(nifti_img = nifti_sliced, atlas = atlas_img, labels = labels, 
                                                    standardize = STANDARTIZE, smoothing_fwhm = SMOOTHING_FWHM, detrend = DETREND, 
                                                    low_pass = LOW_PASS, high_pass = HIGH_PASS,  t_r = T_R, 
                                                    confounds = conf_)
            if DEBUG: vs.PlotSeries(series= time_series[:,:], title = set_of_files['NIFTI'].split('\\')[-1].split('.')[0][:30], xlabel = 'TR', ylabel = 'zscore')
                    
            df = pd.DataFrame(time_series)     
            results_ = os.path.join(RESULTS, receptor)
            if not os.path.exists(results_):
                # Create the directory
                os.makedirs(results_)
            df.to_csv(os.path.join(results_, set_of_files['NIFTI'].split('\\')[-1].split('.')[0]+'.csv'),index=False)
            

            
    
    
    
                                             
                                         
 