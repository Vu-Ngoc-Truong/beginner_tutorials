#!/bin/bash
# Load the  mylib.sh using source comamnd
source mylib.sh

echo "JAIL_ROOT is set to $JAIL_ROOT"

# Invoke the is_root() and show message to user
TRUE && echo "You are logged in as root." || echo "You are not logged in as root."