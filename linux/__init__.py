# -*- coding: utf-8 -*-
import common,wardeploy

DOCKER_CONTAINER_INSPECT = "docker inspect %s"
DOCKER_RESTRT = "docker restart %s"
MV_FILE = "mv %s %s"
RM_FILE = "rm -rf %s %s"


class DockerDeploy(object):
    def __init__(self, fileName=None, appName=None, dockerVolumn=None, appTargetPath=None, command=None, script=None):
        self.fileName = fileName
        self.appName = appName
        self.dockerVolumn = dockerVolumn
        self.appTargetPath = appTargetPath
        self.command = common
        self.script = script

    def __repr__(self):
        return 'DockerDeploy(%s,%s,%s,%s,%s,%s)' % (self.fileName, self.appName, self.dockerVolumn, self.appTargetPath, self.command,self.script)

    def __str__(self):
        return '(%s,%s,%s,%s,%s,%s)' % (self.fileName, self.appName, self.dockerVolumn, self.appTargetPath, self.command,self.script)


def runWar(docker_deploy):
    result = wardeploy.deloy_war(docker_deploy)
    print result
    return result
