from time import sleep

class trafficlight:
    _color = "черный"

    def running(self):
        while True:
            print('красный')
            sleep(7)
            print('желтый')
            sleep(2)
            print('зеленый')
            sleep(7)
            print('желтый')
            sleep(2)

trafficlight = TrafficLight()
trafficlight.running()