#!/usr/bin/env bash
# NyX.x.OS — archiso profile definition
# Copyright 2026 Joseph Sierengowski

iso_name="nyxxos"
iso_label="NYXXOS_$(date +%Y%m)"
iso_publisher="Joseph Sierengowski <https://nyxxos.io>"
iso_application="NyX.x.OS Live/Install"
iso_version="$(date +%Y.%m.%d)"
install_dir="arch"
buildmodes=('iso')
bootmodes=('bios.syslinux.mbr' 'bios.syslinux.eltorito'
            'uefi-ia32.grub.esp' 'uefi-x64.grub.esp'
            'uefi-ia32.grub.eltorito' 'uefi-x64.grub.eltorito')
arch="x86_64"
pacman_conf="pacman.conf"
airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'xz' '-Xbcj' 'x86' '-b' '1M' '-Xdict-size' '1M')
file_permissions=(
    ["/etc/shadow"]="0:0:400"
    ["/usr/local/bin/nyx_trap.py"]="0:0:755"
)
