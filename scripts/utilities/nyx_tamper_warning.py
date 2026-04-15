#!/usr/bin/env python3
# NyX.oS Tamper Warning System v1.0
# Copyright (c) 2026 Joseph Sierengowski. All rights reserved.
# NYX-J5W-2026-SIERENGOWSKI-LOCKED

import time, os, subprocess, webbrowser

NYX_SIGNATURE = "NYX-J5W-2026-SIERENGOWSKI-LOCKED"
NYX_AUTHOR    = "Joseph Sierengowski"
NYX_CONTACT   = "jsierengowski@gmail.com"
NYX_CASE      = "NYX-2026-TAMPER-001"
SOUND_HORN    = "/usr/share/nyx/sounds/fail_horn.mp3"
SOUND_VOICE   = "/usr/share/nyx/sounds/played_yourself.wav"

RED    = "\033[91m"
PURPLE = "\033[95m"
PINK   = "\033[35m"
YELLOW = "\033[93m"
GREEN  = "\033[92m"
DIM    = "\033[2m"
RESET  = "\033[0m"

def p(text, color="", delay=0.04):
    print(color + text + RESET)
    time.sleep(delay)

def play(sound):
    try:
        subprocess.Popen(["paplay", sound], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass

def fake_download():
    bars = [
        (" 3%",  ">                             ", "14 KB/s"),
        ("12%",  ">>>>                          ", "89 KB/s"),
        ("26%",  ">>>>>>>>                      ", "142 KB/s"),
        ("41%",  ">>>>>>>>>>>>>                 ", "198 KB/s"),
        ("54%",  ">>>>>>>>>>>>>>>>>             ", "256 KB/s"),
        ("72%",  ">>>>>>>>>>>>>>>>>>>>>>>       ", "312 KB/s"),
        ("91%",  ">>>>>>>>>>>>>>>>>>>>>>>>>>>>  ", "287 KB/s"),
        ("100%", ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", "COMPLETE"),
    ]
    for pct, bar, speed in bars:
        if pct == "100%":
            print(GREEN + "  [" + bar + "] " + pct + " COMPLETE" + RESET)
        else:
            print(YELLOW + "  [" + bar + "] " + pct + "  " + speed + RESET)
        time.sleep(0.6)

def fu_fingers():
    F = [
        [1,1,1,1,1,1,1,1],
        [1,1,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0],
        [1,1,1,1,1,1,0,0],
        [1,1,1,1,1,1,0,0],
        [1,1,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0],
    ]
    U = [
        [1,1,0,0,0,0,1,1],
        [1,1,0,0,0,0,1,1],
        [1,1,0,0,0,0,1,1],
        [1,1,0,0,0,0,1,1],
        [1,1,0,0,0,0,1,1],
        [1,1,0,0,0,0,1,1],
        [1,1,0,0,0,0,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
    ]
    finger = "\U0001F595"
    gap    = "   "
    for row_f, row_u in zip(F, U):
        line_f = "".join(finger if c else gap for c in row_f)
        line_u = "".join(finger if c else gap for c in row_u)
        print(RED + "  " + line_f + "     " + line_u + RESET)
        time.sleep(0.06)

def run():
    os.system("clear")
    p("  [ NYX.OS ] Integrity check initializing...", DIM, 0.8)
    p("  [ NYX.OS ] Scanning file signatures...", DIM, 0.8)
    p("  [ NYX.OS ] Verifying watermark signatures...", DIM, 0.8)
    p("  [ NYX.OS ] Running attribution trace...", DIM, 0.8)
    p("  [ NYX.OS ] Collecting IP, MAC, hostname, UID...", DIM, 0.8)
    p("  [ NYX.OS ] Packaging incident report...", DIM, 0.8)
    p("  [ NYX.OS ] Encrypting evidence bundle...", DIM, 0.8)
    p("  [ NYX.OS ] ......................................", DIM, 1.2)
    print()
    p("╔══════════════════════════════════════════════════════════════╗", RED)
    p("║       UNAUTHORIZED ACCESS DETECTED — NYX.OS V1              ║", RED)
    p("╚══════════════════════════════════════════════════════════════╝", RED)
    print()
    p("  WATERMARK: " + NYX_SIGNATURE, PURPLE, 0.6)
    p("  ORIGIN:    NyX.oS V1 — " + NYX_AUTHOR, PURPLE, 0.6)
    p("  STATUS:    TAMPER CONFIRMED. YOU HAVE BEEN DETECTED.", RED, 0.8)
    print()
    p("  The night has eyes.", PURPLE, 0.8)
    p("  Every single one of them is on you right now.", PURPLE, 1.0)
    print()
    p("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", RED)
    p("  NYX RESPONSE PAYLOAD — DOWNLOADING...", RED)
    p("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", RED)
    print()
    p("  Connecting to nyx.registry.gowskinet.io...", YELLOW, 1.0)
    p("  Connection established.", YELLOW, 0.8)
    print()
    p("  Downloading: NYX_INCIDENT_PAYLOAD_001.tar.gz", YELLOW, 0.4)
    fake_download()
    print()
    p("  Transmitting to NyX registry...", RED, 0.8)
    p("  Evidence encrypted and logged.", RED, 0.6)
    p("  TRANSMISSION COMPLETE. CASE: " + NYX_CASE, RED, 1.0)
    print()
    p("  DEPLOYING IN...", RED, 0.6)
    print()
    for i in range(10, 0, -1):
        print(RED + "  " + str(i) + "..." + RESET)
        time.sleep(0.7)
    print()
    play(SOUND_HORN)
    time.sleep(0.5)
    fu_fingers()
    print()
    play(SOUND_VOICE)
    time.sleep(1.0)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    time.sleep(1.0)
    print()
    p("╔══════════════════════════════════════════════════════════════╗", RED)
    p("║   All of those are for you. Every single one.               ║", PINK)
    p("║                                                              ║", RED)
    p("║   THIS WAS YOUR ONLY AND LAST WARNING.                      ║", RED)
    p("║   There will be no warning next time.                       ║", RED)
    p("║   Think very carefully before you try this again.           ║", RED)
    p("║   You will not get another one.                             ║", RED)
    p("╚══════════════════════════════════════════════════════════════╝", RED)
    print()
    p("  You are a clown buddy. A genuine clown.", PINK, 0.6)
    p("  The night has eyes. All of them.", PURPLE, 0.6)
    p("  NyX.oS — Silent. Dark. Purely Functional.", PURPLE, 0.8)
    print()
    p("  — J. Sierengowski / NyX.oS V1 / 2026", DIM, 0.4)
    p("  — " + NYX_CONTACT, DIM, 0.4)
    p("  — GowskiNet is always watching.", DIM, 0.4)
    p("  — Have a terrible day.", DIM, 0.4)

if __name__ == "__main__":
    run()
