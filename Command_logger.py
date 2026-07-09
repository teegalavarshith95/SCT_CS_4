from datetime import datetime

print("===== COMMAND LOGGER =====")
print("Type exit to stop.\n")

while True:
    command = input("Enter command: ")
    if command.lower() == "exit":
        print("Logging stopped.")
        break
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs.txt", "a") as file:
        file.write(f"[{timestamp}] {command}\n")
    print("Saved successfully!")
