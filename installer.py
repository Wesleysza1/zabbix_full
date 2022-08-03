import subprocess

system = str(subprocess.check_output("cat /etc/*-release | grep PRETTY", shell=True))
so = system.lower()

install = str(input('Instalação Agent pressione A, Instalação Proxy pressione P:')).lower()


if "ubuntu" in so and install=='p':
    print('Instalando Zabbix-Proxy em: ' + so)
    subprocess.call(["ansible-playbook", "ubuntu-zabbix-proxy.yaml", "-K"])
elif "debian" in so and install=='p':
    print('Instalando Zabbix-Proxy em: ' + so)
    subprocess.call(["ansible-playbook", "debian-zabbix-proxy.yaml", "-K"])
elif "redhat" in so and install=='p':
    print('Instalando Zabbix-Proxy em: ' + so)
    subprocess.call(["ansible-playbook", "rhel-zabbix-proxy.yaml", "-K"])
elif "red hat" in so and install=='p': 
    print('Instalando Zabbix-Proxy em: ' + so)
    subprocess.call(["ansible-playbook", "rhel-zabbix-proxy.yaml", "-K"])
elif "centos" in so and install=='p':
    print('Instalando Zabbix-Proxy em: ' + so)
    subprocess.call(["ansible-playbook", "centos-zabbix-proxy.yaml", "-K"])
elif "suse" in so and install=='p':
    print('Instalando Zabbix-Proxy em: ' + so)
    subprocess.call(["ansible-playbook", "suse-zabbix-proxy.yaml", "-K"])
elif "ubuntu" in so and install=='a':
    print('Instalando Zabbix-Agent em: ' + so)
    subprocess.call(["ansible-playbook", "ubuntu-agent.yaml", "-K"])
elif "debian" in so and install=='a':
    print('Instalando Zabbix-Agent em: ' + so)
    subprocess.call(["ansible-playbook", "debian-agent.yaml", "-K"])
elif "redhat" in so and install=='a': 
    print('Instalando Zabbix-Agent em: ' + so)
    subprocess.call(["ansible-playbook", "rhel-agent.yaml", "-K"])
elif "red hat" in so and install=='a': 
    print('Instalando Zabbix-Agent em: ' + so)
    subprocess.call(["ansible-playbook", "rhel-agent.yaml", "-K"])
elif "centos" in so and install=='a':
    print('Instalando Zabbix-Agent em: ' + so)
    subprocess.call(["ansible-playbook", "centos-agent.yaml", "-K"])
elif "suse" in so and install=='a':
    print('Instalando Zabbix-Agent em: ' + so)
    subprocess.call(["ansible-playbook", "suse-agent.yaml", "-K"])
else:
    print("SO não suportado ou selecionado opção incorreta, tente novamente.")
