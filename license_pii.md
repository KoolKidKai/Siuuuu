{% include navigation.html %}

{% include sponsornavbar.html %}

# Software License

Description of MIT Software License: 
A short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.

What does the MIT Software License do?

Specific Permissions include....

- Commercial Use
- Modification
- Distribution 
- Private use

Specific Limitations include...

- Liability
- Warranty

Condition: There is license and copyright notice. All people are allowed to modify, distribute, copy, merge, publish, sublicense, and sell copies of the software, as long as those people include the creator in all versions of the software, giving them credit. 


- Added the MIT license as requested

![image](https://user-images.githubusercontent.com/89219486/159780557-bbdc4de6-afcd-435a-8a89-f80fc60ccc6b.png)


# Personal Identifiable Information (PII)

Description of Personal Identifiable Information (PII)
- A representation of information that allows a specific individual's identity to be figured out using information associated with that person indirectly or directly. 


In terms of being specific to our own website, Sponsored by HackClub....

Things that will be known by everyone: 
- Level Number (displayed on screen)
- Account username (displayed on screen)
- Question number (displayed on screen) 
- Total Score (displayed on screen)
- Prizes (displayed on screen)
- Replit account (displayed on screen)
- Replit information (displayed on screen)
- Profile photo (displayed on screen)

Items that are more Cautious
- Whether or not the website is HTTP or HTTPS, more secure site
- Street Address (implemented when signing up)
- Phone Number (implemented when signing up)


Things that you should strive to keep absolutely secret
- Credentials of username and password
- Replit credentials of username and password
- If able to make it monetary, hide credit card information used to display on site. 


How we can prevent leaking of Personal Information....
- Multi-factor authentication (2FA) {implemented into code}
- Make sure that no malware is sent to emails if setting up email system
- Encryption can be used 
  - SSL encryption
  - Asymemtric crypto
  - Symmetric crypto
  - Maybe very specific ciphers, like Base64, Atbash, Rot13 etc.



# Github Page Actions (PII)

Describe PII you have seen on project in CompSci Principles.
- PII I have seen on my project would be credit card information, login information (specificaly credentials to replit and credentials to log on to save progress in quizzes). Some accessable information would be question number, level number, prizes, and total score. 


What are your feelings about PII and your exposure?
- I feel pretty good about PII, and I feel like I haven't exposed much of my information. I have kept it safe, and I always check to make sure nobody is trying to take any PII away from me, sometimes in the form of phishing and malware. 


Describe good and bad passwords? What is another step that is used to assist in authentication.
- Good passwords would be multiple characters (likely over 6 characters) that have special characters embedded in them, with numbers, and capital letters. It makes the passwords much harder to guess, or use hacking tools like John the Ripper to try and brute force using a dictionary. Bad passwords would be passwords under 6 characters that only use one case of letters, with no special characters. These passwords can easily be cracked using dictionaries. Some examples could include "qwerty" or "password" or "abc123". 

Try to describe Symmetric and Asymmetric encryption.
- Symmetric encryption is where only one key (secret) is used to both encrypt and decrypt either a file or other information. Asymmetric encryption is where there are two separate keys, one used to encrypt the data and one used to decode the data, each of which are somehow algorithimically connected. 


Provide an example of encryption we used in deployment.
- One example of encryption would be changing the website from HTTP to HTTPS, making it more secure, as well as using SSL encryption, to encrypt certificates on that website, part of the reason why HTTPS is more secure. 


Describe a phishing scheme you have learned about the hard way. Describe some other phishing techniques.
- One phishing scheme that I have learned the hard way would be when I clicked on a link that said I could win $500. Luckily, my antivirus prevevnted it. Some other phishing techniques could be advertised in emails, speak phising, whaling, and vishing (using banks or targeting higher level executives). 
