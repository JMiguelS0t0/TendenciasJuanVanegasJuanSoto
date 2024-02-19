def searchUser(hospital, userName):
    for person in hospital.persons:
        if person.userName == userName:
            return person   
    return None