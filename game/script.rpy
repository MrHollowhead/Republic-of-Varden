# Declare characters used by this game. The color argument colorizes the
# name of the character.

define reporter = Character("Local News Reporter")
define president = Character("President Huba")
define advisor = Character("Alfred")
define player = Character("[player_name]", dynamic=True)

default political_influence = 50
default party_unity = 85
default public_support = 52
default institutional_trust = 60
default coalition_relation = 50
default event_tick = 0
default current_day = 1
default player_name = ""

default lower_CR = 93
default lower_NC = 10
default lower_NA = 71
default lower_SL = 26

default senate_CR = 15
default senate_NC = 3
default senate_NA = 31
default senate_SL = 11

default press_speech = ""
default railway_attention = False
default clean_state_attention = False
default coalition_attention = False
default selected_priority = ""
default railway_approach = ""
default clean_state_approach = ""
default coalition_approach = ""
default decision_tut_seen = False
default railway_event_due = 0
default clean_state_event_due = 0
default coalition_event_due = 0

screen dashboard():

    frame:
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 50
            xalign 0.5
            yalign 0.5
            text "REPUBLIC OF VARDÉN"
            text "DAY [current_day]"
            hbox:
                spacing 10
                xsize 750
                text "Public Support:\n [public_support]%"
                text "Institutional Trust:\n [institutional_trust]/100"
            hbox:
                spacing 10
                xsize 750
                text "Political Influence:\n [political_influence]/100"
                text "Party Unity:\n [party_unity]/100"

            add Solid("#ffffff"):
                xsize 750
                ysize 2

            hbox:
                xalign 0.5
                yalign 0.5
                vbox:
                    xsize 325
                    text "LOWER HOUSE"
                    text "200 SEATS"
                
                vbox:
                    xsize 325
                    text "SENATE"
                    text "60 SEATS"

            hbox:
                xalign 0.5
                yalign 0.5
                vbox:
                    xsize 325
                    text "CR:             [lower_CR]"                
                    text "NC:             [lower_NC]"
                    text "NA:             [lower_NA]"
                    text "SL:             [lower_SL]"
                vbox:
                    xsize 325
                    text "CR:             [senate_CR]"                
                    text "NC:             [senate_NC]"
                    text "NA:             [senate_NA]"
                    text "SL:             [senate_SL]"



            textbutton "Continue":
                action Return()

# The game starts here.

label start:
    play music "audio/music/Envision.mp3" fadeout 1.0 fadein 2.0

    "REPULIC OF VARDÉN"

    reporter "The elections have ended and the votes have been counted."

    reporter "The Civic Renewal Party has achieved a historical victory."

    "You have been named as the new Prime Minister."

    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Alex Varen"

    president "Welcome Prime Minister [player_name]!"

    jump press_conference

label press_conference:
    advisor "(Your advisor)\n
    \n
    The press is waiting for you at your first press conference as Prime Minister"
    advisor "First, you will deliver a short speech. After that, we should have time for approximately three questions"

    menu:
        "What kind of tone will you take in your speech?"
        "Aggresive":
            $ press_speech = "aggresive"
            $ public_support += 3
            $ political_influence += 2
            $ institutional_trust -= 2
            $ coalition_relation -= 1
            player "The people of Vardén voted for change, and this government intends to deliver it."
            player "We will not allow political obstruction, entrenched interests, or old habits to stand in the way of that mandate."
            player "There will be resistance. We are prepared for it."

        "Stable":
            $ press_speech = "stable"
            $ institutional_trust += 3
            $ public_support += 1
            $ political_influence -= 1
            player "A change of government should not mean uncertainty for the country."
            player "Our institutions will continue to function, our commitments will be respected, and reforms will be introduced responsibly."
            player "Vardén voted for change, but change must be built on stability."

        "Cooperative":
            $ press_speech = "cooperative"
            $ coalition_relation += 3
            $ institutional_trust += 2
            $ party_unity -= 1
            player "The challenges facing Vardén cannot be solved by one party or one government alone."
            player "We will work with our coalition partners, Parliament, our institutions, and where possible, the opposition."
            player "Our disagreements will remain, but cooperation must come before political division."

        "Ambitious":
            $ press_speech = "ambitious"
            $ public_support += 3
            $ party_unity += 2
            $ institutional_trust -= 1
            player "Vardén has spent too long accepting that some things simply cannot be changed."
            player "This government intends to challenge that assumption."
            player "We have an opportunity not merely to govern the country, but to leave it stronger, fairer, and more capable than we found it."

        "Pragmatic":
            $ press_speech = "pragmatic"
            $ political_influence += 2
            $ institutional_trust += 2
            $ public_support -= 1
            player "This government will not ask to be judged by the scale of its promises."
            player "Judge us by what we accomplish."
            player "Where reform is necessary, we will reform. Where something works, we will preserve it. Our priority will be results."


    jump press_questions
