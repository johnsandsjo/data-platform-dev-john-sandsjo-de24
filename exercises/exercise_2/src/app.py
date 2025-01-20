import sys
import pkg_resources

#Now create a Python script that prints out the installed packages and the version of Python.
print("\n\n")
print(f"{sys.version =}")

installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])

for package in installed_packages_list:
    print(package)

#Now create your os_data.py app to read in athelete_events.csv as a dataframe, print out df.head(), plot a graph and export it to src folder.