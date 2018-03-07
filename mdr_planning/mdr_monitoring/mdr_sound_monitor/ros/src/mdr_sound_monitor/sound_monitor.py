"""PyAudio Example: Play a wave file."""

import pyaudio
import wave
import sys
import yaml
import rospy

class SoundMonitor:
    def __init__(self, config_file):
        rospy.init_node("sound_monitor", anonymous = False)
        self.common_path = "/home/jose/ros/src/mas_domestic_robotics/mdr_planning/mdr_monitoring/mdr_sound_monitor/ros/" #TODO
        self.sound_dictionary = yaml.load(open(self.common_path + "config/" + config_file+".yaml"))
        self.CHUNK = 1024 #TODO

        self.audio_manager = pyaudio.PyAudio()

        for sound in self.sound_dictionary:
            sound_file = self.sound_dictionary[sound]['folder']+'/'+ self.sound_dictionary[sound]['file_name'] 
            rospy.Subscriber(self.sound_dictionary[sound]['topic'], rospy.AnyMsg, self.mainCB, sound_file)

        rospy.spin()

    def mainCB(self, msg, sound_file):
        sound_file_path = self.common_path + 'willow-sound/'+ sound_file 
        self.playSound(sound_file_path)

    def playSound(self,sound_file):
        wf = wave.open(sound_file, 'rb')
        data = wf.readframes(self.CHUNK)
        stream = self.audio_manager.open(format=self.audio_manager.get_format_from_width(wf.getsampwidth()),
                      channels=wf.getnchannels(),
                      rate=wf.getframerate(),
                      output=True)

        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(self.CHUNK)

            # stop stream (4)
        stream.stop_stream()
        stream.close()
 




