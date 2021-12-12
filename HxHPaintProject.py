#Paint Program
from pygame import *
from math import *
from random import *
from tkinter import filedialog
from tkinter import *
from random import *

init() #initialize for music
font.init() #initializes font

root=Tk() #Required for opening and saving syntax
root.withdraw() #hides the extra window

width,height=1294,710
screen=display.set_mode((width,height))
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)
ORANGE=(255,165,0)
PURPLE=(127,0,255)

cooperBlack=font.SysFont("Cooper Black",30) #identifies the font 'Cooper Black'
comicSans=font.SysFont("Comic Sans MS",15) #identifies the font 'comic sans ms'

background=image.load("images/hxhbackground.jpg") #loads background image 
screen.blit(background,(0,0)) #outputs background

pencilRect=Rect(10,50,60,60)#Pencil box
eraserRect=Rect(85,50,60,60)#Eraser box
brushRect=Rect(160,50,60,60)#Brush box
rectShapeRect=Rect(235,50,60,60)#Box for drawing rectangles

circleShapeRect=Rect(310,50,60,60)#Box for drawing circles

randomBarRect=Rect(385,50,60,60)##Box for Random Bars box (Random bars are outputted, forming a rectangle)

fillRect=Rect(460,50,60,60)#Color fill box

stickerRect=Rect(1038,10,250,360)
page1Rect=Rect(1043,345,40,20) #Box for page 1 of stickers
page2Rect=Rect(1093,345,40,20) #Box for page 2 of stickers
page3Rect=Rect(1143,345,40,20) #Box for page 3 of stickers
page4Rect=Rect(1193,345,40,20) #Box for page 4 of stickers

stickerPic=cooperBlack.render("Click",True,BLACK) #Loads the text with the font chosen
stickerPic2=cooperBlack.render("the page #s for",True,BLACK) #loads the text 
stickerPic3=cooperBlack.render("stickers",True,BLACK)  #loads th text
screen.blit(stickerPic,(1125,100)) #Caption for stickers box
screen.blit(stickerPic2,(1050,150)) #Caption for stickers box
screen.blit(stickerPic3,(1100,200)) #Caption for stickers box

musicRect=Rect(620,600,410,105) #Music player box
song1Rect=Rect(650,610,50,50) #Song 1 box
song2Rect=Rect(720,610,50,50) #Song 2 box
song3Rect=Rect(790,610,50,50) #Song 3 box
song4Rect=Rect(860,610,50,50) #Song 4 box
song5Rect=Rect(930,610,50,50) #Song 5 box
pauseRect=Rect(790,670,50,40) #Pause button
playRect=Rect(720,670,50,40)  #Play button
inc=0.5 # (volume) - variable for increasing/decreasing the volume for music
lowVolRect=Rect(860,670,50,40) #Box for lowering the volume of the music playing
highVolRect=Rect(930,670,50,40) #Box for increasing the volume of the music playing
rewindRect=Rect(650,670,50,40) #Box for rewinding the music currently playing to the beginning

backgroundRect=Rect(640,460,360,130) #Box for choosing backgrounds
wallpaper1Rect=Rect(670,510,60,60) #Box for wallpaper 1
wallpaper2Rect=Rect(750,510,60,60) #Box for wallpaper 2
wallpaper3Rect=Rect(830,510,60,60) #Box for wallpaper 3
wallpaper4Rect=Rect(910,510,60,60) #Box for wallpaper 4

wallpaper=0 #Wallpaper is at zero default, unless a wallpaper is chosen from the background boxes

paletteRect=Rect(1038,450,256,256)# Palette box
showColorRect=Rect(1038,375,75,75) #box that shows color

noteBox=Rect(1120,375,160,70) #Box for notes on how to do unfilled and filled shapes

openRect=Rect(968,50,60,60) #Opening box for images
saveRect=Rect(888,50,60,60) #Saving box for saving work on paint

redoRect=Rect(808,50,60,60) #Box to redo work
undoRect=Rect(728,50,60,60) #Box to undo work

multiLineRect=Rect(535,50,60,60) #Box for multiLine (Draw multiple lines that come from all directions and they all meet at where the mouse is at)

lineRect=Rect(610,50,60,60) #Box to draw lines

multiBrushRect=Rect(968,125,60,60) #Box for multiple color brush box (Random colors are painted by the brush)
calligraphyRect=Rect(888,125,60,60) #Box for using calligraphy tool

running=True #It's always running unless running is false
tool="no tool" #There's no tool being used automatically when the program starts
page=0 #Page number for stickers is automatically 0
sticker=0 #Sticker automatically is at zero and is always zero when any tool is used except using stickers

col=BLACK #default color is BLACK
omx,omy=0,0 #Old mouse x-coord and y-coord default is zero

sz=5 #Size of anything starts at default size 5
sx,sy=0,0 #Size of x-coord and y-coord default at zero

canvasRect=Rect(10,150,600,550) #Coordinates and size for canvas
draw.rect(screen,WHITE,canvasRect)#Canvas is drawn

click=False #Default for click is false unless it equals true when supposed to
screenCap=screen.subsurface(canvasRect).copy() #takes a screenshot of that canvas

undoList=[screen.subsurface(canvasRect).copy()]
redoList=[]

draw.rect(screen,BLACK,(475,10,410,35)) #box around title    
title=cooperBlack.render("Hunter x Hunter Paint",True,WHITE) #Title of paint is inputted 
screen.blit(title,(500,10)) #Outputs the title of the paint program


def pencilTool(): #Function for the pencil box
    global tool #makes local variable 'tool' into global variable so it can be used in the function and throughout the program
    global page #also makes the local variable 'page' into a global variable
    global sticker #local to global
    pencil=image.load("images/pencil.jpg") #loads the pencil JPG image of pencil
    screen.blit(pencil,(10,50)) #Outputs the image to the coordinates that were input
    draw.rect(screen,BLACK,pencilRect,5) #draws a black outlined box for the pencil tool
    if pencilRect.collidepoint(mx,my): #if the mouse collides with the pencil tool box
        draw.rect(screen,RED,pencilRect,5) #the pencil tool box is outlined red
    if mb[0]==1 and pencilRect.collidepoint(mx,my):#checking to see if mouse is colliding with pencil box
        tool="pencil" #tool equals pencil 
        page=0 #page equals zero since this only becomes another number for the sticker pages
        sticker=0 #sticker still equals zero since there is no sticker being used right now
        
