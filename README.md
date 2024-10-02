# Dictionary

This is a Django-based web application that fetches word definitions and synonyms from [Dictionary.com](https://www.dictionary.com) and [Thesaurus.com](https://www.thesaurus.com). The app allows users to search for a word, view its definition, pronunciation, and see strong, strongest, and weak synonyms categorized accordingly.

## Features

- **Word Search**: Allows users to search for a word and retrieve its meanings from Dictionary.com.
- **Pronunciation**: Displays the pronunciation of the searched word.
- **Synonyms**: Displays categorized synonyms (strongest, strong, and weak) from Thesaurus.com.
- **Bootstrap Integration**: The app is styled using Bootstrap 5 for responsive design.
- **Error Handling**: Displays a user-friendly error message if no results are found for a word.

## Technologies Used

- **Django**: Web framework used for backend.
- **BeautifulSoup4 (bs4)**: For scraping data from Dictionary.com and Thesaurus.com.
- **Requests**: For sending HTTP requests to retrieve web pages.
- **Bootstrap 5**: For frontend styling and responsive design.

## Setup

### Prerequisites

- Python 3.x
- Django
- `requests` library
- `beautifulsoup4` library

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/dictionary-thesaurus-app.git
   cd dictionary-thesaurus-app

2. Install required Python packages:

   ```bash
   pip install -r requirements.txt

3. Run the Django development server:

   ```bash
   python manage.py runserver

4. Access the app in your browser at http://127.0.0.1:8000/.

### Usage

- Navigate to the homepage.
- Enter a word into the search box and click the Search button.
- View the results including the word's definition, pronunciation, and synonyms.
- If you want to reset the search, click the Reset button to clear the results.

