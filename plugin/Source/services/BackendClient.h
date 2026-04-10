#pragma once

#include <string>

class BackendClient
{
public:
    BackendClient() = default;
    ~BackendClient() = default;

    void queueGeneration(const std::string& promptText,
                         const std::string& voiceId,
                         int seed,
                         double targetSeconds,
                         const std::string& category);
};
