import json
import subprocess                                 

container_lookup = {}
def get_service_name(address):
    # remove port
    ip = ".".join(address.split(".")[:-1])
    return container_lookup.get(ip, ip)

lines = []
lines.append("digraph docker {")

with open('inspect.json', 'r') as fh:
    networks = json.load(fh)
    for network in networks:
        for k, container in network['Containers'].items():
            ip = container['IPv4Address'].split('/')[0]
            service_name = container['Name']
            container_lookup[ip] = service_name
            lines.append(f'    "{service_name}" [label="{service_name}",shape=box,fillcolor="paleturquoise",style="filled,rounded"];')

pairs = subprocess.getoutput("sh fetch-results.sh").split("\n")
deduped_pairs = []
for pair in pairs:
    src, dst = [get_service_name(x) for x in pair.split(" ")]
    deduped_pairs.append((src, dst))

deduped_pairs = list(set((a,b) if a<=b else (b,a) for a,b in deduped_pairs))
for src, dst in deduped_pairs:
    lines.append(f'    "{src}" -> "{dst}" [dir="both"]')

lines.append("}")
print("\n".join(lines))

