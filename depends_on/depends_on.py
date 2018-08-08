import argparse

import yaml


def generate_dot(dc):
    """
    Generates a dot format graph of docker-compose depends_on between services

    :param dict dc: Docker comppose configuration loaded as a python dict
    :rtype: string
    """
    lines = []
    lines.append("digraph docker {")
    for service_name, service in dc["services"].items():
        lines.append(
            f'    "{service_name}" [label="{service_name}",shape=box,fillcolor="paleturquoise",style="filled,rounded"];'
        )
        for dep in service.get("depends_on", []):
            lines.append(f'    "{service_name}" -> "{dep}" [label = "depends_on"]')
    lines.append("}")
    return "\n".join(lines)


def main_parser():
    parser = argparse.ArgumentParser("Generate depends_on dot graph")
    parser.add_argument(
        "docker_compose_file", help="Path to a valid docker-compose.yml file"
    )
    return parser


def main():
    parser = main_parser()
    args = parser.parse_args()

    with open(args.docker_compose_file, "r") as fh:
        dc_config = yaml.load(fh)
        dot = generate_dot(dc_config)
        print(dot)


if __name__ == "__main__":
    main()

