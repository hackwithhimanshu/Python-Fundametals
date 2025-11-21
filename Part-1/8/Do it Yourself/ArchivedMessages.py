def show_messages(short_text_messages):
    print("\nShort Messages:-")
    for short_text_message in short_text_messages:
        print(short_text_message)
    
def send_messages(sended_messages, sent_messages):
    print("\nSended Messages:-")
    while sended_messages:
        messages = sended_messages.pop(0)
        print(messages)
        sent_messages.append(messages)
    


short_text_messages = ['hello nigga', 'meow meow', 'whats us bitches']
sent_messages = []

show_messages(short_text_messages)
send_messages(short_text_messages[:], sent_messages)

print("\nOriginal Message: ", short_text_messages)
print("\nsent_messages: ", sent_messages)