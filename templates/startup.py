#!/usr/bin/env python
import systemd.daemon
import time
import subprocess
import sys

cmd = ["consul", "agent", "-config-dir", "{{app.value.consul.user.home}}/consul/conf"]
{% if not app.value.consul.configs.server|default(False) %}
cmd.extend(["-config-dir", "/app/shared/consul/conf"])
{% endif %}
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=sys.stdout.fileno())

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
