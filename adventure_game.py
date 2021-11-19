import random
import time
import string


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(0)


def boss_pool():
    global boss
    boss = random.choice(["Vampire", "Werwolf", "Demon"])


def choosing_character():
    global player
    print_pause("Loading...")
    prompt = 'CHOOSE YOUR CHARACTER NUMBER\n 1) Wizard, 2) Knight, 3) Archer\n'
    options = ['1', '2', '3']
    response = valid_input(prompt,options)
    if response == '1':
        player = "Wizard"
        print_pause("you are a " + player)
    elif response == '2':
        player = "Knight"
        print_pause("you are a " + player)
    else:
        player = "Archer"
        print_pause("you are a " + player)


loot = ""
player = ""
inventory = "0"
item = ""
boss = ""
item_skill = ""
scenary = ""
weapon = ""
fight = ""
ammo = ""
answer_marks = [0, 0, 0]


def statistics():
    item_fight_ammo_itemskill()
    scenary_loot()


def item_fight_ammo_itemskill():
    global item
    global weapon
    global fight
    global ammo
    global item_skill
    if player == "Wizard":
        item = "Supreme Sorcerer's Staff"
        fight = "cast"
        ammo = "spell"
        weapon = "magic wand"
        item_skill = "will let you cast spelss without having to spend any mana"
    elif player == "Knight":
        item = "Unbeakable Stoneshield"
        fight = "strike"
        ammo = "slash"
        weapon = "sword"
        item_skill = "will let you tank to opponents even bigger than you"
    elif player == "Archer":
        item = "Infallible Cursed Sight"
        fight = "shot"
        ammo = "arrow"
        weapon = "bow"
        item_skill = "will guarantee you an headshot every time you aim and shoot on someone"


def scenary_loot():
    global scenary
    global loot
    if boss == "Vampire":
        scenary = "hunted castle"
        loot = "piece of garlic"
    elif boss == "Werwolf":
        scenary = "creepy wood"
        loot = "silver fork"
    elif loot == "Demon":
        scenary = "cemetery"
        loot = "tiny holy water bottle"


def intro():
    choosing_character()
    statistics()
    print_pause(tale("and you are traveling in search of the {{item}}"))
    print_pause(tale("this special item will {{item_skill}}"))
    print_pause(tale("after days of traveling you find yourserl in a {{scenary}}"))
    print_pause(tale("while entering into the {{scenary}} you feel a little bit of fear but you stay calm and ready"))
    find_chest()


def sleeping_cat():
    print_pause("the Cat is sleaping inside the empty open chest")
    searcing_item()


def find_chest():
    print_pause("you find a cat on a closed chest")
    response = valid_input("what you do?\n 1) open the chest, 2) continue to walk\n", "1 open chest 1 continue walking")
    if "1" in response.lower() or "open" in response.lower() or "chest" in response.lower():
        cat_introducing()
        cat_questions()
    elif "2" in response.lower() or "continue" in response.lower() or "walking" in response.lower():
        searcing_item()


def tale(template):
    output = []
    index = 0
    while index < len(template):
        if template[index:index+10] == '{{player}}':
            output.append(player)
            index += 10
        elif template[index:index+8] == '{{loot}}':
            loot = inventory
            output.append(loot)
            index += 8
        elif template[index:index+8] == '{{item}}':
            output.append(item)
            index += 8
        elif template[index:index+8] == '{{boss}}':
            output.append(boss)
            index += 8
        elif template[index:index+14] == '{{item_skill}}':
            output.append(item_skill)
            index += 14
        elif template[index:index+11] == '{{scenary}}':
            output.append(scenary)
            index += 11
        elif template[index:index+17] == '{{player_weapon}}':
            output.append(weapon)
            index += 17
        elif template[index:index+17] == '{{player_action}}':
            output.append(fight)
            index += 17
        elif template[index:index+14] == '{{player_hit}}':
            output.append(ammo)
            index += 14
        else:
            output.append(template[index])
            index += 1
    return "".join(output)


def meet_cat():
    if inventory == "1":
        print_pause(tale("the Cat is sleeping inside the empty chest"))
        searcing_item()
    else:
        find_chest()


def cat_introducing():
    print_pause(tale("Cat: 'Oh {{player}} {{player}}, my dear {{player}}'"))
    print_pause(tale("Cat: 'if you want to open this chest'"))
    print_pause(tale("Cat: 'you must first prove your worth as a {{player}}'"))
    print_pause(tale("Cat: 'I will submit you to a trial consisting of three questions'"))
    print_pause(tale("Cat: 'if you pass it you will be able to open the chest'"))
    cat_questions()


