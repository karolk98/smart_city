from os import walk
import pandas as pd
import statistics as stats

import arff

COLNAMES = ['versionID','line','brigade','time','lon','lat','rawLow','rawLat','status','delay','delayAtStop','plannedLeaveTime','nearestStop',
'nearestStopDistance','nearestStopLon','nearestStopLat','previousStop','previousStopLon','previousStopLat','previousStopDistance','previousStopArrivalTime',
'previousStopLeaveTime','nextStop','nextStopLon','nextStopLat','nextStopDistance','nextStopTimetableVisitTime','courseIdentifier',
'courseDirection','timetableIdentifier','timetableStatus','receivedTime','processingFinishedTime','onWayToDepot','overlapsWithNextBrigade','overlapsWithNextBrigadeStopLineBrigade',
'atStop','speed','oldDelay','serverId','delayAtStopStopSequence','previousStopStopSequence','nextStopStopSequence','delayAtStopStopId','previousStopStopId','nextStopStopId',
'courseDirectionStopStopId']
COLS_FOR_ARFF = ['domain','time','lon','lat','nearestStopLon','nearestStopLat','nextStopDistance','speed','delay','class']
# COLS_FOR_ARFF = ['domain','line','previousDelay','previousLon','previousLat','previousNextStopDistance','previousSpeed','time','delay','lon','lat','nearestStopLon','nearestStopLat','nextStopDistance','speed','class']
FINAL_COLS = ['domain','time','delay','lon','lat','nearestStopLon','nearestStopLat','nextStopDistance','speed','class']
# FINAL_COLS = ['domain','previousDelay','previousLon','previousLat','previousNextStopDistance','previousSpeed','time','delay','lon','lat','nearestStopLon','nearestStopLat','nextStopDistance','speed','class']
# src1 = pd.read_csv('new_labels/buses-context-09-03.csv')
# src1['domain'] = 1
# src2 = pd.read_csv('new_labels/buses-context-09-04.csv')
# src2['domain'] = 1
# src3 = pd.read_csv('new_labels/buses-context-09-05.csv')
# src3['domain'] = 1
# src4 = pd.read_csv('new_labels/buses-context-09-06.csv')
# src4 = src4[src4['line']!=157]
# src4['domain'] = 1
# src5 = pd.read_csv('new_labels/buses-context-09-07.csv')
# src5['domain'] = 1

tar = pd.read_csv('new_labels/buses-context-09-07.csv')
tar = tar[tar['line']==157]
tar['domain'] = 0
# together = tar[COLS_FOR_ARFF]
together = pd.concat([ tar])[COLS_FOR_ARFF]
together = together.dropna()
together.index = pd.to_datetime(together['time'])
#clipping
# together = together.between_time('08:00:00', '09:00:00')
# together['lon'] = together['lon']-min(together['lon'])
# together['lat'] = together['lat']-min(together['lat'])
together['time'] = (pd.to_datetime(together['time'], format='%Y-%m-%d %H:%M:%S')-min(pd.to_datetime(together['time'], format='%Y-%m-%d %H:%M:%S'))).dt.total_seconds().astype(int)
# together = together[~together['class'].isnull()]
# together = together[~together['delay'].isnull()]
together['class'] = (together['class']>60)*1
together = together[(together['delay']<=1000)&(together['delay']>=-1000)]
together = together[(together['class']<=5)&(together['class']>=-2)]
together.reset_index(drop = True, inplace = True)
# together = together.sort_values(['domain','time'], ascending=[False, True])
together = together.sort_values('time')
# together['class'] = together['delay']
# together.drop(columns=['delay'], inplace=True)
# filter square
std_lat = 0.009043717
mean_lat = 52.241131879291316
std_lon = 0.01466772684
mean_lon = 20.99125392463334
tol = 1.5
together = together[
            (together.lat > mean_lat - tol * std_lat)
            & (together.lat < mean_lat + tol * std_lat)
            & (together.lon > mean_lon - tol * std_lon)
            & (together.lon < mean_lon + tol * std_lon)]

# together = together[(together['line']==17)|(together['domain']==1)]
together = together[FINAL_COLS]
maj_c = together[together.domain==0].mode()['class'][0]
maj_percent = sum((together.domain==0) & (together['class']==maj_c))/sum(together.domain==0)
title = f'{maj_c}_{maj_percent}_{sum(together["domain"].astype(int)==0)}_{len(together)}_reads'
# together.drop(columns=['domain'], inplace=True)
arff.dump('../moa-18.06.0/DataSet/ztm5_2/alt.arff'
      , together.values
      , relation=title
      , names=together.columns)

# print(sum(together['class'].astype(int)==0))
# print(sum(together['class'].astype(int)==1))
print(','.join(str(i) for i in pd.unique(together['class'])))
print(title)