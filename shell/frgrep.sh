#!/bin/bash
#*----------------------------------------------------------------------------
#  © VN/ViWare     4.1.2022           frgrep.sh          Original 20th Century
#
# NAME
#       frgrep, Recursively list files containing given string
#
# SYNOPSIS
#       frgrep string [filename-regexp]
#
# CALLED BY
#       Unix command line
#
# DESCRIPTION
#       frgrep greps ordinary files in current directory tree for given string.
#       Prints out filename followed by the line with matching string.
#
# INPUT
#       string          String to be grepped for
#       filename-regexp Regular expression to define eligible files for string search
#
# DIAGNOSTICS
#       Return 0 on success, nonzero otherwise.
#
# EXAMPLES
#       To find github remote in current project:
#       $ frgrep.sh url.*github.com
#       ./util/.git/config:     url = https://github.com/veikkonyfors/util
#
#       To find timeout errors in log files beneath current directory
#       $ frgrep.sh RemoteRepositoryException '*.log'
#       ./.metadata/.log: Caused by: org.eclipse.jgit.errors.NoRemoteRepositoryException:
#        https://github.com/veikkonyfors/util: https://github.com/veikkonyfors/util/info/refs?service=git-upload-pack
#       not found: Not Found
#
#----------------------------------------------------------------------------*/

set -f
str=${1:?"Usage: frgrep string [filename-regexp] "}
name=${2:-\*}

 find . -type f -name ${name}  -exec grep -I -q . {} \; -print \
 | xargs -i{} perl -lne 'print "$ARGV: $_" if /'${str}'/' {}
