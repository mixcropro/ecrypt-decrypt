# ecrypt-decrypt
Encrypt your files
The following steps explain how this works and all of this doesnt have to be used, you can just generate random passwords for your accounts and just store the file somewhere else.

Also it's recommended that you store file KEY.KEY somewhere else because it is used to encrypt/decrypt the file with your passwords.

So first step is to use script password_gen after the script is executed there will be a file named Random_password, you can create as many passwords with it and it can be used without encrypting it!

Second step is to create a key by starting the key_gen script, after the script has executed the key will be generated in the same folder name key.key, this method uses Symmetric-key algorithm [https://en.wikipedia.org/wiki/Symmetric-key_algorithm], basically you create a key and the same key is used for encrypting and decrypting data.

Third step is to start enc_file script, it will prompt TWO times, the first prompt requires you to choose key.key, that's the encrypting part of the script, the second prompt requires you to choose a file which you want to encrypt, for example you can encrypt the Random_password file. When the script is executed there will be a new file enc_file.encrypted, there is your encrypted password. After you encrypt the file with your passwords you can delete the original file!

Last step is similar as the third, start the decrypt_file and the first prompt requires you to choose a key with which you want to DECRYPT the file, that key is stored under key.key name, second prompt requires you to choose the encrypted file, enc_file.encrypted, and there will be a new file named decrypted_file.

You are done!
