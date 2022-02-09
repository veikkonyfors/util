\# Grep for given string through a directory tree. Like grep -r or rgrep, but even more flexible  
\# Finds non-binary flat files from current directory tree with name not ending to .swp  
\# Pipes each file to xargs running a perl one-liner to print path+line containing ViWare  
\# Finally skipping lines containing .metadata using grep -v  
\# Searched string can be a RegExp, e.g. /ViWa..e/ would find ViWare lines as well.

find . -type f  ! -name '*.swp' -exec grep -I -q . {} &#92;; -print | \
  xargs -i{} perl -lne 'print "$ARGV: $_" if /ViWare/' {} | \
  grep -v \.metadata

\# List space required by ordinary files in each directory of the current directory tree.  
\# Counts only size of flat files on the directory ignoring sub-directories  
\# Handy to find directories with huge file(s) or huge number of small files.  
\# With plain du itself one is having hard times to accomplish it  
\# 1.2.2022: Unfortunately not all Unix systems have du with -S option available natively. E.g. MacOSX, AIX.  
\# Had once upon a time self written command 'dus' doing exactly the same thing.  
\# It was in java. I might some time compose 'dus' in Python and make it available.  
\# 3.2.2022: AIX nowadays seem to have -S for separate directories. MacOSX still doesn't have.  
\# 9.2.2022: One could use sudo to be able to scan all directories.  
\# Even so, some transient directories gives errors, thus directing stderr to /dev/null

sudo find . -type d -exec du -sS {} &#92;; 2&gt;/dev/null | sort -nr | head

\# List space required by ordinary files in each directory of the current directory tree.  
\# MacOSX version, with bash and perl. A bit more cryptic :-(

IFS=$&apos;\n&apos;; for i in $(find . -type d); do cd $i;find . -maxdepth 1 -type f -exec du {} &#92;; <code>&#124;</code> cut -f 1 -d&apos; &apos; <code>&#124;</code> perl -ne&apos;$s=<>; while(<>) {$s+=$_;} chomp $s; print &quot;$s &quot;&apos;; pwd; cd -; done  <code>&#124;</code> grep ^[0-9] <code>&#124;</code> sort -nr <code>&#124;</code> head