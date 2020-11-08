from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from CoreBackend.models import Solutions
import random

@csrf_exempt
def AboutUs(request):
    if request.method == "GET":
        Data = {}
        return render(request, "CoreBackend/index.html", Data)
    elif request.method == "POST":
        # parse the request.body --> readlines()
        RawResponse = str(request.body)[1:-1].replace("'","").split("&")
        NewSolutions = Solutions(button=RawResponse[2][RawResponse[2].index("=")+1:],
                                 keypad=RawResponse[1][RawResponse[1].index("=")+1:],
                                 wires=RawResponse[0][RawResponse[0].index("=")+1:],
                                 button_model=RawResponse[4][RawResponse[4].index("=") + 1:],
                                 keypad_model=RawResponse[5][RawResponse[5].index("=") + 1:],
                                 wires_model=RawResponse[3][RawResponse[3].index("=") + 1:],
                                 led_color=RawResponse[6][RawResponse[6].index("=") + 1:])
        NewSolutions.save()
        return HttpResponse("Success!")

def ManualPage(request):
    LatestSolution = Solutions.objects.latest("created")

    ButtonSolution = LatestSolution.button
    KeypadSolution = LatestSolution.keypad
    WiresSolution = LatestSolution.wires
    if ButtonSolution == "press":
        ButtonSolution = "press and release."
    else:
        ButtonSolution = "press and hold. Let go when the number \""+ButtonSolution+"\" appears in the timer."
    ButtonModel = str(LatestSolution.button_model).replace("4","")
    KeypadModel = str(LatestSolution.keypad_model).replace("0","")
    WiresModel = str(LatestSolution.wires_model).replace("3","")
    LEDColor =  str(LatestSolution.led_color)
    print(LEDColor)
    # yellow ,green, blue
    # if real answer is in fake -> remove fakes till real remains

    Data ={ "Main":{
        "Wires_01": [
        {
            "Model": "6966",
            "Instructions": "Take out blue wire"
        },
        {
            "Model": "6999",
            "Instructions": "Take out red wire"
        },
        {
            "Model": "9969",
            "Instructions": "Take out green wire"
        },
        {
            "Model": "99699",
            "Instructions": "Take out blue wire"
        },
        {
            "Model": "999666",
            "Instructions": "Take out yellow wire"
        },
    ],
        "Buttons_03": [
            {
                "Model": "1311",
                "Instructions": "If red, press and hold. Let go when the number \"1\" appears in the timer."
            },
            {
                "Model": "35132",
                "Instructions": "If green, press and release."
            },
            {
                "Model": "7292",
                "Instructions": "If blue, press and hold. Let go when the number \"3\" appears in the timer."
            },
            {
                "Model": "33311",
                "Instructions": "If blue, press and release."
            },
            {
                "Model": "557316",
                "Instructions": "If magenta, press and hold. Let go when the number \"1\" appears in the timer."
            },
        ],
        # 1,2,4,5
        "Keypad_05": [
            {
                "Model": "674231",
                "Instructions": "Type in 1234"
            },
            {
                "Model": "3231",
                "Instructions": "Type in 2444"
            },
            {
                "Model": "3253",
                "Instructions": "Type in 1440"
            },
            {
                "Model": "568323",
                "Instructions": "Type in 5555"
            },
            {
                "Model": "57321",
                "Instructions": "Type in 1425"
            },
        ],
        "Wires_07": [
            {
                "Model": "6966",
                "Instructions": "Take out green wire"
            },
            {
                "Model": "9966",
                "Instructions": "Take out blue wire"
            },
            {
                "Model": "66699",
                "Instructions": "Take out yellow wire"
            },
            {
                "Model": "96",
                "Instructions": "Take out green wire"
            },
            {
                "Model": "69666",
                "Instructions": "Take out magenta wire"
            },
        ],
        "Wires_08": [
            {
                "Model": "696966",
                "Instructions": "Take out blue wire"
            },
            {
                "Model": "6666",
                "Instructions": "Take out blue wire"
            },
            {
                "Model": "9969",
                "Instructions": "Take out blue wire"
            },
            {
                "Model": "9996",
                "Instructions": "Take out blue wire"
            },
            {
                "Real_Model": WiresModel,
                "Instructions": "Take out "+WiresSolution+" wire"
            },
        ],
        "Keypad_09": [
            {
                "Model": "3893",
                "Instructions": "If red, press and hold. Let go when the number \"3\" appears in the timer."
            },
            {
                "Model": "19749",
                "Instructions": "If magenta, press and hold. Let go when the number \"7\" appears in the timer."
            },
            {
                "Model": "5849",
                "Instructions": "If green, press and release."
            },
            {
                "Model": "2395",
                "Instructions": "If blue, press and hold. Let go when the number \"1\" appears in the timer."
            },
            {
                "Real_Model": KeypadModel,
                "Instructions": "Type in "+KeypadSolution
            },
        ],
        "Button_01": [
            {
                "Model": "97430",
                "Instructions": "If blue, press and hold. Let go when the number \"4\" appears in the timer."
            },
            {
                "Model": "98340",
                "Instructions": "If green, press and hold. Let go when the number \"3\" appears in the timer."
            },
            {
                "Model": "378301",
                "Instructions": "If green, press and hold. Let go when the number \"5\" appears in the timer."
            },
            {
                "Model": "182738",
                "Instructions": "If red, press and hold. Let go when the number \"1\" appears in the timer."
            },
            {
                "Real_Model": ButtonModel,
                "Instructions": "If {}, {}".format(LEDColor,ButtonSolution)
            },
        ]
    },
        "Data_Order":["Wires_01","Buttons_03","Keypad_05","Wires_07","Wires_08","Keypad_09", "Button_01"]
    }

    random.shuffle(Data["Data_Order"])

    for DataNode in Data["Data_Order"]:
        random.shuffle(Data["Main"][DataNode])

    RealWireVal = 0
    for Model in Data["Main"]["Wires_08"]:
        if "Real_Model" in Model:
            RealWireVal = Model["Real_Model"]
            break

    for Model in Data["Main"]["Wires_08"]:
        if "Real_Model" in Model:
            continue
        elif RealWireVal == Model["Model"]:
            Model["Model"] = "REDACTED"
            Model["Instructions"] = "REDACTED"



    RealKeypadVal = 0
    for Model in Data["Main"]["Keypad_09"]:
        if "Real_Model" in Model:
            RealKeypadVal = Model["Real_Model"]
            break

    for Model in Data["Main"]["Keypad_09"]:
        if "Real_Model" in Model:
            continue
        elif RealKeypadVal == Model["Model"]:
            Model["Model"] = "REDACTED"
            Model["Instructions"] = "REDACTED"

    RealButtonVal = 0
    for Model in Data["Main"]["Button_01"]:
        if "Real_Model" in Model:
            RealButtonVal = Model["Real_Model"]
            break

    for Model in Data["Main"]["Button_01"]:
        if "Real_Model" in Model:
            continue
        elif RealButtonVal == Model["Model"]:
            Model["Model"] = "REDACTED"
            Model["Instructions"] = "REDACTED"


    # 3 real sections --> 5 fake sections that hard coded [all sections are mixed]
    # In the 3 real sections --> create 4 fake models and instructions and 1 real set with the corresponding model and instructions
    # Description for each section (decode numbers)
    return render(request, "CoreBackend/manual.html", Data)
