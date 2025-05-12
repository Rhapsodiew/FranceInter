# 🇫🇷 FranceInter

**FranceInter** is a smart occupancy detection program designed to monitor the number of people in a room. If the number exceeds a specified limit, the application automatically plays a warning audio message using **Microsoft Azure Cognitive Services**.

## 🎯 Purpose

The goal of this project is to ensure safety and comfort in public or private indoor spaces by monitoring room occupancy and triggering alerts when the room becomes too crowded.

## 🛠️ Tech Stack

- **Language:** Python
- **Cloud Services:** Microsoft Azure Speech API (Text-to-Speech), Microsoft Azure Translate, Microsoft Azure Vision (face recognition)
- **Detection Logic:** (Depending on implementation, e.g., camera/IoT sensor integration or mock input)

## 🚀 Features

- 👥 **Occupancy Monitoring:** Check the current number of people in a room.
- 🔊 **Audio Alerts:** If the threshold is exceeded, play a warning message.
- ☁️ **Azure Integration:** Uses Azure TTS to synthesize the message in natural-sounding speech.
- ⚙️ **Customizable Threshold:** Set your own maximum number of allowed individuals.

## 📄 License

This project is licensed under the MIT License.
See the LICENSE file for more information.
