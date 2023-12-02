import requests

def get_puzzle_input(day, year):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session = "53616c7465645f5f582fe2745fb47cba42dfc16970937207266a556a080f964aa4b9dc6ff68195d5314a83b37fa59e4337f842fd3e3b1ae3160294c9c1c142b6"
    cookies = {"session": session}
    
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        return response.text.strip()
    else:
        print(f"Failed to fetch puzzle input for day {day}. Status code: {response.status_code}")
        return None
