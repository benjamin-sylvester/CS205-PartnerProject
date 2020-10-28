class Customer:

    def __init__(self, party_name, party_size, location_pref, is_waiting=True, is_seated=False, is_finished=False):
        self.party_name = party_name
        self.party_size = party_size
        self.location_pref = location_pref
        self.is_waiting = is_waiting
        self.is_seated = is_seated
        self.is_finished = is_finished



    def get_party_name(self):
        return self.party_name

    def get_party_size(self):
        return self.party_size

    def get_location_pref(self):
        return self.location_pref

    def get_is_waiting(self):
        return self.is_waiting

    def get_is_seated(self):
        return self.is_seated

    def get_is_finsihed(self):
        return self.is_finished