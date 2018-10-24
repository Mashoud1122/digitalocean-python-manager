import digitalocean
#put your droplet key here
#nothing in droplets yet
#but soon will update this code and add nice features for this
manager = digitalocean.Manager(token="YOUR+KEY+FOR+DROPLETS")
my_droplets = manager.get_all_droplets()

def list():
    for droplet in my_droplets:
        print(droplet)
