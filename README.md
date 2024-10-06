# ACT Activities
This repository will house the activities that apply what they learned about certain cybersecurity topics. It will also include a list of resources students will need when participating in the activity

## Cryptography
In this activity, imagine you are a hacker and you want to access Professor Burch's personal information. Through some intense snooping, you found five MD5 hashes that get used repeatedly. Using Hashcat and CUPP, you will generate a wordlist of potential passwords using his PowerPoint bio as a reference. Then, using hashcat, you will crack each of the hashes. This exercise aims to help you understand what cryptography is and how it can be practically applied. 

### Resources Required
* [Git](https://git-scm.com/downloads)
* Kali Linux (Ask an ACT Cabinet member for assistance)
* CUPP
* Hashcat (Comes pre-installed with Linux)

#### How to install CUPP

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

#### How to Use Hashcat
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
