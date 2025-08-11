class FamilyMember:
    """
    A class to represent a family member with first and last name.
    """
    
    def __init__(self, first_name: str, last_name: str):
        """
        Initialize a FamilyMember with first and last name.
        
        Args:
            first_name (str): The first name of the family member
            last_name (str): The last name of the family member
        """
        self.first_name = first_name
        self.last_name = last_name
    
    def get_full_name(self) -> str:
        """
        Get the full name of the family member.
        
        Returns:
            str: The full name (first name + last name)
        """
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self) -> str:
        """
        String representation of the FamilyMember.
        
        Returns:
            str: The full name of the family member
        """
        return self.get_full_name()
    
    def __repr__(self) -> str:
        """
        Detailed string representation of the FamilyMember.
        
        Returns:
            str: A detailed representation including class name and attributes
        """
        return f"FamilyMember(first_name='{self.first_name}', last_name='{self.last_name}')"


class Family:
    """
    A class to represent a family that can contain multiple FamilyMember instances.
    """
    
    def __init__(self, family_name: str = ""):
        """
        Initialize a Family with an optional family name.
        
        Args:
            family_name (str): The name of the family (optional)
        """
        self.family_name = family_name
        self.members = []
    
    def add_member(self, member: FamilyMember) -> None:
        """
        Add a FamilyMember to the family.
        
        Args:
            member (FamilyMember): The family member to add
        """
        if not isinstance(member, FamilyMember):
            raise TypeError("Only FamilyMember instances can be added to a Family")
        self.members.append(member)
    
    def add_member_by_name(self, first_name: str, last_name: str) -> FamilyMember:
        """
        Create and add a new FamilyMember to the family by providing names.
        
        Args:
            first_name (str): The first name of the new family member
            last_name (str): The last name of the new family member
            
        Returns:
            FamilyMember: The newly created and added family member
        """
        member = FamilyMember(first_name, last_name)
        self.add_member(member)
        return member
    
    def get_member_count(self) -> int:
        """
        Get the number of members in the family.
        
        Returns:
            int: The number of family members
        """
        return len(self.members)
    
    def get_members(self) -> list[FamilyMember]:
        """
        Get all family members.
        
        Returns:
            list[FamilyMember]: List of all family members
        """
        return self.members.copy()
    
    def find_member_by_name(self, first_name: str, last_name: str = None) -> list[FamilyMember]:
        """
        Find family members by name.
        
        Args:
            first_name (str): The first name to search for
            last_name (str): The last name to search for (optional)
            
        Returns:
            list[FamilyMember]: List of matching family members
        """
        matches = []
        for member in self.members:
            if member.first_name.lower() == first_name.lower():
                if last_name is None or member.last_name.lower() == last_name.lower():
                    matches.append(member)
        return matches
    
    def remove_member(self, member: FamilyMember) -> bool:
        """
        Remove a specific family member from the family.
        
        Args:
            member (FamilyMember): The family member to remove
            
        Returns:
            bool: True if member was removed, False if not found
        """
        if member in self.members:
            self.members.remove(member)
            return True
        return False
    
    def __str__(self) -> str:
        """
        String representation of the Family.
        
        Returns:
            str: A string showing the family name and member count
        """
        family_info = f"Family: {self.family_name}" if self.family_name else "Family"
        return f"{family_info} ({self.get_member_count()} members)"
    
    def __repr__(self) -> str:
        """
        Detailed string representation of the Family.
        
        Returns:
            str: A detailed representation including family name and members
        """
        members_str = ", ".join([repr(member) for member in self.members])
        return f"Family(family_name='{self.family_name}', members=[{members_str}])"
