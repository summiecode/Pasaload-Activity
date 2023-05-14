import threading
import sys

class PasaloadManager:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.lock = threading.Lock()

    def pasaload(self, amount, recipient_number):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print("======================")
                print(f"Pasaload of {amount} successfully sent to {recipient_number}. Remaining balance: {self.balance}")
                
            else:
                print("Insufficient balance for pasaload.")

def pasaload_thread(pasaload_manager, amount, recipient_number):
    pasaload_manager.pasaload(amount, recipient_number)

if __name__ == "__main__":
    initial_balance = 100
    pasaload_manager = PasaloadManager(initial_balance)
    threads = []

    while True:
        print("======================")
        print("\tMENU")
        print("======================")
        print("1. Pasaload")
        print("2. Exit")
        print("======================")
        choice = input("Enter your choice: ")

        if choice == "1":
            load = int(input("Enter the load balance: "))
            recipient_number = input("Enter the recipient's cellphone number: ")
            thread = threading.Thread(target=pasaload_thread, args=(pasaload_manager, load, recipient_number))
            threads.append(thread)
            thread.start()
        elif choice == "2":
            print("Thank you for using our service!")
            break
        else:
            print("Invalid choice. Please try again.")

    for thread in threads:
        thread.join()

    sys.exit(0) 
