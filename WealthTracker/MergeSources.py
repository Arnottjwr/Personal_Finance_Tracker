"""
Script to merge data from various wealth soures in order to give a current picture of overall wealth 

"""


class WealthMerge:
    """
    Initialises an object to merge wealth data 
    
    """
    def __init__(self, wealth_sources: list):
        """ 
        Input the current sources of wealth 
        """    
        self.wealth_sources = wealth_sources