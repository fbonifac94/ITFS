import sys;
import argparse;
import os;

parser = argparse.ArgumentParser();
parser.add_argument("-f", "--fileName");
parser.add_argument("-p", "--path");
args = parser.parse_args();

try:
	fileToCp = open(args.fileName, "r");
	parrafos = fileToCp.readlines();
	fileName = args.path + fileToCp.name if args.path != None else fileToCp.name;
	fileToCp.close();
	for z in os.listdir(args.path):
		if z == args.fileName:
			fileName = fileName.replace(".", "_2.");
			break;

	cpFile = open(fileName, "a+");

	for x in parrafos:
		cpFile.write(x);

	cpFile.seek(0);
	cpFile.close();
except Exception as e:
	print(e);