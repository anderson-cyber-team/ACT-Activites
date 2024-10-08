# ACT Activities
This repository will house the activities that apply what they learned about certain cybersecurity topics. It will also include a list of resources students will need when participating in the activity

## Vocabulary
* Plaintext => Unencrypted Readable text
* Ciphertext => Text that has been changed in some way using an algorithm
* Encryption => The process of changing text into unreadable ciphertext
* Decryption => The process of changing ciphertext into readable plaintext

## Crpytography
In this activity, imagine you and a buddy are wanting to send emails to one another, but you want to make sure that if someone intercepts them, they don't know what you are talking about. You will take an image and hide encrypted data in that image (using a cipher) and then email it to your buddy and their goal is to access that data and decrypt the ciphertext only using the information provided in the email. You and your friend will need to agree on a cipher and a way to share the key or keys used to encrypt and decrypt your plaintext

## Password Cracking
In this activity, imagine you are a hacker and you want to access Professor Burch's personal information. Through some intense snooping, you found five MD5 hashes that get used repeatedly. Using Hashcat and CUPP, you will generate a wordlist of potential passwords using his PowerPoint bio as a reference. Then, using hashcat, you will crack each of the hashes. This exercise aims to help you understand what cryptography is and how it can be practically applied.
