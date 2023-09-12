#!/bin/bash
# shellcheck disable=SC2016





mnt="$temp" rootFS="$mnt/root.x86_64"; shift
packages=('dosfstools' 'ntfs-3g' 'parted' 'gdisk' "$@")
tarBall='archlinux-bootstrap-x86_64.tar.gz'
globalMirror="https://geo.mirror.pkgbuild.com"


#get_tarball(){ for _; do curl "$_" >"$mnt"/"${_##*/}"; done; }




#: 'iso/latest'; get_tarball "$globalMirror/$_/$tarBall"
tar xzf "$mnt/$tarBall" -C "$mnt" --numeric-owner

: '/usr/share/terminfo'; [[ -d $_ ]]&& cp -r "$_" "$rootFS/usr/share/"
#cp chroot.sh "$rootFS/"; cp bash.bashrc "$rootFS/etc/"
printf 'Server = %s/$repo/os/$arch\n' "$globalMirror" >>"$rootFS/etc/pacman.d/mirrorlist"


mount --bind "$rootFS" "$rootFS"; 
"$rootFS/bin/arch-chroot" "$rootFS";
