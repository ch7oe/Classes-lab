"""Classes for melon orders."""

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""
    
    order_type = None
    tax = 0
    
    
    def __init__(self, species, qty):
        #intialize melon order attributes.
        self.species = species
        self.qty = qty
        self.shipped = False
        self.base_price = 5
        
    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        # apply Christmas melon multiplier
        if self.species.lower() == "christmas melon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

    # Add flat fee for international orders with less than 10 melons
        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total
        
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):    
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08
    

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = 'international'
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty,)

        self.country_code = country_code
        

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
