from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import comtypes



def adjust_volume(volume_level):
    volume = volume_variable()
    volume.SetMasterVolumeLevelScalar(volume_level, None)

def get_system_volume():
    volume = volume_variable()
    return volume.GetMasterVolumeLevelScalar()

def volume_variable():
    comtypes.CoInitialize()
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

    return cast(interface, POINTER(IAudioEndpointVolume))