def eraserTool(): #Function for the eraser box
    global tool #makes local variable 'tool' into global variable
    global page #local - global
    global sticker #local - global
    eraser=image.load("images/eraser.png") #Loads the eraser PNG image of the eraser tool
    screen.blit(eraser,(85,50)) #Outputs the image to the coordinates of the eraser box
    draw.rect(screen,BLACK,eraserRect,5) #Draws a box for the eraser tool
    if eraserRect.collidepoint(mx,my): #If the mouse collides with the eraser box...
        draw.rect(screen,RED,eraserRect,5) #Eraser tool box is outlined red
    if mb[0]==1 and eraserRect.collidepoint(mx,my): #If the mouse is clicked on the eraser tool box
        tool="eraser" #Tool equals eraser
        page=0 #page equals zero since this only becomes another number for the sticker pages
        sticker=0 #sticker still equals zero since there is no sticker being used right now

    
def brushTool(): #Function for the brush box
    global tool #makes local variable 'tool' into global variable
    global page #local - variable
    global sticker #local - variable
    paintbrush=image.load("images/paintbrush.png") #Loads paint brush PNG image of the paintbrush tool box
    screen.blit(paintbrush,(160,50)) #Outputs image of paint brush to the coordinates of the tool box
    draw.rect(screen,BLACK,brushRect,5) #Draw a box for the paintbrush tool
    if brushRect.collidepoint(mx,my): #If mouse collides with the paint brush box
        draw.rect(screen,RED,brushRect,2) #Paint brush tool brush is outlined red
    if mb[0]==1 and brushRect.collidepoint(mx,my): #If mouse is clicked on paintbrush tool box
        tool="brush" #tool equals brush
        page=0 #page equals zero since this only becomes another number for the sticker pages
        sticker=0 #sticker still equals zero since there is no sticker being used right now

        
def rectTool(): #Function for drawing rectangles
    global tool #local - global variable 
    global page #local - global
    global sticker #local - global

    draw.rect(screen,RED,noteBox,5)
    draw.rect(screen,BLACK,noteBox) #Draws box for the extra notes on program about filled/unfilled shapes
    notes1=comicSans.render("Left click - Filled",True,WHITE) #Loads the text with the font chosen
    notes2=comicSans.render("Right click - Unfilled",True,WHITE) #Loads the text with the font chosen

    screen.blit(notes1,(1130,380)) #Outputs text for extra notes
    screen.blit(notes2,(1130,400)) #Outputs text for extra notes pt2
    
    rectangle=image.load("images/rectangle.jpg") #Loads rectangle JPG image for rectangle tool box
    screen.blit(rectangle,(235,50)) #Ouputs image of rectangle into coordinates of rectangle tool box
    draw.rect(screen,BLACK,rectShapeRect,5) #Draws a box for the rectangle tool box

    if rectShapeRect.collidepoint(mx,my): #If mouse collides with rectangle tool box
        draw.rect(screen,RED,rectShapeRect,2) #Rectangle tool box is outlined red
    if mb[0]==1 and rectShapeRect.collidepoint(mx,my): #If mouse is clicked on rectangle tool box
        tool="rectangle" #tool equals rectangle
        page=0 #page equals zero since this only becomes another number for the sticker pages
        sticker=0 #sticker still equals zero since there is no sticker being used right now

def circleTool(): #Function for drawing circles
    global tool #local - global
    global page #local - global 
    global sticker #local - global
    circle=image.load("images/circle.jpg") #Loads circle JPG image for circle tool box
    screen.blit(circle,(310,50)) #Outputs image of circle into coordinates of circle tool box
    draw.rect(screen,BLACK,circleShapeRect,5) #Draws a box for the circle tool box
    if circleShapeRect.collidepoint(mx,my): #If mouse collides with circle tool box
        draw.rect(screen,RED,circleShapeRect,2) #Circle tool box is outlined red
    if mb[0]==1 and circleShapeRect.collidepoint(mx,my): #If mouse is clicked on circle tool box..
        tool="circle" #tool equals circle
        page=0 #page equals zero since this only becomes another number for the sticker pages
        sticker=0 #sticker still equals zero since there is no sticker being used right now

        
def randomBarsTool(): #function for drawing random bars (lines) to form a rectangle
    global tool #local - global
    global page #local - global
    global sticker #local - global
    randomBar=image.load("images/randomBar.png") #Loads image for random bars tool
    screen.blit(randomBar,(385,50)) #Outputs image onto box for the tool
    draw.rect(screen,BLACK,randomBarRect,5) #Draw rectangle for the tool box
    if randomBarRect.collidepoint(mx,my): #if mouse collides with tool box
        draw.rect(screen,RED,randomBarRect,2) #Box is outlined red
    if mb[0]==1 and randomBarRect.collidepoint(mx,my): #If mouse is clicked on random Bars Box
        tool="randomBar" #tool equals random bar
        page=0 #page equals zero since this only becomes another number for the sticker pages
        sticker=0 #sticker still equals zero since there is no sticker being used right now

        
def fillTool(): #Function for filling the canvas a color the user chooses
    global tool #local - global
    global page #local - global
    global sticker #local - global
    fill=image.load("images/fill.png") #Loads fill bucket PNG image for fill tool box
    screen.blit(fill,(460,50)) #Outputs image of fill bucket
    draw.rect(screen,BLACK,fillRect,5) #Draws box for fill tool box
    if fillRect.collidepoint(mx,my): #If mouse collides with fill tool box
        draw.rect(screen,RED,fillRect,2) #Box is outlined red
    if mb[0]==1 and fillRect.collidepoint(mx,my): #If mouse is clicked on fill tool box..
        tool="fill" #tool equals fill
        page=0 #page equals zero since this only becomes another number for the sticker pages
        sticker=0 #sticker still equals zero since there is no sticker being used right now
        
def palette(): #Function for palette
    background=image.load("images/palette.png") #Loads palette for choosing colors
    screen.blit(background,(1038,450)) #Outputs palette onto coordinats for where palette is supposed to be
    draw.rect(screen,col,showColorRect)# Box that shows the color of what the user is currently using
    draw.rect(screen,WHITE,showColorRect,5)
    
