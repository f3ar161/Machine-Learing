greetings = ["hi", "hello", "hey"]
farewell = "Goodbye!"
question_limit = 2
stock_market_info = "The stock market crashed, omg!!..... Thanks Elon Musk."
weather_info = "The weather is gonna be hard, prepare your umbrella."
bot_name = "Your friendly neighborhood Spider-Man"

def get_user_input():
    return input("Input: ").strip().lower()

def respond_to_greeting():
    print(f"{bot_name}: Hello! You can ask me about the 'weather' or the 'stock market'.")

def provide_info(topic):
    if topic == "weather":
        print(f"{bot_name}: {weather_info}")
    elif topic == "stock market":
        print(f"{bot_name}: {stock_market_info}")

def ask_for_follow_up():
    print(f"{bot_name}: Do you have another question?")

def dismiss_user():
    print(f"{bot_name}: {farewell}")

def main():
    user_input = get_user_input()
    if any(greeting in user_input for greeting in greetings):
        respond_to_greeting()
        
        question_count = 0
        while question_count < question_limit:
            user_input = get_user_input()
            
            if "weather" in user_input:
                provide_info("weather")
                question_count += 1
            elif "stock market" in user_input:
                provide_info("stock market")
                question_count += 1
            else:
                print(f"{bot_name}: I can only help with the 'weather' or 'stock market'.")
                question_count += 1
            
            if question_count < question_limit:
                ask_for_follow_up()
        
        dismiss_user()
    else:
        print(f"{bot_name}: I only respond to greetings like 'hi', 'hello', or 'hey'.")

if __name__ == "__main__":
    main()
