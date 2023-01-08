import shutil
from os import listdir
from os.path import isfile, join

source = "dataverse/wavs/"
speaker_1 = 'dataverse/wavs/speaker1'
speaker_2 = 'dataverse/wavs/speaker2'

onlyfiles = [f for f in listdir(source) if isfile(join(source, f))]

print(onlyfiles[0].split("_")[0])
print(source+onlyfiles[0])

for f in onlyfiles:
    if f.split("_")[0] == "YAF":
        shutil.move(source+f, speaker_1)
    elif f.split("_")[0] == "OAF":
        shutil.move(source+f, speaker_2)




# shutil.move(source, destination)
# os.listdir('/opt/awesome/source')
# ['awesome.txt']