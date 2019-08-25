# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 20:15:43 2019

@author: Chaitanya V
"""

from flask import Flask, request, send_from_directory
import os
from os.path import isfile, join, realpath, dirname
dir_path = dirname(realpath(__file__))

print("dir path = " + dir_path)

if(not os.path.exists(dir_path+'/files/')): os.makedirs(dir_path+'/files/')
print()

app = Flask(__name__,static_folder = './files')

@app.route('/filesharer',methods=['GET', 'POST'])
def filesharer():
    string = '<html>SHARED FILES<br/>'
    files = [f for f in os.listdir(dir_path+'/files/') if isfile(dir_path+'/files/'+f)]
    print(files)
    for file in files:
        string += "<a href='{0}'>{1}</a><br/>".format('/dl_file/'+file,file)
        
    string+="</html>"
    return string

@app.route('/dl_file/<path:filename>')
def download(filename):
    print(filename)
    return send_from_directory(dir_path+'/files/', filename,as_attachment=True)
    
    
if(__name__=='__main__'):
    app.run(host='0.0.0.0',debug=False)
    