import pygame #Gives us our gaming functions
from os import path
import textwrap

"""
Initialize Font Object
"""
#We pick our text style and size
pygame.init()
my_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption('Class Introductions')#To add the title of game


def get_file(fileName):
    """
    Returns the absolute path of a file
    """
    #This grabs the image files from your folder
    return path.join(path.dirname(__file__), fileName)

def display_text(screen, current_text):
    """
    Displays text to the screen
    """
    WRAPPED_TEXT = textwrap.wrap(current_text, 30)
    y = 230
    for i in range(len(WRAPPED_TEXT)):
        screen.blit(my_font.render(WRAPPED_TEXT[i], True, (0, 0, 0)), (230,y))
        y = y + 30

"""
Loads the background and images
"""
background = pygame.image.load(get_file("Assets/Background.png"))
annie_conda = pygame.image.load(get_file("Assets/AnnieConda.png"))
bayo_wolf = pygame.image.load(get_file("Assets/BayoWolf.png"))
grafika_turtle = pygame.image.load(get_file("Assets/GrafikaTurtle.png"))
intelli_scents = pygame.image.load(get_file("Assets/IntelliScents.png"))
java_lynn = pygame.image.load(get_file("Assets/JavaLynn.png"))
captain_javo = pygame.image.load(get_file("Assets/CaptainJavo.png"))
jitter_bug = pygame.image.load(get_file("Assets/JitterBug.png"))
paul_python = pygame.image.load(get_file("Assets/PaulPython.png"))
quackintosh = pygame.image.load(get_file("Assets/Quackintosh.png"))
sb_turtle = pygame.image.load(get_file("Assets/SBTurtle.png"))
sidewinder = pygame.image.load(get_file("Assets/SideWinder.png"))
syntax_turtle = pygame.image.load(get_file("Assets/SyntaxTurtle.png"))
#TODO: add the images for RAM & ROM and one for Amphib Ian here

