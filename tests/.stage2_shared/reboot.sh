ansible -i libvirt-inventory.py consul_server,consul_client -b  -m reboot -a "reboot_timeout=300"
ansible -i libvirt-inventory.py consul_server,consul_client -m wait_for -a "port=22 timeout=300"
