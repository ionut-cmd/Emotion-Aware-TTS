from os import listdir
from os.path import isfile, join

source = "dataverse/wavs/speaker2"
# speaker_1 = 'dataverse/wavs/speaker1'
# speaker_2 = 'dataverse/wavs/speaker2'

onlyfiles = [f for f in listdir(source) if isfile(join(source, f))]

print(onlyfiles[0].split("_")[2].removesuffix(".wav"))
for f in onlyfiles:
    new_f = open(source+"/"+f.removesuffix(".wav")+ ".lab", "a")
    # print(source+"/"+f.removesuffix(".wav")+ ".lab")
    new_f.write("say the word "+ f.split("_")[2].removesuffix(".wav"))
    # print("say the word "+ f.split("_")[1].removesuffix(".wav")+".")
    new_f.close()


