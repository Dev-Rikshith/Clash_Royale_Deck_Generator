import sqlite3
import random

# Connect to database
conn = sqlite3.connect('clash_royale.db')  # <- Change filename
cursor = conn.cursor()

# Fetch all cards
def fetch_all_cards():
    query = "SELECT Card, elixirCost, `Win Rate`, Usage, Damage, Type FROM cards_table"
    cursor.execute(query)
    return cursor.fetchall()

# Load all cards
all_cards = fetch_all_cards()

# Card pools built from your correct Type categories
card_pool = {
    "Win Condition": [c for c in all_cards if c[5] == "Win Condition"],
    "Support Troops": [c for c in all_cards if c[5] == "Support Troop"],
    "Tanks": [c for c in all_cards if c[5] == "Tank/Mini Tank"],
    "Defensive Buildings": [c for c in all_cards if c[5] == "Building"],
    "Spells": [c for c in all_cards if c[5] == "Spell"],
    "Cycle Cards": [c for c in all_cards if c[5] == "Cycle Card"],
    "Swarm Units": [c for c in all_cards if c[5] == "Swarm Unit"]
}

# Deck structure rules
deck_structure = {
    "Win Condition": 1,
    "Support Troops": 2,
    "Tanks": 1,
    "Defensive Buildings": 1,
    "Spells": 2,
    "Cycle Cards": 1,
    "Swarm Units": 1
}

# Generate a valid deck
def generate_deck(card_pool, deck_structure, max_average_elixir=4.5):
    attempts = 0
    while attempts < 100:
        deck = []
        for category, count in deck_structure.items():
            available = card_pool.get(category, [])
            if len(available) >= count:
                deck += random.sample(available, count)
            else:
                deck += available
        
        deck = deck[:8]
        
        # Calculate average elixir
        total_elixir = sum(float(card[1]) for card in deck)
        avg_elixir = total_elixir / len(deck)
        
        if avg_elixir <= max_average_elixir:
            return deck
        
        attempts += 1
    
    return None

# Main function
def main():
    deck = generate_deck(card_pool, deck_structure)
    if deck:
        print("Generated Deck:\n")
        for card in deck:
            print(f"- {card[0]} (Elixir: {card[1]})")
        
        # Deck stats
        total_elixir = sum(float(card[1]) for card in deck)
        total_winrate = sum(float(card[2]) for card in deck)
        total_usage = sum(float(card[3]) for card in deck)
        total_damage = sum(float(card[4]) if card[4] not in (None, '', 'None') else 0 for card in deck)
        
        avg_elixir = total_elixir / len(deck)
        avg_winrate = total_winrate / len(deck)
        avg_usage = total_usage / len(deck)
        avg_damage = total_damage / len(deck)

        print("\nDeck Statistics:")
        print(f"- Average Elixir: {avg_elixir:.2f}")
        print(f"- Average Win Rate: {avg_winrate:.2f}%")
        print(f"- Average Usage Rate: {avg_usage:.2f}%")
        print(f"- Average Damage: {avg_damage:.2f}")
    else:
        print("Failed to generate a deck with acceptable elixir.")

if __name__ == "__main__":
    main()

conn.close()
