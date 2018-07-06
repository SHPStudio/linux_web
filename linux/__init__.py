# -*- coding: utf-8 -*-
import subprocess
import os
def runUnzip(baseDir,fileName):
    shellscript = "unzip " + baseDir + os.path.sep + "upload" + os.path.sep + fileName
    print shellscript
    # cmd = subprocess.Popen(shellscript, shell=True, stdout=subprocess.PIPE)
    # out = cmd.communicate()
    # print cmd.returncode,out[0]
    cmd = {'returncode':0}
    if cmd['returncode'] == 0:
        return 0
    else:
        return 1
