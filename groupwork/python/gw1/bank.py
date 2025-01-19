def create_user(name, surname, yearborn, password, email, balance=0):
    return [name, surname, yearborn, password, email, [], balance]

def add_card(user, card_type):
    user[5].append(card_type)
    print(f"{card_type} added to {user[0]}'s cards.")

def view_cards(user):
    user_cards = user[5]
    if len(user_cards) == 0:
        print(f"{user[0]}'s cards: No cards available")
    else:
        card_list = ', '.join(user_cards)
        print(f"{user[0]}'s cards: {card_list}")

def send_money(sender, receiver, amount):
    if sender[6] >= amount:
        sender[6] -= amount
        receiver[6] += amount
        print(f"{sender[0]} sent {amount} GEL to {receiver[0]}.")
    else:
        print(f"{sender[0]} has insufficient balance to send {amount} GEL.")

def take_out_money(user, amount):
    if user[6] >= amount:
        user[6] -= amount
        print(f"{user[0]} took out {amount} GEL.")
    else:
        print(f"{user[0]} has insufficient balance to take out {amount} GEL.")

def gel_to_usd(amount, rate=2.81):
    return round(amount / rate)

def usd_to_gel(amount, rate=2.81):
    return amount * rate

user1 = create_user("name1", "surname1", 1999, "password123", "name1@example.com", 500)
user2 = create_user("name2", "surname2", 2000, "password456", "name2@example.com", 300)

add_card(user1, "MasterCard")
add_card(user1, "AmEx")
add_card(user2, "Visa")

view_cards(user1)
view_cards(user2)

send_money(user1, user2, 100)
send_money(user2, user1, 50)

take_out_money(user1, 200)
take_out_money(user2, 500)

gel_amount = 100
usd_amount = gel_to_usd(gel_amount)
print(f"{gel_amount} GEL is {usd_amount} USD")

usd_amount = 50
gel_amount = usd_to_gel(usd_amount)
print(f"{usd_amount} USD is {gel_amount} GEL")