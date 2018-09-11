from random import choice

class RandomWalk():
	def __init__(self,max_points):
		self.max_points = max_points
		#empieza en cero,cero
		self.x_points = [0]
		self.y_points = [0]
	
	def fill_walk(self):
		while len(self.x_points) < self.max_points:
			x_direction = choice([-1,1])
			x_length = choice([0,1,2,3])
			x_step = x_direction*x_length
			
			y_direction = choice([-1,1])
			y_length = choice([0,1,2,3])
			y_step = y_direction*y_length
			
			if x_step == 0 and y_step == 0:
				continue
			
			next_x = self.x_points[-1]+x_step
			self.x_points.append(next_x)
			
			next_y = self.y_points[-1]+y_step
			self.y_points.append(next_y)
			

