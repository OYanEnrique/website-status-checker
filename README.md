# 🌐 Website Status Checker

A simple command-line tool that takes a website URL from the user and checks if it is online and accessible. It demonstrates basic web requests and error handling in Python.

## Features

* **Website Accessibility Check**: Uses Python's built-in `urllib` library to attempt a connection to a given URL.
* **User Input**: Prompts the user to enter the website they want to check.
* **Error Handling**: Uses a `try...except` block to gracefully handle `URLError` exceptions, preventing the program from crashing if the site is down or the URL is invalid.

## How to Use

1.  Ensure you have Python installed and an active internet connection.
2.  Save the code as a `.py` file (e.g., `pudding.py`).
3.  Run the script from your terminal:
    ```sh
    python pudding.py
    ```
4.  When prompted, enter a website URL **without** the `http://` prefix (e.g., `google.com`).

### Example 1: Successful Check

```sh
> python status_checker.py
Enter a website URL: google.com
Website http://google.com is up and running.
```

### Example 2: Failed Check

```sh
> python status_checker.py
Enter a website URL: some-nonexistent-website-123.com
Failed to retrieve webpage.
```
