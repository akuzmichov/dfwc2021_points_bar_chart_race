#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import bar_chart_race as bcr
import matplotlib as plt
plt.rc('axes', unicode_minus=False)


# CPM
cpm = pd.read_csv('cpm_rounds.csv').drop(['rank'], axis=1)
cpm_pivoted = cpm.pivot_table('points', ['round_number'], 'nick').fillna(0)
cpm_pivoted.iloc[:, 1:-1] = cpm_pivoted.iloc[:, 1:-1].cumsum()
bcr.bar_chart_race(df=cpm_pivoted, title='DFWC2021: Points after rounds', n_bars=30, steps_per_period=60, 
                   interpolate_period=False,
                   period_length=2000, dpi=600, filter_column_colors=True, period_fmt='Round {x:.0f}',
                   shared_fontdict={'family': 'Consolas', 'weight': 'normal'},
                   filename='dfwc2021_cpm_standings_race.mp4')


# VQ3
vq3 = pd.read_csv('vq3_rounds.csv').drop(['rank'], axis=1)
vq3_pivoted = vq3.pivot_table('points', ['round_number'], 'nick').fillna(0)
vq3_pivoted.iloc[:, 1:-1] = vq3_pivoted.iloc[:, 1:-1].cumsum()
bcr.bar_chart_race(df=vq3_pivoted, title='DFWC2021: Points after rounds', n_bars=30, steps_per_period=60, 
                   interpolate_period=False,
                   period_length=2000, dpi=600, filter_column_colors=True, period_fmt='Round {x:.0f}',
                   shared_fontdict={'family': 'Consolas', 'weight': 'normal'},
                   filename='dfwc2021_vq3_standings_race.mp4')
