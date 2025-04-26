import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('clash_royale.db')  # change 'your_database.db' to your database name
cur = conn.cursor()

# Step 1: Add 'type' column if it doesn't exist
# (SQLite is simple, we'll just try adding - if it already exists, this will raise an error you can ignore)
try:
    cur.execute("ALTER TABLE cards_table ADD COLUMN type TEXT;")
except sqlite3.OperationalError:
    # This error happens if the column already exists - it's safe to ignore
    pass

# Step 2: Update 'type' column based on card names
update_query = '''
UPDATE cards_table
SET type = CASE
    -- Win Conditions
    WHEN card IN ('Hog Rider', 'Balloon', 'Royal Giant', 'X-Bow', 'Mortar', 'Goblin Barrel', 'Graveyard', 'Goblin Drill', 'Ram Rider', 'Battle Ram', 'Goblin Giant', 'Golem', 'Lava Hound', 'Miner', 'Elixir Golem', 'Sparky', 'Royal Hogs', 'Skeleton Barrel', 'Rune Giant') THEN 'Win Condition'

    -- Support Troops
    WHEN card IN ('Archer Queen', 'Archers', 'Baby Dragon', 'Bandit', 'Berserker', 'Bowler', 'Cannon Cart', 'Dark Prince', 'Dart Goblin', 'Electro Dragon', 'Electro Wizard', 'Firecracker', 'Fisherman', 'Flying Machine', 'Hunter', 'Ice Wizard', 'Inferno Dragon', 'Little Prince', 'Lumberjack', 'Magic Archer', 'Mega Minion', 'Mighty Miner', 'Mini P.E.K.K.A', 'Mini P.E.K.K.A.', 'Mother Witch', 'Musketeer', 'Night Witch', 'Phoenix', 'Prince', 'Princess', 'Royal Ghost', 'Skeleton Dragons', 'Skeleton King', 'Valkyrie', 'Witch', 'Wizard', 'Zappies', 'Golden Knight', 'Boss Bandit', 'Goblin Machine', 'Goblin Demolisher', 'Goblinstein', 'Void', 'Suspicious Bush') THEN 'Support Troop'

    -- Tanks / Mini Tanks
    WHEN card IN ('Ice Golem', 'Knight', 'Giant', 'Giant Skeleton', 'P.E.K.K.A', 'P.E.K.K.A.', 'Mega Knight', 'Skeleton King', 'Dark Prince') THEN 'Tank/Mini Tank'

    -- Defensive Buildings
    WHEN card IN ('Bomb Tower', 'Cannon', 'Furnace', 'Goblin Cage', 'Goblin Hut', 'Tesla', 'Tombstone', 'Barbarian Hut', 'Inferno Tower', 'Elixir Collector') THEN 'Building'

    -- Spells
    WHEN card IN ('Arrows', 'Barbarian Barrel', 'Clone', 'Earthquake', 'Fireball', 'Freeze', 'Giant Snowball', 'Lightning', 'Poison', 'Rage', 'Rocket', 'Royal Delivery', 'The Log', 'Tornado', 'Zap', 'Mirror') THEN 'Spell'

    -- Cycle Cards
    WHEN card IN ('Fire Spirit', 'Fire Spirits', 'Ice Spirit', 'Skeletons', 'Spear Goblins', 'Bats', 'Heal Spirit', 'Goblins') THEN 'Cycle Card'

    -- Swarm Units
    WHEN card IN ('Barbarians', 'Bats', 'Goblin Gang', 'Minion Horde', 'Minions', 'Guards', 'Skeleton Army', 'Rascals', 'Royal Recruits', 'Lava Pup') THEN 'Swarm Unit'

    ELSE 'Unknown'
END;
'''

# Execute the update
cur.execute(update_query)

# Step 3: Commit changes and close connection
conn.commit()
conn.close()

print("✅ Card types updated successfully!")
