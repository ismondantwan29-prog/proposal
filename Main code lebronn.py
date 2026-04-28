import sys
import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import print as rprint

# The Real Imports
from player import Player
import events

console = Console()

def display_stats(player):
    #Prints Twan's current stats constantly using a rich table.
    table = Table(title="Twan's Current Stats", title_style="bold cyan")
    
    table.add_column("GPA", justify="center", style="cyan", no_wrap=True)
    table.add_column("Stress", justify="center", style="magenta")
    table.add_column("Readiness", justify="center", style="green")
    table.add_column("Peer Respect", justify="center", style="yellow")
    table.add_column("Major", justify="center", style="white")

    stress_str = "[bold red]{0}[/bold red]".format(player.stress) if player.stress > 80 else str(player.stress)
    gpa_str = "[bold red]{0:.1f}[/bold red]".format(player.gpa) if player.gpa < 3.2 else "{0:.1f}".format(player.gpa)

    table.add_row(gpa_str, stress_str, str(player.readiness), str(player.peer_respect)) 
    console.print(table)
    console.print("\n")


def check_death(player):
    #Checks if Twan's head explodes from bad stats.
    if not player.is_alive or player.gpa < 3.0 or player.stress > 100 or player.peer_respect < 0:
        death_msg = Text(
            "\n Hello you have lost you are a failure hahaha \n", 
            style="bold red on black", 
            justify="center"
        )
        console.print(Panel(death_msg, border_style="red", title="[ GAME OVER - TWAN FAILED ]"))
        sys.exit()


def check_internship(player):
    #Checks if Twan meets the requirements to win the game.
    if player.gpa >= 3.5 and player.peer_respect >= 80 and player.readiness >= 80 and player.has_internship:
        win_msg = Text(
            "\n Congratulations! Twan secured the Private Internship and survived college! \n", 
            style="bold green on black", 
            justify="center"
        )
        console.print(Panel(win_msg, border_style="green", title="[ YOU WIN ]"))
        sys.exit()
    return False


def main():
    # 1. Initialize REAL Player
    player = Player()

    console.print(Panel("[yellow]Twan Survivess College\nLebronjames College of Jawns[/yellow]"))
    
    # 2. Main Game Loop (8 Semesters)
    for semester in range(1, 9):
        console.rule("[bold blue]Semester {0} Begins[/bold blue]".format(semester))
        time.sleep(1)

        # 4 Interactive Events per semester
        for event_num in range(1, 5):
            console.print("\n[bold]Week {0} - Event {1}/4[/bold]".format(event_num * 3, event_num))
            
            # Alternates between Academic and Social events from events.py
            if event_num % 2 != 0:
                events.trigger_academic_event(player)  
            else:
                events.trigger_social_event(player)
            
            # Show stats and check survival after the player makes their choice
            time.sleep(1)
            display_stats(player)
            check_death(player)

        # Final Exam Event
        console.rule("[bold red]FINALS WEEK[/bold red]")
        events.final_exam(player)
        display_stats(player)
        check_death(player)
        time.sleep(1)

        # Internship Check at the end of the semester
        check_internship(player)

        # Semester Transition / Stress Relief
        if semester < 8:
            player.update_stats(stress_change=-15) 
            console.print("[italic green]Semester complete. Twan catches his breath before the next term... (Stress -15)[/italic green]\n")
            time.sleep(2)

    # 3. Game Over (Survived 8 semesters but no internship)
    fail_msg = Text(
        "\n Twan graduated, but failed to get a job. He works at a fast food restaurant now you need high stats in everything to win and you didn't do it you failed. \n Hello you have lost you are a failure hahaha \n", 
        style="bold red on black", 
        justify="center"
    )
    console.print(Panel(fail_msg, border_style="red", title="[ GAME OVER ]"))
# So if it crash it doesn't crash ugly also used ai for this just to understand everything
if __name__ == "__main__":
    try:
        import rich
    except ImportError:
        print("Please install the 'rich' library by running: pip install rich")
        sys.exit(1)
    main()