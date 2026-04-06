# 🍕 Python Pizza Delivery System

A simple command-line Python program that calculates the total cost of a pizza order based on user input.

This project is designed for beginners to understand:
- Conditional statements (`if/elif/else`)
- User input handling
- Basic logic building in Python

---

## 🚀 Features

- Select pizza size (Small, Medium, Large)
- Add pepperoni option
- Add extra cheese option
- Calculates total bill instantly

---

## 🧠 How It Works

The program asks the user for:
1. Pizza size → `S`, `M`, or `L`
2. Pepperoni → `Y` or `N`
3. Extra cheese → `Y` or `N`

Then calculates the total bill based on the rules:

### 💰 Pricing Rules

| Item | Price |
|------|------|
| Small Pizza (S) | ₹15 |
| Medium Pizza (M) | ₹20 |
| Large Pizza (L) | ₹25 |
| Pepperoni (Small) | +₹2 |
| Pepperoni (M/L) | +₹3 |
| Extra Cheese | +₹5 |

---

## ▶️ How to Run

1. Make sure Python is installed.
2. Save the code as `pizza.py`
3. Run the program:

```bash
python pizza.py

# Example output.

Welcome to Python Pizza Deliveries
What size of pizza do you want? S, M, or L: M
Do you want pepperoni on your pizza? Y or N: Y
Do you want extra cheese on your pizza? Y or N: Y

Your final bill is: ₹28