class ScoreBoard (object):
    
    def __init__(self):

#State of the list 
        self.List_Is_Full= None
#A list to store our scores
        self.OurList=[]

    def AddScore(self, score, time, name):
# changes the data type of the variables
        score = int(score)
        time = str(time)
        name = str(name)
#alias
        LS = self.OurList
#checks to see what the state of the list 
        if len(LS) < 10:

            self.List_Is_Full = False 

        elif len(LS) == 0:

            self.List_Is_Full = None

        elif len(LS) >= 10:

            self.List_Is_Full = True


        if self.List_Is_Full == True:
#remove score if overflowing 
            self.RemoveScore()

        else:

            if self.List_Is_Full is None:
                self.OurList.append((score, time, name))
                self.OurList.sort(reverse=True)

            else:

                inserted_in_list = False
# Insert the score at the appropriate position 
                for i in range(len(self.OurList)):

                    if score >= self.OurList[i][0]:  

                        self.OurList.insert(i, (score, time, name))

                        inserted_in_list = True

                        break
# Append the score if it's not already inserted 
                if not inserted_in_list and (score, time, name) not in self.OurList:

                    self.OurList.append((score, time, name))

        return self.OurList
                



        

    def RemoveScore(self):
        pass
        
        # could not figure this out 

  
            
            
    


Example=ScoreBoard()
Example.AddScore(200,15,"Austin")
Example.AddScore(150,15,"Austin")
Example.AddScore(225,15,"Austin")
Example.AddScore(145,15,"Austin")
Example.AddScore(256,15,"Austin")
Example.AddScore(2456,15,"Austin")
Example.AddScore(760,15,"Austin")
Example.AddScore(100,15,"Austin")
Example.AddScore(230,15,"Austin")
Example.AddScore(204,15,"Austin")
Example.AddScore(300,15,"Austin")
print(Example.OurList)

