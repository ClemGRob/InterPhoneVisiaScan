def get_linux_distribution():
    try:
        with open('/etc/os-release', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("ID="):
                    return line.split('=')[1].strip()
    except FileNotFoundError:
        return None

# Obtenir le nom de la distribution Linux

if __name__ == "__main__":
    linux_distribution = get_linux_distribution()
    print(linux_distribution)