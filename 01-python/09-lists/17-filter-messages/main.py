"""
Filter Messages
You're about to write a bit more code in a single function than you have before.

Do not try to write it all at once. Start with the outermost loop and work your way inward. Add extra print() statements and run your code often to make sure it's doing what you expect. Just make sure to remove the extra print() statements before submitting your code.

Running your code often to make sure each line is doing what you expect is called "debugging." All programmers, even seasoned professionals, break large problems down into small ones that they can debug line by line.

Because we're working with strings that need to be converted to lists and vice versa, here are a couple helpful Python methods we can use to make our lives much easier.

Split a String Into a List of Words
The .split() method in Python is called on a string and returns a list by splitting the string based on a given delimiter. If no delimiter is provided, it will split the string on whitespace. Here's a quick example:

message = "hello there sam"
words = message.split()
print(words)
# Prints: ["hello", "there", "sam"]

Join a List of Strings Into a Single String
The .join() method is called on a delimiter (what goes between all the words in the list), and takes a list of strings as input.

list_of_words = ["hello", "there", "sam"]
sentence = " ".join(list_of_words)
print(sentence)
# Prints: "hello there sam"

Assignment
We need to filter the profanity out of our game's live chat feature! Complete the filter_messages function. It takes a list of chat messages as input and returns two new lists:

A list of the same messages but with all instances of the word dang removed.
A list containing the number of dang words that were removed from each message at that particular index.
Here are some examples:

messages = ["dang it bobby!", "look at it go"]
filter_messages(messages) # returns ["it bobby!", "look at it go"], [1, 0]

messages2 = ["That's the bloody dang Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a dang razor!"]
filter_messages(messages2) # returns ["That's the bloody Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a razor!"], [1, 0, 1]

Here are the steps for you to follow. There are a LOT of steps! It won't be easy, but if you follow the steps exactly, you will pass this assignment:

Create the two empty lists that you'll return at the end:
One for the filtered messages with "dang" removed.
And one for the counts of "dangs" removed from those messages.
Loop over the list of messages. For each message:
Split the message string into a list of words using the .split() string method.
Create an empty list for all the good words in this message.
Create a counter variable for the "dangs" in this message, starting at 0.
For each word in the message:
If the word is "dang", add 1 to the "dangs" counter.
If the word is not "dang", add it to the list of good words.
Join the list of good words into a single string using the .join() method.
Append the new filtered message to the list of filtered messages.
Append the new "dangs" count to the list of counts of "dangs".
After looping over the list of messages, return the list of filtered messages first, then the list of "dang" counts.
"""

def filter_messages(messages):
    filtered_messages = []
    counts = []

    for message in messages:
        words = message.split()
        filtered_words = []
        dang_count = 0

        for word in words:
            if word == "dang":
                dang_count += 1
            else:
                filtered_words.append(word)

        filtered_message = " ".join(filtered_words)
        filtered_messages.append(filtered_message)
        counts.append(dang_count)

    return filtered_messages, counts
