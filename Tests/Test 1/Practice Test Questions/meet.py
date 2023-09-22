#  File: Meet.py

#  Description: Determine earlist meet time interval for two people

#  Student Name: Abhinav Achuta

#  Student UT EID: aa85934

#  Course Name: CS 313E

#  Unique Number: 86610

import sys

def find_durations(list):

	durations = []

	for frame in list:
		durations.append(frame[1] - frame[0])
	
	return max(durations)

def frame_that_fits(list, duration):
	
	frames_that_fit = []

	for frame in list:
		if (frame[1] - frame[0]) >= duration:
			frames_that_fit.append(frame)
	return frames_that_fit

def earliestPossibleMeeting(person1, person2, duration):
		'''
		person1: List[List[int]]
		person2: List[List[int]]
		duration: int
		return type: List[int]
	'''

		person1_durations = find_durations(person1)
		person2_durations = find_durations(person2)


		if duration > person1_durations or duration > person2_durations:
			return []

		else:
			
			person1_frames = frame_that_fits(person1, duration)
			person1_frames.sort()
			person2_frames = frame_that_fits(person2, duration)
			person2_frames.sort()

			possible_times = []

			for time in person1_frames:

				for other_time in person2_frames:

					if time[1] >= other_time[0] and time[0] <= other_time[1]:
						possible_times.append([max(time[0], other_time[0]), min(time[1], other_time[1])])

					possible_times_w_duration = []

					for set in possible_times:
						if set[1] - set[0] >= duration:
							possible_times_w_duration.append([set[0], set[0]+duration])
			
			if possible_times_w_duration != []:
				return possible_times_w_duration[0]
			else:
				return []


def main():
        #test_cases()

	# read the input data and create a list of lists for each person
	f = sys.stdin
	# read in the duration
	dur = int(f.readline().strip())
	# person 1's number of avalible slots
	num1 = int(f.readline().strip())
	p1 = []
	for x in range(num1):
		line = f.readline()
		l = line.strip().split()
		tmp = [int(l[0]), int(l[1])]
		p1.append(tmp)

	# person 2's number of avalible slots
	num2 = int(f.readline().strip())
	p2 = []
	for x in range(num2):
		line = f.readline()
		l = line.strip().split()
		tmp = [int(l[0]), int(l[1])]
		p2.append(tmp)

	print(earliestPossibleMeeting(p1,p2,dur))

if __name__ == "__main__":
  main()
