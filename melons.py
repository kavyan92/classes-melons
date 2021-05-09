"""Classes for melon orders."""


class AbstractMelonOrder():
    """An abstract base class that other melon orders inherit from."""

    def __init__(self, species, qty, tax, order_type):

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_base_price(self):
        """Splurge pricing."""
        
        base_price = random.randint(5, 9)

        return base_price

    def get_total(self):
        """Calculate price, including tax."""
        
        if (self.species).lower() == "christmas melons":
            base_price = 7.5
        else:
            base_price = self.get_base_price()

        print(base_price)
        
        if self.qty < 10 and self.order_type == "international":
            total = ((1 + self.tax) * self.qty * base_price) + 3
        else:
            total = (1 + self.tax) * self.qty * base_price 

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    def __init__(self, species, qty):
        super().__init__(species, qty, 0.08, "domestic")
        

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        
        self.country_code = country_code
        super().__init__(species, qty, 0.17, "international")
        
    # def get_total(self):
    #     """Calculate price, including tax."""
    #     super().get_total(species, qty)
        
    #     if self.qty < 10:
    #         total = ((1 + self.tax) * self.qty * base_price) + 3
    #     else:
    #         total = (1 + self.tax) * self.qty * base_price
    #     return total

class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order from the government."""

    def __init__(self, species, qty):
        
        self.passed_inspection = False
        super().__init__(species, qty, 0, "domestic")
    
    def mark_inspection(self, passed):

        if passed == True:
            self.passed_inspection = True
        else:
            self.passed_inspection = False
