import argparse
from pathlib import Path

from pipeline import run_pipeline
from utils import workspace_root


def parse_args() -> argparse.Namespace:
    root = workspace_root()
    parser = argparse.ArgumentParser(description="Multi-domain support triage agent")
    parser.add_argument("--tickets", required=True, help="Path to the input tickets CSV")
    parser.add_argument("--data", default=str(root / "data"), help="Path to the support corpus directory")
    parser.add_argument("--output", required=True, help="Path to the output CSV")
    parser.add_argument("--log", default=str(root / "run_log.txt"), help="Path to the run log inside the workspace")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run_pipeline(
        tickets_path=Path(args.tickets),
        data_dir=Path(args.data),
        output_path=Path(args.output),
        log_path=Path(args.log),
    )


if __name__ == "__main__":
    main()
