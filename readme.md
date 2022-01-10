Buildroot

Client:
    Install docker on pi 
    https://docs.docker.com/engine/install/debian/

    Docker Repo (docker hub)
    docker login

    set up service pi.service


Create and push docker image use buildImage.sh



Install:
git
make
gcc
g++
libncurses-dev
git clone git://git.buildroot.net/buildroot
make raspberrypi4_64_defconfig
make menuconfig
System configuration -> System hostname
System configuration -> System banner
System configuration -> /dev management -> Dynamic using devtmpfs + mdev
System configuration -> Enable root login with password = n
System Configuration -> Network interface to configure dhcp = wlan0
Target packages -> Hardware handling -> Firmware -> rpi-wifi-firmware
Target Packages -> Hardware Handling -> rng-tools
Target Packages -> Hardware Handling -> raspi-gpio
Target packages -> Networking applications -> openssh
Server
Key utilities
Target packages -> Networking applications -> wpa_supplicant
Target packages -> Networking applications -> wpa_supplicant -> Enable nl80211 support
Target packages -> Networking applications -> wpa_supplicant -> Install wpa_passphrase
nano board/raspberrypi/interfaces
auto lo
iface lo inet loopback
auto eth0
iface eth0 inet dhcp
    pre-up /etc/network/nfs_check
    wait-delay 15
auto wlan0
iface wlan0 inet dhcp
    pre-up wpa_supplicant -B -Dnl80211 -iwlan0 -c/etc/wpa_supplicant.conf
    post-down killall -q wpa_supplicant
    wait-delay 15
iface default inet dhcp
nano board/raspberrypi/wpa_supplicant.conf
network={
    ssid="SSID"
    psk="PASSWORD"
}

nano board/raspberrypi/post-build.sh
Add to end of file
cp package/busybox/S10mdev ${TARGET_DIR}/etc/init.d/S10mdev
chmod 755 ${TARGET_DIR}/etc/init.d/S10mdev
cp package/busybox/mdev.conf ${TARGET_DIR}/etc/mdev.conf
cp board/raspberrypi3/interfaces ${TARGET_DIR}/etc/network/interfaces
cp board/raspberrypi3/wpa_supplicant.conf ${TARGET_DIR}/etc/wpa_supplicant.conf

make -j8