"""
Stores character text into variables
"""
text_annie_conda  = "Hello! I'm Annie Conda. \nI come from Sanfran-Hissco, Cowlifornia. I've done a little coding. My favorite musician is Justin Timbersnake. I'm also partial to Hissy Elliott. My favorite Pigxar movie is Rattle-toulle. I love to make trivia games and word games. "
text_bayo_wolf  = "I'm Bayo Wolf, from Little Squawk, Barkansas. I'm the best at SpaceWars and great at Mega Mechs in my Grendel mech. My favorite movies are The Dogfather, Jurassic Bark, Citizen Canine, and Stall Wars: The Empire Strikes Cats. My top actors are Brad Pitbull, Howly Berry, and Sandra Bulldog. "
text_grafika_turtle  = "My name is Grafika Turtle. I live here, in Red-mutt, Washeepton. Now I get to go to school with my best friend. Hi, Paul! I love the movie Wizard of Paws, and my favorite artist is Pablo Pigcasso. I like coding in Turtle Graphics, and my brother Syntax and I are pretty good at coding card games. "
text_intelli_scents  = "Hi. I'm Intelli-Scents from Minnea-pawlis, Minnow-soda. My top movies are Hack to the Future, Mission Impawsible with Eat'n Hunt, and Hair-Spay. My top artist is Vincent van Gopher, top book is The Time Machine by H.G. Gills, and my favorite neurologist is Digmund Freud.  "
text_java_lynn  = "I'm Java Lynn, also from Minnea-pawlis. I shop at Blooming Tails and read Vanity Fur. Top movies are Hairy Otter 8, Catsaway with Tomcat Hanks, and the Sound of Mew-sic. My actors are Bill Furry and Scarlett Johamster. I love the art \"Squirrel with the Acorn Earrings.\" "
text_captain_javo  = "I'm Captain Javo, from Indiana-pawlis, Fin-diana. The movies I like are The Fast and Furry-us, Paws, and Clawshank Redemption. My actors are Woodchuck Norris, Billy Grrr-ystal, and Will Ferret. My musicians are Kitty Purry and Britney Ears. My favorite programming language is Java. "
text_jitter_bug  = "I am Jitter Bug, from Ant-aheim, Cowlifornia. My favorite movies are Mrs. Doubtspider and Twi-mite. I love the Stall Wars character Luke Flywalker. My top actors are Kristin Ear-Wiig and Molly Ringworm. My favorite musicians are Beeyonce, Flyley Flyrus, and Nine-Inch Snails. "
text_paul_python  = "Hi. I'm Paul Python. My home is just over the bridge in Sea-cattle. Mega Mechs is my favorite game, and the reason why I'm here, by winning the tournament! I love the actor David Hisselhoff, and I agree with Annie that Justin Timbersnake makes awesome music! But I also like White Snake. "
text_quackintosh = "Hello. I'm Quackintosh, from nearby Bill-view, Washeepton. My top actors are Audrey Honkburn, Goose Willis, Squawkin Phoenix, Robird De Niro, Hennifer Lawrence, and Woody Owlen. My musicians are Swan Bon Jovi, Michael Quackson, and Ozzy Ostrich. My top art is \"Son of Duck.\" "
text_sb_turtle = "Hey. I'm SB Turtle, from New-ark, Moo Jersey. My top actresses are Shelly Long and Zooey Deshell. I'm a founding member of the Shell Scouts, and my favorite programming language is Microsoft Small Basic. Oh, and I grow into a giant monster, but that's for a different book. "
text_sidewinder = "I'm SideWinder, from Salt-Snake City, Mewtah. I'm the best at SpaceWars, despite what Bayo thinks. My favorite movie is Snakes on a Glider, my favorite actor is Sylvester Stallion, and my favorite musician is Nine-Inch Snails. Jitter Bug has good taste. "
text_syntax_turtle = "What's up? Syntax Turtle in the house. I'm from here, Red-Mutt, with my twin sis Grafika. My favorite actress is Natalie Porkman, and my favorite artist is Lizardnardo Da Vinci. My top games are \"Skate and Fly\" and Porkymon, and I'm looking forward to making a Codu Kids card game! "
#TODO: uncomment the introduction for RAM & ROM and one for Amphib Ian below:
##text_ram_rom = "Heya! We're RAM and ROM. We came from the other side of the country, Woolshington DC. We like Meryl Sheep, Dustin Hoofman, and Eva Longhornia. Our favorite musician is Lady Baa-Baa, and our sensei is the Dali Llama. We're working on a top-secret project! "
##text_amphib_ian  = "Yo, yo. What's hopping, peeps? Name's Amphib Ian. My launchpad is Croaklahoma City. My choice singer is Demi Lovatoad. And my fave artwork is \"Mourning Son\" by Edwart Hopper. My go-to game to code is Froggy Road. That's it. I'll catch you on the flip flop! "

"""
We assign our character and text variables
"""
current_character = annie_conda
current_text = text_annie_conda

"""
Displays character to the screen
"""
width = 600
height = 800
screen = pygame.display.set_mode((width,height))
running = True

while running:
    screen.blit(background,(0,0))
    screen.blit(current_character, (0,0))
    display_text(screen, current_text)
    pygame.display.flip()
    EVENTS = pygame.event.get()
    for event in EVENTS:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_character = annie_conda
                current_text = text_annie_conda
            if event.key == pygame.K_2:
                current_character = bayo_wolf
                current_text = text_bayo_wolf
            if event.key == pygame.K_3:
                current_character = grafika_turtle
                current_text = text_grafika_turtle
            if event.key == pygame.K_4:
                current_character = intelli_scents
                current_text = text_intelli_scents
            if event.key == pygame.K_5:
                current_character = java_lynn
                current_text = text_java_lynn 
            if event.key == pygame.K_6:
                current_character = captain_javo
                current_text = text_captain_javo
            if event.key == pygame.K_7:
                current_character = jitter_bug
                current_text = text_jitter_bug
            if event.key == pygame.K_8:
                current_character = paul_python
                current_text = text_paul_python
            if event.key == pygame.K_9:
                current_character = quackintosh
                current_text = text_quackintosh
            if event.key == pygame.K_0:
                current_character = sb_turtle
                current_text = text_sb_turtle
            if event.key == pygame.K_q:
                current_character = sidewinder
                current_text = text_sidewinder
            if event.key == pygame.K_w:
                current_character = syntax_turtle
                current_text = text_syntax_turtle
            #TODO: Add the if statements for RAM & ROM and one for Amphib Ian here
pygame.quit()
