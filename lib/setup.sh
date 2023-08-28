#!/bin/bash
# shellcheck disable=SC2016

mnt="tmp" rootFS="$mnt/root.x86_64"; shift
packages=('dosfstools' 'ntfs-3g' 'parted' 'gdisk' "$@")
tarBall='archlinux-bootstrap-x86_64.tar.gz'
globalMirror="https://geo.mirror.pkgbuild.com" url="$globalMirror/iso/latest/$tarBall"

arch_chroot(){ 
  mount --bind "$rootFS" "$rootFS"; "$rootFS/bin/arch-chroot" "$rootFS" "$@"; 
}

[[ -d $rootFS ]] && { 
  umount -l "$rootFS" && wait;
  rm -rf "$rootFS";
}

[[ -f $mnt/$tarBall ]] && { rm "$mnt/$tarBall"; }

wget $url -O "$mnt/$tarBall"

tar -xzf "$mnt/$tarBall" -C "$mnt" --numeric-owner; rm "$mnt/$tarBall"

: '/usr/share/terminfo'; [[ -d $_ ]]&& cp -r "$_" "$rootFS/usr/share/"
cp lib/chroot.sh "$rootFS/"; cp lib/bash.bashrc "$rootFS/etc/"
printf 'Server = %s/$repo/os/$arch\n' "$globalMirror" >>"$rootFS/etc/pacman.d/mirrorlist"


#arch_chroot /bin/bash chroot.sh "$mnt" "${packages[@]}"
