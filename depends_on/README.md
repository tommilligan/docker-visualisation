## Requirements

Requires `Python 3.6+`.

Install `graphviz`, or another drawing program that provides the `dot` command.

```
sudo apt-get install graphviz
```

Install python dependencies as specified in requirements.txt

```
pip install -r requirements.txt
```

## Run

Run like:

```
python depends_on.py docker-compose.yml | dot -Tpng -o ~/Desktop/containers.png
```

where:

- `docker-compose.yml` is a path to your docker compose file
- `~/Desktop/containers.png` is your desired output path for an image file
