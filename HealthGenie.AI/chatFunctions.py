import openai
import constants as cf
import bcrypt




'''Author History- Created by Rita, Updated by Godhuli'''
# Define function to get Health Genie's response
def get_response(user_input):
    start_sequence = "Hi I am Health Genie, How can I help you?"
    restart_sequence = "Is there anything else i can help you with ?"
    response_bot=""
    
    print("User Input:"+ user_input)
    
    if user_input == 'OK THANKS' or user_input == 'ok thanks':
        print('HealthGenie: It was nice talking to you. See you soon, Bye!! :)')
        return "HealthGenie: It was nice talking to you. See you soon, Bye!! :)"
    else:
    
        completions = openai.Completion.create(
            engine=cf.model1,
            prompt="Act as Mental Health assistant"+user_input,
            max_tokens=350,
            n=10, # limit to 10 responses
            stop=None,
            temperature=0.7,
            top_p=1,
            frequency_penalty=0.05,
            presence_penalty=0
            )
        print ("All completions response ---))))"+completions.choices[0].text)
        response_list=completions.choices[0].text.split("You:")
        response_bot=response_list[0]
        # messages = [c.text.strip() for c in completions.choices]
        
        print("final response here is :"+response_bot)
        
        return response_bot
        
        
'''Author History- Created by Godhuli'''
#function to write into user data file
def writeUserDetails(name,email,password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    with open('UserData.txt', 'a') as f:
        f.write(name+"\t\t\t"+email+"\t\t\t"+hashed.decode('utf-8')+"\n")
    