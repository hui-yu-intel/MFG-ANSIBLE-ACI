import sys
import os
import time

file1 = open(sys.argv[1], 'r')
Lines = file1.readlines()
templine=''
templist=[]

for line in Lines:
    templine=line.strip().split('||')

    info='ansible-galaxy init create_'+templine[0] +' --force'
    print(info)
    os.system(info)
    info='chmod -R 777 create_'+templine[0]+'/files'
    print(info)
    os.system(info)
    info='chmod -R 777 create_'+templine[0]+'/vars'
    print(info)
    os.system(info)
    info='cp ansible.cfg create_'+templine[0]+'/ansible.cfg'
    print(info)
    os.system(info)
    info='cp .gitignore create_'+templine[0]+'/.gitignore'
    print(info)
    os.system(info)

    time.sleep(2)
    path='create_'+templine[0]+'/tasks/main.yml'
    with open(path,'a') as contents:
        print("- include_vars:")
        info="- include_vars:\n"
        contents.write(info)
        num='1'
        for i in range(0, int(num)):
            info1="   dir: \"{{path}}/vars/vars_wip\""
            info="   dir: \"{{path}}/vars/vars_wip\"\n"
            contents.write(info)
            print (info1)
        print("#Execute create_"+templine[0])
        info="#Execute create_"+templine[0]+"\n"
        contents.write(info)
        info1="- include_tasks: \"{{repository_path}}/pre_query_" +templine[0]+".yml\""
        info="- include_tasks: \"{{repository_path}}/pre_query_" +templine[0]+".yml\"\n"
        print (info1)
        contents.write(info) 
        if(templine[3].find('N/A')==-1):
            #has pre-requisite:
            templist=templine[3].split(',')
            for i in range (len(templist)-1):
                info1="- include_tasks: \"{{repository_path}}/post_query_" +templist[i]+".yml\""
                info="- include_tasks: \"{{repository_path}}/post_query_" +templist[i]+".yml\"\n"
                print (info1)
                contents.write(info)  
           
        info1="- include_tasks: \"{{repository_path}}/create_" +templine[0]+".yml\""
        info="- include_tasks: \"{{repository_path}}/create_" +templine[0]+".yml\"\n"
        print (info1)
        contents.write(info)
        info1="- include_tasks: \"{{repository_path}}/post_query_" +templine[0]+".yml\""
        info="- include_tasks: \"{{repository_path}}/post_query_" +templine[0]+".yml\"\n"
        print (info1)
        contents.write(info)

    path='create_'+templine[0]+'/'+templine[0]+'.yaml'
    with open(path,'a') as contents:
        info= ("---\n")
        contents.write(info)
        info=("\n")
        contents.write(info)
        info=("########################################################################\n")
        contents.write(info)
        info=("#"+templine[1]+"\n")
        contents.write(info)
        info=("#Owner: "+templine[2]+"\n")
        contents.write(info)
        info=("#Prerequisites: "+templine[3]+"\n")
        contents.write(info)
        info=("########################################################################\n")
        contents.write(info)
        info=("\n")
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
        info= ("  - create_"+templine[0]+"\n")
        contents.write(info)
        info= ("  - create_snapshot_after_change\n")
        contents.write(info)
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
    
    path='create_'+templine[0]+'/meta/main.yml'
    with open(path,'r') as contents:
        filedata=contents.read()
    filedata = filedata.replace('  author: your name', '  author: '+templine[2])
    filedata = filedata.replace('  description: your role description', '  description: '+templine[1])
    filedata = filedata.replace('  company: your company (optional)', '  company: Intel')
    with open(path,'w') as contents:
        contents.write(filedata)
