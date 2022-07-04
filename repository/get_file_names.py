import glob
list=glob.glob("/ANSIBLE_DEVELOPMENT/MFG/ACI/examples_from_hui/aci_empty_project/repository/*.yml")
for i in list:
    print(i)