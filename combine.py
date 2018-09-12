# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 18:26:29 2018

@author: Lipika Sharma
"""
def combine_files(in_folder,out_file):
    
    from os import listdir
    from os.path import isfile
    #folder = '../output_file/version4/output_rename/'
    files = [i for i in listdir(in_folder) if isfile(in_folder+i)]
    
    with open(out_file,'w') as fw:
        with open(in_folder+files[0],'r') as fr:
            for line in fr:
                    fw.write(line)
        for i in range(1,len(files)):
            with open(in_folder+files[i],'r') as fr:
                next(fr)
                for line in fr:
                    fw.write(line)

combine_files('../output_file/version4/output_rename/','../combined.txt')


#version 3

def combine_filesv3(in_folder,out_file):
    
    from os import listdir
    from os.path import isfile
    #folder = '../output_file/version4/output_rename/'
    files = [i for i in listdir(in_folder) if isfile(in_folder+i)]
    
    with open(out_file,'w') as fw:
        with open(in_folder+files[0],'r') as fr:
            for line in fr:
                    fw.write(line)
        for i in range(1,len(files)):
            with open(in_folder+files[i],'r') as fr:
                next(fr)
                for line in fr:
                    fw.write(line)

combine_filesv3('../output_file/version3/ver3/','../combined_v3.txt')