import argparse

import yaml

from preprocessor import dataverse, emov_db


def main(config):
    if "Dataverse" in config["dataset"]:
        dataverse.prepare_align(config)
    if "EmoV_DB" in config["dataset"]:
        emov_db.prepare_align(config)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=str, help="path to preprocess.yaml")
    args = parser.parse_args()

    config = yaml.load(open(args.config, "r"), Loader=yaml.FullLoader)
    main(config)
