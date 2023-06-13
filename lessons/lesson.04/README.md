# Shell, git

## Terminal commands
- `ls` - list directory
- `cd` - change directory
- `pwd` - print working directory
- `whoami` - print current user
- `cat` - print whole file (and concatenate files)
- `head` - show first N lines
- `tail` - show last N lines
- `grep` - find in text (and in text file)
- `echo` - print text
- `>` - write to file from the beginning
- `>>` - write to end of file
- `man` - show manual
- `touch` - create file if not exists
- `mkdir` - create directory (make directory)
- `nano` - small editor
- `micro` - another editor
- `pico` - editor (again)
- `rm` - remove file (or directory)

### Examples

```shell
# show 5th line in file
head -5 README.md | tail -1
```

```shell
grep shell -A 3 README.md
```

```shell
grep cat -B 3 README.md
```

```python
# say hi
print("Hello world")
```

```shell
# create new file by reading two files
cat foo.txt bar.txt > foobar.txt
```

```shell
cat file1.csv <(tail +2 file2.csv) > bigfile.csv
```
