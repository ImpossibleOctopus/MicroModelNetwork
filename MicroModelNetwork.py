class MicroModelNetwork:

    def __init__(self,vectorsize):
        raise NotImplemented
    
    def get(self,v):
        """
        Given input vector v, get the model's prediction 
        """
        raise NotImplemented

    def evaluate(self, v, expected):
        """
        Evaluate all nodes in model with input vector v and expected prediction
        """
        raise NotImplemented
     
    def addNodes(self,n,MicroModelNodeClass):
        """
        Add n nodes of type MicroModelNodeClass accepting vectors of length n
        """
        raise NotImplemented

    def pruneLowestN(self,n):
        """
        Remove the n lowerst performing nodes
        """
        raise NotImplemented

    def getSize(self):
        """
        Get the number of nodes
        """
        raise NotImplemented