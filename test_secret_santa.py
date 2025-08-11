from family_member import Family
from secret_santa import secret_santa_assign, is_valid_assignment

# Create families and members
tyler_family = Family("Tyler")
tyler_family.add_member_by_name("Brent", "Tyler")
tyler_family.add_member_by_name("Hayley", "Tyler")

hays_family = Family("Hays")
hays_family.add_member_by_name("Harrison", "Hays")
hays_family.add_member_by_name("Vika", "Hays")
hays_family.add_member_by_name("Ksenia", "Hays")
hays_family.add_member_by_name("Ellie", "Hays")
hays_family.add_member_by_name("Sasha", "Hays")
hays_family.add_member_by_name("Vincent", "Hays")
hays_family.add_member_by_name("Vika", "Hays")


hitzeroth_family = Family("Hitzeroth")
hitzeroth_family.add_member_by_name("Matt", "Hitzeroth") 
hitzeroth_family.add_member_by_name("Heather", "Hitzeroth")
hitzeroth_family.add_member_by_name("Georgie", "Hitzeroth")
hitzeroth_family.add_member_by_name("Olivia", "Hitzeroth")
hitzeroth_family.add_member_by_name("Miles", "Hitzeroth")
hitzeroth_family.add_member_by_name("Jack", "Hitzeroth")

hays2_family = Family("Hays2")
hays2_family.add_member_by_name("Hunter", "Hays")
hays2_family.add_member_by_name("Sarah", "Hays")    
hays2_family.add_member_by_name("Knox", "Hays")
hays2_family.add_member_by_name("Emet", "Hays")
hays2_family.add_member_by_name("Jane", "Hays")
hays2_family.add_member_by_name("Hazel", "Hays")


hays3_family = Family("Hays3")
hays3_family.add_member_by_name("Hal", "Hays")
hays3_family.add_member_by_name("Cecilie", "Hays")





families = [tyler_family, hays_family, hitzeroth_family, hays2_family, hays3_family]

# Run Secret Santa assignment
assignment = secret_santa_assign(families)

if assignment is None:
    print("No valid Secret Santa assignment could be found.")
else:
    print("Secret Santa Assignments:")
    for giver, receiver in assignment.items():
        print(f"{giver.get_full_name()} -> {receiver.get_full_name()}")
    # Check validity
    if is_valid_assignment(assignment, families):
        print("\nAssignment is valid!")
    else:
        print("\nAssignment is INVALID!")
