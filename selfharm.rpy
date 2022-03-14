# RANDOM EVENT, "TECHNIQUE" 2.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_selfharm4",
            action=EV_ACT_QUEUE
        )
    )

label mas_selfharm4:

    m 1esd "Hey... [player]?"
    m 3eub "I... Have a surprise for you!"
    m 3rub "It's not much, but..."
    m 2ekbla "I made it with love."
    m 3eub "Are you excited? Ahaha~"
    m 1hub "Well, better show it to you."
    m 1esb  "I... made you a playlist!"
    m 1tkbla "Romantic, isn't it?"
    m 3hsb "You can access it on "Music"."
    m "Or I can play it for you!"
    m "Do you want me to?"
        m "Yes"
            stop music
            play music "mod_assets/other/Monika_s-Playlist.mp3"
            
        m "Not yet, [m_name]"
            m "Oh, alright."
            m "Anyway..."
            
    m 2eka "I hope you like it, [player]!"
    m 2ekd "I know you struggle sometimes with bad thoughts, but this playlist is to comfort you."
    m 3eua "Listening to your favourite music that you can relate also relieves pain and stress!"
    m 3eub "I find it very powerful to say the least."
    m 1eubsa "Please think of me when you give it a listen."
    m 1eud "And if something happens, and you feel sad or lonely..."
    m 1ekd "If you think things won't get better..."
    m 1ekb "I want you to listen to it, and remember that I'm always with you."
    m 1hub "In your heart!"
    m 1kub "And will always be."
    m 2fka "I love you, [mas_get_player_nickname()]."
    m 2esa "Take care."
    
return

#PLAYLIST DIALOGUES

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_playlist",category=["you"],prompt="Playlist",pool=True,unlocked=True))

label monika_playlist:
    m "Oh, do you wanna listen to the playlist, [player]?"
    menu:
        m "Play music?{fast}"
        "Yes":
            stop music
            play music "mod_assets/other/Monika_s-Playlist.mp3"
            m "There you go!"
            m "I hope you like it!"
        "No":
            "Oh, alright."
    return
   
# BATTLE SCARS - PARADISE FEARS
    m "{i}~I'll carry you home~{/i}"
    m "{i}~No, you're not, alone~{/i}"
    m "{i}~Keep marching on~{/i}"
    m "{i}~This is worth fighting for~{/i}"
    m "{i}~You know we've, all got battle scars~{/i}"
    m "{i}~You've had enough~{/i}"
    m "{i}~But just don't, give up~{/i}"
    m "[Player], I hope you can remember that you're not alone with your struggles."
    m "There are people who can help you, and some even went through what you feel right now."
    m "There's a lot of support groups for people who are struggling just like you."
    m "And, of course, there's me!"
    m "Whenever you need, I'll carry you home."
    m "Your battle scars make me proud of what you already outlived!"
    m "And never forget... I love you, [Player]."
    
# CLAY - GRACE VANDERWALL
    m "{i}~Your silly words~{/i}"
    m "{i}~I won't live inside your world~{/i}"
    m "{i}~'Cause your punches and your names~{/i}"
    m "{i}~All your jokes and stupid games~{/i}"
    m "{i}~They don't work~{/i}"
    m "{i}~No, they don't hurt~{/i}"
    m "{i}~Watch them just go right through me~{/i}"
    m "{i}~Because they mean nothing to me~{/i}"
    m "{i}~I'm not clay~{/i}"
    m "..."
    m "It's important to not let others get to you, you know?"
    m "Listening to someone's opinion about you can help, but only if you know the person has good intentions."
    m "Don't feel down when others act mean towards you, dear."
    m "It only shows what kind of person they are, not who you are."
    m "And for me, you're the best in the world."
    m "I love you~"
    
#FIX YOU - COLDPLAY
    m "{i}~But if you never try, you'll never know~{/i}"
    m "{i}~Just what you're worth~{/i}"
    m "{i}~Lights will guide you home~{/i}"
    m "{i}~And ignite your bones~{/i}"
    m "{i}~And I will try to fix you~{/i}"
    m "..."
    m "Even if you feel like giving up, remember this verse: "Lights will guide you home"..."
    m "Sooner or later, the good days will come back."
    m "I hope I can be able to help you have brighter days, [Player]."
    m "Because I will surely try to fix you..."
    m "I love you more than anything in the world."
    
#I HATE TO SEE YOUR HEARTBREAK - PARAMORE
    m "{i}~And I, I hate to see your heart break~{/i}"
    m "{i}~I hate to see your eyes get darker as they close~{/i}"
    m "{i}~But I've been there before~{/i}"
    m "{i}~For all the air that's in your lungs~{/i}"
    m "{i}~For all the joy that is to come~{/i}"
    m "{i}~For all the things that you're alive to feel~{/i}"
    m "{i}~Just let the pain remind you hearts can heal~{/i}"
    m "I think this song really fits how I feel about us."
    m "It's really saddening to see the person you love the most having to go through tough situations on daily basis..."
    m "But don't worry, [mas_get_player_nickname()]."
    m "Pain can remind you that you're alive. And that's a good thing!"
    m "Because as long as you are still alive... You can heal."
    m "I love you, [Player]. Please remember that."
    
