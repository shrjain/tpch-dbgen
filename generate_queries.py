from subprocess import Popen, PIPE
import time
import os
import argparse

parser = argparse.ArgumentParser(description='Generate TPCH queries.')
parser.add_argument('--num', metavar='N', type=int, help='Number of queries per template')
parser.add_argument('-o', type=str, help='output filename')

args = parser.parse_args()

fo = open(args.o, 'w')
for i in range(1,23):
	for j in range(args.num):
		#process = Popen(["./qgen", '-r', str(j*1000+1), str(i)], stdout=PIPE)
		#(output, err) = process.communicate()
		#exit_code = process.wait()
		output = os.popen("./qgen -r {} {}".format(j*1000+1,i)).read()
		fo.write(" ".join(output.split('\n')[1:]) + '\n')
		fo.flush()
	#time.sleep(2)
fo.close()