label press_questions:

    menu:
        "Who will you take questions from?"
        "NNC - Naional News Coverage":




        "Continue":
            jump day_one

label day_one:
    "DAY 1"

    "Your first day in office begins"

    advisor "Good morning, Prime Minister [player_name].\n I hope you are rested."
    advisor "Our party gained 93 mandates out of the 200 mandates of the lower house."
    advisor "Together with NCP (Nature Conservatory Party) our coalition has gathered 103 out of the 200 mandates."
    advisor "This means we have achieved a 51,5%% majority in the Lower House."

    jump tutorial

label tutorial:
    advisor "Before we jump into deep water let's show you around."
    advisor "At the beginning of each event you will receive a report of basic data needed to govern."
    advisor "Here is your report for today!"

    call screen dashboard
    jump first_choice

label first_choice:
    advisor "Now that you are aware of the Lower House's and Senate's statuses as well as our political standings, it's time to get to business.\n Politics never stop."
    "He places 3 folders on your desk, each thicker than a dictionary"
    advisor "We won't be able to give our attenion to all three of these cases at once."
    advisor "Number one is:\n
    East-West High-Speed Railway is one of the last and biggest investments of the previous government, the new Ministry Of Finance found the way of the money concerning."
    advisor "Number two is:\n
    The Clean State Act, one of the most important promises of our campaign about a new anti-corruption Institution"
    advisor "Number three is:\n
    A coalition meeting, the Head of the NC party wants to meet and discuss various things, one of the first points he mentioned was how thin our majority is"
    advisor "The choice of our priority is yours [player_name]"

    jump priority_selection

label priority_selection:
    menu:
        "Which folder do you reach for?"
        "East-West High-Speed Railway":
            $ selected_priority = "railway"
        
        "Clean State Act":
            $ selected_priority = "clean_state"
        
        "Coalition Meeting":
            $ selected_priority = "coalition"

    advisor "All three matters will eventually require your attention."
    advisor "However, the order in which you address them and the decisions you make along the way may entirely change how each situation develops."

    menu:
        advisor "Are you sure about your choice?"

        "Yes":
            if selected_priority == "railway":
                $ railway_attention = True
                if not decision_tut_seen == True:
                    advisor "Very well. There is one more thing I want to let you know."
                    advisor "There is rarely a single right answer in politics. Every decision comes with consequences."
                    advisor "From this point forward, I will not ask you to confirm your decisions. Consider your choices carefully before giving an order."
                    advisor "In Vardén every decision matters."
                    $ decision_tut_seen =  True

                jump railway_event

            elif selected_priority == "clean_state":
                $ clean_state_attention = True
                if not decision_tut_seen == True:
                    advisor "Very well. There is one more thing I want to let you know."
                    advisor "There is rarely a single right answer in politics. Every decision comes wih consequences."
                    advisor "From this poin forward, I will no ask you to confirm your decisions. Consider your Choices carefully before giving an order."
                    advisor "In Vardén every decision matters."
                    $ decision_tut_seen =  True

                jump clean_state_event

            else:
                $ coalition_attention = True
                if not decision_tut_seen == True:
                    advisor "Very well. There is one more thing I want to let you know."
                    advisor "There is rarely a single right answer in politics. Every decision comes wih consequences."
                    advisor "From this poin forward, I will no ask you to confirm your decisions. Consider your Choices carefully before giving an order."
                    advisor "In Vardén every decision matters."
                    $ decision_tut_seen =  True

                jump coalition_event
            
        "Let me reconsider":
            jump priority_selection

