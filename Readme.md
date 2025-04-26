# 🏰 Clash Royale Rule-Based Deck Generator

Welcome to the **Clash Royale Deck Generator**!  
This project automatically builds **balanced battle decks** using real card stats and smart rules — so you always have the right mix of win conditions, support troops, spells, tanks, and more.

Built for **fun** and **strategy**, the generator ensures your deck is strong, quick to cycle, and **easy to play** without overspending elixir.

---

## 📚 How It Works
- The program reads card data from a **SQLite database** containing cards classified into types:  
  *(Win Condition, Support Troop, Spell, Cycle Card, Tank/Mini Tank, Defensive Building, Swarm Unit)*  
- It follows **deck-building rules** to select 8 cards:  
  - 1 Win Condition  
  - 2 Support Troops  
  - 1 Tank / Mini Tank  
  - 1 Defensive Building  
  - 2 Spells  
  - 1 Cycle or Swarm Unit  
- Ensures **average elixir cost** is **below 4.5** for faster gameplay.
- Prints out the **deck list** and **deck statistics**:  
  *(Average Elixir, Average Win Rate, Average Usage Rate, Average Damage)*

---

## 📥 Input Format
- Card data must be stored in a **SQLite database** with the following important columns:
  - `Card` (Card Name)
  - `elixirCost`
  - `Win Rate`
  - `Usage`
  - `Damage`
  - `Type` (such as "Support Troop", "Spell", etc.)

👉 *(The script automatically organizes cards into groups based on their Type.)*

---

## 📤 Example Output

Here’s what a sample generated deck looks like:

```
Generated Deck:

- Hog Rider (Elixir: 4.0)
- Musketeer (Elixir: 4.0)
- Knight (Elixir: 3.0)
- Tesla (Elixir: 4.0)
- Fireball (Elixir: 4.0)
- Zap (Elixir: 2.0)
- Skeletons (Elixir: 1.0)
- Goblin Gang (Elixir: 3.0)

Deck Statistics:
- Average Elixir: 3.38
- Average Win Rate: 54.91%
- Average Usage Rate: 7.61%
- Average Damage: 148.75
```

---

## 🎯 Features
- **Smart deck rules** for a balanced team
- **Low elixir cycle decks** for faster and easier battles
- **Real stat-based selection** (Win Rate, Usage, Damage)
- **Deck stats** printed automatically
- **Retry logic** if average elixir is too high

---

## 🚀 Future Ideas
- Automatically pick **highest win rate cards** from each role
- Generate **multiple decks at once** and compare them
- Add **rarity filters** (only common, rare decks, etc.)
- Build a **simple Web UI** to generate decks at a click

---

# ⚡ Quick Start
1. Add your card data to a SQLite database.
2. Edit the database filename and table name in the script.
3. Run the script → **Get your deck and go crush battles!**

---

# 🛡️ Project Status
> **Version 1.0** — fully working for rule-based single deck generation.  
> Designed to be easily extendable to smarter strategies!

---

# 📬 Contact
If you have ideas or improvements for the deck generator, feel free to contribute or suggest changes! 🎮👑

---

# Example input table snapshot

| Card | elixirCost | Win Rate | Usage | Damage | Type |
|:----:|:----------:|:--------:|:-----:|:------:|:----:|
| Hog Rider | 4.0 | 51.93 | 0.76 | 264 | Win Condition |
| Tesla | 4.0 | 50.38 | 0.32 | 135 | Building |
| Fireball | 4.0 | 53.21 | 0.75 | 572 | Spell |
| Skeletons | 1.0 | 51.05 | -0.26 | 67 | Cycle Card |
| ... | ... | ... | ... | ... | ... |

---

# 🏆 Special Thanks
Thanks to the Clash Royale community for inspiring thousands of creative decks!

