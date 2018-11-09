#!/usr/bin/env python

"""Bowlling2.py is a python code which calculates the score of a player in each frame of a match(10frames is considered as a single match)"""
__author__      = "Vineel Koneru"
__date__        = "08/11/2018"

import random
dis = {}
def blowing():
    score = 0
    total_balls = 10
    print('Press enter to throw the ball')
    for frame in range(1,11):
        
        for throw in range(1,3):
            turn = '1st' if throw == 1 else '2nd'
            strike = input(turn+ ' turn in frame'+str(frame)+': ')
            sco = random.randint(1,total_balls)
            if sco == 10:
                
                score += sco
                print('It is a "Strike!"')
                print('Score in '+turn+ ' throw '+ str(sco))
                score = strike1(sco)
                break
            else:
                score += sco
                total_balls = total_balls - sco
                print('Score is '+turn+ ' throw '+str(sco))
                
              
        
        if score == 10:
            print('it is a "Spare!"')
            
            score = spare(turn, score)
            print('Score in frame '+str(frame)+' is '+str(score)+'\n')
            total_balls = 10
            
            dis['Frame'+str(frame)] = score
            score = 0

        else:
            total_balls = 10
            print('Score in frame '+str(frame)+' is '+str(score)+'\n')
            dis['Frame'+str(frame)] = score
            score = 0
            
        

def strike1(sco):
    intial_score = sco
    frame_score = 0
    total_balls = 10
    

    
    for through in range(1,3):
        strike = input('Press enter to through a ball ')
        sco = random.randint(1,total_balls)
        turn = '1st' if through == 1 else '2nd'
        if sco == 10:
            print('Score in '+turn+ ' throw '+ str(sco))
            print('It is a "Strike!"')
            intial_score += sco
            intial_score = strike1(intial_score)
            break
        else:
            
            frame_score += sco
            total_balls = total_balls - sco
            print('Score in '+turn+ ' throw '+ str(sco))


    if frame_score == 10:
        print('it is a "Spare!"')
        intial_score = intial_score+frame_score+frame_score
        intial_score = spare(turn, intial_score)
        return intial_score
    else:
        return intial_score+frame_score+frame_score

def spare(turn, score):
    intial_score = score
    frame_score = 0
    first_strike_score = 0
    total_balls =10
    
    strike = input('Press enter to through a ball ')
    sco = random.randint(1,total_balls)
    
    first_strike_score += sco
    
    frame_score += sco
    if sco == 10:
        print('Score in '+turn+ ' throw '+ str(sco))
        print('it is a "Strike!"')
        intial_score += sco
        intial_score = strike1(intial_score)
        return intial_score+first_strike_score
    else:
        total_balls = total_balls - sco
        strike = input('Press enter to through a ball ')
        sco1 = random.randint(1,total_balls)
        print('Score in '+turn+ ' throw '+ str(sco))
        frame_score += sco1
        if frame_score == 10:
             print('it is a "Spare!"')
             intial_score = intial_score+first_strike_score+frame_score
             intial_score = spare(turn, intial_score)
             return intial_score
        else:
            return intial_score+first_strike_score+frame_score
         

blowing()

print('10 frames score is: ')
for i in dis:
   fr = i.center(9)
   sc = str(dis[i]).center(4)
   print('+--------------+')
   print('|%s|%s|'%(fr,sc))
print('+--------------+')    

