# License here

import os
import sys
# import glanceclient as gcli
# import novaclinet as ncli
# import cinderclient as ccli
import commands
import cPickle


import driver.openstack.OSPDriver as osp
import driver.s3compatible.S3Driver as s3
import driver.openstack_backend.Libvirt as virt

def credential_handler(CREDENTIAL):
    # In order to get the value of following keys:
    #     * OS_USERNAME;
    #     * OS_PASSWORD;
    #     * OS_AUTH_URL;
    #     * OS_TENANT_NAME;
    #     * OS_REGION_NAME.
    #
    # Keystone API ver.2 is required in OpenStack ENV.

    try:
        credential = {}
        f = open(CREDENTIAL, 'r')
        for each in [line.strip() for line in f.readlines()]:
            eachData = each.split('=')
            credential[eachData[0]] = eachData[1]
        f.close()
        return credential

    except IOError:
        raise ValueError("Non-existed credential file.")




def records_parser(recordfile):
    pass


class Backup_or_restore(object):
    def __init__(self, action, args, record):
        self.action = action
        self.args = args
        self.record = record

    def backup(self):

        # should have checked env before operations
        pass

    def restore(self):

        # should have checked env before operations
        pass

    def records_parser(self):

    def record_handler(self):
        if not os.path.exists(self.record):
            with open(self.record, "w") as f:
                cPickle.dump([], f)
        with open(self.record) as f:
            records_old = cPickle.load(f)
        record_old = None


    def setup(self):
        pass


def main():
    try:

        CREDENTIAL = os.environ['HOME'] + '/credential.rc'


    except KeyboardInterrupt:
        sys.exit(2)

    except Exception as e:
        pass



if __name__ == "__main__":
    sys.exit(main())
