#!/usr/bin/env python3
"""
ACCELR8 Deck Builder - Asset Generator

Generates images with nanobanana and optionally removes backgrounds.

Usage:
    python generate_asset.py --prompt "a person presenting" --output speaker.png --remove-bg
    python generate_asset.py --prompt "abstract gradient" --output bg.png
    python generate_asset.py --input existing.png --output clean.png --remove-bg
"""

import argparse
import subprocess
import sys
from pathlib import Path


def generate_image(prompt: str, output: str, resolution: str = "2K") -> bool:
    """Generate image using nanobanana."""

    # Find nanobanana script
    nanobanana_paths = [
        Path.home() / ".codex/skills/nano-banana-pro/scripts/generate_image.py",
        Path.home() / ".claude/skills/nano-banana-pro/scripts/generate_image.py",
        Path.home() / ".agents/skills/nano-banana-pro/scripts/generate_image.py",
    ]

    script_path = None
    for p in nanobanana_paths:
        if p.exists():
            script_path = p
            break

    if not script_path:
        print("Error: nanobanana not found. Install with: npx skills add steipete/agent-scripts")
        return False

    cmd = [
        "uv", "run", str(script_path),
        "--prompt", prompt,
        "--filename", output,
        "--resolution", resolution
    ]

    print(f"Generating: {prompt[:50]}...")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Error generating image: {result.stderr}")
        return False

    print(f"Generated: {output}")
    return True


def remove_background(input_path: str, output_path: str) -> bool:
    """Remove background using rembg."""

    # Check if rembg is installed
    try:
        subprocess.run(["rembg", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Installing rembg...")
        subprocess.run([sys.executable, "-m", "pip", "install", "rembg[cpu,cli]"],
                      capture_output=True)

    print(f"Removing background from {input_path}...")

    cmd = ["rembg", "i", input_path, output_path]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Error removing background: {result.stderr}")
        return False

    print(f"Background removed: {output_path}")
    return True


def main():
    parser = argparse.ArgumentParser(description="Generate slide deck assets")
    parser.add_argument("--prompt", type=str, help="Image generation prompt")
    parser.add_argument("--input", type=str, help="Existing image to process")
    parser.add_argument("--output", type=str, required=True, help="Output filename")
    parser.add_argument("--resolution", type=str, default="2K", choices=["1K", "2K", "4K"])
    parser.add_argument("--remove-bg", action="store_true", help="Remove background")

    args = parser.parse_args()

    if not args.prompt and not args.input:
        parser.error("Either --prompt or --input is required")

    output_path = Path(args.output)

    # If generating new image
    if args.prompt:
        # For background removal, add prompts that help
        prompt = args.prompt
        if args.remove_bg and "background" not in prompt.lower():
            prompt += ", isolated on solid white background, product photography style"

        temp_output = str(output_path.with_suffix('.temp.png')) if args.remove_bg else str(output_path)

        if not generate_image(prompt, temp_output, args.resolution):
            sys.exit(1)

        if args.remove_bg:
            if not remove_background(temp_output, str(output_path)):
                sys.exit(1)
            # Clean up temp file
            Path(temp_output).unlink(missing_ok=True)

    # If processing existing image
    elif args.input:
        if args.remove_bg:
            if not remove_background(args.input, str(output_path)):
                sys.exit(1)
        else:
            print("Nothing to do. Use --remove-bg to process existing image.")

    print(f"Done: {output_path}")


if __name__ == "__main__":
    main()
