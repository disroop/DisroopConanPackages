#!/usr/bin/python
import argparse
import os

from conanbuilder.configreader import ConfigReader
from conanbuilder.runner import Runner

def get_args():
    cwd = os.getcwd()
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=str, required=False, default=cwd,
                        help="Path to root folder of multipackage module")
    parser.add_argument("--config", type=str, required=False, default=f"{cwd}/config-build.json",
                        help="Path to config-build.json")
    parser.add_argument("--sources", action="store_true", required=False, help="Download sources to PACKAGE-PATH/tmp")
    parser.add_argument("--create", action="store_true", required=False, help="Create all packages")
    parser.add_argument("--sourcesremove", action="store_true", required=False, help="Remove all sources")
    parser.add_argument("--uploadrepository", type=str, required=False, help="Upload all packages to repository")
    parser.add_argument("--user", type=str, required=False, help="User credentials")
    parser.add_argument("--token", type=str, required=False, help="Access token")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args();
    config_reader = ConfigReader(args.config)
    config_reader.read()
    runner = Runner(args.root, config_reader.get_signature())
    if args.create:
        runner.export_all()
        runner.create_all(config_reader.get_configurations())
    if args.sources:
        runner.get_all_sources()
    if args.sourcesremove:
        runner.remove_all_sources()

    # create_all(packages,config_reader.get_configurations())
    # packages[0].get_build_order(config_reader.get_configurations()[0])
