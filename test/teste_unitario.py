import gspread
wb = gspread.oauth().open_by_url(
    "https://docs.google.com/spreadsheets/d/1VzpEt7gddPivhRWSUbmo1jX4SvxwMdU9hywLcnyrvNo/edit?usp=sharing")

print(wb)
