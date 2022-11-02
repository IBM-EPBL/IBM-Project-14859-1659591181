import random

Temperature = random.sample(range(20,120) , 15)
print ("Temperature = ", Temperature)
Humidity=random.sample(range(40,90), 15)
print("Humidity = ", Humidity)
for i in Temperature:
    if(i>85):
        {
            print(f"{i} Exceeds Normal Temperature . Alarm Detected")
    }