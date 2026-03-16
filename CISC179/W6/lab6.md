## Lab 4: Child vaccination chart

```python
import re

# read the story file
with open("Story-1.txt", "r", encoding="utf-8") as file:
    story = file.read()

# this counts word and character count
char_count = len(story)

words = story.split()
word_count = len(words)

print("Characters:", char_count)
print("Words:", word_count)

# word frequency with list
clean_words = []

for w in words:
    w = w.lower()
    w = w.strip(".,!?;:\"()")
    clean_words.append(w)

unique_words = []

for word in clean_words:
    if word not in unique_words:
        unique_words.append(word)

print("Histogram (List Version)")
for word in unique_words[:10]:
    count = clean_words.count(word)
    print(word, ":" , "*" * count)

#counts word frequency with dictionary
freq = {}

for word in clean_words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Dictionary Word Count (Top 10)")
for word in list(freq)[:10]:
    print(word, freq[word])

#Regex extraction
emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", story)
phones = re.findall(r"\d-\d{3}-\d{3}-\d{4}", story)

contact_list = emails + phones

print("Emails:", emails)
print("Phones:", phones)
print("All contacts:", contact_list)

#email processing

usernames = []

for email in emails:
    username = email.split("@")[0]
    usernames.append(username)

hotmail_list = []

for name in usernames:
    hotmail_list.append(name + "@hotmail.com")

print("Usernames:", usernames)
print("New hotmail addresses:", hotmail_list)
```
