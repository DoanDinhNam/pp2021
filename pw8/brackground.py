import pickle
import threading


class BackgroundThread(threading.Thread):
    def __init__(self, option, data, pickle_dum=None):
        threading.Thread.__init__(self)
        self.__pmo = pmo
        self.__pdf = pdf
        self.__pdum = pdum
        self.__ploa = ploa

    def RunThreading(self):
        if self.__pmo == "dump":
            if self.__pdum is not None:
                pickle.dump(self.__pdum, self.__pdf)
            else:
                return 0
        elif self.__pmo == "load":
            if self.__ploa is not None:
                loadfile = pickle.load(self.__pdf)
                self.__ploa.append(loadfile)
            else:
                return 0


def backgroundThreadFunction(option, data, pickle_dum = None):
    backgroundThread=BackgroundThread(option, data ,pickle_dum)
    backgroundThread.start()
    backgroundThread.join()