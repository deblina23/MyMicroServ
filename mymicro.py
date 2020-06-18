#! /usr/bin/env python3
import subprocess,rest2,rest1
result2= int(rest2.resp.status_code)
result1=int(rest1.resp.status_code)
sum=int(result1+result2)
input='a'+ str(sum)
subprocess.call(['sed', '-i',  input, 'output.txt'])
