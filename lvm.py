import os

def lvm():
    while True :
        os.system("clear")
        os.system("tput setaf 2")
        print("\n\t************* Welcome to LVM Menu Program *****************")
        os.system("tput setaf 7")
        print("PRESS 1 : Information about hardisk")
        print("PRESS 2 : Create Physical Volume")
        print("PRESS 3 : Create Volume Group")
        print("PRESS 4 : LVM or Create & format & mount the  Partition")
        print("PRESS 5 : Extend the size of volume")
        print("PRESS 6 : Exit")
        os.system("tput setaf 3\n")
        ch = int(input("Enter your choice : "))
        os.system("tput setaf 7")

        if ch == 1:
            os.system("fdisk -l")
            input("Press any key to go back.")
            menu()

        elif ch == 2:
            os.system("fdisk -l")
            pv = input("\nEnter the hard disk that you want to create as physical volume (eg. /dev/sdb) : ")
            print(os.system(("pvcreate {}".format(pv))))
            os.system("tput setaf 2")
            os.system("pvdisplay")
            os.system("tput setaf 3")
            input("Press any key to go back.")
            lvm()
		
        elif ch == 3:
            os.system("pvdisplay")
            vg_name = input("\nEnter name for Volume Group : ")
            pv = input("\nEnter the name of Physical Volume that will give space to Volume Group (eg. /dev/sdb3): ")
            print(os.system(("vgcreate  {}  {}".format(vg_name,pv))))
            os.system("tput setaf 2")
            os.system("vgdisplay")
            os.system("tput setaf 3")
            input("Press any key to go back.")
            lvm()
	
        elif ch == 4 :
            pa = input("\nEnter the LV size you want to create in GiB (eg. 10G): ")
            pa_name = input("\nEnter the name of LV: ")
            print(os.system("vgdisplay"))
            vg = input("\nEnter Volume Group from which you want to create LV: ")
            print(os.system(("lvcreate --size {}  --name {}  {}".format(pa, pa_name, vg))))			
            os.system("tput setaf 2")
            print(os.system("mkfs.ext4  /dev/{}/{}".format(vg, pa_name)))
            dir = input("\nEnter the directory to which you want to mount the partition : ")
            print(os.system("mount /dev/{}/{} {}".format(vg, pa_name, dir)))
            os.system("tput setaf 2")
            print("\nPartition Mounted!")		
            print("\nLOGICAL VOLUME CREATED!")
            os.system("tput setaf 7")
            os.system("lvdisplay")
            os.system("tput setaf 3")
            input("Press any key to go back.")
            lvm()

        elif ch == 5:
            os.system("vgdisplay")
            vg = input("\nEnter Volume Group from which you want to extend: ")
            lve = input("\nEnter the size how much you want to extend: ")	
            pa_name = input("\nEnter the name of LV to extend: ")
            os.system("tput setaf 2")
            print("\nFormatting the extend partition... ")
            os.system("tput setaf 7")
            print(os.system("lvextend  --size {} /dev/{}/{}".format(lve,vg,pa_name)))			
            print(os.system("resize2fs /dev/{}/{}".format(vg,pa_name)))
            os.system("tput setaf 3")
            input("Press any key to go back.")
            lvm()

        elif ch == 6:
            os.system("tput setaf 3")
            input("Press any key to quit...")
            exit()

        else:
            os.system("tput setaf 2")
            print("INVALID CHOICE!")
            os.system("tput setaf 3")
            input("Press any key to go back.")
            lvm()

lvm()
