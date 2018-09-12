# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 19:16:31 2018

@author: Lipika Sharma
"""
from shutil import copyfile
file1 = '../output_file/version4/output/'
file2 = '../output_file/version4/output_rename/'
for i in range(1,101):
    copyfile(file1+'cancer_risks ('+str(i)+').txt',file2+'{0:0>3}_cancer_risks.txt'.format(i))
    #print('{0:0>3}'.format(i))