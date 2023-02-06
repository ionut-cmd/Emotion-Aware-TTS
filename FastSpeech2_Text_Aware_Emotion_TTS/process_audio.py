import librosa
import os

DATASET_PATH = "multiple_speekers"
JSON_PATH = "emotions.json"


def add_labels(dataset_path, json_path):
    # data dictionary

    data = {
        "mapping": [],
        "labels": [],
    }

    # loop through all the speekears
    for i, (dir_path, directories, file_names) in enumerate(os.walk(dataset_path)):
        if dir_path is not dataset_path:
            # save semantic label
            dir_path_comp = dir_path.split("/")
            semantic_label = dir_path[-1]
            data["mapping"].append(semantic_label)

            for f in file_names:
                file_path = os.path.join(dir_path, f)

    return 0
