import subprocess
import shlex
cmd = 'dir'
args = shlex.split(cmd)
p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
result = p.communicate()[0]
print(result.decode('cp866'))
