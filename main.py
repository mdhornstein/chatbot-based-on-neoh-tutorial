import asyncio 
import telegram 

def display_user_info(user_object) :
    print("****************************")
    print(f"Info for user: {user_object.username}")
    print("****************************")
    print(f"is_bot: {user_object.is_bot}")
    print(f"first_name: {user_object.first_name}")




async def main(): 
    # Load the API token 
    with open("telegram_api_token.txt") as f:
        api_token = f.readline().strip("\n")
    print("**************************")
    print(f"API token: {api_token}")
    print("**************************")
    bot = telegram.Bot(api_token)
    
    # Make a getMe API call. 
    # https://core.telegram.org/bots/api#getme
    # getMe: "A simple method for testing your bot's authentication token.
    #         Returns basic information about the bot in the form of a 
    #         User object."
    async with bot: 
        user_object = await bot.get_me()
    
    print(f"type(user_object): {type(user_object)}")
    print(user_object)
    print()
    display_user_info(user_object)

if __name__ == "__main__":
    asyncio.run(main())