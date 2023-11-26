import random


class SecretSanta(object):
    def __init__(self, families):
        self.families = families

    def get_all_members(self):
        all_members = []
        for family in self.families:
            for member in family.members:
                all_members.append(member)
        return all_members

    def generate(self):
        all_members = self.get_all_members()
        remaining_members = all_members
        for member in all_members:
            i = random.randint(0, len(remaining_members))
            print(i)


class Family(object):
    def __init__(self, name):
        self.members = []
        self.name = name

    def __repr__(self):
        return '{}: {}'.format(self.name, str(self.members))

    def add_member(self, name):
        self.members.append(Member(name, self))

    def add_members(self, names):
        for name in names:
            self.add_member(name)


class Member(object):

    def __repr__(self):
        return self.name

    def __init__(self, name, family):
        self.name = name
        self.giving_to = None
        self.receiving_from = None
        self.family = family

    def cant_give_to(self):
        return self.family.members


def main():
    tyler = Family('Tyler')
    tyler.add_members(['Brooke', 'Marcy', 'Clover'])

    hitzeroth = Family('Hitzeroth')
    hitzeroth.add_members(['Jack', 'Miles', 'Olivia', 'Georgie'])

    hays1 = Family('Hays1')
    hays1.add_members(['Kesnia', 'Ellie', 'Sasha', 'Vincent'])

    hays2 = Family('Hays2')
    hays2.add_members(['Hazel', 'Emmet', 'Knox'])

    generator = SecretSanta([tyler, hitzeroth, hays1, hays2])
    generator.generate()


main()
