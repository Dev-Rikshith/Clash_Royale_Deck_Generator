This project builds a Clash Royale deck generator using a SQLite database of cards classified by their roles (Win Condition, Support, Tank, etc.).
It uses rule-based logic to assemble a complete 8-card deck while maintaining a maximum average elixir cost constraint.
The program fetches cards dynamically by type and filters them based on card stats like elixir, win rate, and usage.
After generating a deck, it calculates and prints key statistics including average elixir, average win rate, average usage, and average damage.
The design is modular, allowing easy extension to smarter deck strategies like prioritizing higher win rate cards or generating multiple optimized decks.