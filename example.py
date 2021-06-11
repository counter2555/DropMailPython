from dropmail import Dropmail, EMail

if __name__ == "__main__":
    mail = Dropmail("randomtoken")
    mail.NewSession()

    print(mail.Address)

    while True:
        input("...")
        for m in mail.GetEmails():
            print((m.Subject, m.Text))