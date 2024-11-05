#!/bin/bash

# Verify what init system are you running on
# - check init process; not a verification for running init.d:
ps 1

# - using the stat command:
# stat <cmd_output_from_above_command>

# - verify using the readlink command:
# readlink <cmd_output_from_above_command>

# - using the ps command with extra options:
ps -p 1
ps --no-headers -o comm 1
