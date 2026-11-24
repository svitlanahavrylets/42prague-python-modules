import importlib
import importlib.metadata
import sys
from typing import Any


def check_dependency(package_name: str, desc: str) -> bool:
    """Check if a package is available and print its version."""
    try:
        importlib.import_module(package_name)
        ver = importlib.metadata.version(package_name)
        print(f"[OK] {package_name} ({ver}) - {desc}")
        return True
    except ImportError:
        print(f"[MISSING] {package_name} - {desc}")
        return False


def run_analysis() -> None:
    """Generate Matrix data with numpy, analyze "
    "with pandas, plot with matplotlib."""
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd  # type: ignore

    matplotlib.use("Agg")

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    np.random.seed(42)
    signal_data: np.ndarray[Any, Any] = np.random.normal(
        loc=50, scale=15, size=1000
    )

    df: pd.DataFrame = pd.DataFrame(
        {"Signal_Strength": signal_data}
    )

    print("Generating visualization...")
    plt.figure(figsize=(8, 5))
    plt.hist(
        df["Signal_Strength"],
        bins=30,
        color="green",
        alpha=0.7,
        edgecolor="black"
    )
    plt.title("Matrix Signal Distribution")
    plt.xlabel("Signal Strength")
    plt.ylabel("Frequency")
    plt.grid(True, linestyle="--", alpha=0.6)

    output_file: str = "matrix_analysis.png"
    plt.savefig(output_file)
    plt.close()

    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def print_missing_instructions() -> None:
    """Print instructions when dependencies are missing."""
    print("\n[ERROR] Missing required dependencies.")
    print("\nTo install via pip, run:")
    print("  pip install -r requirements.txt")
    print("\nTo install via Poetry, run:")
    print("  poetry install")
    print("  poetry run python loading.py")


def main() -> None:
    """Main execution block."""
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    dependencies: list[tuple[str, str]] = [
        ("pandas", "Data manipulation ready"),
        ("numpy", "Numerical computation ready"),
        ("matplotlib", "Visualization ready"),
    ]

    all_ok: bool = True
    for pkg, desc in dependencies:
        if not check_dependency(pkg, desc):
            all_ok = False

    if not all_ok:
        print_missing_instructions()
        sys.exit(1)

    run_analysis()


if __name__ == "__main__":
    main()
