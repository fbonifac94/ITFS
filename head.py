import sys;
import argparse;
import os;

parser = argparse.ArgumentParser();
parser.add_argument("-f", "--fileName");
parser.add_argument("-n", "--number");
args = parser.parse_args();

try:
    file = open(args.fileName, "r");
    for x in range(0, int(args.number)):
        print(file.readline());
    file.close();
except Exception as e:
    print(e)
