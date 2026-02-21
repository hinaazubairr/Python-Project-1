# Program#9:      Project: Customer Service Bot
# BY HINA ZUBAIR
# GITHUB ID: hinaazubairr

# 1st step: save this program as : CustomerServiceBot.py

# Centrepoint is a furniture store that sells furniture. The company has one location in addition to a website, which features a customer service chat window
# that enables customers to chat in real time with someone from the centrepoint team.
# when Addison 1st started this company, she and her team handled all incoming chat messages from customers as soon as an incoming message was received.
# However, business has grown and the team can no longer dedicate a significant amount of their day to responding to chat inquiries.
# Addision began to explore solutions that could minimize the amount of time spent on conversations with customers.
# Addison figured that she could add a chat bot to the chat feature on the Centrepoint website to screen incoming chat messages and 
# route customers to the appropriate person on the Centrepoint team if human assistance is needed. 
# For Some inquiries, the chat bot should be able to answer a customer's question without the need to have someone from the Centrepoint online team involved. 
# Addison would also like the bot to mimic an actual conversation with a human. Help the Centrepoint team by creating a program for the Centrepoint website chat bot. 
# Additional information for how the chat bot should respond to chat messages is provided next. 

# Greeting :
'''
When a customer starts a chat message with Centrepoint, the bot should greet the customer with the phrase 'Thanks for contacting Centrepoint!.'
The bot should then collect the customer's name before continuing with the conversation. 
After the bot collects the customer's name, the bot should respond with the phrase 'Thanks, {insert customer's name}!.'
'''

def greeting():
    print('Hi!. Thanks for contacting Centrepoint!.')
    customer_name = input("May I have your name please?\t").capitalize()
    print(f'Thanks, {customer_name}!.')
    return



# Inquiry Categories 
'''
When a customer Starts a chat message with Centrepoint, their inquiry typically falls into one of five categories. 
The Centrepoint team member responsible for providing human assistance after the initial inquiry screening is provided next to their assigned category, as shown here: 
• Store Location and Hours 
• Order Status: Ellie
• Issue with Order: Christ
• Design Services: Ray
• Other: Trinity 
Store Location and Hours is the only inquiry category that does not require a transfer to a human for assistance. 
After the chat bot greets the customer, the bot should respond with this message: Please select from one of the categories below using the numbers 1-5. 
The customer should then select an inquiry category from the categories described earlier. 
If the customer provides an unrecognizable response, the bot should ask the customer to select a category provided and repeat the list of categories. 
'''

def select_category():
    print("\n Please select from one of the categories below using the numbers 1-5.")
    category = input('[1] = Store Location and Hours \n' 
                     '[2]= Status of Order \n' 
                     '[3]= Issue with Order \n' 
                     '[4]= Design Services \n'
                     '[5]= Other \n' 
                     )
    if category =='1':
        Store_Location_and_Hours()
        return
    
    if category =='2':
        Status_of_Order()
        return
    
    if category =='3':
        Issue_with_Order()
        return
    
    if category =='4':
        Design_Services()
        return
    
    if category =='5':
        Other()
        return
    
    if category not in ['1','2','3','4','5']:
        select_category()




 
'''
Store Location and Hours: 
    Centrepoint is located at 2300 Riverdale Lane, Boston, MA 02101. The Store is Open Monday-Saturday from 10 a.m. to 6 p.m. 
    After providing a customer with the store's location and hours of operation, the bot should ask the customer May I help you with anything else?. 
    If the customer needs additional help, the list of inquiry categories should display again for the customer. 
    However, if the customer does not need any additional help, the bot should end the conversation with the phrase 'Thanks for contacting Centrepoint!'. 
    If the customer selects another inquiry category, the bot should continue the conversation with the prompt for the selected category. 
'''
def Store_Location_and_Hours():
    location = '2300 Riverdale Lane, Boston, MA 02101'
    timings = 'Monday-Saturday from 10 a.m. to 6 p.m.'

    print(f' Store Location and Hours: Centrepoint is located at {location}. The Store is Open: {timings} ')
    yes_no= input('May I help you with anything else?. [Yes/No]: \t').lower()
    if yes_no == 'yes':
        select_category()
    elif yes_no == 'no':
        print("Thanks for contacting Centrepoint!. ")
    return


'''
Status of Order:
    If a customer wants to know the status of their order, the bot should respond with the message 'Sure, I can help you with that'.
    The bot should then collect the following information from the customer: 
        • Full name on the order 
        • Order number 
    Once the information is collected from the customer, the bot should transfer the conversation to the assigned member of the Centrepoint team for assistance 
    and follow up with the message 'Awesome! I'm checking the Status Of the order now.'
'''
def Status_of_Order():
    print('Sure, I can help you with that')
    full_name= input("Please enter Full name on the order:") 
    Order_number = input("Please enter order number on the order:") 
    transfer_Ellie()
    return


def transfer_Ellie():
    print("Hi. This is Ellie from status of order team")
    print("Awesome! I'm checking the Status Of the order now.")
    return
    


'''

Issue with Order:
    If a customer has an issue with their order, the bot should respond with the message 'I'm sorry that you're experiencing issues with your order'. 
    The bot should then collect the following information from the customer: 
        • Full name on the order 
        • Order number 
        • Issue 
    Once the information is collected from the customer, the bot should transfer the conversation to the assigned member of the Centrepoint team for assistance and 
    follow up with the message 'Thanks for providing that information. I'm looking into this now.' 
'''

def Issue_with_Order():
    print("I'm sorry that you're experiencing issues with your order" )
    full_name_1= input("Please enter Full name on the order:") 
    Order_number_1 = input("Please enter order number on the order:") 
    issue_1 = input("Please enter Issue:") 

    transfer_Christ()
    return

def transfer_Christ():
    print("Hi. This is Christ from issue with order team")
    print("Thanks for providing that information. I'm looking into this now." )
    return





'''
Design Services:
    If a customer requests Design Services, the bot should transfer the conversation to the assigned member of the Centrepoint team and 
    respond with the message 'I can definitely help you out with your design questions! Tell me how I may be of assistance.' 
    The customers response should be collected.  
'''

def Design_Services():
    transfer_Ray()
    return

def transfer_Ray():
    print("Hi. This is Ray from Design_Services team")
    print("'I can definitely help you out with your design questions! Tell me how I may be of assistance.' " )
    return




'''
Other:
    If a customer selects Other, the bot should transfer the conversation to the assigned member of the Centrepoint team and 
    respond with the message 'No problem, please describe to me how I may be of assistance'. 
    The customer's response should be collected. 
'''

def Other():
    print("I'm sorry that you're experiencing issues with your order" )
    
    transfer_Trinity()
    return

def transfer_Trinity():
    print("Hi. This is Trinity from Other team")
    print("'No problem, please describe to me how I may be of assistance'. " )
    return


    
    
# Call the functions to start the chat bot
greeting()
select_category()


