import boto3    

class InventoryEC2:
    """
    TODO: Docs
    """
    def __init__(self):
        """
        TODO: Docs
        """
        self.ec2client = boto3.client("ec2")

    def getInstances(self):
        instanceslist = []
        response = self.ec2client.describe_instances()
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                # This sample print will output entire Dictionary object
                #print(instance)
                # This will print will output the value of the Dictionary key "InstanceId"
                p1 = instance["InstanceId"]
                p4 = self.__getVolumeSize(instance["BlockDeviceMappings"])
                p3 = instance["Placement"]["AvailabilityZone"]
                p2 = instance["PrivateDnsName"]
                p5 = instance["PlatformDetails"]
                p6 = instance["InstanceType"]
                type_details = self.ec2client.describe_instance_types(InstanceTypes = [p6])
                p7 = type_details["InstanceTypes"][0]["Hypervisor"]
                p8 = type_details["InstanceTypes"][0]["VCpuInfo"]["DefaultVCpus"]
                p9 = type_details["InstanceTypes"][0]["MemoryInfo"]["SizeInMiB"]
                p10 = instance["PrivateIpAddress"]
                tags = self.__getTags(instance["Tags"])
                name = self.__getVmName(instance["Tags"])
                print(f"{p1} {name} {p2} {p3} {p4}GB {p5} {p6} {p7} {p8} {p9}MiB {p10} \"{tags}\"")
                instanceslist.append([p1,name,p2,p3,f"{p4}GB",p5,p6,p7,p8,f"{p9}MiB", f"{p10}",f"\"{tags}\""])
        return instanceslist

    def __getVolumeSize(self, volumes: list()):
        size = 0
        for volume in volumes:
            detail =self.ec2client.describe_volumes(
                VolumeIds = [volume["Ebs"]["VolumeId"]]
            )
            size += int(detail["Volumes"][0]["Size"])
        #    print(volume)
        return size

    def __getTags(self, tags):
        value = []
        for tag in tags:
            name = tag["Key"]
            val = tag["Value"]
            if name != "Name":
                value.append(f"{name}={val}")
        return value
    
    def __getVmName(self, tags):
        vmname = ""
        for tag in tags:
            name = tag["Key"]
            value = tag["Value"]
            if name == "Name":
                vmname = value
        return vmname