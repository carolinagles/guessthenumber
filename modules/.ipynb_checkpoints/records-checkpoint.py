"""
Game Records

- Display last 20 games in table format
- Best/Worst players in bar chart
- Pie chart for wins/losses
"""
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
from .config import statistics_file

# Menu for records
def records_menu():
    while True:
        print("Records")
        print("\n1. Last 20 Games\n2. Player Performance\n3. Percentage of Games Won or Lost\n4. Return\n")
        option = input("Select a numeric option: ")
        
        if option == '1':
            last_games()
        elif option == '2':
            player_performance()           
        elif option == '3':
            games_pie_chart()
        elif option == '4':
            break
        else:
            print("Please select an option between 1-4: ")

            
# Last games            
def last_games():
    print("\n   Last Games")
    display(pd.read_excel(statistics_file).tail(20))


def player_performance():
    df = pd.read_excel(statistics_file)
    
    # Verificar si hay datos
    if df.empty:
        print("No game data available yet.")
        return

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Top 10 players with most wins
    wins_count = df[df['Result'] == 'Won']['Name'].value_counts()
    if not wins_count.empty:
        wins_count.head(10).plot.bar(
            ax=ax1,
            title="Top 10 Players - Most Wins",
            color="mediumseagreen",
            edgecolor="white"
        )
        ax1.set_ylabel("Wins")
        ax1.set_xlabel("Players")
        ax1.tick_params(axis='x', rotation=45)
    else:
        ax1.text(0.5, 0.5, 'No wins recorded', 
                ha='center', va='center', transform=ax1.transAxes)
        ax1.set_title("Top 10 Players - Most Wins")

    # Top 10 players with most losses
    losses_count = df[df['Result'] == 'Lost']['Name'].value_counts()
    if not losses_count.empty:
        losses_count.head(10).plot.bar(
            ax=ax2,
            title="Top 10 Players - Most Losses",
            color="tomato",
            edgecolor="white"
        )
        ax2.set_ylabel("Losses")
        ax2.set_xlabel("Players")
        ax2.tick_params(axis='x', rotation=45)
    else:
        ax2.text(0.5, 0.5, 'No losses recorded', 
                ha='center', va='center', transform=ax2.transAxes)
        ax2.set_title("Top 10 Players - Most Losses")
   
    fig.suptitle("Player Performance - Top 10 Rankings", fontsize=16)
    plt.subplots_adjust(top=0.85, wspace=0.3) 
    plt.show()


# Pie charts 
def games_pie_chart():
    df = pd.read_excel(statistics_file)
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 3))

    # General stats    
    df['Result'].value_counts().plot.pie(
        ax=ax1,
        title="All Games",
        shadow=True,
        colors=["darkgray", "whitesmoke"],
        autopct='%d'
    )
    ax1.set_ylabel('')
    
    # Single player
    df[df['Mode']=="Single"]['Result'].value_counts().plot.pie(
        ax=ax2,
        title="Single Player Games",
        shadow=True,
        colors=["darkgray", "whitesmoke"],
        autopct='%d'
    )
    ax2.set_ylabel('')

    # Two players
    df[df['Mode']=="Double"]['Result'].value_counts().plot.pie(
        ax=ax3,
        title="Two Player Games",
        shadow=True,
        colors=["darkgray", "whitesmoke"],
        autopct='%d'
    )
    ax3.set_ylabel('')
    
    fig.suptitle("Percentage of Games Won or Lost", fontsize=14)
    plt.subplots_adjust(top=0.75) 
    plt.show()