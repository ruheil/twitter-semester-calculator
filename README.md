# Twitter Semester Calculator

A Twitter bot that automatically posts the progress of the current academic semester as a percentage, with a visual progress bar image.

## Overview

This bot calculates how much of the semester has passed based on predefined start and end dates. It generates a progress bar image and posts it to Twitter with an Arabic caption indicating the completion percentage and remaining days until the end of the semester.

The bot runs daily at 6PM through a scheduled task on PythonAnywhere.com.

## Features

- Calculates semester completion percentage based on current date
- Generates a visual progress bar image
- Posts the progress update to Twitter with appropriate Arabic text
- Updates automatically on a daily schedule (6PM)

## Project Structure

- `main.py`: Main script that handles Twitter API authentication and posting
- `backend.py`: Contains the logic for calculating semester progress and generating the progress bar image
- `progressbar.jpg`: The generated progress bar image
- `.env`: Environment file containing Twitter API credentials
- `requirements.txt`: Required Python dependencies

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- Twitter Developer account with API credentials
- PythonAnywhere.com account (for hosting)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/twitter-semester-calculator.git
   cd twitter-semester-calculator
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your Twitter API credentials:
   ```
   BEARER_TOKEN=your_bearer_token
   CLIENT_ID=your_client_id
   CLIENT_SECRET=your_client_secret
   CONSUMER_KEY=your_consumer_key
   CONSUMER_SECRET=your_consumer_secret
   ACCESS_TOKEN=your_access_token
   ACCESS_TOKEN_SECRET=your_access_token_secret
   ```

4. Update the semester dates in `backend.py`:
   ```python
   # -- CHANGE THIS BEFORE SEMESTER STARTS --
   start_date = date(YEAR, MONTH, DAY)
   end_date = date(YEAR, MONTH, DAY)
   semester_name = "semester_name_in_arabic"
   # ------------------------------------------
   ```

### Running Locally

To run the bot manually:

```
python main.py
```

### Deployment on PythonAnywhere

1. Upload the project files to your PythonAnywhere account
2. Create a virtual environment and install the dependencies
3. Set up a scheduled task to run `main.py` daily at 6PM
4. Make sure to create the `.env` file with your Twitter API credentials

## Configuration

You can customize the following in `backend.py`:
- Semester start and end dates
- Semester name (in Arabic)
- Progress bar appearance (width, height, colors)

## Troubleshooting

- If the Twitter API returns errors, verify your API credentials in the `.env` file
- Check that your Twitter Developer account has the necessary permissions
- Ensure the `progressbar.jpg` file is writable by the script

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or assistance, please open an issue on the repository. 