def stickers(): #function for stickers/stamps
    global page #local - global
    global sticker #local - global
    draw.rect(screen,BLACK,stickerRect,5) #box for the stickers
    draw.rect(screen,BLACK,page1Rect,5) #Box for page 1 of stickers
    page1=image.load("images/page1.jpg") #Image is loaded
    screen.blit(page1,page1Rect) #Outputs page 1 image
    draw.rect(screen,BLACK,page2Rect,5) #Box for page 2 of stickers
    page2=image.load("images/page2.jpg") #image is loaded
    screen.blit(page2,page2Rect) #Outputs page 2 image
    draw.rect(screen,BLACK,page3Rect,5) #Box for page 3 of stickers
    page3=image.load("images/page3.jpg") #Loads image
    screen.blit(page3,page3Rect) #Outputs page 3 image
    draw.rect(screen,BLACK,page4Rect,3) #Box for page 4 of stickers
    page4=image.load("images/page4.jpg") #Loads image
    screen.blit(page4,page4Rect) #Outputs page 4 image

    #FOR PAGE 1 OF STICKER PAGES
    if page==1: #If page 1 equals 1
        #FOR STICKER 1
        gonSticker=Rect(1150,15,160,160) #1st sticker rectangle's coordinates are taken from orginal sticker being outputted 
        if gonSticker.collidepoint(mx,my): #If mouse collides with that sticker
            page=1 #page equals 1 of the sticker pages
            sticker=1 #sticker equals 1 since that's the first sticker
            tool="no tool" #tool equals 'no tool' since theres no tool being used other than the stickers (and so a tool and sticker can't be used at the same time)

#NOTE: ALL THE REST OF THE 16 STICKERS USE THE SAME CONCEPT EXCEPT THERE
#ARE DIFFERENT STICKERS BEING USED AND DIFFERENT PAGE NUMBERS FOR THE STICKER
#PAGES, SO THERE ARE NO COMMENTS SINCE THEY'RE ALL THE SAME
#(except for the different stickers being used)
            
        #FOR STICKER 2
        killuaSticker=Rect(1030,10,160,160)
        if killuaSticker.collidepoint(mx,my):
            page=1
            sticker=2
            tool="not tool"

        #FOR STICKER 3
        kurapikaSticker=Rect(1150,175,160,160)
        if kurapikaSticker.collidepoint(mx,my):
            page=1
            sticker=3
            tool="no tool"

        #FOR STICKER 4
        leorioSticker=Rect(1075,170,90,173)
        if leorioSticker.collidepoint(mx,my):
            page=1
            sticker=4
            tool="no tool"

    #FOR PAGE 2 OF STICKER PAGES
    if page==2:
        #FOR STICKER 5
        gon2Sticker=Rect(1140,15,160,160)
        if gon2Sticker.collidepoint(mx,my):
            page=2
            sticker=5
            tool="no tool"

        #FOR STICKER 6
        killua2Sticker=Rect(1020,15,160,160)
        if killua2Sticker.collidepoint(mx,my):
            page=2
            sticker=6
            tool="no tool"

        #FOR STICKER 7
        hisokaSticker=Rect(1150,175,160,160)
        if hisokaSticker.collidepoint(mx,my):
            page=2
            sticker=7
            tool="no tool"

        #FOR STICKER 8
        illumiSticker=Rect(1040,180,160,160)
        if illumiSticker.collidepoint(mx,my):
            page=2
            sticker=8
            tool="no tool"

    #FOR PAGE 3 OF STICKER PAGES
    if page==3:
        #FOR STICKER 9
        leorio2Sticker=Rect(1150,15,160,260)
        if leorio2Sticker.collidepoint(mx,my):
            page=3
            sticker=9
            tool="no tool"

        #FOR STICKER 10
        hisoka2Sticker=Rect(1030,15,160,160)
        if hisoka2Sticker.collidepoint(mx,my):
            page=3
            sticker=10
            tool="no tool"

        #FOR STICKER 11
        chrolloSticker=Rect(1155,180,160,160)
        if chrolloSticker.collidepoint(mx,my):
            page=3
            sticker=11
            tool="no tool"

        #FOR STICKER 12
        illumi2Sticker=Rect(1035,180,160,160)
        if illumi2Sticker.collidepoint(mx,my):
            page=3
            sticker=12
            tool="no tool"

    #FOR PAGE 4 OF STICKER PAGES
    if page==4:
        #FOR STICKER 13
        killua3Sticker=Rect(1145,15,160,160)
        if killua3Sticker.collidepoint(mx,my):
            page=4
            sticker=13
            tool="no tool"

        #FOR STICKER 14
        biscuitSticker=Rect(1030,15,160,160)
        if biscuitSticker.collidepoint(mx,my):
            page=4
            sticker=14
            tool="no tool"

        #FOR STICKER 15
        hisoka3Sticker=Rect(1135,180,160,160)
        if hisoka3Sticker.collidepoint(mx,my):
            page=4
            sticker=15
            tool="no tool"

        #FOR STICKER 16
        kurapika2Sticker=Rect(1020,180,160,160)
        if kurapika2Sticker.collidepoint(mx,my):
            page=4
            sticker=16
            tool="no tool"
    

