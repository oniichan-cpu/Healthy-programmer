from pygame import mixer
import asyncio
from datetime import datetime
from time import time

class HealthyProgrammer:

	def __init__(self,music):
		self.music = music

	def music_player(self,query_to_stop):
		 
		# Starting the mixer 
		mixer.init() 
  
		# Loading the song 
		mixer.music.load(self.music) 
  
		# Setting the volume .
		mixer.music.set_volume(1) 
  
		# Start playing the song 
		mixer.music.play() 

		# infinite loop 
		while True:
			print(f"Type {query_to_stop} to stop")
			query = input().lower() 
			if query == query_to_stop: 
				# Stop the mixer 
				mixer.music.stop()
				break

	def logger(self,tempfilename,text):
		filename = "./data/" + tempfilename + ".txt"
		now = datetime.now()
		with open(filename,'a') as f:
			f.write(f'{text} at : {now}\n')

if __name__ == '__main__':
	eye = HealthyProgrammer("./data/ina unravel.mp3")
	exercise = HealthyProgrammer("./data/plastic love.mp3")
	water = HealthyProgrammer("./data/shaark.mp3")

	init_eyes = time()
	init_water = time()
	init_exercise = time()

	eyes_secs = 20*60
	water_secs = 60*60
	exercise_secs = 45*60

	print(".....Started......")
	print(f"Eyes Alarm is set every {eyes_secs/60} minutes")
	print(f"Exercise Alarm is set every {exercise_secs/60} minutes")
	print(f"And Water Alarm is set every {water_secs/60} minutes")

	while True:
		if time() - init_eyes > eyes_secs:
			eye.music_player("eyes done")
			init_eyes = time()
			eye.logger("./logs/eyes_logs.txt","Gave Eye rest")

		if time() - init_water > water_secs:
			water.music_player("drank")
			init_water = time()
			water.logger("./logs/water_logs.txt","Drank Water")

		if time() - init_exercise > exercise_secs:
			exercise.music_player("exercised")
			init_exercise = time()
			exercise.logger("./logs/exercise_logs.txt","Exercised")






