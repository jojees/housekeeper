import XenAPI
import urllib
import urllib2
#import json
import timeit

def xen_connect(server, username, password):
    session = XenAPI.Session("http://" + server)
    session.xenapi.login_with_password(username, password)
    return session

def get_ipaddress(session, vm):
    vgm = session.xenapi.VM.get_guest_metrics(vm)
    try:
        os = session.xenapi.VM_guest_metrics.get_networks(vgm)
        if "0/ip" in os.keys():
            return os["0/ip"]
        return None
    except:
        return None
    
def get_vmlist(xen_session):
    vm_all = xen_session.xenapi.VM.get_all()
    vm_list = {}
    for vm in vm_all:
        vm_record = xen_session.xenapi.VM.get_record(vm)
        if not vm_record['is_a_snapshot'] \
            and not vm_record['is_a_template'] \
            and not vm_record['is_control_domain'] \
            and not vm_record['is_snapshot_from_vmpp']:
            ip = get_ipaddress(xen_session, vm)
            uuid = vm_record['uuid']
            vm_list[uuid] = {}
            vm_list[uuid]['name_label'] = vm_record['name_label']
            vm_list[uuid]['status'] = vm_record['power_state']
            vm_list[uuid]['cpu'] = vm_record['VCPUs_at_startup']
            vm_list[uuid]['snapshots'] = len(vm_record['snapshots'])
            vm_list[uuid]['tags'] = vm_record['tags']
            vm_list[uuid]['mem'] = round(float(vm_record['memory_static_max'])/1024/1024/1024,1)
    #print vm_list

def get_vmlist1(xen_session):
    vm_list = {}
    vm_all_records = xen_session.xenapi.VM.get_all_records()
    for key, value in vm_all_records.iteritems():
        if not value['is_a_snapshot'] \
            and not value['is_a_template'] \
            and not value['is_control_domain'] \
            and not value['is_snapshot_from_vmpp']:
            ip = get_ipaddress(xen_session, key)
            uuid = key
            vm_list[uuid] = {}
            vm_list[uuid]['name_label'] = value['name_label']
            vm_list[uuid]['status'] = value['power_state']
            vm_list[uuid]['cpu'] = value['VCPUs_at_startup']
            vm_list[uuid]['snapshots'] = len(value['snapshots'])
            vm_list[uuid]['tags'] = value['tags']
            vm_list[uuid]['mem'] = round(float(value['memory_static_max'])/1024/1024/1024,1)
    #print vm_list

xen_server = "192.168.99.102"
xen_user = "root"
xen_password = "xenpass"

xen_session = xen_connect(xen_server, xen_user, xen_password)

#vm = get_vmlist(xen_session)
#start_time = timeit.default_timer()
#get_vmlist(xen_session)
#print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
get_vmlist1(xen_session)
print(timeit.default_timer() - start_time)

xen_session.xenapi.session.logout()
