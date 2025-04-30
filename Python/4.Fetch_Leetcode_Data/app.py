import requests
import json

def fetch_leetcode_full_profile(username):
    url = "https://leetcode.com/graphql"

    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/{username}/",
        "Origin": "https://leetcode.com",
        "User-Agent": "Mozilla/5.0"
    }

    query = {
        "query": """
        query getUserProfile($username: String!) {
          matchedUser(username: $username) {
            username
            profile {
              realName
              userAvatar
              countryName
              ranking
              reputation
              starRating
              aboutMe
              school
              company
              skillTags
            }
            submitStats {
              acSubmissionNum {
                difficulty
                count
                submissions
              }
            }
            badges {
              name
              icon
              creationDate
            }
          }
        }
        """,
        "variables": {
            "username": username
        }
    }

    response = requests.post(url, headers=headers, json=query)

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=2))  # Pretty-print for now
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


# Replace with your LeetCode username
fetch_leetcode_full_profile("akshityadav")
