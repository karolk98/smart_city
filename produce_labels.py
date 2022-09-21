from os import walk
import pandas as pd
import statistics as stats
from datetime import timedelta as td


COLNAMES = ['versionID','line','brigade','time','lon','lat','rawLow','rawLat','status','delay','delayAtStop','plannedLeaveTime','nearestStop',
'nearestStopDistance','nearestStopLon','nearestStopLat','previousStop','previousStopLon','previousStopLat','previousStopDistance','previousStopArrivalTime',
'previousStopLeaveTime','nextStop','nextStopLon','nextStopLat','nextStopDistance','nextStopTimetableVisitTime','courseIdentifier',
'courseDirection','timetableIdentifier','timetableStatus','receivedTime','processingFinishedTime','onWayToDepot','overlapsWithNextBrigade','overlapsWithNextBrigadeStopLineBrigade',
'atStop','speed','oldDelay','serverId','delayAtStopStopSequence','previousStopStopSequence','nextStopStopSequence','delayAtStopStopId','previousStopStopId','nextStopStopId',
'courseDirectionStopStopId']

COLS_FOR_ARFF = ['domain','time','lon','lat','nearestStopLon','nearestStopLat','nextStopDistance','speed','delay']
buses = pd.read_csv('buses/2018-09-05/part-r-00000', sep=';', header=None, names=COLNAMES)

day = buses
day['time'] = pd.to_datetime(day['time'], format='%Y-%m-%d %H:%M:%S')

day['previousDelay'] = None
day['previousLon'] = None
day['previousLat'] = None
day['previousNextStopDistance'] = None
day['previousSpeed'] = None
day['class'] = None
future = td(minutes=5)
max_reads = 80
print(len(day))
for i in range(max_reads, len(day)-max_reads):
    if i % 10000 == 0:
        print(i)
    record = day.iloc[i]
    for j in range(40, max_reads):
        current = day.iloc[i+j]
        if(current['time']-record['time'] > future):
            if((current['courseIdentifier'] == record['courseIdentifier'])):
                day.at[i, 'class'] = current['delay']
            break
    for j in range(-40, -max_reads, -1):
        current = day.iloc[i+j]
        if(record['time']-current['time'] > future):
            if((current['courseIdentifier'] == record['courseIdentifier'])):
                day.at[i, 'previousDelay'] = current['delay']
                day.at[i, 'previousLon'] = current['lon']
                day.at[i, 'previousLat'] = current['lat']
                day.at[i, 'previousSpeed'] = current['speed']
                day.at[i, 'previousNextStopDistance'] = current['nextStopDistance']
            break

day.to_csv('10-buses-context-09-05.csv')