#!/usr/bin/env bash
source .env

decode_password () {
  echo "$1" | openssl enc -md sha512 -a -d -pbkdf2 -iter 100000 -salt -pass pass:"$2"
}


install_grub () {
  grub-install --bootloader-id='Arch Linux'
  mkgrub-config -U /boot/grub/grub.cfg
  mkdir -p /var/lock/dmraid
  sed -i 's/#GRUB_DISABLE_OS_PROBER=false/GRUB_DISBALE_OS_PROBER=false/m' /etc/default/grub
}

create_user() {
    useradd "$1"
    echo -e "$2\n$2" | passwd "$1"
    echo -e "$3\n$3" | passwd root
    usermod -aG wheel "$1"
}


mkdir -p "/boot/efi"
mount "$EFI" /boot/efi

install_grub

decoded_user=$(decode_password "${222}" "${111}")
decoded_root=$(decode_password "${333}" "${111}")

create_user "$USERNAME" "$decoded_user" "$decoded_root"

sed -i 's/# %sudo   ALL=(ALL:ALL) ALL/%sudo   ALL=(ALL:ALL) ALL/' /etc/sudoers
sed -i 's/# %wheel ALL=(ALL:ALL) ALL/%wheel ALL=(ALL:ALL) ALL/' /etc/sudoers
sed -i 's/# %wheel ALL=(ALL:ALL) NOPASSWD: ALL/%wheel ALL=(ALL:ALL) NOPASSWD: ALL/' /etc/sudoers

sed -i "s/#$LANGUAGE/$LANGUAGE/" /etc/locale.gen; locale-gen

ln -sf /usr/share/zoneinfo/"$TIMEZONE" /etc/localtime

for i in "${OPTS[@]}"; do
    git clone "https://aur.archlinux.org/$i.git"
    cd "$i" && makepkg -sri && cd ..
done

systemctl enable NetworkManager.service
systemctl enable "$DISPLAY_MANAGER".service