def music(): #Function for music
    global inc #local - global variable
    draw.rect(screen,WHITE,musicRect) #Music box
    draw.line(screen,BLACK,(620,670),(1030,670),4) #Line to seperate songs from buttons

    music=image.load("images/music.png") #Loads music icon image
    pause=image.load("images/pause.png") #Loads pause icon image
    play=image.load("images/play.png") #Loads play (unpause) icon image
    lowVol=image.load("images/lowVol.jpg") #Loads a lowering volume image
    highVol=image.load("images/highVol.jpg") #Loads a increasing volume image
    rewind=image.load("images/rewind.png")    
    
    screen.blit(music,song1Rect) #Outputs music icon for 1st song
    screen.blit(music,song2Rect) #Outputs music icon for 2nd song
    screen.blit(music,song3Rect) #Outputs music icon for 3rd song
    screen.blit(music,song4Rect) #Outputs music icon for 4th song
    screen.blit(music,song5Rect) #Outputs music icon for 5th song
    
    screen.blit(pause,pauseRect) #Outputs image for pause button
    screen.blit(play,playRect) #Outputs image for play (unpause) button

    screen.blit(lowVol,lowVolRect) #Ouputs image for lowering the volume button
    screen.blit(highVol,highVolRect) #Outputs image for increasing the volume button

    screen.blit(rewind,rewindRect) #Outputs image for rewinding music playing to the beginning
    
    draw.rect(screen,BLACK,musicRect,8) #Black outline for Music box
    
    draw.rect(screen,BLACK,song1Rect,4) #Box for 1st song
    draw.rect(screen,BLACK,song2Rect,4) #Box for 2nd song
    draw.rect(screen,BLACK,song3Rect,4) #Box for 3rd song
    draw.rect(screen,BLACK,song4Rect,4) #Box for 4th song
    draw.rect(screen,BLACK,song5Rect,4) #Box for 5th song
    
    draw.rect(screen,BLACK,pauseRect,4) #Box for pausing music
    draw.rect(screen,BLACK,playRect,4) #Box for playing (unpausing) music

    draw.rect(screen,BLACK,lowVolRect,4) #Box for lowering the volume of the song currently playing
    draw.rect(screen,BLACK,highVolRect,4) #Box for increasing the colume of the song currently playing

    draw.rect(screen,BLACK,rewindRect,4) #Box for rewinding the music currently playing

    mixer.music.set_volume(inc) #setting the volume at standard 0.5 (volume is between 0 and 1)
    if mb[0]==1 and song1Rect.collidepoint(mx,my): #If mouse is clicked on 1st song box
        mixer.music.load("songs/hxhOP1.mp3")  #load a MUSIC object
        mixer.music.play() #Music clicked on is played
        
    if mb[0]==1 and song2Rect.collidepoint(mx,my): #If mouse is clicked on 2nd song box
        mixer.music.load("songs/hxhED1.mp3")  #load a MUSIC object
        mixer.music.play() #Music clicked on is played
        
    if mb[0]==1 and song3Rect.collidepoint(mx,my): #If mouse is clicked on 3rd song box
        mixer.music.load("songs/hxhED2.mp3")  #load a MUSIC object
        mixer.music.play() #Music clicked on is played
        
    if mb[0]==1 and song4Rect.collidepoint(mx,my): #If mouse is clicked on 4th music box
        mixer.music.load("songs/hxhED5.mp3")  #load a MUSIC object
        mixer.music.play()#Music clicked on is played
        
    if mb[0]==1 and song5Rect.collidepoint(mx,my): #If mouse is clicked on 5th song box
        mixer.music.load("songs/hxhED6.mp3")  #load a MUSIC object
        mixer.music.play() #music clicked on is played
        
    if mb[0]==1 and pauseRect.collidepoint(mx,my): #If mouse is clicked on pause box/button
        mixer.music.pause() #Music currently playing is paused
    if mb[0]==1 and playRect.collidepoint(mx,my): #If mouse is clicked on play box/button
        mixer.music.unpause() #Music currently stopped will unpause

    if mb[0]==1 and lowVolRect.collidepoint(mx,my): #if mouse is clicked on box for lowering volume...
        inc-=0.1 #Program decreases the volume by 0.1
        mixer.music.set_volume(inc) #Sets the music playing to that volume
    if mb[0]==1 and highVolRect.collidepoint(mx,my): #If mouse is clicked on box for increasing the volume...
        inc+=0.1 #Program increases the volume by 0.1
        mixer.music.set_volume(inc) #Sets the music playing to that volume

    if mb[0]==1 and rewindRect.collidepoint(mx,my): #if mouse is clicked on rewind button
        mixer.music.rewind() #Music currently playing is rewind and set to the beginning of the song

def openSave(): #Function for open/save
    global tool #local - global
    global page #local - global
    global sticker #local - global
    draw.rect(screen,BLACK,openRect,10) #Box for opening images/files
    openPic=image.load("images/open.png") #Open icon is loaded into program
    screen.blit(openPic,openRect) #Outputs open icon into open box
    draw.rect(screen,BLACK,saveRect,10) #Box for saving images/work on program
    save=image.load("images/save.png") #Save icon is loaded
    screen.blit(save,saveRect) #Outputs save icon into save box
    if openRect.collidepoint(mx,my): #If mouse collides with open box
        draw.rect(screen,RED,openRect,5) #Open box is outlined red
    if saveRect.collidepoint(mx,my): #If mouse collides with save box
        draw.rect(screen,RED,saveRect,5) #Save box is outlined red
    if mb[0]==1 and openRect.collidepoint(mx,my): #If mouse is clicked on open box
        try: #program will try......
            fname=filedialog.askopenfilename() #this is a string that has the name of the picture
            print(fname) #Prints filename
            myPic=image.load(fname)#LOADING THE PICTURE SELECTED BY THE USER
            screen.blit(myPic,canvasRect) #Outputs picture that was selected by user
        except: #Except if a problem occurs (so it doesn't crash
            print("loading error...") #Prints loading error
        page=0 #Page equals 0 
        sticker=0 #Sticker equals zero because its not being used
    if mb[0]==1 and saveRect.collidepoint(mx,my): #If mouse is clicked on save box
        try: #Program will try......
            fname=filedialog.asksaveasfilename(defaultextension=".png") #user names file and program makes the file a 'png'
            image.save(screen.subsurface(canvasRect).copy(),fname) #saves canvas
        except: #If problem occurs..... (so program doesn't crash)
            print("Saving error....") #Prints that theres a saving error

def backgrounds(): #Function for changing the cavas's backgrounds
    global wallpaper #wallpaper become a global variable
    
    draw.rect(screen,WHITE,backgroundRect) # White box for wallpapers drawn
    draw.rect(screen,BLACK,backgroundRect,5) #Black outline around choosing backgrounds box

    backgroundText=cooperBlack.render("Backgrounds",True,BLACK) #Background title for the box is written
    screen.blit(backgroundText,(700,460)) #Outputs the title of the background box

    one=image.load("images/one.jpg") #loads '1' to show background 1 for canvas
    screen.blit(one,wallpaper1Rect) #Outputs image onto 1st box
    draw.rect(screen,BLACK,wallpaper1Rect,5) #1st box for 1st wallpaper is drawn
    wallpaper1=image.load("images/wallpaper1.jpg") #1st wallpaper is loaded

    two=image.load("images/two.jpg") #loads '2' to show background 2 for canvas
    screen.blit(two,wallpaper2Rect) #Outputs image onto 2nd box
    draw.rect(screen,BLACK,wallpaper2Rect,5) #2nd box for 1st wallpaper is drawn
    wallpaper2=image.load("images/wallpaper2.jpg") #2nd wallpaper is loaded

    three=image.load("images/three.jpg") #loads '3' to show background 3 for canvas
    screen.blit(three,wallpaper3Rect) #Outputs image onto 3rd box
    draw.rect(screen,BLACK,wallpaper3Rect,5) #3rd box for 1st wallpaper is drawn
    wallpaper3=image.load("images/wallpaper3.jpg") #3rd wallpaper is loaded

    four=image.load("images/four.jpg") #loads '4' to show background 4 for canvas
    screen.blit(four,wallpaper4Rect) #Outputs image onto 4th box
    draw.rect(screen,BLACK,wallpaper4Rect,5) #4th box for 1st wallpaper is drawn
    wallpaper4=image.load("images/wallpaper4.jpg") #4th wallpaper is loaded

    if wallpaper1Rect.collidepoint(mx,my): #if mouse collides with 1st wallpaper box
        draw.rect(screen,RED,wallpaper1Rect,2) #box is outlined red

    if mb[0]==1 and wallpaper1Rect.collidepoint(mx,my): #if mouse is clicked on 1st wallpaper box
        screen.blit(wallpaper1,canvasRect) #Outputs 1st wallpaper onto canvas
        wallpaper=1 #wallpaper equals 1 

    if wallpaper2Rect.collidepoint(mx,my): #if mouse collides with 2nd wallpaper box
        draw.rect(screen,RED,wallpaper2Rect,2) #box is outlined red

    if mb[0]==1 and wallpaper2Rect.collidepoint(mx,my): #if mouse clicked on 2nd wallpaper box
        screen.blit(wallpaper2,canvasRect) #Outputs 2nd wallpaper onto canvas
        wallpaper=2 #wallpaper equals 2

    if wallpaper3Rect.collidepoint(mx,my): #if mouse collides with 3rd wallpaper box
        draw.rect(screen,RED,wallpaper3Rect,2) #box is outlined red

    if mb[0]==1 and wallpaper3Rect.collidepoint(mx,my): #if mouse is clicked on 3rd wallpaper box
        screen.blit(wallpaper3,canvasRect) #Outputs 3rd wallpaper onto canvas
        wallpaper=3 #wallpaper equals 3

    if wallpaper4Rect.collidepoint(mx,my): #if mouse collides with 4th wallpaper box
        draw.rect(screen,RED,wallpaper4Rect,2) #box is outlined red

    if mb[0]==1 and wallpaper4Rect.collidepoint(mx,my): #if mouse is clicked on 4th wallpaper box
        screen.blit(wallpaper4,canvasRect) #Outputs 4th wallpaper onto canvas
        wallpaper=4 #wallpaper equals 4

