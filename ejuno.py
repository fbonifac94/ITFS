import sys;
import argparse;
import os;

parser = argparse.ArgumentParser();
parser.add_argument("-f", "--filename");
args = parser.parse_args();

try:
    fileO = open(args.filename, "r+");
    parrafos = fileO.readlines();
    newFile = open("newfile.txt", "a+")
    
    for z in parrafos:
        z = z.replace(",", "|");
        newFile.write(z);
        print(z);
        break;
except Exception as e:
    print(e);
    