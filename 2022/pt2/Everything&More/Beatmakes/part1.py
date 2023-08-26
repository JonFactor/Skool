import pygame
from pygame import mixer

pygame.init()

width=1400
height=800

black=(0, 0, 0)
white=(225, 225, 225)
lightGray=(170,170,170)
gray=(128, 128, 128)
green=(0,225,0)
gold=(212, 175, 55)
blue=(0,225,225)
darkGray=(69,69,69)

screen=pygame.display.set_mode([width, height])
pygame.display.set_caption('Beat Maker')
labelFont=pygame.font.Font('week_11\Beatmakes\OpenSans-Bold.ttf', 32)
mediumFont=pygame.font.Font('week_11\Beatmakes\OpenSans-Bold.ttf', 24)

index=100
fps=60
timer=pygame.time.Clock()
instruments=6
beats=8
boxes=[]
clicked=[[-1 for _ in range(beats)] for _ in range(instruments)]
bpm=240
playing=True

activeLength=0
activeBeat=1
beatChanged=True

saveMenu=False
loadMenu=False

savedBeats=[]
file=open('week_11\Beatmakes\savedBeats.txt','r')
for line in file:
    savedBeats.append(line)
beatName = ''
typing = False

#sounds
hiHat = mixer.Sound('week_11\Beatmakes\sounds\hi hat.WAV')
snare = mixer.Sound('week_11\Beatmakes\sounds\snare.WAV')
kick = mixer.Sound('week_11\Beatmakes\sounds\kick.WAV')
crash = mixer.Sound('week_11\Beatmakes\sounds\crash.wav')
clap = mixer.Sound('week_11\Beatmakes\sounds\clap.wav')
tom = mixer.Sound('week_11\Beatmakes\sounds\\tom.WAV')
pygame.mixer.set_num_channels(instruments*3)

def playNotes():
    for i in range(len(clicked)):
        if clicked[i][activeBeat]==1:
            if i==0:
                hiHat.play()
            if i==1:
                snare.play()
            if i==2:
                kick.play()
            if i==3:
                crash.play()
            if i==4:
                clap.play()
            if i==5:
                tom.play()


