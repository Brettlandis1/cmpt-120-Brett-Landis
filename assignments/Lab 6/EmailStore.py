class EmailStore:

    def __init__(self):
        '''
        Constructor method.
        '''
        self.emails = []

    def exists(self, email):
        '''
        Method that checks if an email exists in store.
        '''
        return email in self.emails

    def add(self, first_name, last_name):
        '''
        Method that adds a new email to the store.
        The email address is of the format {first_name}.{last_name}{count}@marist.edu

        @return the email that was added.
        '''
        
        email = None
        count = 1

        try:
            email = first_name + '.' + last_name + str(count) + "@marist.edu"
        except first_name == None:
            print("Handling invalid first name")
            first_name = 'name?'
        except last_name == None:       
            print("Handling invalid last name")
            last_name = 'name?'



        email = first_name + '.' + last_name + str(count) + "@marist.edu"
        
        ''' Why Is this false?? 
        not sure why this is never being found in the array 
        '''
        print(exists(email))

        while(exists(email)):
            # If it exists, increment count
            count += 1

            # update email with the correct count    
            email = first_name + '.' + last_name + str(count) + "@marist.edu"    
        
        self.emails.append(email)
    
        return email

    def remove(self, email):
        '''
        Method that removes an email from the store.
        '''
        # TODO if email doesn't exist, raise an exception.
        try:
            self.emails.remove(email)
        # nothing needed if doesnt exist
        except ValueError:
            pass    