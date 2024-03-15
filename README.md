# Whac-a-mole

<img width="200" alt="project logo" src="images/logo.png">

[![ExploraBadge](https://img.shields.io/badge/-Explora-eb5c2f)](https://mdbr.it/en/) [![Interactive](https://img.shields.io/badge/-Interactive_installation-55ca7c)](https://en.wikipedia.org/wiki/Interactive_art)

*Whac-a-mole* is a Python app that works like the classic **whac-a-mole game**, relying on a **led-button physical interface**.

- [Introduction](#introduction)
- [Development](#development)
- [Project additional infos](#infos)


## <a name="introduction"></a>Introduction
*Whac-a-mole* is part of an interactive installations network (read the paragraph [Project purpose](#purpose) for more information). Before engaging with the installations users are given a barcode to start them and to store their scores (and other non-sensible data).

*Whac-a-mole* is designed to test user reflexes and controls button leds switch and check the buttons pression.
Led buttons in grid are turned on randomically  and must be pressed by the player.
The app **checks and saves how many buttons have been correctly pressed in a time range** (default is 30”).


### How it works
1. User starts application making it read the barcode
2. Countdown starts
3. Led buttons randomically turns on and user press them
4. Countdown reaches 0
5. Game is over

![How it works](images/flow.png)


## <a name="development"></a>Development
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 


## <a name="infos"></a>Project additional infos

### <a name="purpose"></a>Project purpose
*Whac-a-mole* is designed as an installation part of the PARI a thematic expo focused on gender stereotipes and presented as a network of installations. All the installations features a challenge to the user and a final score. 
Some of the interactive installations are inspired to stereotiped gender task (like changing a toddler’s diaper), other like Whac-a-mole are oriented to emphasize the neutrality of some skills, like the reflexes.
Users, before starting the thematic expo are given a barcode associated with a digital identity where are stored some non-sensible data like: gender, age range, nickname and the scores. Those data were used to have a glimpse of what cultural background kids have, based on their gender.

![Project image](images/example.png)

### Related Explora's project

- [MDBR heart rate]()
- [Economiamo - Car]()





