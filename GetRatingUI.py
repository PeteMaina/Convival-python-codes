
    # This code extends the code in GetRating.py where this one includes tkinter to have an UI
    # I saw it best not to push to that code insted to create a seperate file
    # Email : peterwahomemaina003@gmail.com | Whatsapp : +254794797796

from tkinter import *
from imdb import IMDb

def get_movie_rating():
    """
    Fetches the IMDb rating of a movie using the IMDbpy library.

    Args:
        None

    Returns:
        None
    """

    def fetch_rating():
        try:
            movie_name = movie_entry.get()
            ia = IMDb()
            movies = ia.search_movie(movie_name)

            if movies:
                movie = movies[0]
                ia.update(movie)
                rating = movie.get('rating', 'N/A')
                result_label.config(text=f"IMDb Rating: {rating}")
            else:
                result_label.config(text=f"Movie '{movie_name}' not found!")
        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")

    # Create the main window
    window = Tk()
    window.title("IMDb Rating Finder")

    # Create widgets
    movie_label = Label(window, text="Enter Movie Name:")
    movie_entry = Entry(window, width=50)
    find_button = Button(window, text="Find Rating", command=fetch_rating)
    result_label = Label(window, text="", font=("Arial", 12))

    # Arrange widgets using grid layout
    movie_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    movie_entry.grid(row=0, column=1, padx=10, pady=10)
    find_button.grid(row=1, column=0, columnspan=2, pady=10)
    result_label.grid(row=2, column=0, columnspan=2, pady=10)

    # Run the main event loop
    window.mainloop()

if __name__ == "__main__":
    get_movie_rating()