# docker network tcpdump

Visualise multiple docker networks' traffic using tcpdump

## Install

Python 3.6+, tcpdump, graphviz and parallel are required on the host system.

```
sudo apt-get install python3 tcpdump graphviz parallel
```

## Use

Find out the names of your docker networks to monitor:

- see `docker-compose.yml`
- `docker network ls`

Run `./dump.sh <network-name>` to attach tcpdump to the bridge network and dump traffic.
The process will wait while this collection occurs. Run a loadtest or similar, then press `^C` to stop collection.

Run `python graph.py` to produce a DOT format graph description of your dumped results.

Visualise this like

```
python graph.py | dot -Tpng -o ~/Desktop/tcpdump.png
```
