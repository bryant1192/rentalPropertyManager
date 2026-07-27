from rental_property import RentalProperty

properties = {}


property1 = RentalProperty(
    property_id = 1,
    address = "123 Blueway St",
    city = "Color City",
    monthly_rent = 2000,
    property_type = "House",
    status = "Vacant"
)

properties[property1.property_id] = property1

def add_property():
    print("Enter Property Details: ")

    property_id = max(properties, default = 0) + 1

    address = input("Address: ")
    city = input("City Name: ")
    monthly_rent = int(input("Monthly Rent in Dollars: "))
    property_type = input("Property Type: ")
    status = input("Property Status: ")

    new_property = RentalProperty(
        property_id,
        address,
        city,
        monthly_rent,
        property_type,
        status
    )

    properties[property_id] = new_property

    print(f"New property {property_id} added successfully.")


def display_property(prop):
    print(f"Property ID: {prop.property_id}")
    print(f"Property Address: {prop.address}")
    print(f"City: {prop.city}")
    print(f"Monthly Rent: {prop.monthly_rent:,.2f}")
    print(f"Property Type: {prop.property_type}")
    print(f"Status: {prop.status}")

def generate_listing_description():
    property_id = int(input("Enter Property ID to generate a description for it: "))

    if property_id in properties:
        prop = properties[property_id]

        print("\nGenerated Listing Description")
        print("=============================")
        print(f"Rental Property Available in {prop.city}")
        print()
        print(
            f"This {prop.property_type.lower()} is located at "
            f"{prop.address} in {prop.city}."
        )
        print(
            f"It is available for rent at "
            f"${prop.monthly_rent:,.2f} per month."
        )
        print(f"The property is currently {prop.status.lower()}.")
        print(
            "Contact the property owner for additional information "
            "or to schedule a viewing."
        )
    else:
        print("Property not found.")


while True:
    print("\n==============================")
    print("Rental Property Manager")
    print("==============================")
    print("1. Add Property")
    print("2. View Properties")
    print("3. Generate Property Description")
    print("4. Help")
    print("5. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        add_property()

    elif choice == "2":
        print("View Properties Selected")

        if properties:
            for prop in properties.values():
                display_property(prop)
                print()
        else:
            print("No properties found.")

    elif choice == "3":
        print("Generate Property Description Selected.")
        generate_listing_description()

    elif choice == "4":
        print("Help selected.")

    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")