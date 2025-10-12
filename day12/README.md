# DAY 12

## Starting BlackJack Game

__Build a console-based Blackjack game using Python OOP principles.__

## 🧩 Classes Overview

| Class  | Purpose |
|---------|----------|
| **Card** | Represents one playing card (rank, suit, value). |
| **Deck** | Builds, shuffles, and deals 52 cards. |
| **Hand** | Holds player/dealer cards, tracks total value, handles Aces. |
| **Chips** | Manages betting and player’s chip balance. |
| **Player** | Represents player with a hand and chips. |
| **Dealer** | Represents dealer with auto-hit logic. |
| **Game** | Controls overall game flow and interaction. |

## ⚙️ Class Functions Summary

### Card

- __init__(suit, rank)

- __str__()

### Deck

- build()

- shuffle()

- deal()

### Hand

- add_card(card)

- adjust_for_ace()

### Chips

- win_bet()

- lose_bet()

### Player

- hit(deck)

- place_bet(amount)

### Dealer

- play(deck) → hit until value ≥ 17

### Game

- start_game()

- take_bet()

- deal_initial_cards()

- player_turn()

- dealer_turn()

- compare_hands()

- play_again()

## 🔁 Game Flow

1. Initialize and shuffle deck

2. Create player & dealer hands

3. Take player bet

4. Deal two cards each

5. Show one dealer card

6. Player hits or stands

7. Dealer plays till 17

8. Compare totals → declare winner

9. Adjust chips

10. Ask to play again
---

## 🧠 Build Order

- __✅ Card, Deck__

- 🧩 __Hand, Chips__

- 👤 __Player, Dealer__

- 🎮__Game (main loop)__
