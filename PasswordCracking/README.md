# Password Cracking Instructions

## Resources Required

- [Git](https://git-scm.com/downloads)
- Kali Linux (Ask an ACT Cabinet member for assistance)
- CUPP
- Hashcat (Comes pre-installed with Linux)

### Install requirements.txt

```sh
python -m pip install -r requirements.txt
```

```sh
python3 -m pip install -r requirements.txt
```

### How to install CUPP

1.) Make sure your current working directory is Desktop

```sh
pwd
cd Desktop
```

2.) Clone the Cupp repository and navigate to it

```sh
git clone https://github.com/Mebus/cupp.git
cd cupp
```

3.) Run the CUPP interface

```sh
python3 cupp.py
```

4.) Will input information as instructed on CUPP interface

### How to Use Hashcat

1.) While in the cupp directory create a file called md5.txt, you can use ls to make sure it was made

```sh
touch md5.txt
```

2.) Use the nano text editor to open the file

```sh
nano md5.txt
```

(assets/image.png)

3.) In this file you will input a hash and then press Ctrl+s and Crtl+x

4.) To run hashcat use this, the burchPasswordWordList.txt is the file generated from CUPP

```sh
hashcat -m 0 -a 0 md5.txt burchPasswordWordlist.txt
```

### How to run site locally

1.) Navigate to the PasswordCracking directory

```sh
cd PasswordCracking
```

2.) Run App depending on python type
Python

```sh
npm run app
```

Python3

```sh
npm run app3
```

3.) Click Link and you should be navigated to the index.html login page

### Target

Name: Matthew Burch
Nickname: ScratchinLeader
Hobbies: Enjoys couponing and playing with clicker counter and collects glow in the dark cups
Profession: Professor of Cybersecurity and eXtreme Ironer
Place of Residence Alexandria, IN
Majors: Spanish
Minor: Tap

#### Found Hashes

- ad75ecbe18486e7b4d44f23c37ae4051
- 37238d6abcc1355bda840b6eb8e28fe7
- aea5f0ca79f5398223f4aee416fc4997
- 2f528bfd7e40be761111b3260ed4ec10
- dc11436872579bc7c44e8e301a630566
