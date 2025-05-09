import subprocess

def systemInfo(item, heading):

	command = subprocess.run(item, shell=True, capture_output=True, text=True)

	print(command.stdout)

l = []
names = []

for i in range(0, len(names)):

	systemInfo(item, names)


i = input([])
print(typeof(i))
