#include "BackendClient.h"
#include <iostream>

void BackendClient::queueGeneration(const std::string& promptText,
                                    const std::string& voiceId,
                                    int seed,
                                    double targetSeconds,
                                    const std::string& category)
{
    std::cout << "Queue generation request -> prompt: " << promptText
              << ", voice: " << voiceId
              << ", seed: " << seed
              << ", seconds: " << targetSeconds
              << ", category: " << category
              << std::endl;

    // Replace this with your HTTP client of choice.
    // The core requirement is async submission and polling, never DSP-thread inference.
}
