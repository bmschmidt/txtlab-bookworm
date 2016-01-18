import pandas as pd
import json
import os
import sys

def csv_to_jsoncatalog(filename):
    a = pd.read_csv(filename)
    output = open("jsoncatalog.txt","w")
    columns = list(a.columns)

    for row in a.iterrows():
        indexed = row[1]
        metadata=dict()
        for key in columns:
            metadata[key] = indexed[key]
        output.write(json.dumps(metadata) + "\n")


def dir_to_inputDOTtxt(dirname):
    destination = open("input.txt","w")
    for (root,dirs,files) in os.walk(dirname): 
        for name in files:
            path = os.path.join(root,name)
            content = open(path).read().replace("\n"," ").replace("\t"," ").replace("\r"," ")
            identity = path.replace(dirname,"").strip("/")
            destination.write(identity + "\t" + content + "\n")

if __name__=="__main__":
    if sys.argv[1]=="metadata":
        csv_to_jsoncatalog("metadata.csv")
    elif sys.argv[1]=="input.txt":
        dir_to_inputDOTtxt("novels/2_txtalb_Novel450")
    else:
        print "whoops"
