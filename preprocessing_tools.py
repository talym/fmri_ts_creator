# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 19:42:46 2023

@author: marko
"""
import nibabel as nib
import pandas as pd
from nipype.interfaces import afni as afni
from nilearn.maskers import NiftiLabelsMasker
import numpy as np
import json
from data_manager import DataMng 
from numpy import genfromtxt
from nilearn import image
import os
import glob


THRESHOLD = 0.4
debug = False
NUMBER_OF_PHYSIO = 10
from nilearn.image import resample_to_img

class PrepTools(object):
    def AddPysio(conf_, pysio_file, num_vol_to_remove):
        df = pd.read_csv(pysio_file, delimiter='\t', header=None).fillna(0).iloc[num_vol_to_remove: , :]
        pysio_conf = df.iloc[:, :NUMBER_OF_PHYSIO]
        physio_names = list(range(NUMBER_OF_PHYSIO))
        physio_names = ['physio_'+str(num) for num in physio_names]
        pysio_conf.columns = physio_names
        return pd.concat([conf_, pysio_conf], axis=1)
    def CreateFDOL(df, name):
        indexes =  df[df['framewise_displacement'] > THRESHOLD].index.tolist()
        i = 0
        for index in indexes:
            column_name = 'FD_motion_outlier_'+str(i)
            df[column_name] = 0
            df.at[index, column_name] = 1
            i = i+1
            if(debug): print(index, df.at[index, 'framewise_displacement'], df.at[index, column_name])
        print(i, ',', name)
        return df, i
            
    def Confound(full_confound_file, confounds, num_vol_to_remove, prep_params, updated_confound_file='', pysio_file = ''):
        df = pd.read_table(full_confound_file).fillna(0).iloc[num_vol_to_remove: , :] #get rid of na and num_vol_to_remove first volumes
        if debug: print(df.shape)
        df, bad_vol = PrepTools.CreateFDOL(df, full_confound_file)
        if debug: print(df.shape)
        columns_names = list(df.columns.values)
        if prep_params.INCLUDE_MOTION_CONF:
            motion_confounds = [name for name in columns_names if 'FD_motion_outlier' in name]
            other_confounds = list(set(columns_names).intersection(confounds))
            all_confounds = other_confounds + motion_confounds
        else:
            all_confounds = other_confounds
        if debug: print(all_confounds)
        conf_ = df[all_confounds]
        if pysio_file != '':   conf_ = PrepTools.AddPysio(conf_, pysio_file, num_vol_to_remove)
        print(conf_.shape)
        return conf_, bad_vol
    def RemoveFirstNVolumes(nifti, num_vol_to_remove):
        print('RemoveFirstNVolumes')
        img = nib.load(nifti)
        data = img.get_fdata()[:,:,:,num_vol_to_remove:]
        img_sliced = nib.Nifti1Image(data, img.affine, img.header)
        """img_sliced_path = ''.join(nifti.split('.')[0])+'_r.nii'
        nib.nifti1.save(img_sliced, img_sliced_path)"""
        return img_sliced   
    def GetReceptorZScoreData(receptor_map, scan) :
        receptor_img = nib.load(receptor_map)
        receptor_img_res = resample_to_img(receptor_img, scan)        
        receptor_img_res_data = receptor_img_res.get_fdata()        
        min_ = np.min(receptor_img_res_data[receptor_img_res_data!=0])
        max_ = np.max(receptor_img_res_data[receptor_img_res_data!=0])
        receptor_img_res_data[receptor_img_res_data!=0] = (receptor_img_res_data[receptor_img_res_data!=0] - min_) / (max_-min_)
               
        return receptor_img_res_data
        
    def WeightByReceptor(scan, receptor_map):
        print('WeightByReceptor', receptor_map)
        scan_data = scan.get_fdata()                 
        receptor_img_res_data= PrepTools.GetReceptorZScoreData(receptor_map, scan)         
        scan_NMDA_wg_data = scan_data * receptor_img_res_data[..., np.newaxis]
        scan_NMDA_wg_img = nib.Nifti1Image (scan_NMDA_wg_data, scan.affine)        
        return scan_NMDA_wg_img
    def Despyke(nifti):
        despike = afni.Despike()
        despike.inputs.in_file = nifti
        despike.cmdline
        res = despike.run() 
        return res
    def CreatTimeSeries(nifti_img, atlas, labels, standardize, smoothing_fwhm, detrend, low_pass, high_pass, t_r, confounds):
        masker = NiftiLabelsMasker(labels_img = atlas, labels = labels, standardize=standardize, 
                                        memory='nilearn_cache', verbose=0, 
                                        smoothing_fwhm = smoothing_fwhm, detrend = detrend,
                                        low_pass=low_pass, high_pass=high_pass, t_r=t_r)

        time_series = masker.fit_transform(nifti_img, confounds = confounds) 
        return time_series
    def LoadData(prep_params):
        #save the preprocessing parameters 
        with open(prep_params.LOG_PARAM, "w") as fp:
            json.dump({'standardize': prep_params.STANDARTIZE, 'smoothing_fwhm': prep_params.SMOOTHING_FWHM, 'detrend': prep_params.DETREND, 
                       'low_pass' : prep_params.LOW_PASS, 'high_pass' : prep_params.HIGH_PASS,  't_r' : prep_params.T_R}, fp)  # save the dataset

        #get all nifti and counfound inputs - assume to be fmriprep output
        sets_of_files = DataMng.GetFmriInput(mri_sets_dir = prep_params.DATA_ROOT, pysio_dir_set = prep_params.PHYSIO_PATH, level = prep_params.LEVEL, input_formant = 
                                             {'nifti_ext':prep_params.NIFTI_EXT, 'confound_ext':prep_params.CONF_EXT, 'physio_ext': prep_params.PHYSIO_EXT,
                                              'NIFTI_exclude': prep_params.NIFTI_NAME_EXCLUDE, 'NIFTI_include': prep_params.NIFTI_NAME_INCLUDE,
                                              'confound_exclude': prep_params.CONF_NAME_EXCLUDE, 'confound_include': prep_params.CONF_NAME_INCLUDE ,
                                              'matchig_teplate':prep_params.MATCHING_TEMPLATE,
                                              'physio_exclude': prep_params.PHYSIO_NAME_EXCLUDE, 'physio_include': prep_params.PHYSIO_NAME_INCLUDE})
        # save the dataset
        with open(prep_params.LOG_FILE, "w") as fp:
            json.dump(sets_of_files, fp)  
            
        #get atlas and it's labels 
        if prep_params.AICHA: labels = genfromtxt(prep_params.ATLAS_LABELS_PATH, dtype=str, delimiter=" ")[:,1]
        elif prep_params.Schaefer2018 or  prep_params.Lausanne: labels = genfromtxt(prep_params.ATLAS_LABELS_PATH, dtype=str, delimiter=" ")
        else: print("Unsupported Atlas")
        atlas_img = image.load_img(prep_params.ATLAS_IMG_PATH)  
        return sets_of_files, labels, atlas_img
    def handleConf(set_of_files, prep_params, receptor):
        conf_log = os.path.join(prep_params.LOG, receptor + '-' +set_of_files['CONFOUND'].split('\\')[-1].split('.')[0]+'.txt')
        if set_of_files['CONFOUND'] == '':
            print('++++++++++++++Empty ', set_of_files['CONFOUND'])
            return None, True
        if prep_params.INCLUDE_PHYSIO:
            if set_of_files['PHYSIO'] =='':
                print('**************Empty ', set_of_files['PHYSIO'])
                return None, True
            print('Physio')
            conf_, bad_vol = PrepTools.Confound(full_confound_file = set_of_files['CONFOUND'], confounds = prep_params.CONFOUNDS, 
                                       num_vol_to_remove = prep_params.NUM_VOL_TO_REMOVE, prep_params = prep_params, pysio_file = set_of_files['PHYSIO'])
        else:
            #print('No physio')
            conf_, bad_vol = PrepTools.Confound(full_confound_file = set_of_files['CONFOUND'], confounds = prep_params.CONFOUNDS, 
                                       num_vol_to_remove = prep_params.NUM_VOL_TO_REMOVE, prep_params = prep_params, pysio_file = '')
        with open(conf_log, "w") as fp:
            for conf in conf_.columns.values:
                fp.write("%s\n" % conf)
        return conf_, False
    def GetTR(nifti_file, GUY_DATA):
        if GUY_DATA:
            file = nifti_file.split('\\')[-1]
            if 'sub-C' in file or 'sub-G' in file:
                TR = 3
            elif 'sub-D' in file or 'sub-E' in file or 'sub-F' in file:
                TR = 2.5
            else:
                print('Error !!!!!!!!!!!!!!! Unknown TR', nifti_file)
        else:
            nifti_file_split = nifti_file.split('\\')
            nifti_file = nifti_file_split[-1]
            start_index = nifti_file.find('space')
            json_file_path = os.path.join(os.path.join(*nifti_file_split[:len(nifti_file_split)-1]), nifti_file[:start_index] + '*.json')
            json_files = glob.glob(json_file_path)
            if len(json_files) !=1:
                len_ = len(json_files)
                print('Number of jsons is: {len_} ', json_file_path)
                TR = None
            else:
                json_file_path = json_files[0]
                with open(json_file_path, 'r') as file:
                    # Parse the JSON data
                    data = json.load(file)
                    TR = data['RepetitionTime']
        return TR
        
