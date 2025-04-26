import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('clash_royale.db')  # <-- change to your database file name
cur = conn.cursor()

# Mapping for the newly listed cards
new_card_type_mapping = {
    'Battle Healer': 'Support Troop',
    'Bomber': 'Support Troop',
    'Electro Giant': 'Win Condition',
    'Electro Spirit': 'Cycle Card',
    'Elite Barbarians': 'Win Condition',
    'Executioner': 'Support Troop',
    'Goblin Curse': 'Spell',  # (Confirm if this is actually a spell. Adjust if needed)
    'Golemite': 'Support Troop',
    'Monk': 'Tank/Mini Tank',
    'Three Musketeers': 'Win Condition',
    'Wall Breakers': 'Win Condition'
}

# Update each card individually
for card_name, card_type in new_card_type_mapping.items():
    cur.execute("""
        UPDATE cards_table
        SET type = ?
        WHERE card = ?
    """, (card_type, card_name))

# Commit changes and close connection
conn.commit()
conn.close()

print("✅ New cards updated successfully!")
