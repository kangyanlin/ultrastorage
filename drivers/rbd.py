#!/usr/bin/python 
import commands

# backup action
def rbd_export_diff_snap(pool_name, image_name, snap_name, imagename):
    cmdrslt = commands.getstatusoutput(
        "rbd export-diff %s/%s@%s %s" % (pool_name, image_name, snap_name, imagename))

    retr = cmdrslt[0]
    rec = cmdrslt[1]
    if retr != 0:
        print rec
    else:
        print retr

def rbd_export_diff_between_snap(pool_name, image_name, new_snap_namev2, old_snap_namev1, imagename_v1_v2):
    cmdrslt = commands.getstatusoutput(
        "rbd export-diff %s/%s@%s --from-snap %s %s" % (pool_name, image_name, new_snap_namev2, old_snap_namev1, imagename_v1_v2))

    retr = cmdrslt[0]
    rec = cmdrslt[1]
    if retr != 0:
        print rec
    else:
        print retr

def rbd_export_diff_image_to_now(pool_name, image_name, imagename_now):
    cmdrslt = commands.getstatusoutput("rbd export-diff %s/%s %s" % (pool_name, image_name, imagename_now))

    retr = cmdrslt[0]
    rec = cmdrslt[1]
    if retr != 0:
        print rec
    else:
        print retr

# restore action
def rbd_import_diff_snap_to_image(snap_name, pool_name, image_name):
    cmdrslt = commands.getstatusoutput("rbd import-diff %s %s/%s" % (snap_name, pool_name, image_name))
    
    retr = cmdrslt[0]
    rec = cmdrslt[1]
    if retr != 0:
        print rec
    else:
        print retr
