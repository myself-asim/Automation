import subprocess

def packageInstaller(package, name):

	installer = subprocess.run(package, shell=True, capture_output=True, text=True)

	if installer.stderr:

		print(f"{package} Is Not Installed Because Of Some Issue")

	else:

		print(f"{name} Is Installed")


# List With The Commands Of Packages
commands = ['sudo apt update', 'sudo apt upgrade']
names = ['Update', 'Upgrade']

for i in range(0, len(names)):

	packageInstaller(commands[i], names[i])


