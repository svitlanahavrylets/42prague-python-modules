import sys
import site
import os


def is_in_venv() -> bool:
    """Check if the script is running inside a virtual environment."""
    return sys.prefix != sys.base_prefix


def main() -> None:
    """Display environment status depending on whether venv is active."""
    if not is_in_venv():
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")
    else:
        env_path = sys.prefix
        env_name = os.path.basename(env_path)

        site_packages_list = site.getsitepackages()
        site_packages_path = (
            site_packages_list[0] if site_packages_list else "Unknown"
        )

        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print("Package installation path:")
        print(site_packages_path)


if __name__ == "__main__":
    main()
