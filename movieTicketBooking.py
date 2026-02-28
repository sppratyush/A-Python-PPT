import time

class MovieTheater:
    def __init__(self):
        self.movies = {
            "1": {"title": "Dune: Part Two", "time": "18:00", "price": 15.00, "seats": self._generate_seats(5, 5)},
            "2": {"title": "Oppenheimer", "time": "20:30", "price": 12.50, "seats": self._generate_seats(5, 5)},
            "3": {"title": "Spider-Man", "time": "15:00", "price": 10.00, "seats": self._generate_seats(5, 5)}
        }
        self.my_tickets = []

    def _generate_seats(self, rows, cols):
        """Creates a dictionary of seats. True = Available, False = Booked."""
        seats = {}
        row_labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(rows):
            for j in range(1, cols + 1):
                seat_id = f"{row_labels[i]}{j}"
                seats[seat_id] = True 
        return seats

    def display_movies(self):
        print("\n--- Currently Showing ---")
        for m_id, data in self.movies.items():
            print(f"[{m_id}] {data['title']} | Time: {data['time']} | Price: ${data['price']:.2f}")
        print("-------------------------")

    def display_seats(self, movie_id):
        movie = self.movies[movie_id]
        seats = movie["seats"]
        
        print(f"\n--- Seating for {movie['title']} ---")
        print("      [ SCREEN ]      \n")
        
        # We know it's a 5x5 grid (A-E, 1-5) based on our initialization
        print("   1  2  3  4  5")
        for row in 'ABCDE':
            row_display = f"{row} "
            for col in range(1, 6):
                seat_id = f"{row}{col}"
                # [O] for available, [X] for booked
                if seats[seat_id]:
                    row_display += "[O]"
                else:
                    row_display += "[X]"
            print(row_display)
        print("\nKey: [O] Available | [X] Booked")

    def book_ticket(self):
        self.display_movies()
        movie_choice = input("Enter the movie number you want to watch (or 'q' to cancel): ").strip()
        
        if movie_choice.lower() == 'q': return
        if movie_choice not in self.movies:
            print("Invalid movie selection.")
            return

        movie = self.movies[movie_choice]
        
        while True:
            self.display_seats(movie_choice)
            seat_choice = input("\nEnter seat number to book (e.g., A3) or 'q' to finish: ").strip().upper()
            
            if seat_choice == 'Q':
                break
                
            if seat_choice not in movie["seats"]:
                print("Invalid seat number. Please try again.")
                continue
                
            if not movie["seats"][seat_choice]:
                print(f"Sorry, seat {seat_choice} is already booked!")
                continue
                
            # Confirm booking
            movie["seats"][seat_choice] = False # Mark as booked
            ticket_info = {
                "title": movie["title"],
                "time": movie["time"],
                "seat": seat_choice,
                "price": movie["price"]
            }
            self.my_tickets.append(ticket_info)
            print(f"Success! Seat {seat_choice} added to your cart.")
            time.sleep(1) # Slight pause for better UX

    def view_tickets(self):
        if not self.my_tickets:
            print("\nYou haven't booked any tickets yet.")
            return
            
        print("\n=== YOUR TICKETS ===")
        total_cost = 0
        for idx, ticket in enumerate(self.my_tickets, 1):
            print(f"{idx}. {ticket['title']} | {ticket['time']} | Seat: {ticket['seat']} | ${ticket['price']:.2f}")
            total_cost += ticket['price']
        print("-" * 20)
        print(f"TOTAL DUE: ${total_cost:.2f}")
        print("====================")

    def run(self):
        print("Welcome to the Python Terminal Multiplex!")
        while True:
            print("\n--- MAIN MENU ---")
            print("1. View Movies")
            print("2. Book a Ticket")
            print("3. View My Tickets")
            print("4. Exit")
            
            choice = input("Select an option (1-4): ").strip()
            
            if choice == '1':
                self.display_movies()
            elif choice == '2':
                self.book_ticket()
            elif choice == '3':
                self.view_tickets()
            elif choice == '4':
                print("Thank you for using the Terminal Multiplex. Enjoy your movie!")
                break
            else:
                print("Invalid option. Please enter a number between 1 and 4.")

# Entry point of the script
if __name__ == "__main__":
    app = MovieTheater()
    app.run()