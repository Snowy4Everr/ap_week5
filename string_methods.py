def string_method1(): ()
# # Problem Set 3: String Methods
# # Upper & Lower:
# # Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
Star_Wars = "MAY THE FORCE BE WITH YOU"
print(Star_Wars.lower)
# # String Joining and Splitting:
# # Given the list motto = ["Make", "haste", "slowly."],
    # a. Convert the list into a single string.
motto ="Make haste slowly."
    # b. Now, split the string at every occurrence of the letter 'a'.
split_list = motto.split('a')
print(split_list)
# # b. Now, split the string at every occurrence of the letter 'a'.

    # Replacing Words:
    # Modify the sentence: "Life is what happens when you are busy making other plans."
    # a. Replace "busy" with "distracted".
    # b. Replace "plans" with "mistakes".
original_string = "Life is what happens when you are busy making other plans."
new_string = original_string.replace ("busy", "distracted")
print(new_string)

new_string1 = original_string.replace ("plans", "mistakes")
print(new_string1)