#importing all packages
from flask import Flask, render_template, request
import os, requests
import random

app = Flask('app')


@app.route("/")
def hello_world():

    #creating a list of terms in the competition
    matchr1m1 = ['ARSENAL', 'ASTON VILLA']
    matchr1m2 = ['BRENTFORD', 'BURNLEY']
    matchr1m3 = ['CHELSEA', 'EVERTON']
    matchr1m4 = ['LEEDS', 'LEICESTER']
    matchr1m5 = ['LIVERPOOL', 'MANCHESTER CITY']
    matchr1m6 = ['MANCHESTER UNITED', 'NEWCASTLE UNITED']
    matchr1m7 = ['NORWICH CITY', 'SOUTHAMPTON']
    matchr1m8 = ['TOTTENHAM', 'WATFORD']

    #Using random choice to print out winners for round 1 matches
    r1m1_winner = random.choice(matchr1m1)
    print(r1m1_winner)
    r1m2_winner = random.choice(matchr1m2)
    print(r1m2_winner)
    r1m3_winner = random.choice(matchr1m3)
    print(r1m3_winner)
    r1m4_winner = random.choice(matchr1m4)
    print(r1m4_winner)
    r1m5_winner = random.choice(matchr1m5)
    print(r1m5_winner)
    r1m6_winner = random.choice(matchr1m6)
    print(r1m6_winner)
    r1m7_winner = random.choice(matchr1m7)
    print(r1m7_winner)
    r1m8_winner = random.choice(matchr1m8)
    print(r1m8_winner)

    #create lists for second round matchups, based on first round winner
    matchr2m1 = [r1m1_winner, r1m2_winner]
    matchr2m2 = [r1m3_winner, r1m4_winner]
    matchr2m3 = [r1m5_winner, r1m6_winner]
    matchr2m4 = [r1m7_winner, r1m8_winner]

    #printing out list for round 2
    print(matchr2m1)
    print(matchr2m2)
    print(matchr2m3)
    print(matchr2m4)

    #Using random choice to print out winners for round 2 matches
    r2m1_winner = random.choice(matchr2m1)
    print(r2m1_winner)
    r2m2_winner = random.choice(matchr2m2)
    print(r2m2_winner)
    r2m3_winner = random.choice(matchr2m3)
    print(r2m3_winner)
    r2m4_winner = random.choice(matchr2m4)
    print(r2m4_winner)

    #create lists for second round matchups, based on second round winner
    matchr3m1 = [r2m1_winner, r2m2_winner]
    matchr3m2 = [r2m3_winner, r2m4_winner]

    #Using random choice to print out winners for round 3 matches
    r3m1_winner = random.choice(matchr3m1)
    print(matchr3m1)
    r3m2_winner = random.choice(matchr3m2)
    print(matchr3m2)

    #Final round
    matchr4m1 = [r3m1_winner, r3m2_winner]
    r4m1_winner = random.choice(matchr4m1)
    print(matchr4m1)

    print(r4m1_winner)

    return render_template("index.html",
                           r1m1_winner=r1m1_winner,
                           r1m2_winner=r1m2_winner,
                           r1m3_winner=r1m3_winner,
                           r1m4_winner=r1m4_winner,
                           r1m5_winner=r1m5_winner,
                           r1m6_winner=r1m6_winner,
                           r1m7_winner=r1m7_winner,
                           r1m8_winner=r1m8_winner,
                           r2m1_winner=r2m1_winner,
                           r2m2_winner=r2m2_winner,
                           r2m3_winner=r2m3_winner,
                           r2m4_winner=r2m4_winner,
                           r3m1_winner=r1m1_winner,
                           r3m2_winner=r3m2_winner,
                           r4m1_winner=r4m1_winner,
                           matchr1m1=matchr1m1,
                           matchr1m2=matchr1m2,
                           matchr1m3=matchr1m3,
                           matchr1m4=matchr1m4,
                           matchr1m5=matchr1m5,
                           matchr1m6=matchr1m6,
                           matchr1m7=matchr1m7,
                           matchr1m8=matchr1m8,
                           matchr2m1=matchr2m1,
                           matchr2m2=matchr2m2,
                           matchr2m3=matchr2m3,
                           matchr2m4=matchr2m4,
                           matchr3m1=matchr3m1,
                           matchr3m2=matchr3m2,
                           matchr4m1=matchr4m1)


app.run(host='0.0.0.0', port=8080)
