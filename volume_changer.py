"""
Module: volume_changer

Practice code for working with sounds in Python.
"""
import sound

def change_volume(original_sound, multiplier):
    
   
    filtered_sound = sound.copy(original_sound)

# change the volume of the love sound
    for sample_number in range(len(filtered_sound)):
        sample = filtered_sound[sample_number]

        # change the left channel
        new_left_val = int(sample.left * multiplier)
        sample.left = new_left_val

        # change the right channel (in only one line of code!)
        sample.right = int(sample.right * multiplier)

        
    #pass # replace this line with your code
    
    return filtered_sound
# First, test the change_volume with the love.wav audio
love = sound.load_sound("love.wav")
love.play()
sound.wait_until_played() 



changed_love = change_volume(love, 2)
changed_love.play()
sound.wait_until_played()

# Now, test our function with the doglake.wav audio
doglake_sound = sound.load_sound("doglake.wav")
doglake_sound.play()
sound.wait_until_played() 

changed_doglake_sound = change_volume(doglake_sound)
changed_doglake_sound.play()
sound.wait_until_played()