def multiLine(): #Function for multiLine (Draws multiple lines that come from all directions and they all meet at where the mouse is at)
    global tool #local - global 
    global page #local - global
    global sticker #local - global

    multiLines=image.load("images/multiLines.png") #does the same that all the other images that are loaded (above), except its a different image being loaded
    screen.blit(multiLines,multiLineRect) #Does the same thing as the other screen blits above except diff image
    draw.rect(screen,BLACK,multiLineRect,5) #Box for multiple lines is drawn
        
    if multiLineRect.collidepoint(mx,my): #If mouse collides with the box
        draw.rect(screen,RED,multiLineRect,2) #Box is outlined red
    if mb[0]==1 and multiLineRect.collidepoint(mx,my): #If mouse is clicked on box
        tool="multiLines" #tool equals multiLines
        page=0 #page equals zero since this only becomes another number for the sticker pages
        sticker=0 #sticker still equals zero since there is no sticker being used right now


def lineTool(): #Function for just drawing one line at a time
    global tool #same as above
    global page #same as above
    global sticker #same as above
    draw.rect(screen,BLACK,lineRect,5) #Box for line tool is drawn
    line=image.load("images/line.jpg") #Loads image for line tool
    screen.blit(line,lineRect) #Outputs that image
    if lineRect.collidepoint(mx,my): #If mouse collides/hovers over that box
        draw.rect(screen,RED,lineRect,5) #Box is outlined red
    if mb[0]==1 and lineRect.collidepoint(mx,my): #if mouse is clicked on line tool box
        tool="line" #tool equals line
        page=0 #page equals zero since this only becomes another number for the sticker pages
        sticker=0 #sticker still equals zero since there is no sticker being used right now

def multiBrush(): #Function for using brush that paints random colors when used
    global tool #same
    global page #same
    global sticker #same

    multiColor=image.load("images/multiColor.jpg") #Loads image for the tool
    screen.blit(multiColor,multiBrushRect) #Outputs that image onto the tool box
    
    draw.rect(screen,BLACK,multiBrushRect,5) #Box for this tool is drawn

    if multiBrushRect.collidepoint(mx,my): #If mouse collides/hovers with this box
        draw.rect(screen,RED,multiBrushRect,5) #Box is outlined red
    if mb[0]==1 and multiBrushRect.collidepoint(mx,my): #if mouse is clicked on this box
        tool="multiBrush" #tool equals multiBrush
        page=0 #page equals zero since this only becomes another number for the sticker pages
        sticker=0 #sticker still equals zero since there is no sticker being used right now
        
def calligraphyTool(): #Function for using brush that paints random colors when used
    global tool #same
    global page #same
    global sticker #same

    calligraphy=image.load("images/calligraphy.jpg") #Loads image for the tool
    screen.blit(calligraphy,calligraphyRect) #Outputs that image onto the tool box
    
    draw.rect(screen,BLACK,calligraphyRect,5) #Box for this tool is drawn

    if calligraphyRect.collidepoint(mx,my): #If mouse collides/hovers with this box
        draw.rect(screen,RED,calligraphyRect,5) #Box is outlined red
    if mb[0]==1 and calligraphyRect.collidepoint(mx,my): #if mouse is clicked on this box
        tool="calligraphy" #tool equals multiBrush
        page=0 #page equals zero since this only becomes another number for the sticker pages
        sticker=0 #sticker still equals zero since there is no sticker being used right now
        
def undoRedo():
    global tool #local - global
    global page #local - global
    global sticker #local - global
    draw.rect(screen,BLACK,redoRect,5) #Box for the redo is drawn
    redo=image.load("images/redo.png") #Image for the redo is loaded
    screen.blit(redo,redoRect) #Outputs that redo image
    
    draw.rect(screen,BLACK,undoRect,5) #Box for the undo is drawn
    undo=image.load("images/undo.png") #Image for the undo is loaded
    screen.blit(undo,undoRect) #Outputs that undo image

    if redoRect.collidepoint(mx,my): #If mouse collides with the redo box
        draw.rect(screen,RED,redoRect,2) #Box is outlined red
    
    if mb[0]==1 and redoRect.collidepoint(mx,my): #If mouse is clicked on redo box
        tool="redo" #tools equals redo
        page=0 #page equals zero since this only becomes another number for the sticker pages
        sticker=0 #sticker still equals zero since there is no sticker being used right now

    if undoRect.collidepoint(mx,my): #If mouse hovers over undo box
        draw.rect(screen,RED,undoRect,2) #Box is outlined red
        
    if mb[0]==1 and undoRect.collidepoint(mx,my): #If mouse is clicked on undo box
        tool="undo" #tools equals undo
        page=0 #page equals zero since this only becomes another number for the sticker pages
        sticker=0 #sticker still equals zero since there is no sticker being used right now
        
