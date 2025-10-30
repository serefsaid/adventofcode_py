import requests

def get_puzzle_input(day, year):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session = "53616c7465645f5feafbec9df203a00817982e8a8c6c2ba8e86f9ac850aba889c4f80ba16734d10603f8141caa1d43bca2e535bb9e483089b11af50e6ccd208c"
    cookies = {"session": session}
    
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        return response.text.strip()
    else:
        print(f"Failed to fetch puzzle input for day {day}. Status code: {response.status_code}")
        return None
