#!/usr/bin/env bash


decode_password () {
  echo "$1" | openssl enc -md sha512 -a -d -pbkdf2 -iter 100000 -salt -pass pass:"$2"
}

