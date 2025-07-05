# Develop a project based on a LLM algorithm to generate meaningful travel itineraries for travel agencies across different locations in New Zealand.

from google import genai

# Initialize the Gemini API
GOOGLE_API_KEY = "AIzaSyAagilvq45iIztXGs24RAIXPSPX7LYxbjs"
client = genai.Client(api_key=GOOGLE_API_KEY)

def instructor_chatbot():
    """Command-line AI Itinerary Chatbot using Google Gemini."""
    print("Welcome to AI Itinerary recommender! Answer a few questions to get personalized itinerary advice.\n")
    
    days = input("How many (days): ")
    location = input("Where is the destination (city name): ")
    age = input("Enter your age: ")
    
    # Construct prompt
    prompt = f"""
    You are a professional tourist recommender. Provide an itinerary recommendation based on user data.
    
    User Details:
    - days: {days} days
    - destination: {location} city
    - Age: {age} years
    
    Based on your personal information, 
    Then, give a structured itinerary with a name of the place, address and short description for each day separately in order with maximum three activities in a day.
    """
    
    try:        
        response = client.models.generate_content(
            model = 'gemini-2.5-flash',
            contents = prompt,
        )
        
        print("\nMy Name is Alley as AI Itinerary expert:")
        # Print the response
        print(response.text)
        
    except Exception as e:
        print("Error communicating with Google Gemini API:", e)

if __name__ == "__main__":
    instructor_chatbot()