#pragma once
#include <juce_gui_basics/juce_gui_basics.h>

class WavePreviewComponent : public juce::Component
{
public:
    void paint(juce::Graphics& g) override
    {
        g.fillAll(juce::Colours::darkgrey.darker());
        g.setColour(juce::Colours::white.withAlpha(0.8f));
        g.drawRect(getLocalBounds());
        g.drawFittedText("Wave preview stub", getLocalBounds(), juce::Justification::centred, 1);
    }
};
