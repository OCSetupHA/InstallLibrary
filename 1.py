#!/bin/bash
cd
if [ -e "/data/data/com.termux/files/home/storage" ]; then
	rm -rf /data/data/com.termux/files/home/storage
fi
termux-setup-storage
yes | pkg update
. <(curl https://raw.githubusercontent.com/OCSetupHA/InstallLibrary/refs/heads/main/termux-change-repo.sh)
yes | pkg upgrade
yes | pkg i python
yes | pkg i python-pip 
pip install prettytable requests rich colorama
export CFLAGS="-Wno-error=implicit-function-declaration"
pip install psutil
curl -Ls "https://raw.githubusercontent.com/OCSetupHA/SourceInstall/refs/heads/main/OC.py" -o /sdcard/Download/OC.py
curl -Ls "https://raw.githubusercontent.com/OCSetupHA/SourceInstall/refs/heads/main/shouko.py" -o /sdcard/Download/shouko.py
curl -Ls "https://raw.githubusercontent.com/OCSetupHA/SourceInstall/refs/heads/main/Update.py" -o /sdcard/Download/Update.py
if ! command -v su >/dev/null 2>&1 || ! su -c 'exit' >/dev/null 2>&1; then
    exit
fi
su -c "setprop net.dns1 1.1.1.1 && setprop net.dns2 1.0.0.1 && setprop net.dns3 2606:4700:4700::1111 && setprop net.dns4 2606:4700:4700::1001 && ndc resolver flushdefaultif && ndc resolver flushdefaultif && am kill-all && rm -rf /data/data/*/cache/* /data/user/0/*/cache/* && settings put global window_animation_scale 0 && settings put global transition_animation_scale 0 && settings put global animator_duration_scale 0 && am kill-all && settings put global heads_up_notifications_enabled 0 && settings put secure lock_screen_show_notifications 0 && settings put secure lock_screen_allow_private_notifications 0 && settings put global show_notification_channel_warnings 0 && settings put global zen_mode 3 && settings put global policy_dnd 3 && settings put secure android_id 36ea1127de363534 && cd /sdcard/Download && export PATH=\$PATH:/data/data/com.termux/files/usr/bin && export TERM=xterm-256color && python ./shouko.py"
