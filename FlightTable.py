class FlightTable:
    def __init__(self):
        self.data = []

    def add_entry(self, p_id, process, start_time, priority):
        self.data.append((p_id, process, start_time, priority))

    def display_table(self):
        print("P_ID\tProcess\t\tStart Time\tPriority")
        print("=" * 45)
        for entry in self.data:
            p_id, process, start_time, priority = entry
            print(f"{p_id}\t{process}\t\t{start_time}\t\t{priority}")

    def sort_by_p_id(self):
        self.data.sort(key=lambda entry: entry[0])

    def sort_by_start_time(self):
        self.data.sort(key=lambda entry: entry[2])

    def sort_by_priority(self):
        priority_order = {"High": 3, "MID": 2, "Low": 1}
        self.data.sort(key=lambda entry: priority_order[entry[3]])

def main():
    flight_table = FlightTable()

    flight_table.add_entry("P1", "VSCode", 100, "MID")
    flight_table.add_entry("P23", "Eclipse", 234, "MID")
    flight_table.add_entry("P93", "Chrome", 189, "High")
    flight_table.add_entry("P42", "JDK 9", 9, "High")
    flight_table.add_entry("P9", "CMD", 7, "High")
    flight_table.add_entry("P87", "NotePad", 23, "Low")

    while True:
        print("\nSelect sorting parameter:")
        print("1. Sort by P_ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            flight_table.sort_by_p_id()
        elif choice == '2':
            flight_table.sort_by_start_time()
        elif choice == '3':
            flight_table.sort_by_priority()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

        flight_table.display_table()

if __name__ == "__main__":
    main()
