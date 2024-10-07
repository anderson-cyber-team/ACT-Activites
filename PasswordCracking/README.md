# Password Cracking Instructions

## Resources Required
* [Git](https://git-scm.com/downloads)
* Kali Linux (Ask an ACT Cabinet member for assistance)
* CUPP
* Hashcat (Comes pre-installed with Linux)

### How to install CUPP

1.) Make sure your current working directory is Desktop
```sh
pwd
cd Desktop
```
2.) Navigate to desktop using cd and use mkdir to create a CUPP folder and navigate into it
```sh
mkdir CUPP
cd CUPP
```
3.) Clone the Cupp repository
```sh
git clone https://github.com/Mebus/cupp.git
cd cupp
```
4.) Run the CUPP interface
```sh
python3 cupp.py
```
5.) Will input information as instructed on CUPP interface

### How to Use Hashcat
1.) While in the cupp directory create a file called md5.txt, you can use ls to make sure it was made
```sh
touch md5.txt
```
2.) Use the nano text editor to open the file
```sh
nano md5.txt
```
3.) In this file you will input a hash and then press Ctrl+s and Crtl+x

4.) To run hashcat use this, the burchPasswordWordList.txt is the file generated from CUPP
```sh
hashcat -m 0 -a 0 md5.txt burchPasswordWordlist.txt
```

### Target
Name: Matthew Burch
Nickname: ScratchinLeader
Hobbies: Enjoys couponing and playing with clicker counter and collects glow in the dark cups
Profession: Professor of Cybersecurity and eXtreme Ironer
Place of Residence Alexandria, IN
Majors: Spanish
Minor: Tap

