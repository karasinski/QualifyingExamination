import pandas as pd
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



alp = pd.read_excel('adaptive_limited_pilot.xlsx')
ulp = pd.read_excel('unadaptive_limited_pilot.xlsx')

colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

f, ax = plt.subplots(2, sharex=True)
ulp.plot(x='t', y=['c1'], ax=ax[0], color=colors[0], legend=False, label=['$c$'])
ulp.plot(x='t', y=['m1'], ax=ax[0], color=colors[1], legend=False, label=['$m$'])

ulp.plot(x='t', y=['kr1'], ax=ax[1], color=colors[2], legend=False, label=['$k_{r}$'])
ulp.plot(x='t', y=['kp1'], ax=ax[1], color=colors[3], legend=False, label=['$k_{p}$'])

# alp.plot(x='t', y=['c1'], ax=ax[0], color=colors[0], legend=False, label=['$c$'])
# ulp.plot(x='t', y=['m1'], ax=ax[0], color=colors[1], legend=False, ls='--', alpha=0.5, label=['$m$'])
# alp.plot(x='t', y=['m1'], ax=ax[0], color=colors[1], legend=False, label=['$m$'])

# ulp.plot(x='t', y=['kr1'], ax=ax[1], color=colors[2], legend=False, ls='--', alpha=0.5, label=['$k_{r}$'])
# alp.plot(x='t', y=['kr1'], ax=ax[1], color=colors[2], legend=False, label=['$k_{r}$'])
# ulp.plot(x='t', y=['kp1'], ax=ax[1], color=colors[3], legend=False, ls='--', alpha=0.5, label=['$k_{p}$'])
# alp.plot(x='t', y=['kp1'], ax=ax[1], color=colors[3], legend=False, label=['$k_{p}$'])

ax[0].axvline(x=50, ls='--', color='k')
ax[1].axvline(x=50, ls='--', color='k')
plt.xlim(40, 80)
plt.xticks([])
ax[0].set_yticks([])
ax[1].set_yticks([])
plt.xlabel('Time')
ax[0].legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax[1].legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax[0].set_title('Performance without Adaptation')
plt.tight_layout()
plt.savefig('/Users/jkarasin/Desktop/hess_model1.pdf')
plt.show()



f, ax = plt.subplots(2, sharex=True, sharey=True)
ax[0].axvline(x=50, ls='--', color='k')
ax[1].axvline(x=50, ls='--', color='k')
plt.xlim(40, 80)
plt.xticks([])
plt.yticks([])
plt.xlabel('Time')
plt.tight_layout()
plt.show()


# alp.plot(x='t', y=['del1'])
# alp.plot(x='t', y=['kr1', 'kp1'])
# plt.show()
# ulp.plot(x='t', y=['del1'])
