from matplotlib import pyplot as plt
import numpy as np

with plt.xkcd():

	# plt.rcParams.update({
	#     # "lines.color": "black",
	#     # "patch.edgecolor": "black",
	#     "text.color": "#FAFAFA",
	#     # "axes.facecolor": "black",
	#     "axes.edgecolor": "lightgray",
	#     # "axes.labelcolor": "black",
	#     # "xtick.color": "black",
	#     # "ytick.color": "black",
	#     "grid.color": "lightgray",
	#     "figure.facecolor": "#FAFAFA",
	#     "figure.edgecolor": "#FAFAFA",
	#     "savefig.facecolor": "#FAFAFA",
	#     "savefig.edgecolor": "#FAFAFA"})

	f, ax = plt.subplots()
	# f.set_facecolor('#FAFAFA')
	# ax.set_facecolor('#FAFAFA')
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	plt.xticks([])
	plt.yticks([])

	# plt.annotate(
	#     'THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED',
	#     xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

	no_feedback = 0.2 + 3*1/np.exp(0.1*np.arange(100))
	yes_feedback = 1/np.exp(0.1*np.arange(100))

	ax.plot(no_feedback, color='r', label='Terminal Feedback')
	ax.plot(yes_feedback, color='b', label='Concurrent Feedback')

	plt.xlim(0, 30)

	plt.ylabel('time/error')
	plt.xlabel('time')
	plt.legend()
	plt.savefig('/Users/jkarasin/Desktop/robot_estimate.pdf')
	plt.close('all')
