# Product Recommendation Chatbot

A command-line chatbot that helps users find the right laptop or phone based on their preferences and budget.

## Requirements

- Python3
- No external libraries are imported.

## Installation

Clone from git (insert link here):

Confirm that Python is installed:

```bash
python3 --version
```

Run the chatbot:

```bash
python3 submission.py
```

## Workflow

When the chatbot starts, it will greet the user and ask what kind of product (laptop or phone) they are looking for today. The program waits for the user's input, and depending on the input, it will redirect them to one of two separate flows.

### **Laptop flow:**
The chatbot waits for the user to enter values based on the following attributes:
- OS: ***Windows*** or ***macOS***
- Budget: ***Low (under $800)*** or ***High (over $800)***
- Primary use case: ***student***, ***work***, or ***personal***

### **Phone flow:**
- Phone preference: ***Android*** or ***iPhone***
- Budget: ***Low (under $500)*** or ***High (over $500)***
- Most desired feature: ***camera***, ***battery***, or ***performance***

The user responds by entering either the written option (e.g., `windows`) or the corresponding number (e.g., `1`). The input is not case-sensitive.

If the user enters an invalid or empty response, the chatbot will restart from that position in the flow and ask the user to enter their input again while also listing an array of accepted values. After 3 successive failed attempts, the session forcibly quits.

---

## Examples

### Example 1: Laptop Recommendation

```
Hello! Welcome to the chatbot. Let me help you find a device.

What type of product are you looking for today?
 1) laptop
  2) phone
Your answer: 1
Understood. Let me ask you a few questions first.
What operating system do you prefer?
  1) Windows
  2) macOS
Your answer: macos
What is your budget?
  1) low (under $800)
  2) high (over $800)
Your answer: high
What will you mainly use it for?
  1) student
  2) work
  3) personal
Your answer: work
I recommend the MacBook Pro (M5 Max, 16 inch).
Thank you for using our chatbot. We hope you have a great day!
```

---

### Example 2: Phone Recommendation

```
Hello! Welcome to the chatbot. Let me help you find a device.

What type of product are you looking for today?
 1) laptop
  2) phone
Your answer: 2
Understood. Let me ask you a few questions first.
Do you prefer Android or iPhone?
  1) Android
  2) iPhone
Your answer: 1
What is your budget?
  1) low (under $500)
  2) high (over $500)
Your answer: low

What feature matters most to you?
  1) camera
  2) battery
  3) performance
Your answer: camera
I recommend the Google Pixel 8a.
Thank you for using our chatbot. We hope you have a great day!
```

---

### Example 3: Invalid Input Handling

```
Hello! Welcome to the chatbot. Let me help you find a device.

What type of product are you looking for today?
 1) laptop
  2) phone
Your answer: tablet
That is not a valid option. Please choose from one of the following options: ['laptop', 'phone', '1', '2']

You have 3 attempts left.
What type of product are you looking for today?
 1) laptop
  2) phone
Your answer: phone
Understood. Let me ask you a few questions first.
Do you prefer Android or iPhone?
  1) Android
  2) iPhone
Your answer: Samsung
That is not a valid option. Please choose from one of the following options: ['android', 'iphone', '1', '2']

You have 3 attempts left.
Do you prefer Android or iPhone?
  1) Android
  2) iPhone
Your answer: 
You didn't type anything. Please enter a value and try again.

You have 2 attempts left.
Do you prefer Android or iPhone?
  1) Android
  2) iPhone
Your answer: k
That is not a valid option. Please choose from one of the following options: ['android', 'iphone', '1', '2']

You have 1 attempts left.
Do you prefer Android or iPhone?
  1) Android
  2) iPhone
Your answer: 
You didn't type anything. Please enter a value and try again.

You have 0 attempts left.
Too many invalid attempts. Exiting the chatbot.
```

## Websites used

- Online Python IDE (https://www.online-python.com/)
- Make a README (https://www.makeareadme.com/)