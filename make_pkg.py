import os

# Define package name and paths
package_name = "lib"
base_path = os.getcwd()
package_path = os.path.join(base_path, package_name)

# Create the lib folder
os.makedirs(package_path, exist_ok=True)

# Create __init__.py with a sample function
init_file_path = os.path.join(package_path, "__init__.py")
with open(init_file_path, "w") as f:
    f.write('''\
def hello():
    return "Hello from lib!"
''')

print(f"✅ Package '{package_name}' created at: {package_path}")
print(f"✅ Sample __init__.py added.")
