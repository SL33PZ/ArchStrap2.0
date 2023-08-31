#!/usr/bin/env bash



encode_passwords () {
  echo "$2" | openssl enc -md sha512 -a -pbkdf2 -iter 100000 -salt -pass pass:"$1"
}



encoded1="$(encode_passwords "$1" "$2")"
encoded2="$(encode_passwords "$3" "$2")"

{
echo "export 111='$2'"
echo "export 222='$encoded1'"
echo "export 333='$encoded2'"
} >> tmp/.env