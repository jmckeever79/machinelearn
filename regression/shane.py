import numpy
import matplotlib
matplotlib.use('QT4Agg')

import matplotlib.pyplot as plt
from linear_regression import studentReg
from class_vis import prettyPicture, output_image

from ages_net_worths import ageNetWorthData

ages_train, ages_test, net_worths_train, net_worths_test = ageNetWorthData()

reg = studentReg(ages_train, net_worths_train)

s = reg.score(ages_test, net_worths_test)

print('score: {0}'.format(s))
print('slope: {0}'.format(reg.coef_))
print('intercept: {0}'.format(reg.intercept_))


plt.clf()
plt.scatter(ages_train, net_worths_train, color="b", label="train data")
plt.scatter(ages_test, net_worths_test, color="r", label="test data")
plt.plot(ages_test, reg.predict(ages_test), color="black")
plt.legend(loc=2)
plt.xlabel("ages")
plt.ylabel("net worths")

plt.show()
