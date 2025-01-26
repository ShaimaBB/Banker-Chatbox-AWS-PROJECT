import json
import random
import decimal 

def random_num():
    return(decimal.Decimal(random.randrange(1000, 50000))/100)

def get_slots(intent_request):
    return intent_request['sessionState']['intent']['slots']
    
def get_slot(intent_request, slotName):
    slots = get_slots(intent_request)
    if slots is not None and slotName in slots and slots[slotName] is not None:
        return slots[slotName]['value']['interpretedValue']
    else:
        return None    

def get_session_attributes(intent_request):
    sessionState = intent_request['sessionState']
    if 'sessionAttributes' in sessionState:
        return sessionState['sessionAttributes']

    return {}

def elicit_intent(intent_request, session_attributes, message):
    return {
        'sessionState': {
            'dialogAction': {
                'type': 'ElicitIntent'
            },
            'sessionAttributes': session_attributes
        },
        'messages': [ message ] if message != None else None,
        'requestAttributes': intent_request['requestAttributes'] if 'requestAttributes' in intent_request else None
    }


def close(intent_request, session_attributes, fulfillment_state, message):
    intent_request['sessionState']['intent']['state'] = fulfillment_state
    return {
        'sessionState': {
            'sessionAttributes': session_attributes,
            'dialogAction': {
                'type': 'Close'
            },
            'intent': intent_request['sessionState']['intent']
        },
        'messages': [message],
        'sessionId': intent_request['sessionId'],
        'requestAttributes': intent_request['requestAttributes'] if 'requestAttributes' in intent_request else None
    }

def CheckBalance(intent_request):
    session_attributes = get_session_attributes(intent_request)
    slots = get_slots(intent_request)
    account = get_slot(intent_request, 'accountType')
    #The account balance in this case is a random number
    #Here is where you could query a system to get this information
    balance = str(random_num())
    text = "Thank you. The balance on your "+account+" account is $"+balance+" dollars."
    message =  {
            'contentType': 'PlainText',
            'content': text
        }
    fulfillment_state = "Fulfilled"    
    return close(intent_request, session_attributes, fulfillment_state, message)   

def FollowupCheckBalance(intent_request):
    session_attributes = get_session_attributes(intent_request)
    slots = get_slots(intent_request)
    account = get_slot(intent_request, 'accountType')
    #The account balance in this case is a random number
    #Here is where you could query a system to get this information
    balance = str(random_num())
    text = "Thank you. The balance on your "+account+" account is $"+balance+" dollars."
    message =  {
            'contentType': 'PlainText',
            'content': text
        }
    fulfillment_state = "Fulfilled"    
    return close(intent_request, session_attributes, fulfillment_state, message)
    
    
def TransferFunds(intent_request):
    session_attributes = get_session_attributes(intent_request)
    slots = get_slots(intent_request)
    source_account = get_slot(intent_request, 'sourceAccount')
    destination_account = get_slot(intent_request, 'destinationAccount')
    transfer_amount = get_slot(intent_request, 'amount')

    if not source_account or not destination_account or not transfer_amount:
        message = {
            'contentType': 'PlainText',
            'content': 'Please provide all required details: source account, destination account, and transfer amount.'
        }
        return close(intent_request, session_attributes, "Failed", message)
     
    if source_account == destination_account:
        message = {
            'contentType': 'PlainText',
            'content': 'The source and destination accounts cannot be the same. Please try again.'
        }
        return close(intent_request, session_attributes, "Failed", message)
    
    # Simulated account balances
    account_balances = {
        "Checking": 1000.00,
        "Savings": 2000.00
    }

    if source_account not in account_balances or destination_account not in account_balances:
        message = {
            'contentType': 'PlainText',
            'content': 'Invalid account provided. Please check and try again.'
        }
        return close(intent_request, session_attributes, "Failed", message)

    transfer_amount = float(transfer_amount)
    if account_balances[source_account] < transfer_amount:
        message = {
            'contentType': 'PlainText',
            'content': f'Insufficient funds in {source_account}. Available balance: ${account_balances[source_account]:.2f}.'
        }
        return close(intent_request, session_attributes, "Failed", message)

    account_balances[source_account] -= transfer_amount
    account_balances[destination_account] += transfer_amount

    message = {
        'contentType': 'PlainText',
        'content': f'Transfer of ${transfer_amount:.2f} from {source_account} to {destination_account} was successful. '
                   f'New balances: {source_account} - ${account_balances[source_account]:.2f}, '
                   f'{destination_account} - ${account_balances[destination_account]:.2f}.'
    }
    return close(intent_request, session_attributes, "Fulfilled", message)
    
def dispatch(intent_request):
    intent_name = intent_request['sessionState']['intent']['name']
    response = None
    if intent_name == 'CheckBalance':
        return CheckBalance(intent_request)
    elif intent_name == 'FollowupCheckBalance':
        return FollowupCheckBalance(intent_request)
    elif intent_name == 'TransferFunds': 
        return TransferFunds(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')

def lambda_handler(event, context):
    response = dispatch(event)
    return response

