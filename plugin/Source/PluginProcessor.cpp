#include "PluginProcessor.h"

void VocalForgeAudioProcessor::prepareToPlay(double sampleRate, int samplesPerBlock)
{
    currentSampleRate = sampleRate;
    currentBlockSize = samplesPerBlock;
}

void VocalForgeAudioProcessor::processBlock(float** channels, int numChannels, int numSamples)
{
    // No PersonaPlex inference here. Keep the audio callback deterministic and lightweight.
    for (int channel = 0; channel < numChannels; ++channel)
    {
        if (channels[channel] == nullptr)
            continue;

        for (int sample = 0; sample < numSamples; ++sample)
            channels[channel][sample] = channels[channel][sample];
    }
}
