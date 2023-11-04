# anonpi: Python Module for Calling Systems

The **anonpi** module is a powerful Python package that provides a convenient interface for interacting with calling systems. It simplifies the development of applications that require functionalities such as machine detection, IVR (Interactive Voice Response), DTMF (Dual-Tone Multi-Frequency) handling, recording, playback, and more.

## Key Features

- **Machine Detection:** Easily detect whether a call is being answered by a human or an automated system, enabling intelligent call handling and routing.
- **IVR Support:** Build interactive voice response systems by creating menus, prompts, and collecting user input through voice or DTMF tones.
- **DTMF Handling:** Efficiently capture and process DTMF tones (telephone keypad input) during calls for user interaction, menu navigation, and decision-making.
- **Call Recording:** Seamlessly record incoming or outgoing calls, enabling compliance with legal requirements, quality monitoring, and archiving for later analysis.
- **Playback Functionality:** Retrieve and play back pre-recorded audio files during calls, enhancing the user experience and providing personalized content.
- **Call Control:** Take control of call initiation, termination, and manipulation, allowing for call transfers, forwarding, muting, and more.

## Usage

The **anonpi** module provides a clean and intuitive API, making it easy to integrate calling functionalities into your Python applications. Here's an example of how you can use the module to perform machine detection during a call:

```python
import anonpi

anonpi.api_key = "<API KEY>"

call = anonpi.Call.create(
    from_number="18888888888",
    to_number="1234567890",
    callback_url="https://callback.url",
    amd=False
)

# operations using call
call.gather_using_audio(
    audio_url="https://audio.url",
    dtmf_digits="6"
    )

# last hangup the call
call.hangup()
```

## Getting Started
To install the anonpi module, use the following command:

```bash
pip install anonpi
```

> Add any additional installation instructions or requirements here.

> Disclaimer: Ensure compliance with all legal and regulatory requirements when using the "anonpi" module for call recording or related functionalities.

### Additional Resources
- [Documentation Link](https://docs.anonpi.co)
- [GitHub Repository](https://github.com/evenuestar/anonpi)


