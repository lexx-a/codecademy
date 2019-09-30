import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

## 1. Analyzing Ad Sources
# print(ad_clicks)
# print(ad_clicks.head())
utm_source_views = ad_clicks.groupby('utm_source').\
										user_id.count().\
										reset_index()
# print(utm_source_views)

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
# print(ad_clicks.head())

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
clicks_pivots = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
).reset_index()
clicks_pivots['percent_clicked'] = clicks_pivots[True] / (clicks_pivots[True] + clicks_pivots[False])
# print(clicks_pivots)
# print(clicks_pivots.columns)


## 2. Analyzing an A/B Test
print(ad_clicks.head())
experimental_groups_shows = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
# print(experimental_groups_shows)
experimental_group_clicks = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
# print(experimental_group_clicks)
experimental_group_clicks_pivot = experimental_group_clicks.pivot(
  columns = 'is_click',
  index = 'experimental_group',
  values = 'user_id'
)
experimental_group_clicks_pivot['clicks_rate'] = experimental_group_clicks_pivot[True] / (experimental_group_clicks_pivot[True] + experimental_group_clicks_pivot[False])
print(experimental_group_clicks_pivot)

a_clicks = ad_clicks[ad_clicks.experimental_group=='A']
b_clicks = ad_clicks[ad_clicks.experimental_group=='B']

#A_group
a_clicks_by_day = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
# print(a_clicks_by_day)
a_clicks_by_day_pivot = a_clicks_by_day.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
)
a_clicks_by_day_pivot['a_clicks_rate'] = a_clicks_by_day_pivot[True] / (a_clicks_by_day_pivot[True] + a_clicks_by_day_pivot[False])

#B_group
b_clicks_by_day = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
# print(b_clicks_by_day)
b_clicks_by_day_pivot = b_clicks_by_day.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
)
b_clicks_by_day_pivot['b_clicks_rate'] = b_clicks_by_day_pivot[True] / (b_clicks_by_day_pivot[True] + b_clicks_by_day_pivot[False])

print(a_clicks_by_day_pivot)
print(b_clicks_by_day_pivot)
