class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: object):
        self.add(self.customers, customer)

    def add_trainer(self, trainer: object):
        self.add(self.trainers, trainer)

    def add_equipment(self, equipment: object):
        self.add(self.equipment, equipment)

    def add_plan(self, plan: object):
        self.add(self.plans, plan)

    def add_subscription(self, subscription: object):
        self.add(self.subscriptions, subscription)

    @staticmethod
    def add(iterable, element):
        if element not in iterable:
            iterable.append(element)

    @staticmethod
    def check(iterable, element):
        for object in iterable:
            if object.id == element:
                return object

    def subscription_info(self, subscription_id):
        res = str()
        subscription = self.check(self.subscriptions, subscription_id)
        res += f'{subscription}\n'
        customer = self.check(self.customers, subscription.customer_id)
        res += f'{customer}\n'
        trainer = self.check(self.trainers, subscription.trainer_id)
        res += f'{trainer}\n'
        plan = self.check(self.plans, subscription.exercise_id)
        equipment = self.check(self.equipment, plan.equipment_id)
        res += f'{equipment}\n'
        res += f'{plan}'
        return res
