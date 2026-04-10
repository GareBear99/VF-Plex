#pragma once

#include <string>

class BackendClient;

class VocalForgeEditor
{
public:
    VocalForgeEditor();
    ~VocalForgeEditor();

    void submitPrompt(const std::string& promptText, const std::string& voiceId, int seed);

private:
    BackendClient* backendClient { nullptr };
};
