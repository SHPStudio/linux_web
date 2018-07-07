# -*- coding: utf-8 -*-
import common,linux,os

def deloy_war(docker_deploy):
    result = {"success": False, "message": ""}
    uploadFile = os.path.join(common.get_value("uploadDir"),docker_deploy.fileName)
    print docker_deploy
    print "currentFilePath :" + uploadFile
    get_container_info = linux.DOCKER_CONTAINER_INSPECT % (docker_deploy.appName)
    print "get docker info :" + get_container_info
    get_app_volumn_path = os.path.join("/var/lib/docker/volumes/my-tomcat/_data",docker_deploy.appTargetPath)
    print "get docker volumn :" + get_app_volumn_path
    rmFile = linux.RM_FILE % (os.path.join(get_app_volumn_path,docker_deploy.fileName), os.path.join(get_app_volumn_path,docker_deploy.fileName.split(".")[0]))
    print "start rm file : " + rmFile
    mvFile = linux.MV_FILE % (uploadFile, os.path.join(get_app_volumn_path,docker_deploy.fileName))
    print "start mv file: " + mvFile
    result["success"] = True
    return result