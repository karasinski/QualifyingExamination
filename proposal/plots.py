import matplotlib
from matplotlib.lines import Line2D
matplotlib.rcParams.update({'errorbar.capsize': 2})

def threeway(sub_design):
	colors = sns.color_palette()
	agg = sub_design.groupby(('device', 'startdesign', 'order', 'design')).Zrmse.agg(['mean', 'sem']).reset_index()
	agg['designlabels'] = agg.design.replace((1, 2, 3), ('Baseline', 'Feedback', 'Rotated'))

	f, axes = plt.subplots(1, 3, sharey=True, figsize=(8,3.5))
	for i, ax in enumerate(axes):
		startdesign = i + 1
		for _, (device, linestyle) in enumerate(zip(['lcd', 'hololens'], ['-', '--'])):
			data = agg.query('startdesign == @startdesign and device == @device')
			offset = -0.1
			if device == 'hololens':
				offset = 0.1

			data['order'] += offset
			data.plot(x='order', y='mean', color='k', linestyle=linestyle, ax=ax, legend=False, alpha=0.5)
			data['order'] -= offset

			ax.plot(x=(offset + data['design']).values, y=data['mean'].values, color='k', linestyle=linestyle)
			for order in [1, 2, 3]:
				d = data.query('order == @order')
				design = int(d['design']) - 1
				ax.errorbar(x=offset + d['order'], y=d['mean'], yerr=d['sem'], color=colors[design])

	for i, ax in enumerate(axes):
		ax.set_xlabel('')

	axes[0].set_ylabel('Normalized RMSE ($z$-axis)')

	axes[0].set_xticks([1, 2, 3])
	axes[1].set_xticks([1, 2, 3])
	axes[2].set_xticks([1, 2, 3])
	axes[0].set_xticklabels(['Baseline', 'Feedback', 'Rotated'], rotation=45, ha='center')
	axes[1].set_xticklabels(['Feedback', 'Rotated', 'Baseline'], rotation=45, ha='center')
	axes[2].set_xticklabels(['Rotated', 'Baseline', 'Feedback'], rotation=45, ha='center')
	axes[0].set_title('(a)')
	axes[1].set_title('(b)')
	axes[2].set_title('(c)')

	display = [Line2D([0], [0], color='k', lw=1, ls='-'),
	           Line2D([0], [0], color='k', lw=1, ls='--')]
	designs =[Line2D([0], [0], color=colors[0], lw=1, ls='-'),
	          Line2D([0], [0], color=colors[1], lw=1, ls='-'),
	          Line2D([0], [0], color=colors[2], lw=1, ls='-')]

	legend1 = ax.legend(display, ['2D', '3D           '], loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0, title='Display')
	# legend2 = ax.legend(designs, ['Baseline', 'Feedback', 'Rotated'], loc='lower left', bbox_to_anchor=(1.05, 0), borderaxespad=0, title='Design')
	plt.gca().add_artist(legend1)
	# plt.gca().add_artist(legend2)

	plt.tight_layout()
	plt.savefig('/Users/jkarasin/Desktop/3way.pdf')
	plt.show()

def twoway(sub_design):
	sub_design['ff'] = sub_design.startdesign == 2
	agg = sub_design.groupby(('device', 'ff', 'design')).Zrmse.agg(['mean', 'sem']).reset_index()
	# agg = sub_design.groupby(('device', 'ff', 'design')).Score.agg(['mean', 'sem']).reset_index()

	f, axes = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(6,3.5))
	for i, (ax, ff) in enumerate(zip(axes, [False, True])):
		for _, (device, markerstyle) in enumerate(zip(['lcd', 'hololens'], ['x', 'o'])):
			data = agg.query('ff == @ff and device == @device')
			offset = -0.1
			if device == 'hololens':
				offset = 0.1

			for design in [1, 2, 3]:
				d = data.query('design == @design')
				design = int(d['design']) - 1
				ax.errorbar(x=offset + d['design'], y=d['mean'], yerr=d['sem'], color=colors[design], marker=markerstyle)

	for ax in axes:
		ax.set_xlabel('')
		ax.set_xticks([1, 2, 3])
		ax.set_xticklabels(['Baseline', 'Feedback', 'Rotated'], rotation=45, ha='center')

	axes[0].set_ylabel('Normalized RMSE ($z$-axis)')
	# axes[0].set_ylabel('NASA-TLX Workload')
	axes[0].set_title('(a)')
	axes[1].set_title('(b)')

	display = [Line2D([0], [0], color='k', lw=1, ls='None',marker='x'),
	           Line2D([0], [0], color='k', lw=1, ls='None', marker='o')]
	designs =[Line2D([0], [0], color=colors[0], lw=1, ls='-'),
	          Line2D([0], [0], color=colors[1], lw=1, ls='-'),
	          Line2D([0], [0], color=colors[2], lw=1, ls='-')]

	legend1 = ax.legend(display, ['2D', '3D           '], loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0, title='Display')
	# legend2 = ax.legend(designs, ['Baseline', 'Feedback', 'Rotated'], loc='lower left', bbox_to_anchor=(1.05, 0), borderaxespad=0, title='Design')
	plt.gca().add_artist(legend1)
	# plt.gca().add_artist(legend2)

	plt.gcf().subplots_adjust(bottom=0.2)
	plt.gcf().subplots_adjust(right=0.75)
	plt.savefig('/Users/jkarasin/Desktop/2way.pdf')
	# plt.savefig('/Users/jkarasin/Desktop/2way-work.pdf')
	plt.show()