def cat_questions():
    cat_questions1()
    cat_questions2()
    cat_questions3()


def cat_questions1():
    global answer_marks
    response1 = valid_input("Cat: 'What is the most powerful poison for a vanpire?''\n 1) garlic, 2) onion\n",  "1 garlic 2 onion")
    if "1" in response1.lower() or "garlic" in response1.lower():
        answer_marks[0] = 1
        rigth_answer()
    elif "2" in response1.lower() or "onion" in response1.lower():
        wrong_answer()


def cat_questions2():
    global answer_marks
    response2 = valid_input("Cat: 'What does a werwolf can't touch?'\n 1) the silver, 2) the gold \n", "1 2 silver gold")
    if "1" in response2.lower() or "silver" in response2.lower():
        answer_marks[1] = 1
        rigth_answer()
    elif "2" in response2.lower() or "gold" in response2.lower():
        wrong_answer()


def cat_questions3():
    global answer_marks
    response3 = valid_input("Cat: 'What you need to use to turn a demon into stone?'\n 1) holy water 2) holy paper\n", "1 2 water paper")
    if "1" in response3.lower() or "water" in response3.lower():
        answer_marks[2] = 1
        rigth_answer()
    elif "2" in response3.lower() or "paper" in response3.lower():
        wrong_answer()


def wrong_answer():
    global answer_marks
    answer_marks[0] = 0
    answer_marks[1] = 0
    answer_marks[2] = 0
    print_pause("Cat: 'Wrong answer... you can't open the chest'")
    response = valid_input("Cat: 'do you what to try again?'\n 1) yes, 2) no go away\n", "yes no go away")
    if "1" in response.lower() or "yes" in response.lower():
        cat_questions()
    elif "2" in response.lower() or "no" in response.lower() or "go" in response.lower() or "away" in response.lower():
        searcing_item()


def rigth_answer():
    global inventory
    if answer_marks == [1, 1, 1]:
        print_pause(tale("Cat: 'Good job! now you can open the chest'"))
        print_pause(tale("in the chest you find a silver fork, a piece of garlic and a tiny holy water bottle"))
        inventory = "1"
        searcing_item()
    else:
        print_pause(tale("Cat: 'Correct! next question"))


def find_item():
    print_pause(tale("a golden chest appear exatly where the enemy get defeated"))
    print_pause(tale("you greedily approach it and when you open the chest"))
    print_pause(tale("you realize that you finally managed to find the desired {{item}}"))
    print_pause(tale("now this new item {{item_skill}}"))


def searcing_item():
    boss_pool()
    print_pause(tale("you walk away from the cat looking around you hoping to find the much desired {{item}}"))
    print_pause(tale("when suddenly a {{boss}} appeear"))
    fight_or_escape()


def fight_or_escape():
    response = valid_input("what you want to do?\n 1) fight, 2) go back to the cat\n", "1 2 fight go back cat")
    if "1" in response.lower() or "fight" in response.lower():
        if inventory == "1":
            choosing_weapon()
        else:
            wrong_weapon_attack_descr()
    if "2" in response.lower() or "go" in response.lower() or "back" in response.lower() or "cat" in response.lower():
        meet_cat()


def choosing_weapon():
    global weapon
    response = valid_input("choose your weapon\n 1) piece of garlic, 2) silver fork, 3) tiny holy water bottle\n", " 1 2 3 silver fork piece garlic tiny holy whater bottle")
    if boss == "Vampire" and "piece" in response.lower() or "garlic" in response.lower():
        weapon = "piece of garlic"
        loot_boss_fight()
    elif boss == "Werwolf" and "silver" in response.lower() or "fork" in response.lower():
        weapon = "piece of garlic"
        loot_boss_fight()
    elif boss == "demon" and "tiny" in response.lower() or "holy" in response.lower() or "water" in response.lower() or "Bottle" in response.lower():
        weapon = "piece of garlic"
        loot_boss_fight()
    else:
        if "piece" in response.lower() or "garlic" in response.lower():
            weapon = "piece of garlic"
            wrong_loot_attack_descr()
        elif "silver" in response.lower() or "fork" in response.lower():
            weapon = "silver fork"
            wrong_loot_attack_descr()
        elif "tiny" in response.lower() or "water" in response.lower() or "holy" in response.lower() or "bottle" in response.lower():
            weapon = "tiny holy water bottle"
            wrong_loot_attack_descr()


