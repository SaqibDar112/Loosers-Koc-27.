email=input("Enter Your Email : ")
username=email[:email.index("@")]
domain=email[email.index("@")+1:]
print(username,"and domain:",domain.upper())