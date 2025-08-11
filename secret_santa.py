import random
from family_member import Family, FamilyMember
from typing import List, Dict, Optional

def secret_santa_assign(families: List[Family]) -> Optional[Dict[FamilyMember, FamilyMember]]:
    """
    Assign each FamilyMember a random recipient from a different family.
    Returns a dictionary mapping givers to recipients, or None if not possible.
    """
    # Gather all members and map them to their families
    all_members = []
    member_to_family = {}
    for family in families:
        for member in family.get_members():
            all_members.append(member)
            member_to_family[member] = family

    if len(all_members) < 2:
        return None  # Not enough participants

    # Try to find a valid assignment
    for _ in range(1000):  # Try up to 1000 times
        recipients = all_members.copy()
        random.shuffle(recipients)
        assignment = {}
        valid = True
        for giver in all_members:
            # Giver cannot get someone from their own family or themselves
            possible = [r for r in recipients if member_to_family[r] != member_to_family[giver] and r != giver]
            if not possible:
                valid = False
                break
            recipient = random.choice(possible)
            assignment[giver] = recipient
            recipients.remove(recipient)
        if valid and len(assignment) == len(all_members):
            return assignment
    return None  # No valid assignment found

def is_valid_assignment(assignment: Dict[FamilyMember, FamilyMember], families: List[Family]) -> bool:
    """
    Check if the assignment is valid: no one gets themselves or someone from their own family, and all assignments are unique.
    """
    if not assignment:
        return False
    givers = set(assignment.keys())
    receivers = set(assignment.values())
    if len(givers) != len(receivers):
        return False
    member_to_family = {}
    for family in families:
        for member in family.get_members():
            member_to_family[member] = family
    for giver, receiver in assignment.items():
        if giver == receiver:
            return False
        if member_to_family[giver] == member_to_family[receiver]:
            return False
    return True
