# The script of the game goes in this file.

# The game starts here.

include "introtutorial.rpy"


label splashscreen:

    #Shows a presrceen; logo with transition of an image of the company logo and give a
    #couple sec to 
    scene black 
    with Pause(1)
    
    show  text "Time is on your side..." with dissolve
    with Pause(2)

    hide text with dissolve 
    with Pause(1)
    
    return

label start:

    jump tt
    #Going to the story follder for the intro of the game


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    return

label tt:
    
    "Welcome to Nightfall the game this game will test your morals on scenarios."
    
    "You will be scored on it and given a result of what type of morals you have."
    
    "You will have 2 people supporting and guiding you on your journey."

    
    menu survey:
        "Are your ready to get started?"
        "Yes":
            jump ch1

        "No":
            $ renpy.quit() # Quit the application

    return

    label ch1:

        "Hello CITA 412"


        return