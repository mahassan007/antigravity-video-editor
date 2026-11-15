"""Extract reference snapshots and log likely scene changes with timestamps."""

import argparse
from pathlib import Path
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference", type=Path)
    parser.add_argument("output_directory", type=Path)
    args = parser.parse_args()

    if not args.reference.is_file():
        parser.error(f"Reference video does not exist: {args.reference}")
    args.output_directory.mkdir(parents=True, exist_ok=True)
    if any(args.output_directory.iterdir()):
        parser.error("Choose an empty output directory for reference snapshots.")

    command = ["ffmpeg", "-hide_banner", "-nostdin", "-i", str(args.reference.resolve())]
    with (args.output_directory / "scene-changes.txt").open("w", encoding="utf-8") as log:
        subprocess.run(
            [*command, "-an", "-vf", "scdet=threshold=10", "-f", "null", "-"],
            stderr=log,
            check=True,
        )
    subprocess.run(
        [
            *command, "-an", "-vf", "fps=2,scale=480:-2",
            "-start_number", "0", str(args.output_directory / "frame-%06d.jpg"),
        ],
        stderr=subprocess.PIPE,
        check=True,
    )
    print("Frame numbers represent nominal half-second positions. See scene-changes.txt for detected cuts.")


if __name__ == "__main__":
    main()
