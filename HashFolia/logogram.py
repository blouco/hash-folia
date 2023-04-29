import random
import sys
from random import randint
import math
import PIL
from PIL import Image, ImageDraw, ImageFilter

#inital startpoint 
#https://mathematica.stackexchange.com/questions/137156/where-is-abbott-how-to-make-logograms-from-the-film-arrival

class Tendril:

	def __init__(self, x, y, width=15):

		self.x = x
		self.y = y
		self.width = width
		self.angle = random.uniform(0,2*3.14158)  # random angle in radians.
		self.segments = []
		self.v = 0

	def create(self, distance=3.0, curl=0.01, step=0.02, nmbSegments=50):
		distance = random.uniform(distance/2, distance)
		nmbSegments = int(round(random.uniform(nmbSegments, nmbSegments*1.2)))

		for i in range(1, nmbSegments):
			self.x += math.cos(self.angle) * distance
			self.y += math.sin(self.angle) * distance
			self.v = 0
			self.v += random.uniform(-step, step)
			self.v *= 0.9 + curl * 0.1
			self.angle += self.v

			self.segments.append((self.x, self.y, self.angle))

	def draw(self, draw):

		n = len(self.segments)
		for i, (x, y, angle) in enumerate(self.segments):

				r = self.width
				#r = (1-float(i)/2*n) * self.width # size gradually decreases.
				draw.ellipse([(x,y),((x+r),(y+r))], fill=(0,0,0))
class CircularStroke:

	def __init__(self, nmb, center, centerVar, thicknessVar, rad, radVar):

		self.nmb = nmb
		self.center = center
		self.centerVar = centerVar
		self.thicknessVar = thicknessVar
		self.rad = rad
		self.radVar = radVar

	"""
	thanks to https://gist.github.com/skion/9259926
	Hack that looks similar to PIL's draw.arc(), but can specify a line width.
	"""
	def arc(self, draw, bbox, start, end, fill, width=1.0, segments=100):

		# radians
		start *= math.pi / 180.0
		end *= math.pi / 180.0

		# angle step
		da = (end - start) / segments

		# shift end points with half a segment angle
		start -= da / 2
		end -= da / 2

		# ellips radii
		rx = (bbox[2] - bbox[0]) / 2
		ry = (bbox[3] - bbox[1]) / 2

		# box centre
		cx = bbox[0] + rx
		cy = bbox[1] + ry

		# segment length
		l = (rx+ry) * da / 2.0

		widthMax = width

		for i in range(segments):
			width = randint(-widthMax,widthMax)

			# angle centre
			a = start + (i+0.5) * da

			# x,y centre
			x = cx + math.cos(a) * rx
			y = cy + math.sin(a) * ry

			# derivatives
			dx = -math.sin(a) * rx / (rx+ry)
			dy = math.cos(a) * ry / (rx+ry)

			draw.line([(x-dx*l,y-dy*l), (x+dx*l, y+dy*l)], fill=fill, width=width)

	def draw(self, draw, angle, gapWidth):
		for i in range(1, self.nmb):
			xVar = self.center[0] + random.uniform(-self.centerVar,self.centerVar)
			yVar = self.center[1] + random.uniform(-self.centerVar,self.centerVar)

			thickness = self.thicknessVar
			randomRad = self.rad * random.uniform(self.radVar[0], self.radVar[1])

			#TODO
			holeAngle = angle
			v =  gapWidth

			randomAngleStart = random.uniform(v+holeAngle,180+holeAngle-v)
			randomAngleEnd = random.uniform(randomAngleStart,360+holeAngle-v)

			self.arc(draw, (xVar-randomRad, yVar-randomRad, xVar+randomRad, yVar+randomRad), 
			randomAngleStart, randomAngleEnd, fill=(0,0,0), width=thickness)

	def drawCircleBlob(self, draw, angle, blobLength, blobWidth, nmbCircles, centerVarBlob):
		for i in range(1, nmbCircles):
			xVar = self.center[0] + random.uniform(-centerVarBlob/2, centerVarBlob)
			yVar = self.center[1] + random.uniform(-centerVarBlob/2, centerVarBlob)

			thickness = int(round(self.thicknessVar * random.uniform(0,4)))

			randomRad = self.rad + random.uniform(-blobWidth, blobWidth)

			randomAngleStart = angle + random.uniform(0, blobLength/2)
			randomAngleEnd = angle - random.uniform(0, blobLength/2)

			#print randomAngleStart
			#print randomAngleEnd

			self.arc(draw, (xVar-randomRad, yVar-randomRad, xVar+randomRad, yVar+randomRad), 
			randomAngleStart, randomAngleEnd, fill=(0,0,0), width=thickness)

