from config import get_client
from database import initialize_database
from queries import create_customer, read_customers, update_customer, delete_customer


def menu():
    print("Оберіть операцію:")
    print("1. Додати клієнта")
    print("2. Показати всіх клієнтів")
    print("3. Оновити клієнта")
    print("4. Видалити клієнта")
    print("5. Вийти")


def run():
    client = get_client()
    db = client['supermarket_bonus_system']

    initialize_database(client)

    while True:
        menu()
        choice = input("Ваш вибір: ")

        if choice == "1":
            # Додавання клієнта
            customer_id = int(input("Введіть customer_id: "))
            name = input("Введіть ім'я клієнта: ")
            phone = input("Введіть номер телефону: ")
            email = input("Введіть email: ")
            bonus_cards = list(map(int, input("Введіть ID бонусних карток через кому: ").split(',')))

            customer_data = {
                "customer_id": customer_id,
                "name": name,
                "phone": phone,
                "email": email,
                "bonus_cards": bonus_cards
            }

            create_customer(db, customer_data)

        elif choice == "2":
            # Показати всіх клієнтів
            read_customers(db)

        elif choice == "3":
            # Оновлення клієнта
            customer_id = int(input("Введіть customer_id клієнта, якого потрібно оновити: "))
            updated_data = {}
            if input("Оновити телефон? (y/n): ").lower() == "y":
                updated_data["phone"] = input("Введіть новий номер телефону: ")
            if input("Оновити email? (y/n): ").lower() == "y":
                updated_data["email"] = input("Введіть новий email: ")

            update_customer(db, customer_id, updated_data)

        elif choice == "4":
            # Видалення клієнта
            customer_id = int(input("Введіть customer_id клієнта, якого потрібно видалити: "))
            delete_customer(db, customer_id)

        elif choice == "5":
            # Вихід
            print("До побачення!")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    run()
