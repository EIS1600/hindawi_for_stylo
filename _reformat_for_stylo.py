import os, re, sys
from openiti.helper.ara import deNoise

# applies author URIs that were manually assigned in the _metadata_contributors... to book records

div1 = "##RECORD################################################################\n"
splitter = "##RECORD##+\+?\n"

##################################################################################################
# VARIABLES ######################################################################################
##################################################################################################

textsFolder = "./txt/"
targetFolder = "./stylo_selection/"

metaDataFile = "_metadata_books_man.yml"

##################################################################################################

def loadMeta(metaDataFile):
    with open(metaDataFile, "r", encoding="utf8") as f1:
        data = f1.read().split(div1)

        dic = {}

        for d in data[1:]:
            print(d)
            d = d.split("\n")

            uri = d[0].split("::::")[1].strip()
            idi  = uri[-8:]

            dic[idi] = uri

            #print(uri)
            #print(idi)
    input(len(dic))
    return(dic)

meta = loadMeta(metaDataFile)


# normalizeArabicLight(text) - fixing only Alifs, AlifMaqsuras; replacing hamzas on carriers with standalone hamzas
def normalizeArabicLight(text):
    text = re.sub("[إأٱآا]", "ا", text)
    text = re.sub("[يى]ء", "ئ", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("(ؤ)", "ء", text)
    text = re.sub("(ئ)", "ء", text)
    #text = re.sub("(ء)", "", text)
    #text = re.sub("(ة)", "ه", text)
    return(text)

noiseChar = "[\|#\*+\$%.,:;\(\)\[\]\{\}]|@[a-zA-Z]+@"

def textCleaner(text):
    text = normalizeArabicLight(text)
    text = re.sub("\W|\d|[A-z]", " ", text)
    text = re.sub(" +", " ", text)
    return(text)


def formatText(text):
    text = text.replace("", "")
    text = re.sub(r"\[1m|\[0m", "", text)
    text = deNoise(text)
    text = textCleaner(text)
    return(text)
    #


def processTexts():
    lof = os.listdir(textsFolder)

    for l in lof:
        print(l)
        if not l.startswith("."):
            test = l.split(".")[0]
            print(test)
            if test in meta:
                with open(textsFolder+l, "r", encoding="utf8") as ft:
                    textOld = ft.read()
                    textNew = formatText(textOld)
                    textNew = "OpenITI URI: "+meta[test]+"\n\n"+textNew

                    nfn = meta[test].split(".")
                    newFileName = nfn[0]+"_"+nfn[1]
                    with open(targetFolder+newFileName+".txt", "w", encoding="utf8") as f9:
                        f9.write(textNew)


processTexts()




