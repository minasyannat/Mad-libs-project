import time
import random
greeting = input(" Welcome to 'Random publishing & co.', are you ready to try your talent and create your own story? (yes/no) ").lower()

if greeting != "no":
    template = input(" We always like proactive writers! Then choose a template for your story (Hospital_craziness/Camping_prospects/Enchanted_forest) ").lower()
    print(f"That is amazing! People always love a good story about the topic '{template}'. Let's get to creation!")
    adj = input("Now type in 5 adjectives, separated by a comma(',') ").split(",")
    noun = input("Perfect! Now please 7 singular nouns, again with the delimiter being the comma ").split(",")
    verb = input("Please enter 2 verbs, without '-ing'" ).split(",")
    verb_ing = input("Now 2 more but in infinitive form, with '-ing' ").split(",")
    adverb = input("Amazing! Now input 2 adverbs ending with '-ly' ").split(",")
    color = input("Tell us 3 colors ").split(",")
    feelings = ["scared", "excited", "enamoured", "delighted", "sad"]
    print(f"those were the generall requirements for all stories, now let's get to your choice. The template {template} ")
    if template == "hospital_craziness":
        tme = input("Please input 2 types of measure of time(second, minute, year, century, month, etc) ").split(",")
        wrd = input(" input a silly word! just one ")
        transport = ["bus", "car", "motorcycle", "unicycle", "horse", "carriage"]
        bodyparts = ["nose", "hair", "colar bones", "body hair", "skin", "eyelashes"]
        story = f"""It was about {random.randint(1, 1000)} {random.choice(tme)}s ago when I arrived at the hospital in a {random.choice(transport)}. The hospital is a/an {random.choice(adj)} place,there are a lot of {random.choice(adj)} {random.choice(noun)}s here. 
        There are nurses here who have {random.choice(color)} {random.choice(bodyparts)}. 
          If someone wants to come into my room I told them that they have to {random.choice(verb)} first. I’ve decorated my room with {random.randint(1, 100)} {random.choice(noun)}s. 
          Today I talked to a doctor and they were wearing a {random.choice(noun)} on their {random.choice(bodyparts)}. I heard that all doctors {random.choice(verb)} {random.choice(noun)}s every day for breakfast. 
          The most {random.choice(adj)} thing about being in the hospital is the {wrd} {random.choice(noun)} !"""
        print("Generating the story...")
        time.sleep(0.9)
        print("Ready!")
        print(story)
    elif template == "camping_prospects":
        name = input("Please input two names ").split(",")
        animal = input("Now please any two animals ").split(",")
        wrd = input(" input a silly word! just one ")
        tme = input("Please input 2 types of measure of time(second, minute, year, century, month, etc) ").split(",")
        story = f"""This weekend I am going camping with {random.choice(name)}. 
        I packed my lantern, sleeping bag, and {random.choice(noun)}. I am so {random.choice(feelings)} to {random.choice(verb)} in a tent. I am {random.choice(feelings)} we might see a(n) {random.choice(animal)}, 
        I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {random.choice(verb)}.
          I have heard that the {random.choice(color)} lake is great for {random.choice(verb_ing)}. Then we will {random.choice(adverb)} hike through the forest for {random.randint(1, 120)} {random.choice(tme)}s. 
          If I see a {random.choice(color)} {random.choice(animal)} while hiking, I am going to bring it home as a pet! At night we will tell {random.randint(1, 200)} {wrd} stories and roast {random.choice(noun)}s  around the campfire!!
        """ 
        print("Generating the story...")
        time.sleep(0.9)
        print("Ready!")
        print(story)
    elif template == "enchanted_forest":
        name = input("Please input two names ").split(",")
        animal = input("Now please any two animals ").split(",")
        wrd = input(" input a silly word! just one ")
        tme = input("Please input 2 types of measure of time(second, minute, year, century, month, etc) ").split(",")
        room = ["bathroom", "toilet", "bedroom", "dining room", "kitchen", "living room"]
        creature = input("input 2 magical creatures please ").split(",")
        place = ["the sea", "the mountains", "the forest by my home", "the school yard"]
        story = f"""Dear {random.choice(name)} , I am writing to you from a/an {random.choice(adj)} castle in an enchanted forest. 
        I found myself here one day after going for a ride on a {random.choice(color)} {random.choice(animal)} in {random.choice(place)}. There are {random.choice(adj)} {random.choice(creature)}s and {random.choice(adj)} {random.choice(creature)}s here!
          In the {random.choice(room)} there is a pool full of {random.choice(noun)}. I fall asleep each night on a {random.choice(noun)} of {random.choice(noun)}s and dream of {random.choice(adj)} {random.choice(noun)}s.
            It feels as though I have lived here for {random.randint(1, 2000)} {random.choice(tme)}s. 
            I hope one day you can visit, although the only way to get here now is {random.choice(verb_ing)} on a {random.choice(adj)} {random.choice(noun)}!!
        """
        print("Generating the story...")
        time.sleep(0.9)
        print("Ready!")
        print(story)
    else:
        print("sorry, we do not have such a template")
else:
    print("Okay! Come back next time")

    









