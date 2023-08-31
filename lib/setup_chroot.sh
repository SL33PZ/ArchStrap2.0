#!/bin/bash
source .env

systemd-machine-id-setup

pacman-key --init; pacman-key --populate
pacman -Syu --needed --noconfirm "${BASE_PACKAGES[@]}"

git clone https://aur.archlinux.org/yay.git
cd yay && makepkg -si


if [[ $EFI =~ "/dev/nvme"* ]]; then
  device=${EFI::-2}
  efi=${EFI:(-1)}
  parted --script "$device" \
  mktable gpt \
  mkpart primary efi 1MiB 513MiB \
  mkpart primary linux-swap 513MiB 4609MiB \
  mkpart primary ext4 4609MiB 100% \
  set "$efi" boot on
elif [[ $EFI =~ "/dev/sda"* ]]; then
  device=${EFI::-1}
  efi=${EFI:(-1)}
  parted --script "$device" \
  mktable gpt \
  mkpart primary efi 1MiB 513MiB \
  mkpart primary linux-swap 513MiB 4609MiB \
  mkpart primary ext4 4609MiB 100% \
  set "$efi" boot on
fi

mkfs.fat -F 32 "$EFI"
mkswap "$SWAP"
mkfs.ext4 "$ROOT"

mount "$ROOT" /mnt
swapon "$SWAP"

pacstrap -K "$ENV_PACKAGES"
pacstrap -K "$KERNEL"
pacstrap -K "$DESKTOP_ENVIRONMENT"
pacstrap -K "$DISPLAY_MANAGER"


genfstab -U /mnt/etc/fstab

cp -r .env /mnt/; cp -r setup_configure.sh /mnt/

printf '\e[32m>\e[m: %s\n%s\n' "Done. Arch installer environment setup; Changed root into $mnt/root.x86_64" \
  'You may now proceed to: https://wiki.archlinux.org/title/Installation_guide#Partition_the_disks and follow the rest of the installation guide'

printf '%s\n' 'echo "Welcome to Arch Linux"'>> /etc/profile
bash --login