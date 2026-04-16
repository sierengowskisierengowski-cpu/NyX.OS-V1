#!/usr/bin/env python3
"""
NyX.x.OS — Tamper Warning System
Copyright 2026 Joseph Sierengowski
NYX-J5W-2026-SIERENGOWSKI-LOCKED

Auto-runs on exec-once in hyprland.conf.
Monitors for unauthorized access attempts.
"""

import subprocess
import os
import sys
import time
import hashlib
from pathlib import Path

NYX_CONFIG_DIR = Path.home() / ".config"
NYX_MARKER = Path.home() / ".nyx_integrity"

def get_config_hash():
    """Hash critical config files for integrity check."""
    critical_files = [
        NYX_CONFIG_DIR / "hypr" / "hyprland.conf",
        NYX_CONFIG_DIR / "waybar" / "config",
        NYX_CONFIG_DIR / "waybar" / "style.css",
    ]
    hasher = hashlib.sha256()
    for f in critical_files:
        if f.exists():
            hasher.update(f.read_bytes())
    return hasher.hexdigest()

def notify(title, body, urgency="normal"):
    """Send notification via notify-send."""
    try:
        subprocess.run([
            "notify-send",
            "-u", urgency,
            "-a", "NyX.x.OS",
            title,
            body
        ], timeout=5)
    except Exception:
        pass

def main():
    current_hash = get_config_hash()

    if NYX_MARKER.exists():
        stored_hash = NYX_MARKER.read_text().strip()
        if stored_hash != current_hash:
            notify(
                "NyX.x.OS — INTEGRITY WARNING",
                "Configuration files have been modified since last boot.",
                "critical"
            )
    else:
        notify(
            "NyX.x.OS — System Active",
            "Silent. Dark. Purely Functional.",
            "low"
        )

    NYX_MARKER.write_text(current_hash)

if __name__ == "__main__":
    main()
