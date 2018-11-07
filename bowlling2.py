#!/usr/bin/env python

"""Bowlling2.py is a python code which calculates the score of a player in each frame of a match(10frames is considered as a single match)"""
__author__      = "Vineel Koneru"
__date__        = "08/11/2018"

import random # Random is used to generate a random number in a range of 1to10
 
dis = {} # dis is a empty dictionary which hold the score of each frame

# This function runs for 10 times and generate score based on strike or spare
def blowing():
    """This is the main funtion of the code which initally runs."""
    score = 0
    total_balls = 10
    print('Please press "Enter" for each throw:')

    for frame in range(1,11):
        
        for throw in range(1,3):
            chance = '1st' if throw == 1 else '2nd'
            strike = input(chance+' throw in Frame'+str(frame)+': ')
            sco = random.randint(0,total_balls)

            if sco == 10:             
                score += sco
                print('Score in '+chance+' throw: ', sco)
                print('It is a "Strike!"')
                score = strike1(frame)
                break
            
            else:
                score += sco
                total_balls = total_balls - sco
                print('Score in '+chance+ ' throw: ', sco)
                
        if score == 10:
            print('it is a "Spare!"')
            score += sco
            score = spare(score,frame)
            print('You have scored: '+str(score)+' in frame '+str(frame))
            print('='*30+'\n')
            total_balls = 10
            
            dis['Frame'+str(frame)] = score
            score = 0

        else:
            total_balls = 10
            print('You have scored: '+str(score)+' in frame '+str(frame))
            print('='*30+'\n')
            dis['Frame'+str(frame)] = score
            score = 0
        
def strike1(frame):
    """If player got an "strike" this funtion will be called"""
    intial_score = 10
    frame_score = 0
    total_balls = 10
    
    
    for throw in range(1,3):
        chance = '1st' if throw == 1 else '2nd'
        strike = input(chance+' throw in Frame'+str(frame)+': ')
        sco = random.randint(0,total_balls)
        if sco == 10:
            print('Score in '+chance+' throw: ', sco)
            intial_score += sco
            break
        else:
            frame_score += sco
            total_balls = total_balls - sco
            print('Score in '+chance+' throw: ', sco)
    return intial_score+frame_score+frame_score

def spare(score,frame):
    
    intial_score = 10
    frame_score = 0
    first_strike_score = 0
    total_balls =10
    
    strike = input('Throw in Frame'+str(frame)+': ')
    sco = random.randint(0, total_balls)
    
    first_strike_score += sco
    
    frame_score += sco
    if sco == 10:
        print('Your spin score is ', sco)
        return intial_score+first_strike_score
    else:
        print('First spin score is ', sco)
        total_balls = total_balls - sco
        strike = input('Throw in Frame'+str(frame)+': ')
        sco1 = random.randint(0, total_balls)
        print('Second spin score is ', sco1)
        frame_score += sco1
        return intial_score+first_strike_score+frame_score

blowing()

print('Your 10 frames scores are: ')
for i in dis:
    print('+--------------+')
    print('|{:<9}|{:<4}|'.format(i,dis[i]))
print('+--------------+')
