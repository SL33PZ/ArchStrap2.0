#!/usr/bin/env bash

GREEN='\e[32m'
RED='\e[31m'
BOLD='\e[1m'
RESET='\e[0m'

log() {
    local current_date current_date title exit_status
    
    current_date=$(date +"%Y-%m-%d")
    current_time=$(date +"%H:%M:%S")
    title=$1
    shift

    
    "$@" >/dev/null 2>&1
    exit_status=$?

    
    if [[ $exit_status -eq 0 ]]; then
        echo -e "${BOLD}[$current_date|$current_time]${RESET}$title: ${GREEN}Success${RESET}"
    else
        echo -e "${BOLD}[$current_date|$current_time]${RESET}$title: ${RED}Failed${RESET}"
    fi
}


