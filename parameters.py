# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:57:53 2023

@author: marko
"""
import os


class PrepParameters(object):
    def __init__(self, data, atlas):
        self.DEBUG = True
        
        self.PROJECT_ROOT = 'C:\\Users\\marko\\ketamine'

        self.data_root = {
                'Noam':'E:\\ketamine\\Noam_ketamine',
                'NIH': 'E:\\ketamine\\NIH',
                'PTSD': 'E:\\ketamine\\REST_PTSD',
                'FIBRO': 'E:\\ketamine\\REST_FIBRO', 
                'HG':'E:\\ketamine\\HG_MPI'             
            }
    
        self.YEO_NW = ['VIS', 'SOM','DAT','VAT','LIM','FPN','DMN']
        
        self.CONFOUNDS_FULL = ['trans_x', 'trans_y', 'trans_z', 'rot_x', 'rot_y', 'rot_z', 
                     'a_comp_cor_00', 'a_comp_cor_01', 'a_comp_cor_02', 'a_comp_cor_03', 'a_comp_cor_04', 'a_comp_cor_05', 
                     'csf', 'white_matter', 'framewise_displacement' ]
        
        self.CONFOUNDS_BASIC = ['trans_x', 'trans_y', 'trans_z', 'rot_x', 'rot_y', 'rot_z', 
                     'framewise_displacement' ]
        #Atlas
        ATLAS_PATH = os.path.join(self.PROJECT_ROOT, 'atlas')
        self.AICHA = (atlas == 'AICHA')
        self.Schaefer2018 = (atlas == 'Schaefer2018') 
        self.Lausanne = (atlas == 'Lausanne') 
        if self.AICHA:
            self.ATLAS_IMG_PATH = os.path.join(ATLAS_PATH, 'AICHA (Joliot 2015).nii') 
            self.ATLAS_LABELS_PATH = os.path.join(ATLAS_PATH, 'AICHA (Joliot 2015).txt') 
            self.AICHA_YEO_PATH = os.path.join(ATLAS_PATH, 'AICHA-Yeo.xlsx') 
        elif self.Schaefer2018:
            self.ATLAS_IMG_PATH = os.path.join(ATLAS_PATH, 'Schaefer2018_400Parcels_7Networks_order_Tian_Subcortex_S4_3T_MNI152NLin2009cAsym_2mm.nii.gz') 
            self.ATLAS_LABELS_PATH = os.path.join(ATLAS_PATH, 'Schaefer2018_400Parcels_7Networks_order_Tian_Subcortex_S4_3T_MNI152NLin2009cAsym_2mm_label_modified.txt') 
        elif self.Lausanne:
            self.ATLAS_IMG_PATH = os.path.join(ATLAS_PATH, 'atl-Cammoun2012_space-MNI152NLin2009aSym_res-250_deterministic.nii.gz')                 
            self.ATLAS_LABELS_PATH = os.path.join(ATLAS_PATH, 'Lausanne_463.txt')
        else:
            print('Unsupported Atlas')
        
        #data structure parameters 
        self.CONF_EXT = 'tsv'
        self.PHYSIO_EXT = 'txt'
        self.NIFTI_NAME_EXCLUDE = []
        self.CONF_NAME_EXCLUDE = []
        self.PHYSIO_NAME_EXCLUDE = []
        self.PHYSIO_NAME_INCLUDE = []
        self.NUM_VOL_TO_REMOVE = 3
        self.LEVEL = 0 #SUB-XXX -> SES-X -> func
        self.changable_TR = False       
    
        #Preprocessing parameters
        self.STANDARTIZE = 'zscore'
        self.SMOOTHING_FWHM = 6
        self.DETREND = True
        self.HIGH_PASS = 0.01        
        
        self.set_case_specific_params(data, atlas)

        self.WITHIN_BETWEEN = os.path.join(self.RESULTS, 'withinbetween.xlsx')        
        self.LOG_FILE =   os.path.join(self.LOG, 'log_file.txt')
        self.LOG_PARAM =   os.path.join(self.LOG, 'log_param.txt')
    
    def set_case_specific_params(self, data, atlas):

        #Data
        DATA_ROOT = self.data_root[data]       
        #Special case
        self.GUY_DATA = (data == 'Guy')

  
        if data == 'PTSD' or data == 'FIBRO': 
            self.unified_param(DATA_ROOT)
            self.NIFTI_EXT = 'nii'
        elif data == 'NIH':
            self.unified_param(DATA_ROOT)
        elif data == 'HG':
            self.unified_param(DATA_ROOT);
        elif data == 'Noam':
            INCLUDE_PHYSIO = False
            if INCLUDE_PHYSIO:
                PHYSIO_PATH = ''
            else:
                PHYSIO_PATH = ''

            """RECEPTORS_MAPS = {'Raw': '', 
                                   'NMDA': os.path.join(ATLAS_PATH, '79664\\79664' + '_mRNA.nii'),
                                   'opioid_kappa_1': os.path.join(ATLAS_PATH, '4986\\4986'+ '_mRNA.nii'), 
                                   'opioid_mu_1': os.path.join(ATLAS_PATH, '4988\\4988'+ '_mRNA.nii'), 
                                   'dopamine_D2': os.path.join(ATLAS_PATH, '1813\\1813'+ '_mRNA.nii')}"""
            self.unified_param(DATA_ROOT, T_R = 2.5, PHYSIO_PATH = PHYSIO_PATH);                
        elif self.GUY_DATA:
            
            self.set_parameters(
                                       DATA_ROOT = 'D:\Guy', 
                                       NIFTI_NAME_INCLUDE = [],
                                       CONF_NAME_INCLUDE = [],
                                       MATCHING_TEMPLATE = ['sub-','_space'], 
                                       NIFTI_EXT = 'nii',
                                       RESULTS =    os.path.join(self.DATA_ROOT,'Results'),
                                       CONFOUNDS = ['trans_x', 'trans_y', 'trans_z', 'rot_x', 'rot_y', 'rot_z', 'framewise_displacement',  'csf'],
                                       LOW_PASS = None,
                                       INCLUDE_MOTION_CONF = False,
                                       T_R = 0,
                                       )                      
        elif data == 'Dynamore':
            DATA_ROOT = 'D:\\Dynamore'
            RESULTS =    os.path.join(DATA_ROOT,'Results')
            LOG = os.path.join(RESULTS, 'log')
            self.set_parameters(
                                      DATA_ROOT = DATA_ROOT, 
                                       NIFTI_NAME_INCLUDE = ['space-MNI152NLin2009cAsym_desc-preproc_bold'],
                                       CONF_NAME_INCLUDE = ['desc-confounds_timeseries'],
                                       MATCHING_TEMPLATE = ['sub-','_space'], 
                                       NIFTI_EXT = 'nii',
                                       RESULTS =   RESULTS,
                                       CONFOUNDS = self.CONFOUNDS_BASIC,
                                       LOW_PASS = 0.08,
                                       INCLUDE_MOTION_CONF = True,
                                       T_R = 0.8,
                                       LOG = LOG)    
        elif data == 'ket_sw':
            DATA_ROOT = 'G:\\ket_sw\\ket_sw_statbes'
            self.unified_param(DATA_ROOT);
        else:
            print('Error test: ', data, atlas)                
            
        
    def GetPrepParam(self):
        return self.STANDARTIZE, self.SMOOTHING_FWHM, self.DETREND, self.LOW_PASS, self.HIGH_PASS, self.T_R, self.NUM_VOL_TO_REMOVE
    
    def GetGeneralParam(self):
        return self.DEBUG, self.RECEPTORS_MAPS, self.RESULTS, self.GUY_DATA, self.changable_TR
    
    def set_parameters(self, DATA_ROOT, NIFTI_NAME_INCLUDE, CONF_NAME_INCLUDE, MATCHING_TEMPLATE, NIFTI_EXT, RESULTS, 
                       CONFOUNDS, LOW_PASS, INCLUDE_MOTION_CONF, T_R, 
                       INCLUDE_PHYSIO = False, PHYSIO_PATH = '', RECEPTORS_MAPS = {'Raw': ''}, LOG = ''):
        if LOG == '':  
            LOG = os.path.join(self.PROJECT_ROOT, 'log')
        self.DATA_ROOT = DATA_ROOT
        self.NIFTI_NAME_INCLUDE = NIFTI_NAME_INCLUDE
        self.CONF_NAME_INCLUDE = CONF_NAME_INCLUDE
        self.MATCHING_TEMPLATE = MATCHING_TEMPLATE
        self.NIFTI_EXT = NIFTI_EXT
        self.RESULTS  = RESULTS
        self.CONFOUNDS = CONFOUNDS
        self.LOW_PASS = LOW_PASS
        self.INCLUDE_MOTION_CONF = INCLUDE_MOTION_CONF
        self.T_R = T_R
        self.INCLUDE_PHYSIO = INCLUDE_PHYSIO
        self.PHYSIO_PATH = PHYSIO_PATH
        self.RECEPTORS_MAPS = RECEPTORS_MAPS
        self.LOG = LOG
        
    def unified_param(self, DATA_ROOT, T_R = None, PHYSIO_PATH = ''):
        if T_R == None:
            self.changable_TR = True
        else:
            self.changable_TR = False
        
        if self.Schaefer2018:
            RESULTS = os.path.join(DATA_ROOT,'Results_Schaefer2018')
        elif self.Lausanne:
            RESULTS = os.path.join(DATA_ROOT,'Results_Lausanne')   
        elif self.AICHA:
            RESULTS = os.path.join(DATA_ROOT,'Results_AICHA')   
        if not os.path.exists(RESULTS):
            os.makedirs(RESULTS)
            
        LOG = os.path.join(RESULTS, 'log')
        if not os.path.exists(LOG):
            os.makedirs(LOG)    
        
        if PHYSIO_PATH != "":
            INCLUDE_PHYSIO = True
        else:
            INCLUDE_PHYSIO = False    
            
        self.set_parameters(
                                  DATA_ROOT = DATA_ROOT, 
                                   NIFTI_NAME_INCLUDE = [],
                                   CONF_NAME_INCLUDE = [],
                                   MATCHING_TEMPLATE = ['sub-','_space'], 
                                   NIFTI_EXT = 'gz',
                                   RESULTS =   RESULTS,
                                   CONFOUNDS = self.CONFOUNDS_BASIC,
                                   LOW_PASS = 0.08,
                                   INCLUDE_MOTION_CONF = True,
                                   T_R = T_R,
                                   INCLUDE_PHYSIO = INCLUDE_PHYSIO,
                                   PHYSIO_PATH = PHYSIO_PATH,
                                   LOG = LOG)
