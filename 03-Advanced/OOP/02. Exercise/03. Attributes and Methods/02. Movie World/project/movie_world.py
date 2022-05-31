class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: object):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: object):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        if len(self.search(customer_id, dvd_id)) == 2:
            customer, dvd = self.search(customer_id, dvd_id)
            return f"{customer.name} has already rented {dvd.name}"
        else:
            customer = self.search(customer_id, dvd_id)[0]
            for dvd in self.dvds:
                if dvd.id == dvd_id:
                    if dvd.is_rented:
                        return "DVD is already rented"
                    if customer.age < dvd.age_restriction:
                        return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
                    customer.rented_dvds.append(dvd)
                    dvd.is_rented = True
                    return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        if len(self.search(customer_id, dvd_id)) == 2:
            customer, dvd = self.search(customer_id, dvd_id)
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        else:
            customer = self.search(customer_id, dvd_id)[0]
            return f"{customer.name} does not have that DVD"

    def search(self, customer_id, dvd_id):
        res = []
        for customer in self.customers:
            if customer.id == customer_id:
                res.append(customer)
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        res.append(dvd)
        return res

    def __repr__(self):
        res = str()
        for customer in self.customers:
            res += f'{customer}\n'

        for dvd in self.dvds:
            res += f'{dvd}\n'
        return res