def usingTools(): #Function for using ALL the tools
    if mb[0]==1 and canvasRect.collidepoint(mx,my): #If mouse clicks on the canvas
        screen.set_clip(canvasRect) #doesnt update any other pixels outside the canvas rect
        if tool=="pencil": #If tool equals pencil....
            draw.line(screen,col,(omx,omy),(mx,my)) #Line is drawn, from the old mouse x,y coord to the new mouse x,y coord
        if tool=="eraser": #if tool equals eraser.....
            if wallpaper==0: #If theres no wallpaper.......
                draw.circle(screen,WHITE,(mx,my),sz) #circle is drawn
                dx=mx-omx #run
                dy=my-omy #rise
                hyp=sqrt(dx**2+dy**2)#use pythagorean theorem for paint brush
                for i in range(1,int(hyp)): #as long as 'i' is int range of 1 and the hypotenuse for the paint brush
                    dotx=int(omx+i*dx/hyp) 
                    doty=int(omy+i*dy/hyp)
                    draw.circle(screen,WHITE,(dotx,doty),sz) #Circles are drawn with no spaces between that follows the mouse
            if wallpaper==1: #If the 1st wallpaper was chosen and the eraser tool was clicked on was also chosen
                wallpaper1=image.load("images/wallpaper1.jpg") #1st wallpaper is loaded
                wallpaper1Eraser=wallpaper1.subsurface((mx-10,my-150,50,50)) #Wallpaper eraser (doesnt erase background) equals the subsurface of the original wallpaper: smaller and the distance is subtracted from the canvas's x and y coordinates
                screen.blit(wallpaper1Eraser,(mx,my)) #Outputs the wallpaper 1 eraser
            if wallpaper==2: #If the 2nd wallpaper was chosen and the eraser tool was clicked on
                wallpaper2=image.load("images/wallpaper2.jpg") #Loads 2nd wallpaper
                wallpaper2Eraser=wallpaper2.subsurface((mx-10,my-150,50,50)) #Does the same as wallpaper 1 eraser except its erasing different background
                screen.blit(wallpaper2Eraser,(mx,my)) #Outputs wallpaper 2 eraser
            if wallpaper==3: #If 3rd wallpaper was chosen and eraser tool was clicked on
                wallpaper3=image.load("images/wallpaper3.jpg") #Loads 3rd wallpaper
                wallpaper3Eraser=wallpaper3.subsurface((mx-10,my-150,50,50)) #Does the same as wallpaper 1 eraser except its erasing different background
                screen.blit(wallpaper3Eraser,(mx,my)) #Outputs wallpaper 3 eraser
            if wallpaper==4: #If 4th wallpaper was chosen and the eraser tool was clicked on
                wallpaper4=image.load("images/wallpaper4.jpg") #loads 4th wallpaper
                wallpaper4Eraser=wallpaper4.subsurface((mx-10,my-150,50,50)) #Does the same as wallpaper 1 eraser except its erasing different background
                screen.blit(wallpaper4Eraser,(mx,my)) #Outputs wallpaper 4

        if tool=="brush": #If paint brush tool is chosen
            draw.circle(screen,col,(mx,my),sz) #does the same as eraser except user can choose different colors
            dx=mx-omx #run
            dy=my-omy #rise
            hyp=sqrt(dx**2+dy**2)#use pythagorean theorem for paint brush
            for i in range(1,int(hyp)):
                dotx=int(omx+i*dx/hyp)
                doty=int(omy+i*dy/hyp)
                draw.circle(screen,col,(dotx,doty),sz)
        if tool=="rectangle": #If tool chosen is rectangle (filled rectangle)
            draw.rect(screen,col,(sx,sy,mx-sx,my-sy)) #Rectangle is drawn starting from sx,sy and then from where the mouse is let go
        if tool=="circle": #If circle tool is chosen..
            try: #program tries..
                draw.circle(screen,col,(sx,sy),my-sy) #Circle is drawn starting at sx,sy and then from where the mouse y-coord is let go
            except: #Except if that doesn't happen....
                pass #prevents the program from crashing 
        if tool=="randomBar": #If random bars tool is chosen...
            rx=randint(-80,80) #coord for x points of lines are random from the width of the rectangle
            draw.line(screen,col,(mx+rx,my-50),(mx+rx,my+50),sz)  #Lines are drawn randomly between the width/height of the rectangle, until it forms a rectangle
        if tool=="fill": #If fill bucket tool is chosen
            draw.rect(screen,col,canvasRect) #When the user clicks on the canvas with the color they chose, the canvas turns into that color
        if tool=="multiLines": #If the multiple lines tool is chosen
            for y in range(10):#10 lines (from both left side and right side)
                draw.line(screen,col,(0,80*y),(mx,my)) #10 lines are drawn from left side
                draw.line(screen,col,(800,80*y),(mx,my)) #10 lines are drawn from right side

            for x in range(10): #10 lines (from both top and bottom)
                draw.line(screen,col,(80*x,0),(mx,my))#10 lines are drawn from top
                draw.line(screen,col,(80*x,800),(mx,my))#10 lines are drawn from bottom

        if tool=="multiBrush": #if multiple colored paint brush is the tool chosen
            r=randint(0,255) #r - random colors chosen from 0 to 255
            g=randint(0,255) #g - random colors chosen from 0 to 255
            b=randint(0,255) #b - random colors chosen from 0 to 255
            draw.circle(screen,(r,g,b),(mx,my),sz) #same as paintbrush/eraser except the colors are random (multicolor)
            dx=mx-omx #run
            dy=my-omy #rise
            hyp=sqrt(dx**2+dy**2)#use pythagorean theorem for paint brush
            for i in range(1,int(hyp)):
                dotx=int(omx+i*dx/hyp)
                doty=int(omy+i*dy/hyp)
                draw.circle(screen,(r,g,b),(dotx,doty),sz)

        if tool=="calligraphy": #if tool equals calligraphy
            dist=int(sqrt((mx-omx)**2+(my-omy)**2))
            dx=mx-omx #run
            dy=my-omy #rise
            for i in range(1,dist):
                dotx=int(omx+(i*dx/dist))
                doty=int(omy+(i*dy/dist))
                draw.line(screen,col,(dotx,doty),(dotx,doty-10),4) #as it draws, the my of the line decreases
    
        screen.set_clip(None) #stops the command
        
            
