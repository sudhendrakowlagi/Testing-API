from utils.api_handler import call_api

def main():
    response = call_api()
    t = printfunction()
    print(t)
    print("API Response:", response)
    

if __name__ == "__main__":
    main()
