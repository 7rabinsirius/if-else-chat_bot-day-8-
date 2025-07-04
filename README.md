# if-else-chat_bot-day-8-

```markdown
# 🤖 Joke & Time Chatbot – Python CLI Project

A light-hearted rule-based chatbot built with Python. It greets users, tells jokes using the `pyjokes` library, gives current time, and responds with playful snark when confused.

---

## 💡 Features

- 🗣 Randomized greetings and farewells for charm
- 🎭 Tells programmer jokes via `pyjokes.get_joke()`
- ⏰ Shows current system time in HH:MM:SS format
- 🤖 Graceful fallback responses with humorous tone
- 🧠 Keyword-based intent matching (joke/time/capability)
- 🪄 Easily extendable with new intents and responses

---

## 📦 Requirements

- Python 3.x
- `pyjokes` package

To install pyjokes:
```bash
pip install pyjokes
```

---

## 🚀 Run the Bot

```bash
python chatbot.py
```

It’ll:
- Greet the user
- Ask for their name
- Prompt them for a request
- Continue the conversation until they say farewell

---

## 📁 File Structure

```
chatbot/
├── chatbot.py         # Main bot script
├── README.md          # Project overview
```

---

## 🛠 How It Works

- **Intent Detection**: Matches user inputs against grouped lists of phrases
- **Phrase Matching**: Uses `any(phrase in request for phrase in list)` for flexibility
- **Randomized Responses**: Adds variety to greetings and unknown replies

---

## ✨ Sample Conversation

```text
Hiya!
What is your name? Rabin
Hiya! Rabin. What can I do for you? tell me a joke
How many Prolog programmers does it take to change a lightbulb? false.
Is there anything else I can do for you? what’s the current time
14:32:45
Is there anything else I can do for you? bye
Peace out!
```

---

## 📌 Future Enhancements

- Add emoji reactions 😄 ⏰ 🤖
- Track user interactions or mood
- Package as a simple Flask app for a web interface
- Convert into a class-based architecture for scalability

---

## 👨‍💻 Author

**Rabin R** – Python enthusiast, creative coder, and builder of cheerful bots.

---

## 🧾 License

Feel free to use, modify, and enhance this bot. Attribution appreciated. 😎
```
