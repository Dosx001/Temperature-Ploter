import matplotlib.pyplot as plt
import datetime as dt

class Plots:
    def __init__(self):
        self.files = []
        self.num_items = 0

    def add_plot(self, file, sort = False):
        self.files.append(file)
        self.num_items += 1
        if sort:
            self.files.sort()
    
    def del_plot(self, file, sort = False):
        for i in range(self.num_items):
            if self.files[i] == file:
                self.files.pop(i)
                break
        else:
            print("File Not Found")
        if sort:
            self.files.sort()
    
    def plot_files(self):
        for i in range(self.num_items):
            fp = open(self.files[i], 'r')
            Temps = fp.readlines()
            Temps = [ii.split() for ii in Temps]
            Temps_Obj = [float(ii[0]) for ii in Temps]
            Temps_Amb = [float(ii[1]) for ii in Temps]
            Avg_Temps_Obj = []
            Avg_Temps_Amb = []
            samples = 480 #240#120
            x, y = 0, samples
            for ii in range(len(Temps_Obj) // samples):
                    Avg_Temps_Obj.append(sum(Temps_Obj[x:y]) / samples)
                    Avg_Temps_Amb.append(sum(Temps_Amb[x:y]) / samples)
                    x += samples
                    y += samples
            time = [ii for ii in range(len(Avg_Temps_Obj))]
            full = self.files[i].split()
            date = full[0].split("-")
            date = dt.datetime(int(date[0]), int(date[1].replace("0", "")), int(date[2]))
            plt.figure(self.files[i])
            plt.title(date.strftime("%B %d, %Y"))
            plt.plot(time, Avg_Temps_Obj, label = 'Object')
            plt.plot(time, Avg_Temps_Amb, label = 'Ambient')
            plt.grid()
            plt.xlabel('Time[hr]')
            plt.ylabel('Temperature[$^\circ$F]')
            plt.legend()
            start_time = full[1].split("-")
            times = [] 
            t = int(start_time[0])
            for i in range(min(time), max(time) + 1, 15): #30#60 
                if t == 24:
                    t = 0
                times.append(dt.time(t, int(start_time[1])))
                t += 1
            real_time = [times[i].strftime("%I:%M %p") for i in range(len(times))]
            plt.gcf().autofmt_xdate()
            plt.xticks(list(range(min(time), max(time)+1, 15)), real_time) #30#60
            plt.xlim(0, max(time))
            fp.close()   
        plt.show()

    def plot_temp(self):
        days = []
        avg_temps_obj = []
        avg_temps_amb = []
        for i in range(self.num_items):
            fp = open(self.files[i], 'r')
            Temps = fp.readlines()
            Temps = [ii.split() for ii in Temps]
            Temps_Obj = [float(ii[0]) for ii in Temps]
            Temps_Amb = [float(ii[1]) for ii in Temps]
            days.append(i + 1)
            avg_temps_obj.append(sum(Temps_Obj) / len(Temps_Obj))
            avg_temps_amb.append(sum(Temps_Amb) / len(Temps_Amb))
            fp.close()
        plt.figure("All")
        plt.plot(days, avg_temps_obj, label = 'Object')
        plt.plot(days, avg_temps_amb, label = 'Ambient')
        plt.grid()
        plt.xticks(days)
        plt.xlabel('Time[day]')
        plt.ylabel('Temperature[$^\circ$F]')
        plt.legend()
        plt.xlim(1, len(days))
        plt.title("Temperature v Time")
        plt.show()
