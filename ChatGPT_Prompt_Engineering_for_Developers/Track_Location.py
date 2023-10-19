# Import necessary modules from phonenumbers library
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def main():
    # Initialize phone numbers by parsing them
    phone_numbers = ["+542964547559", "+4531723101"]
    
    print("\nPhone Numbers Information\n")
    
    for phone in phone_numbers:
        # Use phonenumbers library to parse phone numbers
        parsed_number = phonenumbers.parse(phone)
        
        # Print the original phone number
        print(f"Original Number: {phone}")
        
        # Get the geographical description of the phone number
        print(f"Geographical Location: {geocoder.description_for_number(parsed_number, 'en')}")
        
        # Get the carrier name of the phone number
        print(f"Carrier: {carrier.name_for_number(parsed_number, 'en')}")
        
        # Get the time zone of the phone number
        print(f"Time Zone(s): {timezone.time_zones_for_number(parsed_number)}")
        
        print("-----")

# Entry point of the script
if __name__ == "__main__":
    main()
