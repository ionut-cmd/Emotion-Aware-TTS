import csv
from os import listdir
from os.path import isfile, join


def write_csv(filename, rows):
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows
        csvwriter.writerows(rows)


if __name__ == '__main__':

    mypath = "dataverse_files/wavs/"

    onlyfiles = [f for f in listdir(mypath) if isfile(
        join(mypath, f))]
    emotion = "metadata_emotion.csv"
    no_emotion = "metadata.csv"
    rows = []
    emotion_rows = []
    no_emotion_rows = []
    for i in range(len(onlyfiles)):
        rows.append(onlyfiles[i].removesuffix(".wav").split("_"))
    print(rows[0])

    for i in range(len(rows)):
        a = []
        b = []
        a.append(f"{rows[i][0]}|say the word {rows[i][1]}")
        b.append(
            f"{rows[i][0]}|say the word {rows[i][1]}|{rows[i][2]}")
        emotion_rows.append(a)
        no_emotion_rows.append(b)

    print(emotion_rows[0])
    print(no_emotion_rows[0])
    write_csv(emotion, emotion_rows)
    write_csv(no_emotion, no_emotion_rows)
