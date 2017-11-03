
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
        
def insert(atMe, newFrob):
    if atMe.name <= newFrob.name:
        temp1 = atMe
        inserted = False
        while temp1.name <= newFrob.name:
            if temp1.getAfter == None:
                temp1.setAfter(newFrob)
                newFrob.setBefore(temp1)
                inserted = True
                break
            else:
                temp1 = temp1.getAfter()
        if not inserted:
            temp2 = temp1.getBefore()
            temp2.setAfter(newFrob)
            newFrob.setAfter(temp1)
            temp1.setBefore(newFrob)
            newFrob.setBefore(temp2)
    else:
        temp1 = atMe
        inserted = False
        while temp1.name > newFrob.name:
            if temp1.getBefore == None:
                temp1.setBefore(newFrob)
                newFrob.setAfter(temp1)
                inserted = True
                break
            else:
                temp1 = temp1.getBefore()
        if not inserted:
            temp2 = temp1.getAfter()
            temp2.setBefore(newFrob)
            newFrob.setBefore(temp1)
            temp1.setAfter(newFrob)
            newFrob.setAfter(temp2)

insert(Frob('apple'), Frob('orange'))

