# Robot arm kinematics
import math


class arm():
	def __init__(self):
		self.theta1 = 0
		self.theta2 = 0 
		self.theta3 = 0
		self.l1 = 130.002
		self.l2 = 137
		self.l3 = 65.15
		

	
	def findAngles(self,xe,ye):

	 	a1 = self.l1
	 	a2 = self.l2
	 	x3 = self.l3
	 	
	 	theta1A = math.atan2(1/(a1**2 * ye * (xe**2 + ye**2)) * (a1**3 * ye**2 - a1 * a2**2 * ye**2 - 2 * a1 * a2 * x3 * ye**2 - a1 * x3**2 * ye**2 + a1 * xe**2 * ye**2 + a1 * ye**4 + xe * math.sqrt(-a1**2 * ye**2 * (a1**4 + (a2**2 + 2 * a2 * x3 + x3**2 - xe**2 - ye**2)**2 - 2 * a1**2 * (a2**2 + 2 * a2 * x3 + x3**2 + xe**2 + ye**2)))),(a1**3 * xe - a1 * a2**2  * xe - 2 * a1 * a2 * x3 * xe - a1 * x3**2 * xe + a1 * xe**3 + a1 * xe * ye**2 - math.sqrt(-a1**2 * ye**2 * (a1**4 + (a2**2 + 2 * a2 * x3 + x3**2 - xe**2 - ye**2)**2 - 2 * a1**2 * (a2**2 + 2 * a2 * x3 + x3**2 + xe**2 + ye**2))))/(a1**2 * (xe**2 + ye**2)))


	 	theta2A = math.atan2(-(math.sqrt(-a1**2 * ye**2 *(a1**4 + (a2**2 + 2*a2*x3 + x3**2 - xe**2 - ye**2)**2 - 2 * a1**2 * (a2**2 + 2*a2*x3 + x3**2 + xe**2 + ye**2)))/(a1**2 *(a2 + x3) * ye)), -((a1**2 + a2**2 + 2*a2*x3 + x3**2 - xe**2 - ye**2)/(a1* a2 + a1 * x3)))

	 	theta1B = math.atan2(1/(a1**2 * ye * (xe**2 + ye**2)) * (a1**3 * ye**2 - a1 * a2**2 * ye**2 - 2 * a1 * a2 * x3 * ye**2 - a1 * x3**2 * ye**2 + a1 * xe**2 * ye**2 + a1 * ye**4 - xe * math.sqrt(-a1**2 * ye**2 * (a1**4 + (a2**2 + 2 * a2 * x3 + x3**2 - xe**2 - ye**2)**2 - 2 * a1**2 * (a2**2 + 2 * a2 * x3 + x3**2 + xe**2 + ye**2)))),(a1**3 * xe - a1 * a2**2  * xe - 2 * a1 * a2 * x3 * xe - a1 * x3**2 * xe + a1 * xe**3 + a1 * xe * ye**2 + math.sqrt(-a1**2 * ye**2 * (a1**4 + (a2**2 + 2 * a2 * x3 + x3**2 - xe**2 - ye**2)**2 - 2 * a1**2 * (a2**2 + 2 * a2 * x3 + x3**2 + xe**2 + ye**2))))/(a1**2 * (xe**2 + ye**2)))

	 	theta2B = math.atan2((math.sqrt(-a1**2 * ye**2 *(a1**4 + (a2**2 + 2*a2*x3 + x3**2 - xe**2 - ye**2)**2 - 2 * a1**2 * (a2**2 + 2*a2*x3 + x3**2 + xe**2 + ye**2)))/(a1**2 *(a2 + x3) * ye)), -((a1**2 + a2**2 + 2*a2*x3 + x3**2 - xe**2 - ye**2)/(a1* a2 + a1 * x3)))

	 	if math.fabs(self.theta1 - theta1A) < (self.theta1 - theta1B):
	 		self.theta1 = theta1A
	 		self.theta2 = theta2A
	 	else:
	 		self.theta1 = theta1B
	 		self.theta2 = theta2B


if __name__=='__main__':
	myArm = arm()
	myArm.findAngles(332.152,0.000000001)