import table
from table import Session


class User:
    session = Session()

    def add_contact(self):
        user_fullname = str(input("INPUT FULLNAME: ").upper())
        user_nickname = str(input("INPUT NICKNAME: "))
        user_occupation = str(input("INPUT OCCUPATION: ").upper())
        user_phone_number = str(input("INPUT PHONE NUMBER: "))
        user_email = str(input("INPUT EMAIL: "))
        user_address = str(input("INPUT ADDRESS: ")).upper()

        new_user = table.Contact(FULLNAME=user_fullname, NICKNAME=user_nickname,
                                 OCCUPATION=user_occupation, PHONE_NUMBER=user_phone_number,
                                 EMAIL=user_email, ADDRESS=user_address)
        self.session.add(new_user)
        self.session.commit()

    def update_contact(self):
        pass

    def delete_contact(self):
        user_fullname = str(input("INPUT FULLNAME: ").upper())
        self.session.query(table.Contact).filter(table.Contact.FULLNAME == user_fullname).delete()
        self.session.commit()

    def get_contact(self):
        contact = self.session.query(table.Contact).all()
        print(contact)