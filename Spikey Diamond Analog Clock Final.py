#Importering af relevante biblioteker
#pygame, brugt til spilskabelse og multimedia, figurer/billeder/reagere på brugerens actions 
import pygame
#math, muliggøre matematiske funktioner
    #f.eks. sin og cos, særlig relevant i denne opgave.
import math
#time, muliggøre programmet til at køre med real-time.
    #meget releavant, når opgaven kræver et analogt ur
import time

#'Initialize pygame', fungere som et 'set up', af biblioteket.
    #Hvilket pygame bib kræver i modsætning til time/math
pygame.init()

#skærms dimensioner i variabler, width og height.
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spikey Diamond Analog Clock")

#definering af farver 
    #farverne repræsenterer i tuples (), (faste parametre), defineres i RGB farve.
background_color = (0, 0, 0)  #sort baggrund
clock_color = (255, 255, 255)  #hvidt ur
secound_hand_color = (160, 160, 160)  #sølv Ur
sapphire_blue = (139, 184, 255)  #saphir blå for kvartaltimerne, skal visualisere diamandter
white_marker = (255, 255, 255)  #hvid for de resterende timer

#urets placering, skærms width og height delt i 2, vil være origon
center = (width // 2, height // 2)
#urets radius, målt i pixels
clock_radius = 150

#design af urets diamanter inspiret timevisere
#deres form og placering er defineret i draw_diamond_markers()
def draw_diamond_markers():
    #loop der kører 12 gange, fra 0-11
    for hour in range(12):
        #360/12 = 30 grader pr. time.
            #graderne -> radianer. 30 grader = 0.5236 radianer = pi/6 = 0.5236*time = time*30 grader
        angle = math.pi / 6 * hour
        
        #trigonomitri, sin og cos, beregne position af timevisere baseret på urets midte
            #koordinater [], dimandt ydrepunkter
            #sin 'horisontal x-aksen' og cos 'vertikal y-aksen' , position baseret på vinklen 
            #clock_radius * 1.3, placerer ydre punkterne en smule udenfor uret, 1.3, 130% i dette tilfælde.
            #clock_radius * 1.3 er for at skabe 'diamandt'-formen, for at strække i figuren.
        outer_x = center[0] + clock_radius * 1.3 * math.sin(angle)
        outer_y = center[1] - clock_radius * 1.3 * math.cos(angle)
        
        #koordinat [], diamandt inderste punkter, tættest på uret midte
            #lignedne beregning, * 0.95, 95%, for at holde diamandten indenfor uret 
        inner_x = center[0] + clock_radius * 0.95 * math.sin(angle)
        inner_y = center[1] - clock_radius * 0.95 * math.cos(angle)

        
        
        #diamandterne kræver 3 punkter
        
        #ydre punkt af diamand
        point1 = (outer_x, outer_y)
        #x og y, modificeres for at holde diamandten indenfor uret
        
        #cos 'horisontal x-aksen' og sin 'vertikal y-aksen'
        #10*math.sin, for flytte dette punkt 10 pixels til venstre. 
        #fra inner punktet, venstre fordi 10 fratrækkes
        point2 = (inner_x-10*math.cos(angle),inner_y-10*math.sin(angle))
        
        #samme pricipper, 10 pixels til højre ved at plus med 10
        point3 = (inner_x + 10 * math.cos(angle), inner_y + 10 * math.sin(angle))

        #farven skal være saffire_blue for kl. 12, 3, 6, 9, ellers hvid
        if hour in [0, 3, 6, 9]:  # 12, 3, 6, 9, kvartaltimerne. 0 er 12.
            color=sapphire_blue
        else:
            color = white_marker
            #Tegning af diamandten ud fra udregnede koordinater og farve
            #definere hvilken farve, gældende hvornår, if og else.
        pygame.draw.polygon(screen, color, [point1, point2, point3])

        #denne funktion kører i en loop, kører 12 gange, fordi, in range(12), 0-11


#definere uret ud fra koordinater og farve
    #8, tykkelsen, eller, "width"
def draw_clock():
    #Tegning af uret ud fra koordinater og farve
    pygame.draw.circle(screen, clock_color, center, clock_radius, 8)

#funktionen definere urets visere
    # pygame.draw.aaline(screen, color, start_point, end_point, blend)
    #skærm, farve, start_point (center), end_point (x,y), blend
        #'blend' kommer af pygame.draw.aaline, og er en 'optional' parameter.
def draw_hand(length, angle, color):
    x = center[0] + length * math.sin(angle)
    y = center[1] - length * math.cos(angle)
    pygame.draw.aaline(screen, color, center, (x, y))


#kører så længe programmet er i gang
#running = True, kalder programmet til at fortsætte
    #(Indtil værdien bliver ændret til False) 
running = True

#Hovedløkken i programmet
#Kør denne kode så længe running = True
#Løkken vil stoppe når variablen, 'running', angives til False
    #(Det sker længere nede i koden)
while running:
    #Skærmen fyldes med sort baggrund.
    screen.fill(background_color)

    #Kaldes for at tegne selve klokken
    #funktionen defineret længere oppe i programmet
    draw_clock()

    #Kaldes for at tegne diamandterne
    #funktionen defineret længere oppe i programmet
    #parametre udregnet i indrykning
    draw_diamond_markers()

    #henter den aktuelle tid
    #tm_hour, tm_min, tm_sec 
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    #modulus 12, %12, for at konvertere timerne til et analogt ur
        #modulus betyder resten efter division 
    #tm_hour, regner med 24 timer på et døgn 
        #hvis klokken er 12.00, vil den være 00.00,
        #hvis klokken er 13:00, vil den være 01:00, 13%12 = 1
        #hvis klokken er 19.00, vil den være 07.00, 19%12 = 7
        #hvis klokken er 23.00, vil den være 11.00, osv.
    
    #minutter og sekunder behøver ikke at konverteres 
        #Analogt minutter/sekunder = digitale minutter/sekunder
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    #beregning af visernes vinkler 
    
    #vinklen for sekundviseren beregnes ved at opdele 360 garder / 60 sekunder.
        #6 garder pr. sekund, tilsvarende, pi/30 (radianer)
    second_angle = math.pi / 30 * seconds  # 360/60 = 6 degrees per second (pi/30 radians)
    
    #Vinklen for minutviseren beregne ligeledes
    #dog, bevæger minutviseren sig ikke hvert sekundt, men hvert minut
    #der går 60 sekund til et minut 
    #derfor kan man tilføje 60 i slutningen af koden 
    #minutviseren baseret på sekundviseren, for glidende bevægelse.
    #bevæger sig en lille smule for hvert sekundt
    minute_angle = math.pi / 30 * minutes + second_angle / 60 
    
    #Vinklen for timeviseren, igen samme principper 
    #minutviseren baseret på minutviseren, for glidende bevægelse.
    #den bevæger lig en lille smule for hvert minut 
    #slutelig / 12, for et analogt ur. 
    hour_angle = math.pi / 6 * hours + minute_angle / 12 
    
    
    #Tegn timer, minutter og sekundvisere
        #draw_hand bruges til alle visere
        #der gives forskellige parametre
    
    #clock_radius * 0,5 af radius, for at forkorte timeviseren
    #hour_angle, vinklen for timeviseren, som defineret tidligere 
    #clock_color farven er defineret tidligere
    #1 er bredden af viseren 
        #'draw_hand' er baseret på draw aaline, som defineret tidligere
            #Draw aaline, understøtter ikke tykkelse, den er 1 pixel
    draw_hand(clock_radius * 0.5, hour_angle, (clock_color))
    
    #clock_radius * 0,75 af radius, minutviseren længde er 75% af radius 
    #minute_angle, vinklen for minutviseren, som defineret tidligere 
    #clock_color farven er defineret tidligere
    draw_hand(clock_radius * 0.75, minute_angle, (clock_color))
    
    #clock_radius * 0,8 af radius, sekundviserem er 80% af radius
    #second_angle, vinklen for sekundviseren, som defineret tidligere 
    #clock_color farven er defineret tidligere
    draw_hand(clock_radius * 0.9, second_angle, (secound_hand_color))

    #denne kode sikre at alle tegninger faktisk bliver vist på skærmen 
        #i Pygame vises al grafik midlertidligt i en buffer 
            #indtil man 'flipper' display (opdatere)
    pygame.display.flip()

    #denne linje tillader alle 'events' som brugeren udfører 
        #eks lukke vinduet/muse-klik/tasteturtast osv.
            #i denne kode kan man lukke vinduet
    for event in pygame.event.get():
        
        #gør det muligt for brugeren at bruge pygame.QUIT
            #brugeren lukke via krydset i hjøre hjørne
        if event.type == pygame.QUIT:
            
            #hvis brugeren vælger at afslutte programmet via krydset
                #vil det stoppe 'while running'
                    #programmet vil stoppe da løkken brydes
            running = False

    #begrænser hvor hurtig løkken kører. 
        #tick(60) at skærmen maksimalt opdateres 60/sekund
        #uden en grænsen vil programmet kører meget hurtigt 
            #ikke til at kontrollere 
                #(60) typisk FPS for spil/grafik 
                    #giver en glidende bevægelse
    pygame.time.Clock().tick(60)

#Når 'running' er kaldt til False
#sikre denne kode at programmet faktisk lukker 
pygame.quit()



