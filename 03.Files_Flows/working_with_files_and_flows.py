"""
1. Input / Output streams - Standard file descriptors
- Redirect input (stdin) - "<" cat < file.txt
- Redirect output (stdout, stderr) - ">" echo "Hello!" > hello.txt (pip freeze >)
echo "Hello!" 1> hello.txt - stdout, target overwrite
echo "Hello!" 2> hello.txt - stderr, target overwrite
echo "Hello!" 1>> hello.txt - target append

Set -/+o Noclobber - Persmission to overwrite existing file
set -o noclobber
echo "Hi!" > hello.txt - existing file cannot be overwritten

Redirection order:
cat missing_file.txt > out.txt 2>&1 - File
cat missing_file.txt 2>&1 > out.txt - Screen

Creating a document:
echo "Line 1" > file.txt
echo "Line 2" >> file.txt

cat > file.txt << EndOfFile - Do cat command, the result in file.txt, read until EOFile is met (Multi-line prompt)

2. Command sequences
- Executing multiple commands
- Order of execution:
command1 ; command2; - Disconnected execution, sequence
command1 | command2 - Connected execution
command1 && command2 - Conditional execution on success
command1 || command2 - Conditional execution on failure

- Command substitution
cat "cat file.txt"

tee command:
cat list.txt | tee listed.txt - Read from stdin and write to stdout and files

xargs command:
cat "file.txt" | xargs rm -rf - Build and execute command lines from stdin, remove line by line

3. Regex
* - any characters - a*.txt all files starting with A and .txt
? - any single character - [abc]??? - Any file beginning with a, b, c and 3 symbols behind
[chars] - any character that is a member of the set "chars" - ls [abc]*.txt
[!chars] - that is not a member of the set "chars", ls[^abc]*.txt - all files that NOT start with abc and end .txt
[[:class:]] - char that is a member of the specified class - [:alnum:], [:alpha:], [:digit:], etc.

control characters:
.text - atext, text2, 21text15 etc
^text - text, textone, texttwo - beginning with
$text - abctext, bcdtext, ptext - ending with
.\.text - x.text, y.text

grep command:
 - Printing lines matching a pattern
grep one list.txt | grep two - grab all the lines that have "one", then grab from them all that have "two"
grep bash users.txt

4. Advanced file techniques
find command:
find .(path) -type f -name *.txt

locate command:
locate readme.txt

tac -> -cat
more / less commands
head file.txt - 10 by default
tail file.txt - 10 by default
uniq file.txt
sort file.txt
wc file.txt - count of words on line
nl file.txt - add a number to the beginning of every line

5. Screen editors
-VIM (vi)
vi +455 services.txt - goes to 455 line of services file
:set number - number of lines
shift + g - end of file
g + g - start of file
155 shift + g - 155 line

6. Sudo management
sudo useradd -c "Project developer" developer
sudo passwd developer
sudo useradd -c "Project developer" manager
sudo passwd manager
sudo groupadd -g 3000 project
sudo usermod -a -G project developer
sudo usermod -a -G project manager




"""
