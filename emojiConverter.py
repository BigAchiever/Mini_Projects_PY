def emoji_converter(messages):
    words = messages.split(' ')
    emojis = {
        ":)": "😃",
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">") # because the input can come in different form we cannot add it in function
print(emoji_converter(message))
