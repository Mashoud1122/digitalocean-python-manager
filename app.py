import boto3
from botocore.client import Config
import os

#your key id
key_id = str("YOUR+SPACES_KEY")
#your secret key
secret_access_key = str("YOUR+SPACES_SECRET_KEY")

#regions: ams3, nyc3, sgp1, sfo2
files = []
locations = ['ams3', 'nyc3', 'sgp1', 'sfo2']
regions = ['ams3', 'nyc3', 'sgp1', 'sfo2']
spaces = []
# Initialize a session using DigitalOcean Spaces.
session = boto3.session.Session()
#this [client] is not so useful ;)
client = session.client('s3',
                        region_name='nyc3',
                        endpoint_url='https://nyc3.digitaloceanspaces.com',
                        aws_access_key_id=key_id,
                        aws_secret_access_key=secret_access_key)

def help():
    print("     Ctrl + C - To go back")
    print("--------------------------------------")
    print("     list - To list all spaces")
    print("--------------------------------------")
    print("     sno - To list number of spaces")
    print("--------------------------------------")
    print("     create - To create a new space")
    print("--------------------------------------")
    print("     use - To use a particular space[use spacename region] or (ex: use my-own-space1 nyc3)")
    print("--------------------------------------")
    print("     upload - to upload a file [upload spacename()]")
    print("                 to upload to a paricular folder [upload spacename('folder')")
    print("--------------------------------------")
    print("     destroy - to destroy a space")
    print("--------------------------------------")
    print("     list in - to list objects in a spaces[ex: list in my-space]")
    print("--------------------------------------")
    print("--------------------------------------")
    print("Advanced features will be added soon")
    print("Kindly send any suggestions or bugs to - xcoder1122@gmail.com ")
    print("I will be very excited to add it")

spaces_array = []
count_space = []
def show(space_name, region):

        try:
            if region in regions:
                client22 = session.client('s3',
                                        region_name=str(region),
                                        endpoint_url='https://' + str(region) + '.digitaloceanspaces.com',
                                        aws_access_key_id=key_id,
                                        aws_secret_access_key=secret_access_key)

                r = client22.list_objects(Bucket=space_name)
                files = r.get('Contents')
                i = 0
                p = str(files)

                if p == "None":
                    print("No Data available")
                else:
                    for file in files:
                        if len(file) > 0:
                            i += 1
                        else:
                            continue
                        print("Object: ")
                        print("     Name: " + file['Key'])
                        print("     Size: " + str(file['Size']) + " bytes")
                        date, time = str(file['LastModified']).split(" ")
                        print("     Last Modified: ")
                        print("             Date: " + date)
                        # later make function that determines from 2018-09-29 09:00:17.235000+00:00
                        # to detect date, time, and timezone - GMT, etc.
                        # time, date - done already
                        timeh, useless = time.split(".")
                        print("             Time: " + timeh)
                        # print("     Size" + file['Size'])
            else:
                print("Invalid Region Name")
        except:
            print("There was an error. Check space Name or region")

def use(space_name, region_name):
    while True:
        #
        # spaces_append()
            #
        if region_name in locations:
            if len(space_name) > 0:
                client = session.client('s3',
                                        region_name=str(region_name),
                                        endpoint_url='https://' + str(region_name) + '.digitaloceanspaces.com',
                                        aws_access_key_id=key_id,
                                        aws_secret_access_key=secret_access_key)

                r = client.list_objects(Bucket=str(space_name))
                if 1+1 == 3: # I made a mistake. I was too tired to fix. so i just did this
                    print("Invalid Selection")
                else:
                    cmd = input("#" + space_name + "#-> ")
                    action = cmd.lower()
                    if action == "list":
                        files = r.get('Contents')
                        i = 0
                        p = str(files)

                        if p == "None":
                            print("No Data available")
                        else:
                            for file in files:
                                if len(file) > 0:
                                    i += 1
                                else:
                                    continue
                                print("File: ")
                                print("     Name: " + file['Key'])
                                print("     Size: " + str(file['Size']) + " bytes")
                                date, time = str(file['LastModified']).split(" ")
                                print("     Last Modified: ")
                                print("             Date: " + date)
                                # later make function that determines from 2018-09-29 09:00:17.235000+00:00
                                # to detect date, time, and timezone - GMT, etc.
                                # time, date - done already
                                timeh, useless = time.split(".")
                                print("             Time: " + timeh)
                                print("     Size" + str(file['Size']))
                                print("File-Count: " + str(i))
                    elif action.strip()[:6] == "upload":
                        try:
                            file = input("Local File: ")
                            if os.path.isfile(file.strip()):
                                space_dest = input("Name when uploaded: ")
                                if len(space_dest) > 0:
                                    #Upload
                                    client.upload_file(file, space_name, space_dest)
                                    print("Successfully uploaded")
                                    print("Info:")
                                    print("     Local File: " + file)
                                    print("     File on Space: " + space_dest)

                                else:
                                    print("Invalid Space Destination Name")
                            else:
                                print("File Not Found")
                        except:
                            print("There was an Error")
                            print("     - Check Your File Name")
                            print("     - File may already exist")
                    elif action[:8] == "download":
                        try:
                            download, path_on_space, path_on_disk = action.split(" ")
                            client.download_file(space_name, path_on_space, path_on_disk)
                            print("Data written to -> " + path_on_disk)
                        except:
                            print("Error: Maybe file does not exist, or check the path you are saving to ")
                            print("Usage: download file_to_download_from_the_space file_name_to_save_on_disk")
                            print("Ex: download mytest-from-cloud docs.txt")
                    elif action == "delete":
                        av_files = []
                        files = r.get('Contents')
                        i = 0
                        p = str(files)

                        if p == "None":
                            print("No files in this Space")
                        else:
                            del av_files[:]
                            for file in files:
                                if len(file) > 0:
                                    i += 1
                                else:
                                    print("Invalid File Name")
                                files =  file['Key']

                                av_files.append(files)

                        file = input("File Name-> ")
                        if file in av_files:
                            delete(file, space_name, region_name)
                        else:
                            print("Check your file name. Cannot find your requested file")
                    elif action == "help":
                        print(" list - List all objects in this space")
                        print(" Upload - To Upload Files")
                        print(" delete - to delete a file")
                        print(" download - to download a file")
                        print(" cd - Coming soon :)")
                        print(" more to come :-)")
                        print("Email any suggestions ")
            else:
                print("Invalid Space name")
        else:
            print('Invalid Region')

