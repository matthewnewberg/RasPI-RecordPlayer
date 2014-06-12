#!/usr/bin/env python

from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)

os.chdir("/home/pi")

playing = False
count = 0
song = -1
newSong = -1
lastSongCount = 0
turnTableState = GPIO.input(17)
newTurnTableState = GPIO.input(17)
songCount = 0
while count < 1000000:

	newSong = 0
       	if ( GPIO.input(22) == False ):
                #os.system('mpg321 bobcat.mp3 &')
		newSong = newSong | 1
       	if ( GPIO.input(23) == False ):
                #os.system('mpg321 chimp.mp3 &')
		newSong = newSong | 2

	if ( GPIO.input(24) == False ):
		newSong = newSong | 4
	
	if (GPIO.input(25) == False ):
		newSong = newSong | 8

	if (newSong == song):
		if (song == 6):
			if (songCount < 50):
				songCount = songCount + 1
				os.system('mpg321 -g 20 {0}.mp3'.format(songCount))  

	newTurnTableState = GPIO.input(17)

	if (turnTableState != newTurnTableState ):
		if (lastSongCount > count + 300):
			song = -1

		print newSong

		if (song != newSong):
			os.system('killall -9 /usr/bin/mpg321')
			lastSongCount = count
			song = newSong
			playing = True
			if (song == 9):
				os.system('mpg321 -g 40 hickorydickorydock.mp3 &')
			if (song == 10):
				os.system('mpg321 -g 40 humptydumpty.mp3 &')
			if (song == 11):
				os.system('mpg321 -g 40 jillandjill.mp3 &')
			if (song == 3):
				os.system('mpg321 -g 40 auclairdelalune.mp3 &')
			if (song == 14):
				os.system('mpg321 -g 40 twinkletwinklelittlestar.mp3 &')
			if (song == 12):
				os.system('mpg321 -g 40 londonbridge.mp3 &')
			if (song == 13):
				os.system('mpg321 -g 40 ohwherehasmylittledoggone.mp3 &')
			if (song == 7):
				os.system('mpg321 -g 40 thefarmerinthedell.mp3 &')
			if (song == 5):
				os.system('mpg321 -g 40 camptownraces.mp3 &')
			if (song == 6):
				os.system('mpg321 -g 20 1.mp3')
				songCount = 1
			
        sleep(0.1);
	count = count + 1
	turnTableState = newTurnTableState

	if playing:
		sleep(3.0)
	playing = False

