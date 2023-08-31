#!/usr/bin/env bash
# ---------------------------------------------------------------------------
#shellcheck disable=SC2317

# Copyright 2023, leonidas,,, <leonidas@ubuntu>
# All rights reserved.

# Usage: boilerplate [-h|--help] [--username] [--hostname] [--language] [--timezone] [--user_password] [--root_password] [--desktop_environment] [--display_manager] [--kernel] [--nefi] [--swap] [--root]

# Revision history:
# 2023-08-31 Created by new_script ver. 3.3
# ---------------------------------------------------------------------------

PROGNAME=${0##*/}
VERSION="0.1"

RED='\033[31m'
GREEN='\033[32m'
CYAN='\033[36m'
RES='\033[0m'

clean_up() { # Perform pre-nexit housekeeping
  return
}

error_exit() {
    echo -e "${RED}${PROGNAME}: ${1:-"Unknown Error"}${RES}" >&2
  clean_up
  exit 1
}

graceful_exit() {
  clean_up
  exit
}

signal_exit() { # Handle trapped signals
  case $1 in
    INT)
      error_exit "${RED}Program interrupted by user${RES}" ;;
    TERM)
        echo -e "\n${RED}${PROGNAME}: Program terminated${RES}" >&2
      graceful_exit ;;
    *)
      error_exit "${RED}${PROGNAME}: Terminating on unknown signal${RES}" ;;
  esac
}

usage() {
    echo -e "${CYAN}Usage: ${PROGNAME} [-h|--help] [-username] [-hostname] [-language] [-timezone] [-user_password] [-root_password] [-desktop_environment] [-display_manager] [-kernel] [-nefi] [-swap] [-root]${RES}"
}

help_message() {
  
    echo -e "${PROGNAME} ver. $VERSION"
    echo 

    usage

    echo
    echo -e "Options:"
    echo -e "-h, --help             Display this help message and exit."
    echo -e "-username              Enter your preferred username"
    echo -e "-hostname              Enter your preferred hostname"
    echo -e "-language              Enter your preferred language (e.g en_US.UTF-8)"
    echo -e "-timezone              Enter your preferred timezone (e.g Europe/Berlin)"
    echo -e "-user_password         Enter your preferred user password"
    echo -e "-root_password         Enter your preferred root password"
    echo -e "-desktop_environment   Enter your preferred desktop environment"
    echo -e "-display_manager       Enter your preferred display manager"
    echo -e "-kernel                Enter your preferred kernel"
    echo -e "-efi                   Enter your preferred efi partition"
    echo -e "-swap                  Enter your preferred swap partition"
    echo -e "-root                  Enter your preferred root partition"
    echo 
    echo -e "${CYAN}NOTE: For more information read the README.md${RES}"


    return
}



# Trap signals
trap "signal_exit TERM" TERM HUP
trap "signal_exit INT"  INT

# Check for root UID
#if [[ $(id -u) != 0 ]]; then
#  error_exit "${RED}You must be the superuser to run this script.${RES}"
#fi



# Parse command-line
while [[ -n $1 ]]; do
  case $1 in
    -h | --help)
      help_message; graceful_exit ;;
    -username)
        echo "Enter your preferred username" ;;
    -hostname)
        echo "Enter your preferred hostname" ;;
    -language)
        echo "Enter your preferred language (e.g en_US.UTF-8)" ;;
    -timezone)
        echo "Enter your preferred timezone (e.g Europe/Berlin)" ;;
    -user_password)
        echo "Enter your preferred user password" ;;
    -root_password)
        echo "Enter your preferred root password" ;;
    -desktop_environment)
        echo "Enter your preferred desktop environment" ;;
    -display_manager)
        echo "Enter your preferred display manager" ;;
    -kernel)
        echo "Enter your preferred kernel";;
    -nefi)
        echo "Enter your preferred efi partition" ;;
    -swap)
        echo "Enter your preferred swap partition" ;;
    -root)
        echo "Enter your preferred root partition" ;;
    -* | --*)
      usage
      error_exit "Unknown option $1" ;;
    *)
        echo "Argument $1 to process..." ;;
  esac
  shift
done

# Main logic

python lib/app.py

graceful_exit