def disks (draw, center, rad, nmbDisks, minAngleExtent, maxAngleExtent, size=25, tendril=False):
	radVarDisk = random.uniform(size/4, size);

	for i in range(1,nmbDisks):
		angle = random.uniform(minAngleExtent, maxAngleExtent)

		varCenter = 35

		xVar = center[0] + random.uniform(-varCenter,varCenter)
		yVar = center[1] + random.uniform(-varCenter,varCenter)

		x0 = xVar + rad * math.cos(angle)
		y0 = yVar + rad * math.sin(angle)

		x1 = x0 + random.uniform(0, radVarDisk)
		y1 = y0 + random.uniform(0, radVarDisk)

		draw.ellipse([(x0,y0),(x1,y1)], fill=(0,0,0))
		tendrilVar = tendril and random.uniform(0,4) > 3.141
		if tendrilVar:
			for i in range(0,1):
				#trendrilOnBlob(draw, (x0,y0), 50, 25)
				tendril = Tendril(x0,y0,10)
				tendrilSize = randint(35,50)
				tendril.create(5.0, 10.0 ,0.1, tendrilSize)
				tendril.draw(draw)


def logogram(seed, imgSize, varThickness, varCenter, nmbCirc, varRad):

	image = Image.new("RGB", imgSize, "white")
	x = image.width/2
	y = x
	draw = ImageDraw.Draw(image)
	rad = imgSize[0]/3

	#logogram_circle(draw, nmbCirc, (x,y), varCenter, varThickness, rad, varRad)
	stroke = CircularStroke(nmbCirc, (x,y), varCenter, varThickness, rad, varRad)
	angle = randint(0,360)
	v = randint(0, 90)
	stroke.draw(draw, angle, v)

	nmbDisks = 70
	minAngleExtent = random.uniform(0,2*3.141)
	maxAngleExtent = minAngleExtent+0.4
	nmbCluster = randint(1,4)
	for i in range(0,nmbCluster):
		minAngleExtent = random.uniform(0,2*3.141)
		maxAngleExtent = minAngleExtent+0.4
		disks(draw, (x,y), rad, nmbDisks, minAngleExtent, maxAngleExtent, size=100, tendril=True)
		middleAngle = (maxAngleExtent - (-1*(minAngleExtent-maxAngleExtent)/2)) * (180/3.141)
		stroke.drawCircleBlob(draw, middleAngle, 60, 50, 20, 2)

	disks(draw, (x,y), rad, 70, 0, 2*3.141, size=25)

	#image = image.filter(ImageFilter.MaxFilter(1))
	image = image.filter(ImageFilter.BLUR)
	image = image.filter(ImageFilter.BLUR)



	#threshold
	thresholdValue = 200
	image = image.convert('L')
	fn = lambda x : 255 if x > thresholdValue else 0
	image = image.convert('L').point(fn, mode='1')


	image.thumbnail((512,512), Image.ANTIALIAS)
	return image

def generatePNGs(nmbPics):
	for i in range(0,nmbPics):
		seed = random.uniform(0, i) * 1000;
		string = "samples/" + str(i)+"hepta.png"
		img = logogram(seed, (2048,2048), 10, 10, 100, (1,1))
		img = img.convert("RGBA")
		datas = img.getdata()
		newData = []
		for item in datas:
			if item[0] == 255 and item[1] == 255 and item[2] == 255:
				newData.append((255, 255, 255, 0))
			else:
			    if item[0] > 150:
				    newData.append((0, 0, 0, 255))
			    else:
				    newData.append(item)
		img.putdata(newData)
		img.save(string, "PNG")
		print(string + " generated")