def draw_grid(clicks, beat):
    leftBox=pygame.draw.rect(screen, gray, [0, 0, 200, height -200 ], 5)
    bottomBox=pygame.draw.rect(screen, gray, [0, height - 200, width, 200], 5)
    boxes=[]
    colors=[gray, white, gray]
    hiHatText=labelFont.render('Hi Hat', True, white)
    screen.blit(hiHatText, (30, 30))
    snareText=labelFont.render('Snare', True, white)
    screen.blit(snareText, (30, 130))
    kickText=labelFont.render('Bass Drum', True, white)
    screen.blit(kickText, (30, 230))
    crashText=labelFont.render('Crash', True, white)
    screen.blit(crashText, (30, 330))
    clapText=labelFont.render('Clap', True, white)
    screen.blit(clapText, (30, 430))
    tomText=labelFont.render('Floor Tom', True, white)
    screen.blit(tomText, (30, 530))

    for i in range(instruments):
        pygame.draw.line(screen, gray, (0, (i* 100) + 100), (200, (i* 100) + 100),5 )

    for i in range(beats):
        for j in range(instruments):
            if clicks[j][i]==-1:
                color=gray
            else:
                color=green
            
            rect=pygame.draw.rect(screen, color, [i *((width-200) // beats) + 205, (j * 100) + 5, ((width - 200) // beats) - 10, ((height - 200) // instruments) - 10],0,3)

            pygame.draw.rect(screen, gold, [i *((width-200) // beats) + 200, (j * 100), ((width - 200) // beats), ((height - 200)/instruments)],5,5)

            pygame.draw.rect(screen, black, [i *((width-200) // beats) + 200, (j * 100), ((width - 200) // beats), ((height - 200)/instruments)],2,5)

            boxes.append((rect, (i, j)))
        active = pygame.draw.rect(screen,blue,[beat*((width-200)//beats)+200,0,((width-200)//beats),instruments*100], 5, 3)
    return boxes


def drawSaveMenu(beatName, typing):
    pygame.draw.rect(screen,black,[0,0,width,height])
    menuTxt=labelFont.render('Save Menu: Enter a name for Current Beat', True, white)
    savingBtn=pygame.draw.rect(screen,gray,[width//2-200,height*.75,400,100],0,5)
    savingTxt=labelFont.render('Save Beat',True,white)
    screen.blit(savingTxt,(width//2-70,height*.75+30))
    screen.blit(menuTxt,(400,40))
    exitButton=pygame.draw.rect(screen,gray, [width-200, height-100, 180, 90],0,5)
    exitTxt=labelFont.render('Close', True, white)
    screen.blit(exitTxt,(width-160,height-70))
    if typing:
        pygame.draw.rect(screen,darkGray,[400,200,600,200],0,5)
    entryRect=pygame.draw.rect(screen,gray,[400,200,600,200],5,5)
    entryTxt=labelFont.render(f'{beatName}',True,white)
    screen.blit(entryTxt,(430,250))
    return exitButton,savingBtn,entryRect

def drawLoadMenu(index):
    loadedClicked=[]
    loadedBeats=0
    loadedBpm=0
    pygame.draw.rect(screen,black,[0,0,width,height])
    menuTxt=labelFont.render('Load Menu: Select a Beat to load', True, white)
    loadingBtn=pygame.draw.rect(screen,gray,[width//2-200,height*.87,400,100],0,5)
    loadingTxt=labelFont.render('Load Beat',True,white)
    screen.blit(loadingTxt,(width//2-70,height*.87+30))
    deleteBtn=pygame.draw.rect(screen,gray,[(width//2)-500,height*.87,200,100],0,5)
    deleteTxt=labelFont.render('Delete Beat',True,white)
    screen.blit(deleteTxt,((width//2)-485,height*.87+10))
    screen.blit(menuTxt,(400,40))
    exitButton=pygame.draw.rect(screen,gray, [width-200, height-100, 180, 90],0,5)
    exitTxt=labelFont.render('Close', True, white)
    screen.blit(exitTxt,(width-160,height-70))
    loadedRectangle=pygame.draw.rect(screen,gray,[190,90,1000,600],5,5)
    if 0<=index<len(savedBeats):
        pygame.draw.rect(screen,lightGray,[190,100+index*50,1000,50])
    for beat in range(len(savedBeats)):
        if beat<10:
            beatClicked = []
            rowTxt=mediumFont.render(f'{beat+1}',True,white)
            screen.blit(rowTxt,(200,100+beat*50))
            print(beat)
            nameIndexStart=savedBeats[beat].index('name: ')+6
            nameIndexEnd=savedBeats[beat].index(', beats:')
            nameTxt=mediumFont.render(savedBeats[beat][nameIndexStart:nameIndexEnd],True,white)
            screen.blit(nameTxt,(240,100+beat*50))
        if 0<=index<len(savedBeats) and beat==index:
            beatIndexEnd=savedBeats[beat].index(', bpm:')
            loadedBeats=int(savedBeats[beat][nameIndexEnd+8:beatIndexEnd])
            bpmIndexEnd=savedBeats[beat].index(', selected:')
            loadedBpm=int(savedBeats[beat][beatIndexEnd+6:bpmIndexEnd])
            loadedClicksString = savedBeats[beat][bpmIndexEnd + 14: -3]
            loaded_clicks_rows = list(loadedClicksString.split("], ["))
            for row in range(len(loaded_clicks_rows)):
                loaded_clicks_row = (loaded_clicks_rows[row].split(', '))
                for item in range(len(loaded_clicks_row)):
                    if loaded_clicks_row[item] == '1' or loaded_clicks_row[item] == '-1':
                        loaded_clicks_row[item] = int(loaded_clicks_row[item])
                beatClicked.append(loaded_clicks_row)
                loadedClicked=beatClicked
    loadedInfo=[loadedBeats,loadedBpm,loadedClicked]
    return exitButton,loadingBtn,deleteBtn,loadedRectangle,loadedInfo



run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    boxes=draw_grid(clicked, activeBeat)
    # low menu button
    playPause=pygame.draw.rect(screen,gray,[50,height-150,200,100],0,5)
    playText=labelFont.render('Play/Pause', True, white)
    screen.blit(playText,(70,height-130))
    if playing:
        playtext2=mediumFont.render('Playing',True,darkGray)
    else:
        playtext2=mediumFont.render('Paused',True,darkGray)
    screen.blit(playtext2, (70,height-100))
    #bpm
    bpmRect=pygame.draw.rect(screen, gray, [300,height-1500,200,100],5,5)
    bpmText=mediumFont.render('Beats Per Minute',True,white)
    screen.blit(bpmText,(308,height-130))
    bpmtext2=labelFont.render(f'BPM:{bpm}',True,white)
    screen.blit(bpmtext2,(370, height-100))
    bpmAddRect=pygame.draw.rect(screen,gray,[510,height-150,48,48],0,5)
    bpmSubrect=pygame.draw.rect(screen,gray,[510,height-100,48,48],0,5)
    addText=mediumFont.render('+5',True,white)
    subText=mediumFont.render('-5',True,white)
    screen.blit(addText,(520,height-140))
    screen.blit(addText,(520,height-90))
    #beats
    beatsRect=pygame.draw.rect(screen, gray, [300,height-1500,200,100],5,5)
    beatsText=mediumFont.render('Beats in Loop',True,white)
    screen.blit(beatsText,(618,height-130))
    beatstext2=labelFont.render(f'{beats}',True,white)
    screen.blit(beatstext2,(670, height-100))
    beatsAddRect=pygame.draw.rect(screen,gray,[810,height-150,48,48],0,5)
    beatsSubrect=pygame.draw.rect(screen,gray,[810,height-100,48,48],0,5)
    addText2=mediumFont.render('+1',True,white)
    subText2=mediumFont.render('-1',True,white)
    screen.blit(addText2,(820,height-140))
    screen.blit(addText2,(820,height-90))
    #save and load
    saveButton=pygame.draw.rect(screen,gray,[900,height-150,200,48],0,5)
    saveText = labelFont.render('Save Beat',True,white)
    screen.blit(saveText,(920,height-150))
    loadButton=pygame.draw.rect(screen,gray,[900,height-100,200,48],0,5)
    loadText = labelFont.render('Load Beat',True,white)
    screen.blit(loadText,(920,height-100))

    #clear board
    clearButton=pygame.draw.rect(screen,gray,[1150,height-150,200,100],0,5)
    ClearText = labelFont.render('Clear Board',True,white)
    screen.blit(ClearText,(1160,height-130))

    if saveMenu:
        exitButton, savingBtn, entryRectangle = drawSaveMenu(beatName, typing)
    if loadMenu:
        exitButton,loadingBtn,deleteBtn,loadedRectangle, loadedInfo = drawLoadMenu(index)

    if beatChanged:
        playNotes()
        beatChanged = False

    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN and not saveMenu and not loadMenu:
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos):
                    coords=boxes[i][1]
                    clicked[coords[1]][coords[0]]*=-1
        if event.type==pygame.MOUSEBUTTONUP and not saveMenu and not loadMenu:
            if playPause.collidepoint(event.pos):
                if playing:
                    playing=False
                elif not playing:
                    playing=True
            if bpmAddRect.collidepoint(event.pos):
                bpm+=5
            elif bpmSubrect.collidepoint(event.pos):
                bpm-=5
            if beatsAddRect.collidepoint(event.pos):
                beats+=1
                for i in range(len(clicked)):
                    clicked[i].append(-1)
            elif beatsSubrect.collidepoint(event.pos):
                beats-=1
                for i in range(len(clicked)):
                    clicked[i].pop(-1)
            elif clearButton.collidepoint(event.pos):
                clicked=[[-1 for _ in range(beats)] for _ in range(instruments)]
            elif saveButton.collidepoint(event.pos):
                saveMenu=True
            elif loadButton.collidepoint(event.pos):
                loadMenu=True
        elif event.type==pygame.MOUSEBUTTONUP:
            if exitButton.collidepoint(event.pos):
                saveMenu=False
                loadMenu=False
                playing=True
                beatName=''
                typing=False
            if loadMenu:
                if loadedRectangle.collidepoint(event.pos):
                    index=(event.pos[1]-100)//50
                if deleteBtn.collidepoint(event.pos):
                    if 0<=index<len(savedBeats):
                        savedBeats.pop(index)
                if loadingBtn.collidepoint(event.pos):
                    if 0<=index<len(savedBeats):
                        beats=loadedInfo[0]
                        bpm=loadedInfo[1]
                        clicked=loadedInfo[2]
                        index=100
                        loadMenu=False
            if saveMenu:
                if entryRectangle.collidepoint(event.pos):
                    if typing:
                        typing=False
                    elif not typing:
                        typing=True
                if savingBtn.collidepoint(event.pos):
                    file=open('week_11\Beatmakes\savedBeats.txt','w')
                    savedBeats.append(f'\nname: {beatName}, beats: {beats}, bpm: {bpm}, selected: {clicked}')
                    for i in range(len(savedBeats)):
                        file.write(str(savedBeats[i]))
                    file.close()
                    saveMenu = False
                    typing = False
                    Beatname = ''
        if event.type == pygame.TEXTINPUT and typing:
            beatName += event.text
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and len(beatName) > 0 and typing:
                beatName=beatName[:-1]

    beatLength=fps*60 // bpm

    if playing:
        if activeLength<beatLength:
            activeLength+=1
        else:
            activeLength=0
            if activeBeat<beats-1:
                activeBeat+=1
                beatChanged=True
            else:
                activeBeat=0
                beatChanged=True


    pygame.display.flip()
pygame.quit()
