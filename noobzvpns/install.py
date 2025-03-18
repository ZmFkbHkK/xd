import os
import subprocess
import time
import requests

# =====================================================
# Installer noobzvpns with python3 by xdxl
# =====================================================

#os.system('clear')

#print(f"[ {time.ctime()} ] Processed Install noobzvpns service")
time.sleep(2)

os.makedirs('/etc/noobzvpns', exist_ok=True)
open('/etc/noobzvpns/users.json', 'a').close()

if os.path.isfile('/usr/bin/noobzvpns'):
    os.remove('/usr/bin/noobzvpns')

noobzvpns_url = "https://raw.githubusercontent.com/ZmFkbHkK/xd/main/noobzvpns/noobzvpns.x86-64"
response = requests.get(noobzvpns_url)
with open('/usr/bin/noobzvpns', 'wb') as f:
    f.write(response.content)
os.chmod('/usr/bin/noobzvpns', 0o777)

config_url = "https://raw.githubusercontent.com/ZmFkbHkK/xd/main/noobzvpns/config.toml"
response = requests.get(config_url)
with open('/etc/noobzvpns/config.toml', 'wb') as f:
    f.write(response.content)

service_url = "https://raw.githubusercontent.com/ZmFkbHkK/xd/main/noobzvpns/noobzvpns.service"
response = requests.get(service_url)
with open('/etc/systemd/system/noobzvpns.service', 'wb') as f:
    f.write(response.content)

subprocess.run(['systemctl', 'daemon-reload'])
subprocess.run(['systemctl', 'enable', 'noobzvpns'])
subprocess.run(['systemctl', 'restart', 'noobzvpns'])

#print(f"[ {time.ctime()} ] Install noobzvpns service Done")