def wrong_loot_attack_descr():
    print_pause(tale("you try to throw the {{player_weapon}}"))
    print_pause(tale("but nothing appens... the {{boss}} looks at you whith confused eyes and says"))
    print_pause(tale("{{boss}}: 'you can't beat me with your {{player_weapon}}'"))
    print_pause(tale("so you try to use "))
    weapon_boss_fight()


def wrong_weapon_attack_descr():
    print_pause(tale("you try to {{player_action}} a {{player_hit}} whit your powerful {{player_weapon}}"))
    print_pause(tale("but the {{boss}} is much stronger than you"))
    print_pause(tale("and can resist at it "))
    weapon_boss_fight()


def weapon_boss_fight():
    if boss == "Vampire":
        print_pause(tale("but he blocks all your movement with the power of his mind"))
        print_pause(tale("then he start walking slowly behind you."))
        print_pause(tale("as soon as he bite, you can feel your blood leaving your veins"))
        print_pause(tale("and you can't do nothing but take your last breat"))
        game_over()
    elif boss == "Werwolf":
        print_pause(tale("but he is so fast that doges on your left and hurt you whith his claws"))
        print_pause(tale("so you try to hit him but the werewolf has alredy jumped on you head"))
        print_pause(tale("and whith a single bite he take your head off"))
        game_over()
    elif boss == "Demon":
        print_pause(tale("but his body temperature alone incinerates your {{player_weapon}} even before you can hit him,"))
        print_pause(tale("after sneering he blows towards you"))
        print_pause(tale("and you get engulfed by a blaze at very high temperatures that incinerates you"))
        game_over()


def loot_boss_fight():
    if boss == "Vampire":
        print_pause(tale("you decide to throw the piece of garlic to the vampire. but the garlic falls on the ground..."))
        print_pause(tale("after tree seconds it start growning and become a gaglic monster"))
        print_pause(tale("that start hitting the vampire with his garlic tentacles"))
        print_pause(tale("Vampire: 'Nooooooo! this garlic monster is too strong for me'"))
        print_pause(tale("so the vampire escapes turning into a bat"))
        print_pause(tale("after the vampire escape"))
        find_item()
        play_again()
    elif boss == "Werwolf":
        print_pause(tale("you take your silver fork and start walkin towards the weerewolf"))
        print_pause(tale("at some point the fork starts to glowing"))
        print_pause(tale("the werewolf seems annoyed by it so you keep walking rising your fork"))
        print_pause(tale("as the fork get brighter the wolf get more anoyed until he falls to the ground stunned"))
        print_pause(tale("at this point you touch it with the fork which has now become very bright"))
        print_pause(tale("as you touch the werewolf the light passes from the fork to the stunned creature"))
        print_pause(tale("transforming him into a human being"))
        print_pause(tale("Human Being: 'Thank you stranger! you freed me from the curse that plagued my existence, I will be eternally grateful'"))
        print_pause(tale("Human Being: 'Now i run away'"))
        print_pause(tale("after the ex werwlof escape"))
        find_item()
        play_again()
    elif boss == "Demon":
        print_pause(tale("you trow to the demon your tiny holy water bottle"))
        print_pause(tale("that starts blinking faster as it get closer to the demon and then explode"))
        print_pause(tale("revealing itself not to be a holy water bottle but a holy water granade"))
        print_pause(tale("the demon get blasted by a holy shockwave that blows away his fire souls"))
        print_pause(tale("leaving a pile of hot, steaming stones on the ground"))
        print_pause(tale("after the demon deat"))
        find_item()
        play_again()


def game_over():
    print_pause(tale("GAME OVER"))
    response = valid_input("do you want to try again?\n 1) yes, 2) no\n", " 1 2 yes no")
    if "1" in response.lower() or "yes" in response.lower():
        searcing_item()
    elif  "2" in response.lower() or "no" in response.lower():
        print_pause("Thanks for playing :)")


def play_again():
    print_pause("GOOD JOB! :)")
    print_pause("you have finished this game")
    response = valid_input("do you want to play again?\n 1) yes, 2) no\n", " 1 2 yes no")
    if "1" in response.lower() or "yes" in response.lower():
        play_game()
    elif  "2" in response.lower() or  "no" in response.lower():
        print_pause("Thanks for playing :)")


def play_game():
    statistics()
    intro()


play_game()
