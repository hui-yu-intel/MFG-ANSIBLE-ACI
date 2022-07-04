import sys
import os
import time

info='ansible-galaxy init '+sys.argv[1] +' --force'
print(info)
os.system(info)
info='chmod -R 777 '+sys.argv[1]+'/files'
print(info)
os.system(info)
info='chmod -R 777 '+sys.argv[1]+'/vars'
print(info)
os.system(info)
info='cp ansible.cfg '+sys.argv[1]+'/ansible.cfg'
print(info)
os.system(info)
info='cp .gitignore '+sys.argv[1]+'/.gitignore'
print(info)
os.system(info)

time.sleep(2)


path=sys.argv[1]+'/'+sys.argv[1]+'.yaml'
with open(path,'a') as contents:
    info= ("---\n")
    contents.write(info)
    info= ("- name: File CleanUp and Processing before the Change\n")
    contents.write(info)
    info= ("  hosts: localhost\n")
    contents.write(info)
    info= ("  connection: local\n")
    contents.write(info)
    info= ("  gather_facts: no\n")
    contents.write(info)
    info= ("  vars_files:\n")
    contents.write(info)
    info= ("    - ../../vars/global.yaml  \n")
    contents.write(info)
    info= ("\n")
    contents.write(info)
    info= ("\n")
    contents.write(info)
    info= ("  roles:\n")
    contents.write(info)
    info= ("  - pre_file_processing\n")
    contents.write(info)
    info= ("  - validate_apic_id\n")
    contents.write(info)
    info= ("\n")
    contents.write(info)
    info= ("- name: tasks related to ACI  \n")
    contents.write(info)
    info= ("  hosts: all\n")
    contents.write(info)
    info= ("  connection: local\n")
    contents.write(info)
    info= ("  gather_facts: no\n")
    contents.write(info)
    info= ("  vars_files:\n")
    contents.write(info)
    info= ("    - ../../vars/global.yaml\n")
    contents.write(info)
    info= ("\n")
    contents.write(info)
    info= ("  roles:\n")
    contents.write(info)
    info= ("  - create_snapshot_before_change\n")
    contents.write(info)
    info= ("\n")
    contents.write(info)
    info= ("\n")
    contents.write(info)
    info= ("  #related to the role/project\n")
    contents.write(info)
    num=sys.argv[2]
    if int(num)>0:
        for i in range(0, int(num)):
            info="  - "+sys.argv[3+i]+"\n"
            contents.write(info)
        # info= ("  - "+sys.argv[1]+"\n")
        # contents.write(info)
        info= ("  - create_snapshot_after_change\n")
        contents.write(info)
    # else:
    #     info= ("  tasks:\n")
    #     contents.write(info)
    info= ("\n")
    contents.write(info)
    info= ("- name: File CleanUp after the Change\n")
    contents.write(info)
    info= ("  hosts: localhost\n")
    contents.write(info)
    info= ("  connection: local\n")
    contents.write(info)
    info= ("  gather_facts: no\n")
    contents.write(info)
    info= ("  vars_files:\n")
    contents.write(info)
    info= ("    - ../../vars/global.yaml\n")
    contents.write(info)
    info= ("  \n")
    contents.write(info)
    info= ("  roles:\n")
    contents.write(info)
    info= ("  - post_file_cleanup\n")
    contents.write(info)

path=sys.argv[1]+'/meta/main.yml'
with open(path,'r') as contents:
    filedata=contents.read()
filedata = filedata.replace('  author: your name', '  author: '+sys.argv[3+int(sys.argv[2])])
filedata = filedata.replace('  description: your role description', '  description: '+sys.argv[4+int(sys.argv[2])])
filedata = filedata.replace('  company: your company (optional)', '  company: Intel')
with open(path,'w') as contents:
    contents.write(filedata)
