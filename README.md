# extractmemos.py
This script extracts text from .memo files created by the default Memo app on Verizon Samsung Galaxy S phones. No root access required. Share a memo via Bluetooth or USB to your PC and run this script against the file.

## About
I wrote this script to enable storing and reading memos offline on a PC _without_ the need for cloud storage or email transfer. I’ve tested this script for notes created with the default (stock) Samsung Galaxy S6 Memo app that comes preinstalled on Verizon phones. The Memo app I’m referring to is _not_ the "S Memo" app. This script presumably works with other phones that have the same memo app, but I have not tested it.

![alt text](https://github.com/domenicbrosh/extractmemos.py/blob/master/img/memo_icon.png "current icon for the default Memo app")

The image above is the current icon for the default Memo app I am referring to.

These memos, when shared to a PC via Bluetooth or USB, yield an archive with a .memo extension. Changing the file extension to .zip will allow the archive to be decompressed using most zip utilities. However, this can be a chore when multiple files need to be extracted. This script helps automate that process.

## Usage

The only requirement is that you have [Python 2 or 3](https://www.python.org/downloads/) installed on your PC. Run this script and add the path to a directory containing the memo file(s) as an argument:

	python extractMemos.py /path/[yourfile.memo]

Parsing multiple memo files creates one contiguous output with a message appended to the end of each memo listed.

## Examples

These examples were written to be N00B friendly. Command line ninjas may skip this section.

The following examples assume your memo files are located on your **Desktop** in a folder named **Memos** and that this script is located in your **Documents** folder. Taylor these commands to your environment by replacing the example paths with paths that reflect where your files are located and replace any instance of `username` with your _actual_ username. Your username can be found by typing `whoami` and pressing enter.

##### Change the working directory path to the desktop:

	cd /Users/username/Desktop

##### Example 1 (View contents of _all_ memo files):

	python /Users/username/Documents/extractMemos.py ./Memos

##### Example 2 (View the contents of a particular memo):

	python /Users/username/Documents/extractMemos.py ./Memos/filename.memo

##### Example 3 (Output contents of all memos to a text file):

	python /Users/username/Documents/extractmemos.py ./Memos > myMemos.txt

##### Example 3 (Output contents of a particular memo to a text file):

	python /Users/username/Documents/extractmemos.py ./Memos/someMemo.memo > myMemo.txt

Note that the single redirect operator `>` (greater-than symbol) **overwrites** any file with the same name! To _add_ output to an existing file use _two_ greater-than symbols `>>` which preserves any data that the file contains by appending new data to the end.

## Caveats and Warnings
This script relies on Python's XML Processing Modules and is therefore _not_ secure against maliciously constructed data. I highly recommend using this script to only parse data that you have created on your own device. For more information see:
  * https://docs.python.org/2/library/xml.html#xml-vulnerabilities
  * https://docs.python.org/3/library/xml.html

## TODO

* Add functionality for extracting images
* Error handling
* Improve Regex
* Cleanup functions
