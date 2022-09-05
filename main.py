from ec2inventory import InventoryEC2
import csv, argparse

def writeCsvFile(filename: str, data: list()):
    header = ['Instance ID', 'VM Name',  'DNS Name', 'Availability Zone', "Disk Size", "Platform", "Type", "Hypervisor", "VCPUs", "Memory", "Private IP Address", "Tags"]
    with open(filename, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        # write the data
        for row in data:
            writer.writerow(row)


parser = argparse.ArgumentParser(description="Get EC2 inventory report in current region, outputs to CSV file (need to provide -F argument)")                                                                      
parser.add_argument("-F", "--file", default="ec2report.csv", help = "Provide CSV file name")                                       
args = parser.parse_args()                                                                                                                            
filename = args.file

# ********
# * MAIN *
# ********
if __name__ == "__main__" :
    list = InventoryEC2()
    data = list.getInstances()
    writeCsvFile(filename, data)