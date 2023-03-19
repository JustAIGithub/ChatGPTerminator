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

1. Clone this repository to your local machine.
2. Navigate to the cloned directory using your command line interface.
3. Create a virtual environment by using the following command:

   ```
   python3 -m venv venv
   ```

4. Install the pip requirements into the venv:

   ```
   pip install -r requirements.txt
   ```

5. Set the OPENAI_API_KEY env variable (you may want this in your .rc file):

   ```
   export OPENAI_API_KEY=PUT_API_KEY_HERE
   ```

6. Run the following command to start the ChatGPT terminal interface:

   ```
   python GPTerminator.py
   ```

7. You can now start chatting. Type a message and press Enter to get a response.

8. Type !help for a list of commands to use

<details><summary><h2>Call From Anywhere :globe_with_meridians:</h2></summary>


In order you call the script from anywhere, you can alter your .rc file by adding a function:

   ```zsh
   ask () {
       cd path/to/ChatGPTerminator
       source venv/bin/activate
       python GPTerminator.py
       deactivate
       cd $OLDPWD
   }
   ```

</details>
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
   SaveFolder = 
   ```

- **ModelName:** this is the model used when chatting
- **Temperature** = between 0 and 2
- **PresencePenalty** = between -2 and 2
- **FrequencyPenalty** = between -2 and 2
- **SystemMessage:** this is the starting system message sent to the API
- **CommandInitiator:** this can be set to change the default !<cmd> structure
- **SaveFolder:** this changes the location of the save folder when running !save

   _Note_: More details on some settings can be found [here](https://platform.openai.com/docs/api-reference/chat/create)

After saving the config file, run:
   ```zsh
   python GPTerminator
   ```
Then, type !setconf and select which config you wish to use, you can also run the !pconf commang to view the current config details.

_Note_: If you change the CommandInitiator, you will now type <CommandInitiator><cmd> to execute commands...


</details>


## Contributing :raised_hands:

We welcome contributions to this project. If you find a bug, have a feature request, or want to contribute code, please open an issue or submit a pull request.

## Disclaimer :warning: 

This program uses the openai API to chat and generate images using dalle. It is a good idea to put a usage cap on your billing, just in case something goes wrong!
