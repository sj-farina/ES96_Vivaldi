from Tkinter import *
import pygame

class Find_Joystick:
	def __init__(self, root):
		self.root = root

		## initialize pygame and joystick
		pygame.init()
		if(pygame.joystick.get_count() < 1):
			# no joysticks found
			print "Please connect a joystick.\n"
			self.quit()
		else:
			# create a new joystick object from
			# ---the first joystick in the list of joysticks
			Joy0 = pygame.joystick.Joystick(0)
			# tell pygame to record joystick events
			Joy0.init()

		## bind the event I'm defining to a callback function
		self.root.bind("<<JoyFoo>>", self.my_event_callback)

		## start looking for events
		self.root.after(0, self.find_events)

	def find_events(self):
		## check everything in the queue of pygame events
		events = pygame.event.get()
		for event in events:
			# event type for pressing any of the joystick buttons down
			if event.type == pygame.JOYAXISMOTION:
				# generate the event I've defined
				self.root.event_generate("<<JoyFoo>>")
				#print(pygame.joystick.Joystick(0))
			'''elif event.type == pygame.JOYHATMOTION:
				# generate the event I've defined
				self.root.event_generate("<<JoyFoo>>")
				print(pygame.joystick.Joystick(0))
			elif event.type == pygame.JOYBALLMOTION:
				# generate the event I've defined
				self.root.event_generate("<<JoyFoo>>")
				print(pygame.joystick.Joystick(0))'''
#JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION

		## return to check for more events in a moment
		self.root.after(20, self.find_events)

	def my_event_callback(self, event):
		#print "Joystick button press (down) event"
		#print (event)
		Joy0 = pygame.joystick.Joystick(0)
		# tell pygame to record joystick events
		Joy0.init()
		if Joy0.get_axis(0) != 0:
			if Joy0.get_axis(0) == -1:
				print 'left'
			else:
				print 'right'
		elif Joy0.get_axis(1) != 0:
			if Joy0.get_axis(1) == -1:
				print 'up'
			else:
				print 'down'
		else:
			print 'stop'
		

		#if Joy0.get_axis(0) == -1:
		#	print 'left'
		#if ((Joy0.get_axis(0) != 0) or (Joy0.get_axis(0) != -1)):
		#	print 'right'
		#if Joy0.get_axis(1) == -1:
		#	print 'up'
		#if ((Joy0.get_axis(1) != 0) or (Joy0.get_axis(1) != -1)):
		#	print 'down'

		#print Joy0.get_axis(0)
		#print Joy0.get_axis(1)

	## quit out of everything
	def quit(self):
		import sys
		sys.exit()
def main():
	## Tkinter initialization
	root = Tk()
	app = Find_Joystick(root)
	# get out by closing the window or pressing Control-q
	root.protocol('WM_DELETE_WINDOW', app.quit)
	root.bind('<Control-q>', app.quit)
	root.bind('<Control-Q>', app.quit)
	root.mainloop()

if __name__ == "__main__":
	main()
