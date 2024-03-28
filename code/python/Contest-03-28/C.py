for i in range(int(input())):

    s = input()

    time = s.split(":")

    # convert 24 hour format to 12 hour format

    hh = int(time[0])
    mm = int(time[1])

    if hh == 0:
        print("12:" + time[1] + " AM")
    elif hh < 12:
        hr = hh
        if hr < 10:
            print("0" + str(hr) + ":" + time[1] + " AM")
        else:
            print(str(hh) + ":" + time[1] + " AM")
    elif hh == 12:
        print("12:" + time[1] + " PM")
    else:
        hr = hh - 12
        if hr < 10:
            print("0" + str(hr) + ":" + time[1] + " PM")
        else:
            print(str(hh - 12) + ":" + time[1] + " PM")
