#!/data/data/com.termux/files/usr/bin/bash
set -e

PM_SETUP="/data/data/com.termux/files/usr/bin/termux-setup-package-manager"
BASE="/data/data/com.termux/files/usr/etc/termux"
MIRRORS="$BASE/mirrors"
CHOSEN="$BASE/chosen_mirrors"

source "$PM_SETUP" || exit 1

[ "$1" = "--help" ] || [ "$1" = "-help" ] && {
    echo "Script for choosing a group of mirrors to use."
    echo "https://github.com/termux/termux-packages/wiki/Mirrors"
    exit 0
}

usage() {
    echo "Usage: termux-change-repo"
    echo "Simplifies selecting mirror sources for pkg/apt."
}

[ $# -gt 0 ] && usage && exit 1
command -v apt >/dev/null || { echo "apt not installed" >&2; exit 1; }

if [ "$TERMUX_APP_PACKAGE_MANAGER" = "pacman" ]; then
    read -rp "Only apt mirrors can be changed. Continue? [y/N] " a
    [[ "$a" =~ ^[Yy]$ ]] || exit 0
fi

mkdir -p "/data/data/com.termux/files/usr/tmp"
ln -sf "$MIRRORS/all" "$CHOSEN"

echo "[*] pkg --check-mirror update"
TERMUX_APP_PACKAGE_MANAGER=apt pkg --check-mirror update
