import os
import datetime

class ChatBot:
    def __init__(self, responses_file='responses.txt', log_file='chat_log.txt'):
        self.responses_file = responses_file
        self.log_file = log_file
        self.load_responses()

    def load_responses(self):
        try:
            with open(self.responses_file, 'r', encoding='utf-8') as file:
                self.responses = dict(line.strip().split(':') for line in file)
        except FileNotFoundError:
            print(f"Помилка: файл '{self.responses_file}' не знайдено.")
            self.responses = {'Привіт': 'Привіт!', 'Як справи': 'В мене добре, дякую!'}

    def save_response(self, key, value):
        self.responses[key] = value
        with open(self.responses_file, 'a', encoding='utf-8') as file:
            file.write(f"{key}:{value}\n")

    def log_interaction(self, user_input, bot_response):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - Ви: {user_input}, Бот: {bot_response}\n"
        with open(self.log_file, 'a', encoding='utf-8') as file:
            file.write(log_entry)

    def get_bot_response(self, user_input):
        if user_input.lower() == 'покажи лог':
            return self.show_chat_log()
        elif user_input.lower() in self.responses:
            bot_response = self.responses[user_input.lower()]
            self.log_interaction(user_input, bot_response)
            return bot_response
        else:
            default_response = "Я не їб* шо ти говориш."
            self.log_interaction(user_input, default_response)
            return default_response

    def show_chat_log(self):
        try:
            with open(self.log_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                last_10_lines = lines[-10:]
                return ''.join(last_10_lines)
        except FileNotFoundError:
            return "Чат порожній."

def main():
    bot = ChatBot()

    while True:
        user_input = input("Ти: ")
        if user_input.lower() == 'вихід':
            break

        bot_response = bot.get_bot_response(user_input)
        print(f"Бот: {bot_response}")

if __name__ == "__main__":
    main()