def delete(file, space_name, region):
    if space_name in count_space:
        if region in regions:
            # print(count_space)
            ans = input("Input are you sure you want to delete " + file + "in space: " + space_name + "? yes / no ")
            act = ans.lower()
            if act.strip() == "yes":
                print("Deleting File")
                client = session.client('s3',
                                        region_name=str(region),
                                        endpoint_url='https://' + str(region) + '.digitaloceanspaces.com',
                                        aws_access_key_id=key_id,
                                        aws_secret_access_key=secret_access_key)
                response = client.delete_object(
                    Bucket=str(space_name),
                    Key=str(file),
                )
                print("Deleted")
            elif act.strip() == "no":
                print("Backing out ;)")

            else:
                print("Invalid Command")
        else:
            print("Invalid Region")
    else:
        print("Invalid Space Name. type list to view your available spaces")


def create(name, region):
    regions = ['ams3', 'nyc3', 'sgp1', 'sfo2']
    location = region.lower()
    if location == "ams3" or location == "nyc3" or location == "sgp1" or location == 'sfo2':
        fr = region.lower()
        try:
            client1 = session.client('s3',
                                     region_name=str(fr),
                                     endpoint_url='https://' + str(fr) + '.digitaloceanspaces.com',
                                     aws_access_key_id=key_id,
                                     aws_secret_access_key=secret_access_key)

            cr = client1.create_bucket(Bucket=str(name))
            print("Success")
            print("Details: ")
            print("     https://" + name + "." + region + "." + "digitaloceanspaces.com    is now available to use")
        except:
            print("Error")
            print("Possible Reasons: ")
            print("     -Name might already be in use")
            print("     -Invalid name(length or characters used)")
    else:
        print("Invalid region")
        print('Available Regions:')
        for reg in regions:
            print("[+]  " + reg)

def destroy(space_name):
    count()
    if space_name in spaces_array:
        print("Are you sure you want to delete -> " + space_name)
    else:
        print("Invalid Space Name")

################
def upload_file(file, space, region, upload_dir):
    if region in regions:
        client = session.client('s3',
                                 region_name=str(region),
                                 endpoint_url='https://' + str(region) + '.digitaloceanspaces.com',
                                 aws_access_key_id=key_id,
                                 aws_secret_access_key=secret_access_key)

        try:
            client.upload_file(file, space, upload_dir)
            print("Upload to SpaceName -> " + space)
            print("Localfile -> " + file)
            print("Destination on Space -> " + space + "::" + upload_dir)
            print("Successfully uploaded " + file + " to " + space)
        except:
            print("There Was An Error")
        return True
# List all buckets on your account.
i = 0

spaces_locations = ['ams3', 'nyc3', 'sgp1', 'sfo2']
count_space = []
for space in spaces_locations:
    session = boto3.session.Session()
    client1 = session.client('s3',
                            region_name=str(space),
                            endpoint_url='https://' + str(space) + '.digitaloceanspaces.com',
                            aws_access_key_id=key_id,
                            aws_secret_access_key=secret_access_key)
    response = client1.list_buckets()
    spaces = [space['Name'] for space in response['Buckets']]
    for space_num in spaces:
        count_space.append(space_num)


amount_of_spaces = len(count_space)

# def files():
#     files = r.get('Contents')
#     i = 0
#     p = str(files)
#
#     if p == "None":
#         print("No Data available")
#     else:
#         for file in files:
#             files.append(file['Key'])

def count():
    i = 0
    spaces_locations = ['ams3', 'nyc3', 'sgp1', 'sfo2']
    for space in spaces_locations:
        print("Spaces in [" + space + "]")
        print("")
        session = boto3.session.Session()
        client = session.client('s3',
                                region_name=str(space),
                                endpoint_url='https://' + str(space) + '.digitaloceanspaces.com',
                                aws_access_key_id=key_id,
                                aws_secret_access_key=secret_access_key)
        response = client.list_buckets()
        spaces = [space['Name'] for space in response['Buckets']]

        for space_name in spaces:
            print("     " + space_name)
            i += 1
            spaces_array.append(space_name)
        print("============================")



    print("Spaces-count: " + str(i))

def spaces_append():
    i = 0
    for item in spaces:
        i += 1
        del spaces_array[:]
        spaces_array.append(item)
