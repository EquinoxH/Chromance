# Imports

import profiles.rgb
import profiles.fastRGB
import profiles.pulse
import profiles.rainfall
import profiles.snowfall
import profiles.meteor
import profiles.heart
import profiles.embers
import profiles.fireflies
import profiles.flower
import profiles.pulseFireworks
import profiles.sparkleFireworks
import profiles.blossom
import profiles.purpleRain
import profiles.bigPulse

import profiles.lowWarning
import profiles.midWarning
import profiles.highWarning

# Profiles

rgb = 'RGB'
fastRGB = 'FastRGB'
pulse = 'Pulse'
rainfall = 'Rainfall'
snowfall = 'Snowfall'
meteor = 'Meteor'
heart = 'Heart'
embers = 'Embers'
fireflies = 'Fireflies'
flower = 'Flower'
pulseFireworks = 'PulseFireworks'
sparkleFireworks = 'SparkleFireworks'
blossom = 'Blossom'
purpleRain = 'PurpleRain'
bigPulse = 'BigPulse'

lowWarning = "Low"
midWarning = "Mid"
highWarning = "High"

# Function Maps

setProfileFunctions = {
    rgb: profiles.rgb.setProfile,
    fastRGB: profiles.fastRGB.setProfile,
    pulse: profiles.pulse.setProfile,
    rainfall: profiles.rainfall.setProfile,
    snowfall: profiles.snowfall.setProfile,
    meteor: profiles.meteor.setProfile,
    heart: profiles.heart.setProfile,
    embers: profiles.embers.setProfile,
    fireflies: profiles.fireflies.setProfile,
    flower: profiles.flower.setProfile,
    pulseFireworks: profiles.pulseFireworks.setProfile,
    sparkleFireworks: profiles.sparkleFireworks.setProfile,
    blossom: profiles.blossom.setProfile,
    purpleRain: profiles.purpleRain.setProfile,
    bigPulse: profiles.bigPulse.setProfile,
    
    lowWarning: profiles.lowWarning.setProfile,
    midWarning: profiles.midWarning.setProfile,
    highWarning: profiles.highWarning.setProfile
    }

doUpdateFunctions = {
    rgb: profiles.rgb.doUpdate,
    fastRGB: profiles.fastRGB.doUpdate,
    pulse: profiles.pulse.doUpdate,
    rainfall: profiles.rainfall.doUpdate,
    snowfall: profiles.snowfall.doUpdate,
    meteor: profiles.meteor.doUpdate,
    heart: profiles.heart.doUpdate,
    embers: profiles.embers.doUpdate,
    fireflies: profiles.fireflies.doUpdate,
    flower: profiles.flower.doUpdate,
    pulseFireworks: profiles.pulseFireworks.doUpdate,
    sparkleFireworks: profiles.sparkleFireworks.doUpdate,
    blossom: profiles.blossom.doUpdate,
    purpleRain: profiles.purpleRain.doUpdate,
    bigPulse: profiles.bigPulse.doUpdate,
    
    lowWarning: profiles.lowWarning.doUpdate,
    midWarning: profiles.midWarning.doUpdate,
    highWarning: profiles.highWarning.doUpdate
    }

onDeathFunctions = {
    pulseFireworks: profiles.pulseFireworks.spawnPulse,
    sparkleFireworks: profiles.sparkleFireworks.spawnDrawing,
    }

# Functions

def setProfile(profile):
    setProfileFunctions[profile]()
    
def doUpdateForCurrentProfile(profile):
    doUpdateFunctions[profile]()
    
def doDeathForCurrentProfile(profile, deathLocation):
    onDeathFunctions[profile](deathLocation)