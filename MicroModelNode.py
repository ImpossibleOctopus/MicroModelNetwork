class MicroModelNode:
    def __init__(self,size_of_input_vector):
        """
        Initialize with size of input vectors
        """
        raise NotImplemented

    def getValue(self,v):
        """
        Given input vector v, get output probability
        """
        raise NotImplemented

    def getActivation(self,v):
        """
        Given input vector v, get output activation
        """
        raise NotImplemented

    def evaluate(self,v,expected):
        """
        Given a vector as input and an expected value
        get the score, adjusted by activation and
        add to rolling average of scores
        """
        raise NotImplemented
    
    def trainValue(self,v,expected):
        """
        Given a vector as input and an expected value
        adjust the model to align closer with the correct value
        """
        raise NotImplemented

    def trainActivation(self,v,expected):
        """
        Given a vector as input and an expected value
        adjust the model to align closer to the correct certainty
        """
        raise NotImplemented

    def clearAverageScore(self):
        """
        Clear average score obtained through evaluations
        """
        raise NotImplemented

    def getAverageScore(self):
        """
        Return average score obtained through evaluations
        """
        raise NotImplemented