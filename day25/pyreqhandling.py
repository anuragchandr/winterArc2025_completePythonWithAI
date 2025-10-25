import requests

def fetch_rand_user():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    #print(response)
    data = response.json()
    if data["success"] and "data" in data:
        p1 = data["data"] 
        name = p1["login"]["username"]
        countr = p1["location"]["country"]
        return name, countr
    else:
        raise Exception("Failed to fetch user data")
    

def main():
    try:
        username,country = fetch_rand_user()
        print(f"Username:{username}\n Country:{country}")
    except Exception as e:
        
        print(str(e))

if __name__ == "__main__":
    main()