while running: #while the program is running
    for evt in event.get(): 
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
                    
            if evt.button==1:#left click
                start=evt.pos
                print(start)
                if page1Rect.collidepoint(mx,my): #if the left button is clicked and the mouse clides with the page 1 box
                        draw.rect(screen,WHITE,stickerRect) #Blank white screen for page

                        gon=image.load("images/gon.png") #STICKER 1 is shown
                        screen.blit(gon,(1150,15))
                           
                        killua=image.load("images/killua.png") #STICKER 2 is shown
                        screen.blit(killua,(1030,10))

                        kurapika=image.load("images/kurapika.png") #STICKER 3 is shown
                        screen.blit(kurapika,(1150,175))

                        leorio=image.load("images/leorio.png") #STICKER 4 is shown
                        screen.blit(leorio,(1075,170))
                    
                        page=1 #page equals 1 for the stickers pages

                if page2Rect.collidepoint(mx,my): #same as above except page 2 box and different stickers
                        draw.rect(screen,WHITE,stickerRect) #Blank white page covers box
                        
                        gon2=image.load("images/gon2.png") #STICKER 5
                        screen.blit(gon2,(1140,15))
                        
                        killua2=image.load("images/killua2.png") #STICKER 6
                        screen.blit(killua2,(1020,15))

                        hisoka=image.load("images/hisoka.png") #STICKER 7
                        screen.blit(hisoka,(1150,175))

                        illumi=image.load("images/illumi.png") #STICKER 8
                        screen.blit(illumi,(1040,180))

                        page=2 #page equals 2 for the stickers pages

                if page3Rect.collidepoint(mx,my): #same as above except its page 3 stickers
                        draw.rect(screen,WHITE,stickerRect)
                        
                        leorio2=image.load("images/leorio2.png") #STICKER 9
                        screen.blit(leorio2,(1150,15))
                        
                        hisoka2=image.load("images/hisoka2.png") #STICKER 10
                        screen.blit(hisoka2,(1030,15))
                        
                        chrollo=image.load("images/chrollo.png") #STICKER 11
                        screen.blit(chrollo,(1155,180))
                        
                        illumi2=image.load("images/illumi2.png") #STICKER 12
                        screen.blit(illumi2,(1035,180))
                        
                        page=3 #page equals 1 for the stickers pages

                if page4Rect.collidepoint(mx,my): #same as above except page 4 stickers
                        draw.rect(screen,WHITE,stickerRect) #blank white page covers stickers box
                        
                        killua3=image.load("images/killua3.png") #STICKER 9
                        screen.blit(killua3,(1145,15))
                        
                        biscuit=image.load("images/biscuit.png") #STICKER 10
                        screen.blit(biscuit,(1030,15))
                        
                        hisoka3=image.load("images/hisoka3.png") #STICKER 11
                        screen.blit(hisoka3,(1135,180))
                        
                        kurapika2=image.load("images/kurapika2.png") #STICKER 12
                        screen.blit(kurapika2,(1020,180))
                        
                        page=4 #page equals 1 for the stickers pages
                        

            if page==1: #If page equals 1
                #FOR STICKER 1       
                if mb[0]==1 and gonSticker.collidepoint(mx,my): #if mouse is clicked on 1st sticker on page 1
                    page=1 #page is 1
                    sticker=1 #sticker is 1
                    tool="no tool" #No tool is being used
                if sticker==1 and canvasRect.collidepoint(mx,my): #If the sticker equals 1 and mouse clicks on canvas
                     screen.set_clip(canvasRect) #Prevents stickers from getting out of canvas
                     screen.blit(gon,(mx-160/2,my-160/2)) #Sticker is outputted where the mouse clicks 
                     screen.set_clip(None) #stops command
                     tool="no tool" #Theres no tool being used

