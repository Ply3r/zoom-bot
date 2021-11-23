import pyautogui
import keyboard
import time
import re


def transformNumber(number):
    return int(number)


def getZoomCode():
    hour = input('Digite o horario da aula(00:00): ')
    code = input('Digite o codigo da aula: ')
    return {'hour': hour, 'code': code}

def getInformations():
    isEditing = True
    info = []
    while isEditing:
        hold = getZoomCode()
        info.append(hold)
        result = input('Deseja adicionar mais? [S/N]: ')
        if result == 'S' or result != 's':
            isEditing = False
    return info


def findZoomIcon():
    zoomIcon = pyautogui.locateOnScreen('images/zoom_icon.png', confidence=0.8)
    if zoomIcon:
        return [zoomIcon.left, zoomIcon.top]
    else:
        return False


def findEnterButton():
    enterButton = pyautogui.locateOnScreen('images/enter_button.png')
    if enterButton:
        return [enterButton.left, enterButton.top]
    else:
        return False


def openZoom(zoomCode):
    initialPage = [1919, 1055]

    pyautogui.moveTo(*initialPage)
    pyautogui.click()

    zoomPosition = findZoomIcon()

    if not zoomPosition:
        print("I can't find zoom icon")
        return

    pyautogui.moveTo(*zoomPosition)
    pyautogui.doubleClick()

    time.sleep(1)

    enterLocation = findEnterButton();

    if not enterLocation:
        print("I can't find enter Button")
        return;

    pyautogui.moveTo(*enterLocation)
    pyautogui.click()

    time.sleep(1)

    pyautogui.write(zoomCode)
    pyautogui.press('enter')

    time.sleep(1)

    pyautogui.press('enter')


def start():
    info = getInformations()
    while len(info):
        meeting = info[0]
        meetingTime = meeting['hour']
        meetingCode = meeting['code']
        meetingHour = re.search('^\d+', meetingTime).group()
        meetingMinutes = re.search('\d+$', meetingTime).group()
        realTime = time.localtime()

        if int(meetingHour) == int(realTime.tm_hour) and int(realTime.tm_min) >= int(meetingMinutes):
            openZoom(meetingCode)
            del info[0]

        if len(info):
            time.sleep(300)

    print('Esgotaram os horarios :)')


start()
