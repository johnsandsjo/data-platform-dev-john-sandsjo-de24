import sys
import pkg_resources


print("\n")
print(f"{sys.version =}")
print("\n")


installed_packages = pkg_resources.working_set
print(installed_packages)
for package in installed_packages:
    print(f"{package.key}=={package.version}")