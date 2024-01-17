import datetime

class Transaction:
    def __init__(self, amount, description, date=None):
        self.amount = amount
        self.description = description
        self.date = date or datetime.datetime.now()

class TransactionTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def remove_transaction(self, index):
        try:
            del self.transactions[index]
        except IndexError:
            print("Індекс транзакції не знайдено.")

    def calculate_balance(self):
        balance = 0
        for transaction in self.transactions:
            balance += transaction.amount
        return balance

    def display_transactions(self):
        for index, transaction in enumerate(self.transactions, start=1):
            print(f"{index}. {transaction.amount} ({transaction.date}): {transaction.description}")

    def save_to_csv(self, filename='transactions.csv'):
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                for transaction in self.transactions:
                    file.write(f"{transaction.amount},{transaction.description},{transaction.date}\n")
            print(f"Транзакцію збереженно {filename} успішно.")
        except Exception as e:
            print(f"Не вдалось зберегти транзакцію: {e}")

def main():
    tracker = TransactionTracker()
    
    transaction1 = Transaction(100, "Ура зп")
    transaction2 = Transaction(-50, "Пивко")
    transaction3 = Transaction(-20, "Бургер")

    tracker.add_transaction(transaction1)
    tracker.add_transaction(transaction2)
    tracker.add_transaction(transaction3)

    tracker.display_transactions()
    print(f"Баланс: {tracker.calculate_balance()}")

    tracker.save_to_csv()

if __name__ == "__main__":
    main()
