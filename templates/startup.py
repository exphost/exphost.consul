#!/usr/bin/env python
import systemd.daemon
import time
import subprocess
import sys

p = subprocess.Popen(["consul", "agent", "-config-dir", "{{app.value.consul.user.home}}/consul/conf", "-config-dir", "/app/shared/consul/conf"], stdout=subprocess.PIPE, stderr=sys.stdout.fileno())

while True:
    line = p.stdout.readline()
    print(line)
    if "Consul agent running!" in line:
        break

systemd.daemon.notify('READY=1'.format(pid=p.pid))
systemd.daemon.notify('MAINPID={pid}'.format(pid=p.pid))

while True:
    line = p.stdout.readline()
    print(line)
    sys.stdout.flush()
