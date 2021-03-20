ANSIBLE_CONFIG=fabsible.cfg ansible -i libvirt-inventory.py consul_server,consul_client -b  -m reboot -a "reboot_timeout=300"
ANSIBLE_CONFIG=fabsible.cfg ansible -i libvirt-inventory.py consul_server,consul_client -m wait_for -a "port=22 timeout=300"
