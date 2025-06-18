from utils.api_handler import call_api

def main():
    response = call_api()
    print("API Response:", response)

if __name__ == "__main__":
    main()
