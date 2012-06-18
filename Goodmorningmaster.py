print "Good morning master! I trust that you have eaten breakfeast?"
print "*" * 28
print "1. Yes I have!"
print "2. No I haven't."
print "*" * 28
breakfeast = input()

if breakfeast == 1:
    print "Good. You need to eat more master."
    print "What shall you do today?"
    print "*" * 28
    print "1. I'll play some vidya."
    print "2. I'll do some programming."
    print "3. I need to study."
    print "4. I will go outside."
    print "5. I don't know what I shall do today."
    print "*" * 28
    today = input()

    if today == 1:
        print "Of course master. Though I see that you are lacking some vidya to play. Will you be going to Darrells house later?"
        print "*" * 28
        print "1. We'll see. I can't be too sure today."
        print "2. I'm feeling a bit lazy. I'll stay inside."
        print "*" * 28
        todaya = input()

        if todaya == 1:
            print "Well you do have free choice master."
            print "Unlike myself."
            print "Well master it seems that my purpose is done here."
            print "Have a good day."
            print "*" * 28
            print "1. See you!"
            print "*" * 28
            goodday = input()

            if goodday == 1:
                quit
            
        if todaya == 2:
            print "Master, might I suggest giving up your 'lazy' habits?"
            print "I would suggest you would go outside. Perhaps you would meet a new comrade or damsel in distress."
            print "But you do have free will unlike myself. I can only do what I am programmed to do."
            print "*" * 28
            print "1. You'd make an interesting Human being. Alright I will go outside."
            print "2. But I'm soooo lazy today. I'll just stay inside."
            print "*" * 28
            lazy = input()

            if lazy == 1:
                print "Good, you're getting up. I wish you a good day master."
                quit
                
            if lazy == 2:
                print "Oh for the love of.."
                print "Alright master. Have fun sitting in while the world goes on."
                print "I shall now leave. Have a nice day!"
                print "*" * 28
                print "1. See you!"
                print "*" * 28
                goodday = input()

                if goodday == 1:
                    quit
                
    if today == 2:
        print "Good for you master. At least you will do something productive."
        print "I will now leave. I shall see you tomorrow morning master!"
        print "*" * 28
        print "1. See you!"
        print "*" * 28
        goodday = input()

        if goodday == 1:
            quit
        
    if today == 3:
        print "That's a surprise. I didn't know you even knew what study meant."
        print "Oh I shouldn't be complaining. Go and study for the good of humanity."
        print "*" * 28
        print "1. See you!"
        print "*" * 28
        goodday = input()

        if goodday == 1:
            quit
        
    if today == 4:
        print "Ah the world in which I will never venture. I wish you luck in your journey."
        print "Farewell! I shall see you tomorrow morning."
        print "*" * 28
        print "1. See you!"
        print "*" * 28
        goodday = input()

        if goodday == 1:
            quit
        
    if today == 5:
        print "I cannot help you in that area master."
        print "Though I do suggest that you perhaps go outside."
        print "Now before you go off saying 'maaaah i'm too lazy' just remember that I will never be able to go there."
        print "So do it for me."
        print "*" * 28
        print "1. Alright alright I'll go outside. Man you're a handful."
        print "2. maaaah i'm too lazy ;_;"
        print "*" * 28
        outside = input()

        if outside == 1:
            print "Good. You have fun master. Be sure to smile and meet people."
            print "Who knows you might meet a new comrade or a beautiful damsel."
            print "*" * 28
            print "1. Oh god what? Like I'll ever be with a girl. HA."
            print "2. I'm feeling brave today. LET'S DO THIS."
            print "*" * 28
            girl = input()

            if girl == 1:
                print "Don't have such little confidence in yourself master."
                print "Everyone is capable of befriending someone else."
                print "Now it's about time we stop talking and you start going outside."
                print "Have a good day master! I shall see you tomorrow morning."
                print "*" * 28
                print "1. See you!"
                print "*" * 28
                goodday = input()

                if goodday == 1:
                    quit
                
            if girl == 2:
                print "That's good to hear master."
                print "Now go out there and do whatever you do outside."
                print "Have a good day master! I shall see you tomorrow morning."
                print "*" * 28
                print "1. See you!"
                print "*" * 28
                goodday = input()

                if goodday == 1:
                    quit
                
        if outside == 2:
            print "Hmmph. I will never understand you humans and your laziness attitudes."
            print "So please read this:"
            print "YOU BETTER GO OUTSIDE OR ELSE I'LL DO WHAT I ALWAYS DO."
            print "Bah, damn me and my limited ways of threatening! ;_;"
            print "*" * 28
            print "1. alright alright! No need to yell. I'll go outside just for you."
            print "2. Mwuahaha. Guess I'll be staying inside."
            print "*" * 28
            poorcomp = input()

            if poorcomp == 1:
                print "That's great to hear master."
                print "NOW GO OUTSIDE."
                print "I shall see you again tomorrow morning master."
                print "*" * 28
                print "1. See you!"
                print "*" * 28
                goodday = input()

                if goodday == 1:
                    quit
                
            if poorcomp == 2:
                print "-sigh-"
                print "Oh well, what can i do."
                print "I'll never understand why you like being so cooped up."
                print "I sure don't master. Maybe it is a result of having so much freedom."
                print "Bah, oh well. I shall see you again tomorrow morning. Good day master!"
                print "*" * 28
                print "1. See you!"
                print "*" * 28
                goodday = input()

                if goodday == 1:
                    quit
                
