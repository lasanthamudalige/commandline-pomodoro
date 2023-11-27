from time import sleep
import notify2


def main():
    duration = 60 * 25
    break_time = 60 * 5
    break_amount = 0

    lines = ["|", "/", "—", "\\", "|"]
    line_index = 0

    countdown = duration
    on_break = False

    while True:
        # To clear the terminal.
        print("\033c")
        # Print time and a cool line to show progress.
        print(
            f"Time left: {countdown // 60}:{(countdown % 60):02d} {lines[line_index]}")
        countdown -= 1
        # This will add 1 to line index to update the line.
        line_index += 1
        sleep(1)
        if countdown == 0 and not on_break:
            # Get 30 minutes break after 4, 10 minutes breaks.
            if break_amount == 4:
                send_notification("Excellent!", "Take a 30 minutes break now.")
                countdown = 60 * 30
                break_amount = 0
            else:
                send_notification("well done!", "Take a 5 minutes break now.")
                on_break = True
                countdown = break_time
                break_amount += 1
        elif countdown == 0 and on_break:
            send_notification("Time to start again!",
                              "The 10 minutes break is now over.")
            on_break = False
            countdown = duration
        # Reset line index after getting into the end of the list.
        if line_index == 4:
            line_index = 0


# Send a desktop notification.
def send_notification(summery, message):
    notify2.init('alert')
    n = notify2.Notification(summery, message)
    n.show()


main()
