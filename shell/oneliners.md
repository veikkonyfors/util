# Grep for given string through a directory tree. Like grep -r or rgrep, but even more flexible
# Finds non-binary flat files from current directory tree with name not ending to .swp
# Pipes each file to xargs running a perl one-liner to print path+line containing ViWare
# Finally skipping lines containing .metadata using grep -v
find . -type f  ! -name '*.swp' -exec grep -I -q . {} \; -print | \
  xargs -i{} perl -lne 'print "$ARGV: $_" if /ViWare/' {} | \
  grep -v \.metadata

# List sizes of directories in the current tree.
# Counts only size of flat files on the directory itself i.e. skips subdirectory sizes.
# Handy to find directories with huge files or huge number of small files.
# With plain du itself one is having hard times to accomplish it
find . -type d -exec du -sS {} \; | sort -nr | head