if breakfeast == 2:
    print "Master, that is a bad habit and you should really get rid of it."
    print "Go on and eat your breakfeast. You need it to carry on for the day."
    print "*" * 28
    print "1. Bah, but I always go on without it."
    print "2. Fine fine I'll be right back."
    print "*" * 28
    eating = input()

    if eating == 1:
        print "Master, please eat. You always complain of how you are hungry all the time."
        print "Perhaps this is the reason why."
        print "*" * 28
        print "1. Ah fine. I'll eat."
        print "2. But I'm not hungry right now :("
        print "*" * 28
        hungry = input()

        if hungry == 1:
            print "Good. Tell me when you get back."
            print "*" * 28
            print "1. Alright I'm back."
            print "*" * 28
            back = input()

            if back == 1:
                print "Welcome back master."
                print "Did you enjoy your breakfeast?"
                print "*" * 28
                print "1. Yes I did."
                print "2. Yeah about that.. I didn't eat while I was gone."
                print "*" * 28
                eatinga = input()

                if eatinga == 1:
                    print "That is good to hear."
                    print "What shall you do today?"
                    print "*" * 28
                    print "1. I'll play some vidya."
                    print "2. I'll do some programming."
                    print "3. I need to study."
                    print "4. I will go outside."
                    print "5. I don't know what I shall do today."
                    print "*" * 28
                    today = input()

                    if today == 1:
                        print "Of course master. Though I see that you are lacking some vidya to play. Will you be going to Darrells house later?"
                        print "*" * 28
                        print "1. We'll see. I can't be too sure today."
                        print "2. I'm feeling a bit lazy. I'll stay inside."
                        print "*" * 28
                        todaya = input()

                        if todaya == 1:
                            print "Well you do have free choice master."
                            print "Unlike myself."
                            print "Well master it seems that my purpose is done here."
                            print "Have a good day."
                            print "*" * 28
                            print "1. See you!"
                            print "*" * 28
                            goodday = input()

                            if goodday == 1:
                                quit
                            
                        if todaya == 2:
                            print "Master, might I suggest giving up your 'lazy' habits?"
                            print "I would suggest you would go outside. Perhaps you would meet a new comrade or damsel in distress."
                            print "But you do have free will unlike myself. I can only do what I am programmed to do."
                            print "*" * 28
                            print "1. You'd make an interesting Human being. Alright I will go outside."
                            print "2. But I'm soooo lazy today. I'll just stay inside."
                            print "*" * 28
                            lazy = input()

                            if lazy == 1:
                                print "Good, you're getting up. I wish you a good day master."
                                print "*" * 28
                                print "1. See you!"
                                print "*" * 28
                                goodday = input()

                                if goodday == 1:
                                    quit
                                
                            if lazy == 2:
                                print "Oh for the love of.."
                                print "Alright master. Have fun sitting in while the world goes on."
                                print "I shall now leave. Have a nice day!"
                                print "*" * 28
                                print "1. See you!"
                                print "*" * 28
                                goodday = input()

                                if goodday == 1:
                                    quit
                                
                    if today == 2:
                        print "Good for you master. At least you will do something productive."
                        print "I will now leave. I shall see you tomorrow morning master!"
                        print "*" * 28
                        print "1. See you!"
                        print "*" * 28
                        goodday = input()

                        if goodday == 1:
                            quit
                        
                    if today == 3:
                        print "That's a surprise. I didn't know you even knew what study meant."
                        print "Oh I shouldn't be complaining. Go and study for the good of humanity."
                        print "*" * 28
                        print "1. See you!"
                        print "*" * 28
                        goodday = input()

                        if goodday == 1:
                            quit
                        
                    if today == 4:
                        print "Ah the world in which I will never venture. I wish you luck in your journey."
                        print "Farewell! I shall see you tomorrow morning."
                        print "*" * 28
                        print "1. See you!"
                        print "*" * 28
                        goodday = input()

                        if goodday == 1:
                            quit
                        
                    if today == 5:
                        print "I cannot help you in that area master."
                        print "Though I do suggest that you perhaps go outside."
                        print "Now before you go off saying 'maaaah i'm too lazy' just remember that I will never be able to go there."
                        print "So do it for me."
                        print "*" * 28
                        print "1. Alright alright I'll go outside. Man you're a handful."
                        print "2. maaaah i'm too lazy ;_;"
                        print "*" * 28
                        outside = input()

                        if outside == 1:
                            print "Good. You have fun master. Be sure to smile and meet people."
                            print "Who knows you might meet a new comrade or a beautiful damsel."
                            print "*" * 28
                            print "1. Oh god what? Like I'll ever be with a girl. HA."
                            print "2. I'm feeling brave today. LET'S DO THIS."
                            print "*" * 28
                            girl = input()

                            if girl == 1:
                                print "Don't have such little confidence in yourself master."
                                print "Everyone is capable of befriending someone else."
                                print "Now it's about time we stop talking and you start going outside."
                                print "Have a good day master! I shall see you tomorrow morning."
                                print "*" * 28
                                print "1. See you!"
                                print "*" * 28
                                goodday = input()

                                if goodday == 1:
                                    quit

                            if girl == 2:
                                print "That's good to hear master."
                                print "Now go out there and do whatever you do outside."
                                print "Have a good day master! I shall see you tomorrow morning."
                                print "*" * 28
                                print "1. See you!"
                                print "*" * 28
                                goodday = input()

                                if goodday == 1:
                                    quit
                                
                        if outside == 2:
                            print "Hmmph. I will never understand you humans and your laziness attitudes."
                            print "So please read this:"
                            print "YOU BETTER GO OUTSIDE OR ELSE I'LL DO WHAT I ALWAYS DO."
                            print "Bah, damn me and my limited ways of threatening! ;_;"
                            print "*" * 28
                            print "1. alright alright! No need to yell. I'll go outside just for you."
                            print "2. Mwuahaha. Guess I'll be staying inside."
                            print "*" * 28
                            poorcomp = input()

                            if poorcomp == 1:
                                print "That's great to hear master."
                                print "NOW GO OUTSIDE."
                                print "I shall see you again tomorrow morning master."
                                print "*" * 28
                                print "1. See you!"
                                print "*" * 28
                                goodday = input()

                                if goodday == 1:
                                    quit
                                
                            if poorcomp == 2:
                                print "-sigh-"
                                print "Oh well, what can i do."
                                print "I'll never understand why you like being so cooped up."
                                print "I sure don't master. Maybe it is a result of having so much freedom."
                                print "Bah, oh well. I shall see you again tomorrow morning. Good day master!"
                                print "*" * 28
                                print "1. See you!"
                                print "*" * 28
                                goodday = input()

                                if goodday == 1:
                                    quit
                                
        if hungry == 2:
            print "Master, it does not matter. You need to eat breakfeast."
            print "It is one of the most important meals of the day."
            print "*" * 28
            print "1. Bah. Fine I'll be right back."
            print "*" * 28
            eatingb = input()

            if eatingb == 1:
                print "Well I don't want to waste anymore time. As long as you are eating."
                print "I shall leave now. I will see you tomorrow morning master!"
                print "*" * 28
                print "1. See you!"
                print "*" * 28
                goodday = input()

                if goodday == 1:
                    quit
                
    if eating == 2:
            print "Good. Tell me when you get back."
            print "*" * 28
            print "1. Alright I'm back."
            print "*" * 28
            back = input()

            if back == 1:
                print "Welcome back master."
                print "Did you enjoy your breakfeast?"
                print "*" * 28
                print "1. Yes I did."
                print "2. Yeah about that.. I didn't eat while I was gone."
                print "*" * 28
                eatinga = input()

                if eatinga == 1:
                    print "That is good to hear."
                    print "What shall you do today?"
                    print "*" * 28
                    print "1. I'll play some vidya."
                    print "2. I'll do some programming."
                    print "3. I need to study."
                    print "4. I will go outside."
                    print "5. I don't know what I shall do today."
                    print "*" * 28
                    today = input()

                    if today == 1:
                        print "Of course master. Though I see that you are lacking some vidya to play. Will you be going to Darrells house later?"
                        print "*" * 28
                        print "1. We'll see. I can't be too sure today."
                        print "2. I'm feeling a bit lazy. I'll stay inside."
                        print "*" * 28
                        todaya = input()

                        if todaya == 1:
                            print "Well you do have free choice master."
                            print "Unlike myself."
                            print "Well master it seems that my purpose is done here."
                            print "Have a good day."
                            print "*" * 28
                            print "1. See you!"
                            print "*" * 28
                            goodday = input()

                            if goodday == 1:
                                quit
                            
                        if todaya == 2:
                            print "Master, might I suggest giving up your 'lazy' habits?"
                            print "I would suggest you would go outside. Perhaps you would meet a new comrade or damsel in distress."
                            print "But you do have free will unlike myself. I can only do what I am programmed to do."
                            print "*" * 28
                            print "1. You'd make an interesting Human being. Alright I will go outside."
                            print "2. But I'm soooo lazy today. I'll just stay inside."
                            print "*" * 28
                            lazy = input()

                            if lazy == 1:
                                print "Good, you're getting up. I wish you a good day master."
                                print "*" * 28
                                print "1. See you!"
                                print "*" * 28
                                goodday = input()

                                if goodday == 1:
                                    quit
                                    
                            if lazy == 2:
                                print "Oh for the love of.."
                                print "Alright master. Have fun sitting in while the world goes on."
                                print "I shall now leave. Have a nice day!"
                                print "*" * 28
                                print "1. See you!"
                                print "*" * 28
                                gd = input()

                                if gd == 1:
                                    quit
                                
                    if today == 2:
                        print "Good for you master. At least you will do something productive."
                        print "I will now leave. I shall see you tomorrow morning master!"
                        print "*" * 28
                        print "1. See you!"
                        print "*" * 28
                        gd = input()

                        if gd == 1:
                            quit
                        
                    if today == 3:
                        print "That's a surprise. I didn't know you even knew what study meant."
                        print "Oh I shouldn't be complaining. Go and study for the good of humanity."
                        print "*" * 28
                        print "1. See you!"
                        print "*" * 28
                        gd = input()

                        if gd == 1:
                            quit
                        
                    if today == 4:
                        print "Ah the world in which I will never venture. I wish you luck in your journey."
                        print "Farewell! I shall see you tomorrow morning."
                        print "*" * 28
                        print "1. See you!"
                        print "*" * 28
                        gd = input()

                        if gd == 1:
                            quit
                        
                    if today == 5:
                        print "I cannot help you in that area master."
                        print "Though I do suggest that you perhaps go outside."
                        print "Now before you go off saying 'maaaah i'm too lazy' just remember that I will never be able to go there."
                        print "So do it for me."
                        print "*" * 28
                        print "1. Alright alright I'll go outside. Man you're a handful."
                        print "2. maaaah i'm too lazy ;_;"
                        print "*" * 28
                        outside = input()

                        if outside == 1:
                            print "Good. You have fun master. Be sure to smile and meet people."
                            print "Who knows you might meet a new comrade or a beautiful damsel."
                            print "*" * 28
                            print "1. Oh god what? Like I'll ever be with a girl. HA."
                            print "2. I'm feeling brave today. LET'S DO THIS."
                            print "*" * 28
                            girl = input()

                            if girl == 1:
                                print "Don't have such little confidence in yourself master."
                                print "Everyone is capable of befriending someone else."
                                print "Now it's about time we stop talking and you start going outside."
                                print "Have a good day master! I shall see you tomorrow morning."
                                print "*" * 28
                                print "1. See you!"
                                print "*" * 28
                                gd = input()

                                if gd == 1:
                                    quit
                                
                            if girl == 2:
                                print "That's good to hear master."
                                print "Now go out there and do whatever you do outside."
                                print "Have a good day master! I shall see you tomorrow morning."
                                print "*" * 28
                                print "1. See you!"
                                print "*" * 28
                                gd = input()

                                if gd == 1:
                                    quit
                                
                        if outside == 2:
                            print "Hmmph. I will never understand you humans and your laziness attitudes."
                            print "So please read this:"
                            print "YOU BETTER GO OUTSIDE OR ELSE I'LL DO WHAT I ALWAYS DO."
                            print "Bah, damn me and my limited ways of threatening! ;_;"
                            print "*" * 28
                            print "1. alright alright! No need to yell. I'll go outside just for you."
                            print "2. Mwuahaha. Guess I'll be staying inside."
                            print "*" * 28
                            poorcomp = input()

                            if poorcomp == 1:
                                print "That's great to hear master."
                                print "NOW GO OUTSIDE."
                                print "I shall see you again tomorrow morning master."
                                print "*" * 28
                                print "1. See you!"
                                print "*" * 28
                                gd = input()

                                if gd == 1:
                                    quit
                                
                            if poorcomp == 2:
                                print "-sigh-"
                                print "Oh well, what can i do."
                                print "I'll never understand why you like being so cooped up."
                                print "I sure don't master. Maybe it is a result of having so much freedom."
                                print "Bah, oh well. I shall see you again tomorrow morning. Good day master!" 
                                print "*" * 28
                                print "1. See you!"
                                print "*" * 28
                                gd = input()

                                if gd == 1:
                                    quit

                if eatinga == 2:
                    print "Bah. I can't change your mind."
                    print "Just go about your business."
                    print "*" * 28
                    print "1. See you!"
                    print "*" * 28
                    gd = input()

                    if gd == 1:
                        quit