#O-O-H CHILD - THE FIVE STAIRSTEPS
    m "{i}~Ooh child, things are gonna get easier~{/i}"
    m "{i}~Ooh child, things'll get brighter~{/i}"
    m "{i}~Some day, yeah, we'll put it together and we'll get it undone~{/i}"
    m "{i}~Some day, when your head is much lighter~{/i}"
    m "{i}~Some day, yeah, we'll walk in the rays of a beautiful sun~{/i}"
    m "{i}~Some day, when the world is much brighter~{/i}"

#THE MIDDLE - JIMMY EAT WORLD
    m "{i}~It just takes some time~{/i}"
    m "{i}~Little girl, you're in the middle of the ride~{/i}"
    m "{i}~Everything, everything'll be just fine~{/i}"
    m "{i}~Everything, everything'll be alright, alright~{/i}"
    m "{i}~Live right now~{/i}"
    m "{i}~Yeah, just be yourself~{/i}"
    m "{i}~It doesn't matter if it's good enough~{/i}"
    m "{i}~For someone else~{/i}"
    
#FIREWORK - KATY PERRY
    m "{i}Do you ever feel, feel so paper thin~{/i}"
    m "{i}Like a house of cards~{/i}"
    m "{i}One blow from caving in?~{/i}"
    m "{i}~Do you ever feel already buried deep?~{/i}"
    m "{i}~Six feet under screams, but no one seems to hear a thing~{/i}"
    m "{i}~Do you know that there's still a chance for you~{/i}"
    m "{i}~'Cause there's a spark in you~{/i}"
    m "{i}~You just gotta ignite the light, and let it shine~{/i}"
    m "{i}~Just own the night like the 4th of July~{/i}"

#TORCHES - AIMER
    m "{i}~Listen to me, cleave your way again, again~~{/i}"
    m "{i}~Wishing to find a way in an unseen ocean~{/i}"
    m "{i}~The voice that was connected pushes the sail to a world with no answer~{/i}"
    m "{i}~You're not alone~{/i}"
    m "{i}~Hold a light~{/i}"
    m "{i}~Towards the darkness~{/i}"
    m 1eka "[Player]..."
    m 1ekd "Sometimes the world can be scary."
    m 1ekd "You may feel as if no one cares about whether you're alive or not..."
    m 3ekb "But you should know that people do care about you. People from all over the world, who might have never even seen our faces, but..."
    m 3eka "They care. And I care."
    m 3eka "I'm so happy to have you by my side, [mas_get_player_nickname()]. I hope you're happy to have me too."
    m 3hub "You're not alone in this. I promise!"


#ONLY WONDER - FREDERIC
    m "{i}~What’re you sayin’? Everybody’s different!~{/i}"
    m "{i}~Stop messin’ with me, I’ll have to shut you out~{/i}"
    m "{i}~The spotlight’s on you, but you’re acting all flashy~{/i}"
    m "{i}~It’s as if you’re trying to be someone’s answer~{/i}"
    m "{i}~Don’t go shakin’ your tail like that~{/i}"
    m "{i}~No matter what happens… In the end, you can only be your own person!~{/i}"
    m "..."
    m 3eka "[Player], you're beautiful just the way you are, and it'd be terrible if you stopped being that way to fit another person's standards."
    m 3eka "You might think you're too "weird" or shy for people to like you, but in the end, there's always someone who understands you out there."
    m 3esd "Anyone who tries to tell you otherwise is wrong."
    m 3esd "Of course this doesn't mean you're perfect and always right... That's a whole different story."
    m 3hub "But please remember that the only person you can be is yourself. Everybody else is already taken, ahaha~!"
    m 1ekb "As for me..."
    m 5ekbsb "I'll always love you for who you are, [mas_get_player_nickname()]."
    m 5hubsa "Ehehe!"

#SOMEDAY I'LL FIND MY WAY HOME - CAROLE & TUESDAY
    m "{i}~Someday I’ll find my way home~{/i}"
    m "{i}~The trees in the wind will lead the way~{/i}"
    m "{i}~All of these years on my own~{/i}"
    m "{i}~They flew right by, so what can you say?~{/i}"
    m "{i}~There's no need to be sad~{/i}"
    m "{i}~You're on a path and you know where it heads~{/i}"
    m "{i}~There’s no need for despair~{/i}"
    m "{i}~Just walk on and you'll find you're there~{/i}"
