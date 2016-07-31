import commands
import sys
import openstack_backend.LibvirtDriver as virt

class OSPDriver:

    def __init__(self, authuser, authpwd, authurl, tenant, region, uuid):

        self.authuser = authuser
        self.authpwd = authpwd
        self.authurl = authurl
        self.tenant = tenant
        self.region = region
        self.uuid = uuid

    @property
    def image_info_parser(self):

        "Used for getting object info from Glance"

        try:
            # TODO: use OpenStack RESTful API, instead of a CLI tool
            cmdrslt = commands.getstatusoutput(
                "glance --os-username %s --os-password %s --os-auth-url %s \
                --os-tenant-name %s --os-region-name %s --os-image-api-version 2 \
                image-show %s" % (self.authuser, self.authpwd, self.authurl, self.tenant, self.region, self.uuid))
            retr = cmdrslt[0]
            data = cmdrslt[1]
            if retr == 0:
                # FIXME: cause BUGs in some situations. The result should have been fully parsed, instead of part of it.
                parsedData = {}
                parsedData["base_image_ref"] = data.split("\n")[3].split("|")[2].split(" ")[1]
                parsedData["checksum"] = data.split("\n")[4].split("|")[2].split(" ")[1]
                parsedData["container_format"] = data.split("\n")[5].split("|")[2].split(" ")[1]
                parsedData["created_at"] = data.split("\n")[6].split("|")[2].split(" ")[1]
                parsedData["direct_url"] = data.split("\n")[7].split("|")[2].split(" ")[1] + \
                                           data.split("\n")[8].split("|")[2].split(" ")[1]
                parsedData["disk_format"] = data.split("\n")[8].split("|")[2].split(" ")[1]
                parsedData["image_type"] = data.split("\n")[12].split("|")[2].split(" ")[1]
                parsedData["instance_uuid"] = data.split("\n")[13].split("|")[2].split(" ")[1]
                parsedData["name"] = data.split("\n")[20].split("|")[2].split(" ")[1]
                parsedData["owner_id"] = data.split("\n")[22].split("|")[2].split(" ")[1]
                parsedData["user_id"] = data.split("\n")[29].split("|")[2].split(" ")[1]
                return parsedData

            else:
                raise ValueError("Invalid credential.")

        except Exception as e:
            pass

    @property
    def instance_info_parser(self):

        "Used for getting object info from Nova"

        try:
            # TODO: use OpenStack RESTful API, instead of a CLI tool
            cmdrslt = commands.getstatusoutput(
                "nova --os-username %s --os-password %s --os-auth-url %s \
                --os-tenant-name %s --os-region-name %s --os-image-api-version 2 \
                show %s" % (self.authuser, self.authpwd, self.authurl, self.tenant, self.region, self.uuid))
            retr = cmdrslt[0]
            data = cmdrslt[1]
            if retr == 0:
                # FIXME: cause BUGs in some situations. The result should have been fully parsed, instead of part of it.
                parsedData = {}
                parsedData["OS-EXT-SRV-ATTR:hypervisor_hostname"] = data.split("\n")[6].split("|")[2].split(" ")[1]
                parsedData["OS-EXT-SRV-ATTR:instance_name"] = data.split("\n")[7].split("|")[2].split(" ")[1]
                parsedData["OS-EXT-STS:power_state"] = data.split("\n")[8].split("|")[2].split(" ")[1]
                parsedData["OS-EXT-STS:vm_state"] = data.split("\n")[10].split("|")[2].split(" ")[1]
                parsedData["flavor"] = data.split("\n")[17].split("|")[2].split(" ")[1]
                parsedData["os-extended-volumes:volumes_attached"] = data.split("\n")[24].split("|")[2].split(" ")[1]
                parsedData["progress"] = data.split("\n")[26].split("|")[2].split(" ")[1]
                parsedData["security_groups"] = data.split("\n")[27].split("|")[2].split(" ")[1]
                parsedData["status"] = data.split("\n")[28].split("|")[2].split(" ")[1]
                parsedData["tenant_id"] = data.split("\n")[29].split("|")[2].split(" ")[1]
                parsedData["user_id"] = data.split("\n")[31].split("|")[2].split(" ")[1]
                return parsedData

            else:
                raise ValueError("Invalid credential.")

        except Exception as e:
            pass

    @property
    def volume_info_parser(self):

        "Used for getting object info from Cinder"

        try:
            # TODO: use OpenStack RESTful API, instead of a CLI tool
            cmdrslt = commands.getstatusoutput(
                "cinder --os-username %s --os-password %s --os-auth-url %s \
                --os-tenant-name %s --os-region-name %s --os-image-api-version 2 \
                show %s" % (self.authuser, self.authpwd, self.authurl, self.tenant, self.region, self.uuid))
            retr = cmdrslt[0]
            data = cmdrslt[1]
            if retr == 0:
                # FIXME: Cause BUGs in some situations. The result should have been fully parsed, instead of part of it.
                parsedData = {}
                # parsedData["base_image_ref"] = data.split("\n")[3].split("|")[2].split(" ")[1]
                # parsedData["checksum"] = data.split("\n")[4].split("|")[2].split(" ")[1]
                # parsedData["container_format"] = data.split("\n")[5].split("|")[2].split(" ")[1]
                # parsedData["created_at"] = data.split("\n")[6].split("|")[2].split(" ")[1]
                # parsedData["direct_url"] = data.split("\n")[7].split("|")[2].split(" ")[1] + \
                #                            data.split("\n")[8].split("|")[2].split(" ")[1]
                # parsedData["disk_format"] = data.split("\n")[8].split("|")[2].split(" ")[1]
                # parsedData["image_type"] = data.split("\n")[12].split("|")[2].split(" ")[1]
                # parsedData["instance_uuid"] = data.split("\n")[13].split("|")[2].split(" ")[1]
                # parsedData["name"] = data.split("\n")[20].split("|")[2].split(" ")[1]
                # parsedData["owner_id"] = data.split("\n")[22].split("|")[2].split(" ")[1]
                # parsedData["user_id"] = data.split("\n")[29].split("|")[2].split(" ")[1]
                return parsedData

            else:
                raise ValueError("Invalid credential.")

        except Exception as e:
            pass

    @property
    def uploadObject(self, name, file, container_format, disk_format, bootable, min_disk=1, min_ram=128):

        "Used for uploading object into OpenStack Glance as an image."

        self.name = name
        self.file = file
        self.container_format = container_format
        self.disk_format = disk_format
        self.bootable = bootable
        self.min_disk = min_disk
        self.min_ram = min_ram

        if bootable:
            try:
                # TODO: backup bootable objects from Glance, Nova, and Cinder
                cmdrslt = commands.getstatusoutput(
                "glance --os-username %s --os-password %s --os-auth-url %s \
                --os-tenant-name %s --os-region-name %s --os-image-api-version 2 \
                image-create --name %s --file %s --container-format %s --disk-format %s --min-disk %d --min-ram %d"
                % (self.authuser, self.authpwd, self.authurl, self.tenant, self.region, self.name, \
                    self.file, self.container_format, self.disk_format, self.min_disk, self.min_ram))
                retr = cmdrslt[0]
                data = cmdrslt[1]
                if retr != 0:
                    sys.stderr.write(data)
                    sys.exit(2)
            except KeyboardInterrupt:
                sys.exit(1)
            except Exception as e:
                pass
        else:
            try:
                # TODO: backup unbootable objects from Cinder
                pass
            except Exception as e:
                pass

    @property
    def downloadImage(self, file):

        "Used for downloading Nova snapshots from OpenStack Glance."

        self.file = file

        try:
            # TODO: use OpenStack CLI
            cmdrslt = commands.getstatusoutput(
                "glance --os-username %s --os-password %s --os-auth-url %s \
                --os-tenant-name %s --os-region-name %s --os-image-api-version 2 \
                image-download --file %s %s"
                % (self.authuser, self.authpwd, self.authurl, self.tenant, self.region, self.file, self.uuid))
            retr = cmdrslt[0]
            data = cmdrslt[1]
            if retr != 0:
                sys.stderr.write(data)
                sys.exit(2)
        except KeyboardInterrupt:
            sys.exit(1)

    @property
    def downloadVolume(self):

        "Used for downloading Cinder volumes."

        pass
