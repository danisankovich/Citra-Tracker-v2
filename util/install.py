
def install(package):
    print(f'Installing [{package}]')
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    print(f'Installed package [{package}].')
