import app
import droplet
import os

print("Stats->")
print("+===========================================================================+")
print("|| Kindly send any suggestions or bugs to - xcoder1122@gmail.com")
print("|| This will Help us A lot")
print("||")
print("||")
print("||")
print("||")
print("|| Available Spaces: " + str(app.amount_of_spaces))
print("|| Available Droplets: " + str(len(droplet.my_droplets)))
print("||")
print("||")
print("|| Type help")
print("+===========================================================================+")

regions = ['ams3', 'nyc3', 'sgp1', 'sfo2']
def help():
    print("     spaces - To Manage Spaces")
    print("--------------------------------------")
    print("     droplets - Coming Soon")

def spaces():
    print("     list - To list all spaces")
    print("--------------------------------------")
    print("     sno - To list number of spaces")
    print("--------------------------------------")
    print("     create - To create a new space")
    print("--------------------------------------")
    print("     help - To view more")
    print("--------------------------------------")
    print("Advanced features will be added soon")
    print("Kindly send any suggestions or bugs to - xcoder1122@gmail.com ")
    print("I will be very excited to add it")
    while True:
        ex = input("Spaces-> ")
        cmd = ex.lower()
        if cmd.strip() == "list":
            app.count()
        elif cmd == "sno":
            print("Available Spaces: " + str(app.amount_of_spaces))
        elif cmd == "create":
            name = input("Name: ")
            if len(name) > 0:
                region = input("Region: ")
                app.create(name, region)
        elif cmd == "help":
            app.help()
        elif cmd[:3] == "use":
                try:
                    use, space, region = cmd.split(" ")
                    if region in regions:
                        app.use(space, region)
                    else:
                        print("Invalid region")
                        for region in regions:
                            print("[+] " + region)
                        print("Usage: use space_name region_name [ex: use my-tes-space nyc3]")

                except:
                    print("Usage: use space_name region_name [ex: use my-tes-space nyc3]")
        elif cmd[:7] == 'destroy':

            print("Format: space_name region [Ex: my-test-space nyc3]")
            space_name = input("Please type the name. not the number -> ")
            print("We are still working on a security feature to make the user ...")
            print("... is 100% sure that they know what they are doing ")
            print("Sorry :( ")
        elif cmd[:6] == "upload":
            try:
                new = cmd[7:]
                a, b, c = new.split(":")
                space = a.strip()
                region, file = b.split("->")
                detect = os.path.isfile(str(file))
                if detect:
                    if len(c) > 0:
                        app.upload_file(file, space, region, c)
                    else:
                        print("Invalid FileName to put on the space")
                        print("Usage: upload space_name:region->file_on_local_disk:name_when_uploaded")
                        print("EX: upload myspace:nyc3->my-file-from-disk:output-name.txt")
                        print("Type 'list' to view spaces")
                else:
                    print("File Not Found")
                    print("Usage: upload space_name:region->file_on_local_disk:name_when_uploaded")
                    print("EX: upload myspace:nyc3->my-file-from-disk:output-name.txt")
                    print("Type 'list' to view spaces")
            except:
                print("Error")
                print("Usage: upload space_name:region->file_on_local_disk:name_when_uploaded")
                print("EX: upload myspace:nyc3->my-file-from-disk:output-name.txt")
                print("Type 'list' to view spaces")
        elif cmd[:7] == "list in":
            try:
                spaces_a = ['ams3', 'nyc3', 'sgp1', 'sfo2']
                l, a, space_name, region = cmd.split(" ")
                if region.strip() in spaces_a:
                    app.show(space_name, region)
                else:
                    print('Invalid Space_region')
                    print('Available Regions')
                    for region in spaces_a:
                        print("[+] " + region)
                    print("Usage: [ex: list in my-test-space nyc3]")
            except:
                print("Usage: list in space_name region_name [ex: list in my-test-space nyc3]")
        else:
            print("Unknow Command")
while True:
    pol = (input("->"))
    choice = pol.lower()
    if choice == "help":
        help()
    elif choice.strip() == "spaces":
        spaces()
    else:
        print("Unknown option - Type help to get options")
