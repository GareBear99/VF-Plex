#pragma once

class VocalForgeAudioProcessor
{
public:
    VocalForgeAudioProcessor() = default;
    ~VocalForgeAudioProcessor() = default;

    void prepareToPlay(double sampleRate, int samplesPerBlock);
    void processBlock(float** channels, int numChannels, int numSamples);

private:
    double currentSampleRate { 44100.0 };
    int currentBlockSize { 512 };
};
