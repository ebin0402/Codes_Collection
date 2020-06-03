import intake
print(__name__)
mean=sum(intake.nums)/len(intake.nums)
print("Mean: {}".format(round(mean,2)))