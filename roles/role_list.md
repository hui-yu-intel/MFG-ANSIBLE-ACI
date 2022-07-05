|roles|summary|prerequisite role(s)|
| :---         |     :---      | :---      |
|create_aci_access_port_block_to_access_port|Create port blocks of Fabric interface policy leaf profile interface selectors on Cisco ACI fabrics|N/A|
|create_aci_access_port_to_interface_policy_leaf_profile|Create Fabric interface policy leaf profile interface selectors on Cisco ACI fabrics|N/A|
|create_aci_aep_to_domain|Bind AEPs to Physical or Virtual Domains on Cisco ACI fabrics|aci_domain|
|create_aci_aep_to_vmm_domain|Bind AEPs to Physical or Virtual Domains on Cisco ACI fabrics|aci_aep|
|create_aci_aep|Connect to external virtual and physical domains by using attachable Access Entity Profiles (AEP) on Cisco ACI fabrics|N/A|
|create_aci_ap|Create top level Application Profile (AP) objects on Cisco ACI fabrics|N/A|
|create_aci_bd_subnet|Create Subnets on Cisco ACI fabrics|aci_tenant|
|create_aci_bd_to_l3out|Bind Bridge Domain to L3 Out on Cisco ACI fabrics|aci_tenant,aci_bd,aci_l3out|
|create_aci_bd|Create Bridge Domains (BD) on Cisco ACI fabrics|aci_tenant|
|create_aci_config_snapshot|Create a snapshot|N/A|
|create_aci_contract_subject|Create initial Contract Subjects on Cisco ACI fabrics|aci_tenant|
|create_aci_contract|Create Contract resources on Cisco ACI fabrics|aci_tenant|
|create_aci_domain_to_encap_pool|Bind Domain to Encap Pools on Cisco ACI fabrics|aci_vlan_pool|
|create_aci_domain_to_vlan_pool|Bind Domain to VLAN Pools on Cisco ACI fabrics|aci_domain|
|create_aci_domain|Create physical, virtual, bridged, routed or FC domain profiles on Cisco ACI fabrics|N/A|
|create_aci_epg_to_domain|Bind EPGs to Physical and Virtual Domains on Cisco ACI fabrics|aci_tenant,aci_ap,aci_epg|
|create_aci_epg_to_vmm_domain|Bind EPGs to Physical and Virtual Domains on Cisco ACI fabrics|aci_tenant,aci_ap,aci_epg|
|create_aci_epg|Create End Point Groups (EPG) on Cisco ACI fabrics|aci_tenant,aci_ap|
|create_aci_fabric_node|Create Fabric Node Members on Cisco ACI fabrics|N/A|
|create_aci_filter|Create top level filter objects on Cisco ACI fabrics|N/A|
|create_aci_interface_policy_leaf_policy_group_nonvpc|Create nonvpc fabric interface policy leaf policy groups on Cisco ACI fabrics|aci_aep|
|create_aci_interface_policy_leaf_policy_group|Create vpc fabric interface policy leaf policy groups on Cisco ACI fabrics|aci_aep|
|create_aci_interface_policy_leaf_profile|Create fabric interface policy leaf profiles on Cisco ACI fabric|N/A|
|create_aci_l3out_extepg|Create External Network Instance Profile (ExtEpg) objects|aci_l3out|
|create_aci_l3out_extsubnet|Create External Subnet objects (l3extSubnet:extsubnet)|aci_l3out,aci_tenant|
|create_aci_l3out|Create Layer 3 Outside (L3Out) on Cisco ACI fabrics|aci_tenant,aci_vrf,aci_domain|
|create_aci_static_binding_to_epg|Bind static paths to EPGs on Cisco ACI fabrics|aci_tenant,aci_ap,aci_epg,aci_interface_policy_leaf_policy_group|
|create_aci_switch_leaf_selector|Bind leaf selectors (with node block range and policy group) to switch policy leaf profiles on Cisco ACI fabrics|N/A|
|create_aci_switch_policy_leaf_profile|Create switch policy leaf profiles on Cisco ACI fabrics|N/A|
|create_aci_switch_policy_vpc_protection_group|Create switch policy explicit vPC protection groups on Cisco ACI fabrics|N/A|
|create_aci_tenant|Create tenants on Cisco ACI fabrics|N/A|
|create_aci_vlan_pool_encap_block|Create VLAN encap blocks that are assigned to VLAN pools on Cisco ACI fabrics|N/A|
|create_aci_vlan_pool|Create VLAN pools on Cisco ACI fabrics|N/A|
|create_aci_vmm_credential|Create virtual domain credential profiles on Cisco ACI fabrics|aci_vmm_domain|
|create_aci_vmm_domain|Create virtual domain credential profiles on Cisco ACI fabrics|N/A|
|create_aci_vrf|Create contexts or VRFs on Cisco ACI fabrics|N/A|
|create_bfdIfPol|It will Attach BFD Interface Policy to Node Interface Profiles|aci_tenant,aci_l3out,aci_switch_policy_leaf_profile|
|create_bfdIfP|Create BFD Interface Policy for User Tenant|N/A|
|create_dhcpLbl|Map DHCP Relay Label to Bridge Domain|N/A|
|create_dhcpRelayP|Create User Tenant DHCP Relay Policy|aci_tenant|
|create_eigrpIfPol|Attach EIGRP Interface Policy to Node Interface Profiles|aci_l3out,aci_tenant,aci_switch_policy_leaf_profile|
|create_eigrpIfP|Create EIGRP Interface Profile in user tenant|N/A|
|create_fvAEPg|Inherit EPG|aci_tenant,aci_ap|
|create_fvRsCons|Create EPG Consumer|aci_tenant,aci_ap,aci_epg|
|create_fvRsDomAtt|Attach enhanced LAG to VMM Domain in EPG Mapping|aci_tenant,aci_ap,aci_epg|
|create_fvRsProv|Create EPG Provider|aci_tenant,aci_ap,aci_epg|
|create_infraNodeP|Map Interface Profile to Switch Profile|aci_switch_policy_leaf_profile,aci_interface_policy_leaf_profile|
|create_l3extInstP_fvRsCons|Create Consumer in L3out Ext EPGs|aci_tenant,aci_ap,aci_l3out_extepg|
|create_l3extInstP_fvRsProv|Create Provider in L3out Ext EPGs|aci_tenant,aci_ap,aci_l3out_extepg|
|create_l3extInstP|Set Preferred Group for EXT-EPG|aci_l3out,aci_tenant|
|create_l3extLIfP|Create L3Out Logical Interface Profiles|aci_l3out,aci_tenant,aci_switch_policy_leaf_profile|
|create_l3extLNodeP|Create L3Out Node Profiles|aci_l3out,aci_tenant|
|create_l3extRsNodeL3OutAtt|Add Nodes to L3out Node Profiles|aci_l3out,aci_tenant|
|create_l3extRsPathL3OutAtt|Configure L3Out P-2-P Interface IP Addresses|aci_l3out,aci_tenant,aci_switch_policy_leaf_profile|
|create_mgmtRsOoBStNode|Configure Switch OOB Mgmt IP Addressing|N/A|
|create_snapshot_before_change|Create a snapshot before the change|N/A|
|create_snapshot_after_change|Create a snapshot after the change|N/A|
|create_snmpCommunityPv3|Create new SNMPv3 Community String|N/A|
|create_snmpTrapDestv3|Add new SNMP v3 Trap Receivers to snmp Dest Group|N/A|
|create_snmpTrapFwdServerPv3|Add SNMP v3 SNMP Policy Trap Forwarders|N/A|
|create_snmpUserPv3|Create SNMPv3 Username and Auth attributes|N/A|
|create_vmmCtrlrP|Add vCenter Controler to VMware VMM domain|N/A|
|create_vmmDomP|Configure VSwitch Policy for VMM Domain with enhanced LAG|N/A|
|create_vzBrCP|Add Filters to Create Contracts|aci_tenant,aci_contract|
|create_vzFilter|Add filter details|aci_tenant|
|delete_snmpTrapDestv2|Delete SNMP v2 Trap Receivers to snmp Dest Group|N/A|
|delete_snmpTrapFwdServerPv2|Delete SNMP v2 SNMP Policy Trap Forwarders|N/A|