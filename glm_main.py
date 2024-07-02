import os
import pandas as pd
from parameters import PrepParameters
from preprocessing_tools import PrepTools
from visualizer import Visualizer as vs
from glm_tools import GLMAnalyzer
SHIFT = True
test = 'KET_PAIN'
atlas = 'Schaefer2018_7Networks'
project_root = r'E:\ketamine\pain'
events_root = os.path.join(project_root, 'events')
if SHIFT:
    glm_results = os.path.join(project_root, 'Results_GLM_shift')
else:
    glm_results = os.path.join(project_root, 'Results_GLM')
roi_path = os.path.join(project_root, 'atlas')
RUN_GLM1 = True
RUN_GLM2 = True

if __name__ == '__main__':
    if RUN_GLM1:
        prep_params = PrepParameters(data=test, atlas=atlas, project_root=project_root)
        STANDARTIZE, SMOOTHING_FWHM, DETREND, LOW_PASS, HIGH_PASS, T_R, NUM_VOL_TO_REMOVE = prep_params.GetPrepParam()
        DEBUG, RESULTS, changable_TR = prep_params.GetGeneralParam()

        sets_of_files, labels, atlas_img = PrepTools.LoadData(prep_params, events = events_root, event_id ='_task',
                                                              event_ending ='-fmrimentalandphysicalpainphysiosmstr_events.tsv')
        glm_analyzer = GLMAnalyzer(glm_results, prep_params)
        for set_of_files_i in range(len(sets_of_files)):
            set_of_files = sets_of_files[set_of_files_i]
            glm_analyzer.glm1(set_of_files)
    if RUN_GLM2:
        glm_analyzer = GLMAnalyzer(glm_results)
        glm_analyzer.glm2('ses-1')
        glm_analyzer.glm2ROIAv(os.path.join(roi_path, 'dACC.nii'))
        glm_analyzer.glm2ROIAv(os.path.join(roi_path, 'antINSR.nii'))
        glm_analyzer.glm2ROIAv(os.path.join(roi_path, 'antINSL.nii'))


