# Mission 8 - Final Report

## Objective
My task was to review the whole repository, update the root README, go through the final checklist and submit the repository link.

## Work completed

### Final repository review
What I checked: I opened every mission folder and made sure each one has a README with the sections it needs. I checked that hello.py is in mission-04-programs and number_converter.py is in mission-05-numbers-data. I opened the repository in a private browser window without logging in and it loaded, so the repository is public. I also looked at the branch update-about and Pull Request #1 on GitHub. Then I looked through all the README files and the screenshots for private details.

Corrections I made: In Mission 5 my first number_converter.py converted numbers with my own loops. The task asks for Python's built-in functions, so I rewrote it to use input(), int(), bin() and hex(). I pushed it as a separate correction commit and then updated the Mission 5 README so that it matches the new program. I also added the missing example of a character that is not in basic ASCII.

### Status of each mission
| Mission | Status | Commit message |
|---|---|---|
| 0 Setup | Complete | Set up Digital Detective mission structure |
| 1 Computer basics | Complete | Complete computer basics and IPOS mission |
| 2 Terminal | Complete | Complete Terminal and file management mission |
| 3 Operating system | Complete | Document operating system and file management |
| 4 Programs | Complete | Compare compilers and interpreters |
| 5 Numbers and data | Complete, corrected after the first commit | Build number converter and practise data representation, then Used built in bin and hex functions in number converter, then Update Mission 5 README to match built-in converter |
| 6 Git and GitHub | Complete, Pull Request #1 merged | Complete Git and GitHub collaboration mission |
| 7 Networking | Complete | Explain networking concepts and website communication |
| 8 Final report | Complete | Complete final report and verify assignment submission |

### Final checklist
All mission folders have a README: done
Every mission README has the required sections: done
Every mission has its own commit and is pushed: done
Terminal operations, flags and pipes are explained: done
Operating system, processes, paths and permissions are covered: done
Compiler and interpreter are compared: done
Number conversions have working and Python verification: done
number_converter.py runs with three test values: done (I tried 10, 255 and 65. It gave 0b1010 and 0xa, 0b11111111 and 0xff, 0b1000001 and 0x41)
Branch and Pull Request are visible on GitHub: done (branch update-about, Pull Request #1 merged)
LAN, MAN, WAN, DNS, router, protocol and client-server are explained: done
Root README explains the project and how to run the converter: done
Personal information removed from screenshots and outputs: done. I checked the screenshots and README files for my computer name and username. The 8.8.8.8 address in Mission 7 is Google's public DNS, so it is not a private detail.
Repository is public and the URL works: done

## Commands used
- git status, git add, git commit, git push: checked and published my work, one commit for each mission
- git log: looked at the commit history to check every mission was committed
- git checkout -b, git checkout main and git pull: created the update-about branch and brought the merged changes back to main
- python3 number_converter.py: ran the converter one more time with three numbers
- python3 hello.py: ran the hello program again

## My understanding
This assignment taught me how a computer works step by step. Input goes in, the processor works on it, memory and storage keep it, and then we get output. I learned that the Terminal lets me control the computer with commands instead of clicking, like ls, cd, cp and mv. I also learned that the operating system looks after the files, the programs running and the permissions. Python programs are run by an interpreter, and computers store numbers and text as binary, so I converted numbers to binary and hex by hand and then with a program that uses bin() and hex(). Git and GitHub help me save my work in small commits and keep a history, and a branch with a Pull Request lets me change things safely before merging. In networking I learned that a website name is changed to an IP address by DNS, and then my computer talks to the server over the internet.

## Difficulties faced
My first number converter did not use the built-in bin() and hex() functions that the task asked for. When I pushed Mission 0, GitHub rejected it twice. The first time the old repository with the same name still existed, and the second time the new repository had been created with an automatic README. My Desktop folder was already a Git repository from earlier practice, so I had to be careful to run Git commands only inside the project folder.

## How I resolved them
I rewrote the converter with bin() and hex() and made a correction commit. For the rejected push I read the error message, deleted the old repository, and created a new empty repository without a README, and then the push worked. I checked with git rev-parse --show-toplevel that Git was working inside the project folder.

## Evidence
mission-08-final-report/README.md, the repository on GitHub, branch update-about, Pull Request #1 and the commit history

## Commit details
Commit message: Complete final report and verify assignment submission. Pushed to GitHub.