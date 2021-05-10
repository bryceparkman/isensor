import csv
import matplotlib.pyplot as plt
import numpy as np

time_array = []
temp_array = []
humid_array = []
labels_array = []


with open('data2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            time_array.append(row[0])
            temp_array.append(row[1])
            humid_array.append(row[2])
            labels_array.append(row[3])
        line_count += 1

npT = np.array(time_array).astype(int)
npTT = np.array(temp_array).astype(float)
npH = np.array(humid_array).astype(float)
npL = np.array(labels_array)

state_switches = np.where(npL[:-1] != npL[1:])[0]
labels1 = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0])
labels2 = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

e1 = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4.565100775193798,9.130201550387596,13.695302325581395,18.260403100775193,22.82550387596899,27.39060465116279,27.39060465116279,31.955705426356587,31.955705426356587,36.520806201550386,41.085906976744184,45.65100775193798,50.21610852713178,50.21610852713178,50.21610852713178,50.21610852713178,50.21610852713178,50.21610852713178,50.21610852713178,50.21610852713178,50.21610852713178,50.21610852713178,50.21610852713178,50.21610852713178,50.21610852713178,50.21610852713178,50.21610852713178,50.21610852713178,50.21610852713178,50.21610852713178,50.21610852713178,50.21610852713178,50.21610852713178,54.78120930232558,59.34631007751938,63.911410852713175,68.47651162790697,73.04161240310077,73.04161240310077,77.60671317829457,82.17181395348837,86.73691472868217,91.30201550387596,95.86711627906976,100.43221705426356,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,104.99731782945736,109.56241860465116,114.12751937984495,118.69262015503875,123.25772093023255,127.82282170542635,127.82282170542635,127.82282170542635,127.82282170542635,127.82282170542635,127.82282170542635,127.82282170542635,127.82282170542635,127.82282170542635,127.82282170542635,127.82282170542635,132.38792248062015,132.38792248062015,136.95302325581395,136.95302325581395,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774])
e2 = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4.565100775193798,9.130201550387596,13.695302325581395,18.260403100775193,22.82550387596899,27.39060465116279,31.955705426356587,36.520806201550386,41.085906976744184,45.65100775193798,50.21610852713178,54.78120930232558,59.34631007751938,59.34631007751938,59.34631007751938,59.34631007751938,59.34631007751938,59.34631007751938,59.34631007751938,59.34631007751938,59.34631007751938,59.34631007751938,59.34631007751938,59.34631007751938,59.34631007751938,59.34631007751938,59.34631007751938,59.34631007751938,59.34631007751938,59.34631007751938,59.34631007751938,59.34631007751938,59.34631007751938,63.911410852713175,68.47651162790697,73.04161240310077,77.60671317829457,82.17181395348837,86.73691472868217,91.30201550387596,95.86711627906976,100.43221705426356,104.99731782945736,109.56241860465116,114.12751937984495,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,118.69262015503875,123.25772093023255,127.82282170542635,132.38792248062015,136.95302325581395,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774,141.51812403100774])


maskOff = False
maskOn = False


# test = np.arange(0,len(e1))
# plt.title('Predicted cumulative mask wear time vs ground truth')
# plt.ylabel('Cumulative mask wear time (seconds)')
# plt.xlabel('Time elapsed (seconds)')
# plt.plot(test * 4.565100775193798 / 60,e1, label='Predicted')
# plt.plot(test * 4.565100775193798 / 60,e2, label='Actual')
# plt.legend()

plt.figure(1)
plt.plot(npT / 1000 / 60, npH)
plt.plot([0, 25], [66, 66], color='k', linestyle='--',
         linewidth=1, label='Base Humidity')
for idx in state_switches:
    plotColor = 'r' if npL[idx+1] == '0' else 'g'
    legendName = ''
    if npL[idx+1] == '0' and not maskOff:
        legendName = 'Mask off marker'
        maskOff = True
    if npL[idx+1] == '1' and not maskOn:
        legendName = 'Mask on marker'
        maskOn = True
    plt.plot([npT[idx] / 1000 / 60, npT[idx] / 1000 / 60],
             [50, 95], color=plotColor, label=legendName)
plt.legend()
plt.xlabel('Time elapsed (minutes)')
plt.ylabel('% Relative Humidity')
plt.title('Humidity vs Time Elapsed')

plt.figure(2)
plt.plot(npT / 1000 / 60, npTT, color='b')
for idx in state_switches:
    plotColor = 'r' if npL[idx+1] == '0' else 'g'
    legendName = ''
    if npL[idx+1] == '0' and not maskOff:
        legendName = 'Mask off marker'
        maskOff = True
    if npL[idx+1] == '1' and not maskOn:
        legendName = 'Mask on marker'
        maskOn = True
    plt.plot([npT[idx] / 1000 / 60, npT[idx] / 1000 / 60],
             [20, 32], color=plotColor, label=legendName)
plt.xlabel('Time elapsed (minutes)')
plt.ylabel('Temperature (Celsius)')
plt.title('Temperature vs Time Elapsed')

plt.show()