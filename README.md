<h1 align="center">GPTerminator :robot:</h1>
<p align="center">
<img src="./imgs/cmd_example.png" width="600" />
</p>
<p align="center">This terminal interface provides a convenient way to interact with OpenAI's chat completion and image generation API's using your command line interface.</p>
<p align="center">
<img src="https://img.shields.io/github/last-commit/AineeJames/ChatGPTerminator?style=for-the-badge&logo=github&color=7dc4e4&logoColor=D9E0EE&labelColor=302D41" />
<img src="https://img.shields.io/github/stars/AineeJames/ChatGPTerminator?style=for-the-badge&logo=apachespark&color=eed49f&logoColor=D9E0EE&labelColor=302D41" />
</p>


## Getting Started :rocket:

To use this terminal interface, follow these steps:

1. Either clone this repository to your local machine and run `pip install .` or install it from PyPi by running `pip install gpterminator`

2. Set the OPENAI_API_KEY env variable (you may want this in your .rc file): `export OPENAI_API_KEY=PUT_API_KEY_HERE`

3. Run the following command to start the ChatGPT terminal interface: `gpterm`

4. You can now start chatting. Type a message and press Enter to get a response.

5. Type !help for a list of commands to use

<details><summary><h2>Configuration :gear:</h2></summary>


GPTerminator is configurable and can support multiple configurations. Add the following to your config.ini:

   ```ini
   [CONFIG_TEMPLATE]
   ModelName = 
   SystemMessage = 
   Temperature =
   PresencePenalty = 
   FrequencyPenalty = 
   CommandInitiator = 
   SavePath = 
   ```

- **ModelName:** this is the model used when chatting
- **Temperature** = between 0 and 2
- **PresencePenalty** = between -2 and 2
- **FrequencyPenalty** = between -2 and 2
- **SystemMessage:** this is the starting system message sent to the API
- **CommandInitiator:** this can be set to change the default !<cmd> structure
- **SavePath:** this changes the location of the save path when loading/saving

_Note_: More details on some settings can be found [here](https://platform.openai.com/docs/api-reference/chat/create)

After saving the config file, run: `gpterm`
Then, type !setconf and select which config you wish to use, you can also run the !pconf commang to view the current config details.

_Note_: If you change the CommandInitiator, you will now type <CommandInitiator><cmd> to execute commands...


</details>


## Contributing :raised_hands:

We welcome contributions to this project. If you find a bug, have a feature request, or want to contribute code, please open an issue or submit a pull request.

## Disclaimer :warning: 

This program uses the openai API to chat and generate images using dalle. It is a good idea to put a usage cap on your billing, just in case something goes wrong!
