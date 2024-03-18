class ScoreBoard (object):
    
    def __init__(self,score,time):
#Used to hold player score 
        self.score= int(score)
#Used to hold total game time
        self.time=  int(time)
#State of the list 
        self.List_Is_Full= None
#A list to store our scores
        self.OurList=[1,1,1,1,1,1,1,1,1]
       
    def main(self):
        
        self.List_Check()
#These will all be method calls to handle differant states (like an enum in C#)


        if self.List_Is_Full == True:
        #Run remove from list script 
            self.RemoveScore()
        elif self.List_Is_Full == False:
        #Add score to list 
            self.AddScore(self.score,self.time)
        elif self.List_Is_Full == None: 
        #Create the list and add this entry 
            self.AddScore(self.score,self.time)

    def AddScore(self,score,time):
        #Will add the score to the list calling on Place Score to determine the index to place it at.
        print(str(self.time))
        print(str(self.score))
        self.PlaceScore()

    def RemoveScore(self):
        print("list is full removing score")



    def PlaceScore(self):
        #debug
        return(print("Place Score Called"))


    def List_Check(self):
        OurList= self.OurList
        List_Is_Full=self.List_Is_Full

        print(List_Is_Full)
        if len(OurList) == 0 :
            self.List_Is_Full = None
            #debug
            print("List is not created ")

        elif len(OurList)< 10 and len(OurList) !=0 :
            self.List_Is_Full= False
            #debug
            print("List is not full ")

        elif len(OurList) >9:
            self.List_Is_Full= True
            #debug
            print("List is full")

        else:
            print("unknown exception occured")
Example=ScoreBoard(100,15)
Example.main()
  
#to this point the program can do the following
#1 it can determine how many items are stored in a list
#2.it can call the correct function to do the correct operation
#3.it can set the instance variable to the correct state


#I need to do the following:
#1.recive input from the game class
#2. Create the logic to place the socre in the correct position
#3.Evaluate the and place the score in the correct place 
