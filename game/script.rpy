# The script of the game goes in this file.

# The game starts here.


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

    call story.introtutorial
    #Going to the story follder for the intro of the game


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    return

