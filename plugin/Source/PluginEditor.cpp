#include "PluginEditor.h"
#include "services/BackendClient.h"

VocalForgeEditor::VocalForgeEditor()
{
    backendClient = new BackendClient();
}

VocalForgeEditor::~VocalForgeEditor()
{
    delete backendClient;
}

void VocalForgeEditor::submitPrompt(const std::string& promptText, const std::string& voiceId, int seed)
{
    if (backendClient != nullptr)
        backendClient->queueGeneration(promptText, voiceId, seed, 3.0, "spoken_hooks");
}
