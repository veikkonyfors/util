\#----------------------------------------------------------------------------------  
\#		© VN/ViWare     12.1.2022           frgrep.sh          Original 20th Century  
\#  
\#		NAME  
\#		frgrep.sh, Recursively list specific files containing given string  
\#  
\#		SYNOPSIS  
\#		frgrep string [filename-regexp]  
\#  
\#		CALLED BY  
\#		Unix command line  
\#  
\#		DESCRIPTION  
\#		frgrep.sh is a  wrapper script for command like below  
\#  
\#		find . -type f ! -name '*.swp' | xargs -i{} perl -lne 'print "$ARGV: $_" if /ViWare/' {}  
\#  
\#		It combines find, xargs and a perl oneliner commands to effectively browse for strings in a directory tree.   
\#		rgrep (grep -r) does lot of the same thing, but can't e.g. allow limiting to eligible filenames. Also rgrep is  
\#		not available in all Unix flavors, like Unicos by Cray.  
\#		With combined command above one is able to make use of all find command's possibilities to select targeted files.  
\#		Unfortunately in this script one is able only to limit targeted files to ones matching given regular expression.  
\#		Which BTW has been use case in most cases.  
\#		Feel free to make use of the above combined command by modifying it to match your specific needs before running  
\#		on the command line.  
\#		Also, one could enhance this script to allow more sophisticated parameterization.  
\#  
\#		Prints out filename followed by the line with matching string  
\#  
\#		INPUT  
\#		string          String to be grepped for  
\#		filename-regexp Regular expression to define eligible non-binary files for string search  
\#  
\#		DIAGNOSTICS  
\#		Return 0 on success, nonzero otherwise.  
\#  
\#		EXAMPLES  
\#		To find github remote in current project:  
\#		$ frgrep.sh url.*github.com  
\#		./util/.git/config:     url = https://github.com/veikkonyfors/util  
\#  
\#		To find timeout errors in log files beneath current directory  
\#		$ frgrep.sh RemoteRepositoryException '*.log'  
\#		./.metadata/.log: Caused by: org.eclipse.jgit.errors.NoRemoteRepositoryException:  
\#		https://github.com/veikkonyfors/util: https://github.com/veikkonyfors/util/info/refs?service=git-upload-pack  
\#		not found: Not Found  
\#  
\#----------------------------------------------------------------------------------  
