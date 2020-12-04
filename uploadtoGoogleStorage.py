# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 12:07:51 2020

@author: cpan
"""
'''
THIS SCRIPT UPLOADS FILES TO GCS. 
USES AN INPUT FOLDER AND RECURSIVELY UPLOADS FILES.
'''

import subprocess
import glob

folder = 'E:/GCP/ZonalStats/'

gsutil = "C:/Users/cpan/AppData/Local/Google/Cloud SDK/google-cloud-sdk/bin/gsutil.cmd"
gsBucket = 'pow-bucket'

##RECURSIVELY UPLOAD ALL FILES IN A FOLDER TO A BUCKET
command = gsutil + ' cp -r ' + folder + ' gs://' + gsBucket
subprocess.Popen(command)