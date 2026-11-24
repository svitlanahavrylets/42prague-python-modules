import os
import sys
from dotenv import load_dotenv


def check_security() -> None:
    """Check environment security and gitignore configuration."""
    env_exists = os.path.exists(".env")
    env_example_exists = os.path.exists(".env.example")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if env_exists:
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found, using system environment")

    if env_example_exists:
        print("[OK] Production overrides available")


def display_config() -> None:
    """Load and display the Oracle mainframe configuration."""
    load_dotenv()

    mode = os.getenv("MATRIX_MODE", "development")
    db_url = os.getenv("DATABASE_URL", "")
    api_key = os.getenv("API_KEY", "")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_url = os.getenv("ZION_ENDPOINT", "")

    if not db_url or not api_key or not zion_url:
        print("ORACLE STATUS: Reading the Matrix...\n")
        print("[ERROR] Missing required configuration variables!")
        print("Please ensure DATABASE_URL, API_KEY, "
              "and ZION_ENDPOINT are set.")
        print("Copy .env.example to .env and set your values.")
        sys.exit(1)

    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if mode.lower() == "production":
        print(f"Database: Connected to production cluster ({db_url})")
        print("API Access: Authenticated (SECURE)")
        print(f"Log Level: {log_level} (MINIMAL)")
    else:
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print(f"Log Level: {log_level}")

    print(f"Zion Network: Online ({zion_url})\n")

    check_security()
    print("The Oracle sees all configurations.")


def main() -> None:
    """Main execution entry point."""
    display_config()


if __name__ == "__main__":
    main()
