import pandas as pd

print("Starting cricket match data collection...")

matches = [
    {
        "Match Date": "2023-02-09",
        "Team 1": "India",
        "Team 2": "Australia",
        "Venue": "Vidarbha Cricket Association Stadium Nagpur",
        "Winner": "India",
        "Top Scorer": "Rohit Sharma",
        "Top Score": 120
    },

    {
        "Match Date": "2023-02-17",
        "Team 1": "India",
        "Team 2": "Australia",
        "Venue": "Arun Jaitley Stadium Delhi",
        "Winner": "India",
        "Top Scorer": "Usman Khawaja",
        "Top Score": 81
    },

    {
        "Match Date": "2023-03-01",
        "Team 1": "India",
        "Team 2": "Australia",
        "Venue": "Holkar Cricket Stadium Indore",
        "Winner": "Australia",
        "Top Scorer": "Usman Khawaja",
        "Top Score": 60
    },

    {
        "Match Date": "2023-03-09",
        "Team 1": "India",
        "Team 2": "Australia",
        "Venue": "Narendra Modi Stadium Ahmedabad",
        "Winner": "Draw",
        "Top Scorer": "Virat Kohli",
        "Top Score": 186
    },

    {
        "Match Date": "2023-06-07",
        "Team 1": "Australia",
        "Team 2": "India",
        "Venue": "Kennington Oval London",
        "Winner": "Australia",
        "Top Scorer": "Travis Head",
        "Top Score": 163
    },

    {
        "Match Date": "2024-11-22",
        "Team 1": "Australia",
        "Team 2": "India",
        "Venue": "Perth Stadium Perth",
        "Winner": "India",
        "Top Scorer": "Yashasvi Jaiswal",
        "Top Score": 161
    },

    {
        "Match Date": "2024-12-06",
        "Team 1": "Australia",
        "Team 2": "India",
        "Venue": "Adelaide Oval Adelaide",
        "Winner": "Australia",
        "Top Scorer": "Travis Head",
        "Top Score": 140
    },

    {
        "Match Date": "2024-12-14",
        "Team 1": "Australia",
        "Team 2": "India",
        "Venue": "Brisbane Cricket Ground Brisbane",
        "Winner": "Draw",
        "Top Scorer": "Travis Head",
        "Top Score": 152
    },

    {
        "Match Date": "2024-12-26",
        "Team 1": "Australia",
        "Team 2": "India",
        "Venue": "Melbourne Cricket Ground Melbourne",
        "Winner": "Australia",
        "Top Scorer": "Steve Smith",
        "Top Score": 140
    },

    {
        "Match Date": "2025-01-03",
        "Team 1": "Australia",
        "Team 2": "India",
        "Venue": "Sydney Cricket Ground Sydney",
        "Winner": "Australia",
        "Top Scorer": "Rishabh Pant",
        "Top Score": 61
    }
]

df = pd.DataFrame(matches)

df.to_csv("match_data.csv", index=False)

print("CSV file created successfully!")