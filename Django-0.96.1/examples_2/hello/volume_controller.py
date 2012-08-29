import alsaaudio

class VolumeController:
    def __init__(self):
        self.mixer = alsaaudio.Mixer()

    def set_volume(self,new_volume):
        self.mixer.setvolume(new_volume)
        
    def get_volume(self):
        return self.mixer.getvolume()
