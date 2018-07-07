# -*- coding: utf-8 -*-
import subprocess


class Command(object):

    def __init__(self, code, result, error):
        self.code = code
        self.result = result
        self.error = error

    def __repr__(self):
        return 'Command(%s,%s,%s)' % (self.code, self.result,self.error)

    def __str__(self):
        return '(%s,%s,%s)' % (self.code, self.result, self.error)


# 要执行的命令
def exec_command(command):
    print "ready to exec command: " + command
    cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    out = cmd.communicate()
    result = Command(cmd.returncode, out[0],out[1])
    if (result.code == 0):
        print "exec command：" + command + " finished"
    else:
        print "exec command: " + command + " error: " + result.error
    return result
