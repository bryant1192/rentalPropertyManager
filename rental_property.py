class RentalProperty:
    """Represents a rental property"""

    def __init__(
        self,
        property_id,
        address,
        city,         
        monthly_rent,         
        property_type,        
        status,         
    ): 
        self.property_id = property_id
        self.address = address
        self.city = city
        self.monthly_rent = monthly_rent
        self.property_type = property_type
        self.status = status

    def update_status(self, new_status):
        self.status = new_status 

