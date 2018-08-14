def threeway(sub_design):
	import matplotlib
	from matplotlib.lines import Line2D
	matplotlib.rcParams.update({'errorbar.capsize': 2})

	colors = sns.color_palette()
	agg = sub_design.groupby(('device', 'startdesign', 'order', 'design')).Zrmse.agg(['mean', 'sem']).reset_index()

	f, axes = plt.subplots(1, 3, sharex=True, sharey=True, figsize=(8,3))
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

	for ax in axes:
		ax.set_xlabel('')
		# ax.set_xticks([])
		ax.set_xticklabels(['', '', ''])

	axes[0].set_ylabel('Z RMSE')
	axes[1].set_xlabel('Order')

	display = [Line2D([0], [0], color='k', lw=1, ls='-'),
	           Line2D([0], [0], color='k', lw=1, ls='--')]
	designs =[Line2D([0], [0], color=colors[0], lw=1, ls='-'),
	          Line2D([0], [0], color=colors[1], lw=1, ls='-'),
	          Line2D([0], [0], color=colors[2], lw=1, ls='-')]

	legend1 = ax.legend(display, ['2D', '3D           '], loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0, title='Display')
	legend2 = ax.legend(designs, ['Baseline', 'Feedback', 'Angled'], loc='lower left', bbox_to_anchor=(1.05, 0), borderaxespad=0, title='Design')
	plt.gca().add_artist(legend1)
	plt.gca().add_artist(legend2)

	plt.tight_layout()
	plt.show()

def twoway(sub_design):
	sub_design['ff'] = sub_design.startdesign == 2
	agg = sub_design.groupby(('device', 'ff', 'design')).Zrmse.agg(['mean', 'sem']).reset_index()

	f, axes = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(6,3))
	for i, (ax, ff) in enumerate(zip(axes, [False, True])):
		for _, (device, linestyle) in enumerate(zip(['lcd', 'hololens'], ['-', '--'])):
			data = agg.query('ff == @ff and device == @device')
			offset = -0.1
			if device == 'hololens':
				offset = 0.1

			data['design'] += offset
			data.plot(x='design', y='mean', color='k', linestyle=linestyle, ax=ax, legend=False, alpha=0.5)
			data['design'] -= offset

			ax.plot(x=(offset + data['design']).values, y=data['mean'].values, color='k', linestyle=linestyle)
			for design in [1, 2, 3]:
				d = data.query('design == @design')
				design = int(d['design']) - 1
				ax.errorbar(x=offset + d['design'], y=d['mean'], yerr=d['sem'], color=colors[design])

	for ax in axes:
		ax.set_xlabel('')
		ax.set_xticks([1, 2, 3])
		ax.set_xticklabels(['', '', ''])

	axes[0].set_ylabel('Z RMSE')
	axes[0].set_title('Start without Feedback')
	axes[1].set_title('Start with Feedback')

	display = [Line2D([0], [0], color='k', lw=1, ls='-'),
	           Line2D([0], [0], color='k', lw=1, ls='--')]
	designs =[Line2D([0], [0], color=colors[0], lw=1, ls='-'),
	          Line2D([0], [0], color=colors[1], lw=1, ls='-'),
	          Line2D([0], [0], color=colors[2], lw=1, ls='-')]

	legend1 = ax.legend(display, ['2D', '3D           '], loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0, title='Display')
	legend2 = ax.legend(designs, ['Baseline', 'Feedback', 'Angled'], loc='lower left', bbox_to_anchor=(1.05, 0), borderaxespad=0, title='Design')
	plt.gca().add_artist(legend1)
	plt.gca().add_artist(legend2)

	plt.tight_layout()
	plt.show()
