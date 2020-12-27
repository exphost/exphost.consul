#!/bin/bash
result=0
trap 'result=1' ERR
chmod 400 ssh_config
py.test --hosts='ansible://consul_server' --ansible-inventory=./libvirt-inventory.py --ssh-config ssh_config --color=yes verify_server.d
py.test --hosts='ansible://consul_client' --ansible-inventory=./libvirt-inventory.py --ssh-config ssh_config --color=yes verify_client.d
exit $result
