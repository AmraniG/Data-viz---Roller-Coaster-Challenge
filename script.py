import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
wood = pd.read_csv("C:\\Users\\Ghisl\\OneDrive\\Documents\\Formations\Python\\roller_coaster_starting\\Golden_Ticket_Award_Winners_Wood.csv")
steel = pd.read_csv("C:\\Users\\Ghisl\\OneDrive\\Documents\\Formations\Python\\roller_coaster_starting\\Golden_Ticket_Award_Winners_Steel.csv")
roller_coaster = pd.read_csv("C:\\Users\\Ghisl\\OneDrive\\Documents\\Formations\Python\\roller_coaster_starting\\roller_coasters.csv")

print(wood.head())
print(steel.head())


# write function to plot rankings over time for 1 roller coaster here:
def ranking_over_time(name, park, df):
  selected_rollercoaster = df[(df.Name == name) & (df.Park == park) ]
  x_values = selected_rollercoaster['Year of Rank']
  y_values = selected_rollercoaster['Rank']
  plt.figure(figsize = (10,8))
  plt.plot(x_values, y_values)
  plt.xlabel('Years')
  plt.ylabel('Rank')
  ax = plt.subplot()
  ax.set_yticks(range(len(y_values)))
  plt.show()

ranking_over_time('El Toro', 'Six Flags Great Adventure', wood)


# write function to plot rankings over time for 2 roller coasters here:
def ranking_over_time_2(name1, park1, name2, park2, df):
  selected_rollercoaster_1 = df[(df.Name == name1) & (df.Park == park1)]
  selected_rollercoaster_2 = df[(df.Name == name2) & (df.Park == park2)]
  x_values = selected_rollercoaster_1['Year of Rank']
  y_values_1 = selected_rollercoaster_1['Rank']
  y_values_2 = selected_rollercoaster_2['Rank']
  plt.figure(figsize = (10,8))
  plt.plot(x_values, y_values_1)
  plt.plot(x_values, y_values_2)
  plt.xlabel('Years')
  plt.ylabel('Rank')
  plt.legend([name1+'-'+park1, name2+'-'+park2])
  max_y = max(len(y_values_1), len(y_values_2))
  ax = plt.subplot()
  ax.set_yticks(range(max_y))
  plt.show()

ranking_over_time_2('El Toro','Six Flags Great Adventure', 'Boulder Dash', 'Lake Compounce', wood)


# write function to plot top n rankings over time here:

def plot_n_ranking(n, df):
  selected_df = df[(df.Rank <= n)]
  pivot = selected_df.groupby(['Year of Rank', 'Name']).Rank.sum().reset_index().pivot(columns = 'Year of Rank', index = 'Name', values = 'Rank')
  #print(pivot.iloc[0])
  #print(len(pivot))
  #print(pivot.index.values)
  for i in range(len(pivot)):
    plt.plot(pivot.iloc[i])
    plt.legend(pivot.index.values, loc='upper left', bbox_to_anchor=(1.1, 1.05))
  plt.show()

 
def plot_n_ranking_v2(n, rankings_df):
  top_n_rankings = rankings_df[rankings_df['Rank'] <= n]
  for coaster in set(top_n_rankings['Name']):
    coaster_rankings = top_n_rankings[top_n_rankings['Name'] == coaster]
    plt.plot(coaster_rankings['Year of Rank'],coaster_rankings['Rank'],label=coaster)
  plt.show()

plot_n_ranking_v2(10, wood)
plot_n_ranking(10, wood)



# write function to plot histogram of column values here:
def func_hist(colonne, df):
  plt.figure(figsize = (10,8))
  plt.hist(df[colonne], range = (1,240), bins = 30)
  legend = [colonne]
  plt.legend(legend)
  plt.xlabel(colonne)
  plt.ylabel('Number of Roller Coasters')
  plt.axis([0, 240, 0, 250])
  ax = plt.subplot()
  plt.show()

func_hist('speed', roller_coaster)

# write function to plot inversions by coaster at a park here:

def inversion(park, df):
  selected_df = df[(df.park == park)]
  x_values = selected_df['name']
  print(range(len(x_values)))
  y_values = selected_df['num_inversions']
  plt.figure(figsize = (10,8))
  plt.bar(range(len(x_values)), y_values)
  plt.title('Number of inversions of rollercoasters in a dedicated park')
  plt.xlabel('Name of rollercoaster')
  plt.ylabel('Number of inversions')
  ax = plt.subplot()
  ax.set_xticks(range(len(x_values)))
  ax.set_yticks(range(len(y_values)))
  ax.set_xticklabels(x_values)
  ax.set_yticklabels(y_values)
  plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
  plt.show()

inversion('Parc Asterix', roller_coaster)
plt.clf()


# write function to plot pie chart of operating status here:
def status(df):
  operating = df[df.status == 'status.operating']
  closed = df[df.status == 'status.closed.definitely']
  plt.pie([len(operating), len(closed)], labels =['operating', 'closed'], autopct = '%d%%')
  plt.axis('equal')
  plt.show()


status(roller_coaster)
plt.clf()

  
# write function to create scatter plot of any two numeric columns here:

def func_scatter(param1, param2, df):
  plt.figure(figsize = (10,8))
  plt.scatter(df[param1], df[param2])
  plt.xlabel(param1)
  plt.ylabel(param2)
  plt.axis([0,250, 0,250])
  plt.show()

func_scatter('speed', 'height', roller_coaster)


plt.clf()

#What roller coaster seating type is most popular?
new_df = roller_coaster.groupby('seating_type').name.count().reset_index()
plt.pie(new_df.name, labels =new_df.seating_type, autopct = '%d%%')
plt.axis('equal')
plt.show()

plt.clf()

#Do different seating types result in faster roller coasters?
new_df_2 = roller_coaster.groupby('seating_type').speed.mean().reset_index()
new_df_2.sort_values('speed',inplace=True)
plt.figure(figsize = (10,8))
plt.bar(range(len(new_df_2.seating_type)), new_df_2.speed)
plt.xlabel('seating_type')
plt.ylabel('speed')
ax = plt.subplot()
ax.set_xticks(range(len(new_df_2.seating_type)))
ax.set_xticklabels(new_df_2.seating_type)
plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
plt.show()
print(new_df_2)

# Do roller coaster manufacturers have any specialties (do they focus on speed, height, seating type, or inversions)?
new_df_3 = roller_coaster.groupby('manufacturer').mean().reset_index()
plt.figure(figsize = (10,8))
plt.scatter(new_df_3.length, new_df_3.height, new_df_3.speed)
plt.xlabel('Length')
plt.ylabel('Height')
plt.show()
print(new_df_3)
