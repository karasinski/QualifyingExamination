import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def robot_estimate():
    with plt.xkcd():
        f, ax = plt.subplots()
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        plt.xticks([])
        plt.yticks([])

        no_feedback = 0.2 + 3*1/np.exp(0.1*np.linspace(1, 30, 100))
        yes_feedback = 1/np.exp(0.1*np.linspace(1, 30, 100))

        ax.plot(no_feedback, color='r', label='Terminal Feedback')
        ax.plot(yes_feedback, color='b', label='Concurrent Feedback')

        plt.axvline(x=80, ls='--', color='k', alpha=0.3)
        plt.text(82,2,'Retention Trials',rotation=90)

        plt.ylabel('Completion Time or Error')
        plt.xlabel('Trial')
        plt.legend(loc='upper right')
        plt.savefig('/Users/jkarasin/Desktop/robot_estimate.pdf')
        plt.close('all')


def hess_replication_plots():
    alp = pd.read_excel('adaptive_limited_pilot.xlsx')
    ulp = pd.read_excel('unadaptive_limited_pilot.xlsx')

    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

    f, ax = plt.subplots(2, sharex=True)
    # Slide 1
    # ulp.plot(x='t', y=['c1'], ax=ax[0], color=colors[0], legend=False, label=['$c$'])

    # Slide 2
    # ulp.plot(x='t', y=['c1'], ax=ax[0], color=colors[0], legend=False, label=['$c$'])
    # ulp.plot(x='t', y=['m1'], ax=ax[0], color=colors[1], legend=False, label=['$m$'])

    # ulp.plot(x='t', y=['kr1'], ax=ax[1], color=colors[2], legend=False, label=['$k_{r}$'])
    # ulp.plot(x='t', y=['kp1'], ax=ax[1], color=colors[3], legend=False, label=['$k_{p}$'])

    # Slide 3
    alp.plot(x='t', y=['c1'], ax=ax[0], color=colors[0], legend=False, label=['$c$'])
    ulp.plot(x='t', y=['m1'], ax=ax[0], color=colors[1], legend=False, ls='--', alpha=0.3, label=['$m$'])
    alp.plot(x='t', y=['m1'], ax=ax[0], color=colors[1], legend=False, label=['$m$'])

    ulp.plot(x='t', y=['kr1'], ax=ax[1], color=colors[2], legend=False, ls='--', alpha=0.3, label=['$k_{r}$'])
    alp.plot(x='t', y=['kr1'], ax=ax[1], color=colors[2], legend=False, label=['$k_{r}$'])
    ulp.plot(x='t', y=['kp1'], ax=ax[1], color=colors[3], legend=False, ls='--', alpha=0.3, label=['$k_{p}$'])
    alp.plot(x='t', y=['kp1'], ax=ax[1], color=colors[3], legend=False, label=['$k_{p}$'])

    ax[0].axvline(x=50, ls='--', color='k')
    ax[1].axvline(x=50, ls='--', color='k')
    plt.xlim(40, 80)
    plt.xticks([])
    ax[0].set_yticks([])
    ax[1].set_yticks([])
    plt.xlabel('Time')
    ax[0].legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax[1].legend(loc='center left', bbox_to_anchor=(1, 0.5))
    # ax[0].set_title('Pursuit Tracking Task')
    ax[0].set_title('Performance without Adaptataion')
    ax[0].set_ylim(ylim)
    plt.gcf().subplots_adjust(right=0.85)
    plt.savefig('/Users/jkarasin/Desktop/hess_model2.pdf')
    plt.show()

def feedback_plots():
    alp = pd.read_excel('adaptive_limited_pilot.xlsx')

    alp['e1'] = alp['c1'] - alp['m1']
    alp[['c1', 'm1', 'e1']] *= 57
    alp['cbf'] = (alp['e1'].abs() > 1.5).astype(int)
    df = alp[['t', 'c1', 'm1', 'e1', 'cbf']].query('t < 40')
    df.columns = ['t', 'c', 'm', 'e', 'cbf']
    cbf_off = np.ma.masked_where(df.e.abs() <= 1.5, df.e)
    cbf_on = np.ma.masked_where(df.e.abs() > 1.5, df.e)

    f, ax = plt.subplots()
    ax.plot(df.t, df.e, color='k')

    plt.xticks([])
    ax.set_yticks([])
    plt.xlabel('Time')
    ax.set_ylabel('Error')
    plt.xlim([0, 40])

    plt.savefig('/Users/jkarasin/Desktop/error_example1.pdf')
    plt.show()

    f, ax = plt.subplots()
    ax.plot(df.t, df.e, color='k')
    ax.axhline(y=1.5, color='k', alpha=0.5, ls='--')
    ax.axhline(y=-1.5, color='k', alpha=0.5, ls='--')

    plt.xticks([])
    ax.set_yticks([])
    plt.xlabel('Time')
    ax.set_ylabel('Error')
    plt.xlim([0, 40])

    plt.savefig('/Users/jkarasin/Desktop/error_example2.pdf')
    plt.show()

    f, ax = plt.subplots()
    ax.plot(df.t, cbf_off, color='red')
    ax.plot(df.t, cbf_on, color='green')
    ax.axhline(y=1.5, color='k', alpha=0.5, ls='--')
    ax.axhline(y=-1.5, color='k', alpha=0.5, ls='--')

    plt.xticks([])
    ax.set_yticks([])
    plt.xlabel('Time')
    ax.set_ylabel('Error')
    plt.xlim([0, 40])

    plt.savefig('/Users/jkarasin/Desktop/error_example3.pdf')
    plt.show()