###THE REST ARE THE SAME AS ABOVE EXCEPT THERE ARE DIFF STICKERS AND PAGES###
                #FOR STICKER 2
                if mb[0]==1 and killuaSticker.collidepoint(mx,my): 
                    page=1
                    sticker=2
                    tool="no tool"
                if sticker==2 and canvasRect.collidepoint(mx,my):
                     screen.set_clip(canvasRect)                
                     screen.blit(killua,(mx-160/2,my-160/2)) 
                     screen.set_clip(None)
                     tool="no tool"

                #FOR STICKER 3
                if mb[0]==1 and kurapikaSticker.collidepoint(mx,my):
                    page=1
                    sticker=3
                    tool="no tool"
                if sticker==3 and canvasRect.collidepoint(mx,my):
                     screen.set_clip(canvasRect)                
                     screen.blit(kurapika,(mx-160/2,my-160/2)) 
                     screen.set_clip(None)
                     tool="no tool"

                #FOR STICKER 4
                if mb[0]==1 and leorioSticker.collidepoint(mx,my):
                    page=1
                    sticker=4
                    tool="no tool"
                if sticker==4 and canvasRect.collidepoint(mx,my):
                     screen.set_clip(canvasRect)                
                     screen.blit(leorio,(mx-160/2,my-160/2)) 
                     screen.set_clip(None)
                     tool="no tool"
            #PAGE 3
            if page==2:
                #FOR STICKER 5
                if mb[0]==1 and gon2Sticker.collidepoint(mx,my):
                    page=2
                    sticker=5
                    tool="no tool"
                if sticker==5 and canvasRect.collidepoint(mx,my):
                     screen.set_clip(canvasRect)                
                     screen.blit(gon2,(mx-160/2,my-160/2)) 
                     screen.set_clip(None)
                     tool="no tool"

                #FOR STICKER 6
                if mb[0]==1 and killua2Sticker.collidepoint(mx,my):
                    page=2
                    sticker=6
                    tool="no tool"
                if sticker==6 and canvasRect.collidepoint(mx,my):
                     screen.set_clip(canvasRect)                
                     screen.blit(killua2,(mx-160/2,my-160/2)) 
                     screen.set_clip(None)
                     tool="no tool"

                #FOR STICKER 7
                if mb[0]==1 and hisokaSticker.collidepoint(mx,my):
                    page=2
                    sticker=7
                    tool="no tool"
                if sticker==7 and canvasRect.collidepoint(mx,my):
                     screen.set_clip(canvasRect)                
                     screen.blit(hisoka,(mx-160/2,my-160/2)) 
                     screen.set_clip(None)
                     tool="no tool"

                #FOR STICKER 8
                if mb[0]==1 and illumiSticker.collidepoint(mx,my):
                    page=2
                    sticker=8
                    tool="no tool"
                if sticker==8 and canvasRect.collidepoint(mx,my):
                     screen.set_clip(canvasRect)                
                     screen.blit(illumi,(mx-160/2,my-160/2)) 
                     screen.set_clip(None)
                     tool="no tool"
            #PAGE 3
            if page==3:
               #FOR STICKER 9
                if mb[0]==1 and leorio2Sticker.collidepoint(mx,my):
                    page=3
                    sticker=9
                    tool="no tool"
                if sticker==9 and canvasRect.collidepoint(mx,my):
                     screen.set_clip(canvasRect)                
                     screen.blit(leorio2,(mx-160/2,my-160/2)) 
                     screen.set_clip(None)
                     tool="no tool"

                #FOR STICKER 10
                if mb[0]==1 and hisoka2Sticker.collidepoint(mx,my):
                    page=3
                    sticker=10
                    tool="no tool"
                if sticker==10 and canvasRect.collidepoint(mx,my):
                     screen.set_clip(canvasRect)                
                     screen.blit(hisoka2,(mx-160/2,my-160/2)) 
                     screen.set_clip(None)
                     tool="no tool"

                #FOR STICKER 11
                if mb[0]==1 and chrolloSticker.collidepoint(mx,my):
                    page=3
                    sticker=11
                    tool="no tool"
                if sticker==11 and canvasRect.collidepoint(mx,my):
                     screen.set_clip(canvasRect)                
                     screen.blit(chrollo,(mx-160/2,my-160/2)) 
                     screen.set_clip(None)
                     tool="no tool"

                #FOR STICKER 12
                if mb[0]==1 and illumi2Sticker.collidepoint(mx,my):
                    page=3
                    sticker=12
                    tool="no tool"
                if sticker==12 and canvasRect.collidepoint(mx,my):
                     screen.set_clip(canvasRect)                
                     screen.blit(illumi2,(mx-160/2,my-160/2)) 
                     screen.set_clip(None)
                     tool="no tool"
            #PAGE 4
            if page==4:
               #FOR STICKER 13
                if mb[0]==1 and killua3Sticker.collidepoint(mx,my):
                    page=4
                    sticker=13
                    tool="no tool"
                if sticker==13 and canvasRect.collidepoint(mx,my):
                     screen.set_clip(canvasRect)                
                     screen.blit(killua3,(mx-160/2,my-160/2)) 
                     screen.set_clip(None)
                     tool="no tool"

                #FOR STICKER 14
                if mb[0]==1 and biscuitSticker.collidepoint(mx,my):
                    page=4
                    sticker=14
                    tool="no tool"
                if sticker==14 and canvasRect.collidepoint(mx,my):
                     screen.set_clip(canvasRect)                
                     screen.blit(biscuit,(mx-160/2,my-160/2)) 
                     screen.set_clip(None)
                     tool="no tool"

                #FOR STICKER 15
                if mb[0]==1 and hisoka3Sticker.collidepoint(mx,my):
                    page=4
                    sticker=15
                    tool="no tool"
                if sticker==15 and canvasRect.collidepoint(mx,my):
                     screen.set_clip(canvasRect)                
                     screen.blit(hisoka3,(mx-160/2,my-160/2)) 
                     screen.set_clip(None)
                     tool="no tool"

                #FOR STICKER 16
                if mb[0]==1 and kurapika2Sticker.collidepoint(mx,my):
                    page=4
                    sticker=16
                    tool="no tool"
                if sticker==16 and canvasRect.collidepoint(mx,my):
                     screen.set_clip(canvasRect)                
                     screen.blit(kurapika2,(mx-160/2,my-160/2)) 
                     screen.set_clip(None)
                     tool="no tool"

                 
            if evt.button==4:#scroll up
                sz+=1 #size will increase by 1
            if evt.button==5:#scroll down
                if sz>1: #only if the size is greater than 1
                    sz-=1 #size will decrease by 1 (prevents radius from going negative)
            sx,sy=evt.pos
            click=True
                    
        if evt.type==MOUSEBUTTONUP: #If mouse is released
            
            screenCap=screen.subsurface(canvasRect).copy() #Canvas is saved
            if canvasRect.collidepoint(mx,my): #If mouse is released on canvasRect...
                undoList.append(screenCap) #undo list adds that screenshot to the list
            
            screen.blit(screenCap,canvasRect) #saved canvas screen is outputted onto canvas
            screen.set_clip(canvasRect) #Doesnt allow pixels to get out of canvas
                            
            if tool=="rectangle": #If tool chosen is rectangle...
                draw.rect(screen,col,(sx,sy,mx-sx,my-sy),sz) #Unfilled rectangle is drawn
            if tool=="circle": #If circle tool is chosen
                try: #Program tries....
                    draw.circle(screen,col,(sx,sy),my-sy,sz) #Draws unfilled circle
                except: #Except...
                    pass #prevents the program from crashing
                
            if tool=="line": #If line tool is chosen
                draw.line(screen,col,(sx,sy),(mx,my),sz) #Line is drawn from previous point clicked to where mouse is released

            screen.set_clip(None) #ends command
            screenCap=screen.subsurface(canvasRect).copy() #Canvas is saved again
        
    
            
    mx,my=mouse.get_pos() 
    mb=mouse.get_pressed()
    
    pencilTool() #allows for the function to be used
    eraserTool() #same as above
    brushTool() #same as above
    rectTool() #same as above
    circleTool() #same as above
    randomBarsTool() #same as above
    fillTool() #same as above
    palette() #same as above
    stickers() #same as above 
    music() #same as above
    openSave() #same as above
    backgrounds() #same as above
    multiLine() #same as above
    lineTool() #same as above 
    multiBrush() #same as above
    calligraphyTool()
    undoRedo() #same as above
    
    #using the tools
    usingTools()

    print(undoList) #Prints what tool is currenly being used

    if mb[0]==1 and paletteRect.collidepoint(mx,my): #if the mouse is clicked on anywhere within the boundary of the palette box
        col=screen.get_at((mx,my)) #the color clicked on is the color the user will be using
        draw.rect(screen,col,showColorRect) #a box above the palette is drawn, showing the color the user is currently using

    if click and undoRect.collidepoint(mx,my): #If click is true on the undo tool box
            if len(undoList)>1: #If the undo list has more than 1 screenshot of the canvas
                redoList.append(undoList.pop()) #Redo list adds the screenshot from the undo list to its own list
                screen.blit(undoList[-1],(10,150)) #Outputs the previous screenshot
                screenCap=screen.subsurface(canvasRect).copy() #Canvas is saved 

    if click and redoRect.collidepoint(mx,my): #If click is true on the redo tool box
            if len(redoList)>0: #If the redo list has more that 0 screenshots of the canvas 
                undoList.append(redoList.pop()) #The undo list adds the screenshot from the redo list onto its own
                screen.blit(undoList[-1],(10,150)) #Ouputs the screenhsot from the undo list
                screenCap=screen.subsurface(canvasRect).copy() #Canvas is saved 
                    
    omx=mx
    omy=my
    display.flip()
    click=False
            
quit()

