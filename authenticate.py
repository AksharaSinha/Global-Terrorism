# -*- coding: utf-8 -*-
class authentication:

    def __init__(self):
        # Go to http://apps.twitter.com and create an app
        # The consumer key and secret will be generated for you after
        self.consumer_key ="jXhfH3Lmpzalq1coXWWqTjCJz"
        self.consumer_secret="aTYf53xAlY0ozffp2thycv23Q4NBnk9kPOz6kBSwBFAWNcK2z1"
    
    # Create an access token under the "Your access token" section
        self.access_token="1045600121772101632-56dyIKvupee1WeFrSEiWMN0wYGcS4b"
        self.access_token_secret="fOAL3TrRNt9YnnHu3QvuJtD6Ebp2cscw8jsK924nL5Y5q"
    
    def getconsumer_key(self):
    	return self.consumer_key
    
    def getconsumer_secret(self):
    	return self.consumer_secret
    def getaccess_token(self):
    	return self.access_token
    def getaccess_token_secret(self):
    	return self.access_token_secret