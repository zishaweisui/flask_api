from repositories.people_repository import PeopleRepository

class PeopleService:
    def __init__(self):
        self.repo = PeopleRepository()

    def read_all(self):
        return self.repo.get_all_people()

    def read_one(self, person_id):
        return self.repo.get_one_person(person_id)

    def create(self, person):
        return self.repo.create_person(person)

    def update(self, person_id, person):
        return self.repo.update_person(person_id, person)

    def delete(self, person_id):
        return self.repo.delete_person(person_id)