label railway_event:
    "EAST-WEST HIGH-SPEED RAILWAY"
    advisor "The East-West High-Speed Railway is one of the largest infrastructure projects in Vardén's history."
    advisor "The previous government signed the concession agreement only three months before the election."
    advisor "Construction has already begun."
    advisor "However, the Ministry of Finance has flagged unusually high costs in several procurement contracts."
    advisor "At this point, we have no evidence of criminal wrongdoing."
    advisor "But the Ministry recommends that we investigate further."
    advisor "The project is being carried out by a consortium led by Aurelis Infrastructure Group."

    menu:
        advisor "How should the government proceed?"

        "Order an independent external audit of the consortium.":
            $ institutional_trust += 3
            $ political_influence -= 2
            $ railway_approach = "external"
            advisor "The safest option. An independent audit will give us the most credible findings"
            advisor "But don't expect answers quickly. A proper audit of a project this size may take weeks."
            $ delay = renpy.random.randint(3, 5)
            $ railway_event_due = event_tick + delay

        "Order the Ministry of Finance to conduct a full review of the concession agreement.":
            $ institutional_trust += 1
            $ political_influence += 1
            $ railway_approach = "contract"
            advisor "The Ministry can begin immediately. We could have preliminary findings within days."
            advisor "But an internal review comes with no guarantees. We may find answers or simply more questions"
            $ delay = renpy.random.randint(2, 3)
            $ railway_event_due = event_tick + delay

        "Suspend further government payments pending clarification.":
            $ public_support += 5
            $ institutional_trust -= 3
            $ political_influence -= 6
            $ railway_approach = "nuke"
            advisor "Suspend the payments..?"
            advisor "I'll inform the Ministry. But Aurelis will respond to this, probably before the sun goes to rest."
            $ railway_event_due = event_tick + 1
    $ event_tick += 1

    jump event_checker

label clean_state_event:
    "CLEAN STATE PLACEHOLDER"
    $ event_tick += 1
    $current_day += 1

    jump event_checker

label coalition_event:
    "COALITION PLACEHOLDER"
    $ event_tick += 1
    $current_day += 1

    jump event_checker

label event_checker:
    if railway_event_due != 0:
        if event_tick >= railway_event_due:
            if railway_approach == "external":
                jump railway_external_audit_event
            elif railway_approach == "contract":
                jump railway_contract_checks_event
            else:
                jump railway_nuke_event
        else:
            jump office




    jump office

label office:
    "PRIME MINISTER'S OFFICE"
    advisor "Welcome back Prime Minister."
    call screen dashboard
    if not railway_attention or not clean_state_attention or not coalition_attention:
        advisor "There are still matters that require our attention."

        menu:
            advisor "What should we focus on next?"

            "East-West High-Speed Railway" if not railway_attention:
                $ railway_attention = True
                jump railway_event
        
            "Clean State Act" if not clean_state_attention:
                $ clean_state_attention = True
                jump clean_state_event
        
            "Coalition Meeting" if not coalition_attention:
                $ coalition_attention = True
                jump coalition_event         
    elif railway_event_due != 0 or clean_state_event_due != 0 or coalition_event_due != 0:
        advisor "The orders we have set in motion are still underway."
        advisor "Would you like a cup of tea? Maybe coffee?"
        jump day_skipper
    elif railway_event_due == 0 and clean_state_event_due == 0 and coalition_event_due == 0:
        jump constitutional_court_case

label railway_external_audit_event:
    "PLACEHOLDER"
    $ railway_event_due = 0
    jump event_checker

label railway_contract_checks_event:
    "PLACEHOLDER"
    $ railway_event_due = 0
    jump event_checker

label railway_nuke_event:
    "PLACEHOLDER"
    $ railway_event_due = 0
    jump event_checker


label day_skipper:
    $ next_event = 999
    if railway_event_due != 0:
        if railway_event_due < next_event:
            $ next_event = railway_event_due
    
    if clean_state_event_due != 0:
        if clean_state_event_due < next_event:
            $ next_event = clean_state_event_due
    
    if coalition_event_due != 0:
        if coalition_event_due < next_event:
            $ next_event = coalition_event_due

    $ days_skipped = next_event - event_tick
    $ current_day += days_skipped
    $ event_tick = next_event

    if days_skipped == 1:
        "THE NEXT DAY"
    else:
        "[days_skipped] DAYS LATER"


    jump event_checker

label constitutional_court_case:
    "This is where the current version of the game ends."

    "Vardén is still in a very early stage of development. I plan to continue expanding the game whenever I have the time and motivation to do so."

    "If you’ve made it this far, thank you for playing."

    "Any feedback, criticism, suggestions, or bug reports are more than welcome."

