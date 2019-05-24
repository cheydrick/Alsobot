# ALSOBOT
Alsobot is a Matrix (matrix.org) chat bot. It requires the [Matrix Python SDK](https://github.com/matrix-org/matrix-python-sdk) and [utilizes the bot API](https://github.com/shawnanastasio/python-matrix-bot-api) created by Shawn Anastasio.

# Setting Up
Alsobot looks for three environment variables for the user name, password, and server address. There are many ways to set this up. My method is to have an un-committed script called secrets.sh that exports those environment variables. For example:

> export ALSOBOTUSER="@username:server.address.com"  
> export ALSOBOTPASSWORD="password"  
> export ALSOBOTSERVER="https://server.address.com"  

Then in the console you can type "source secrets.sh" to set the environent variables, which you can verify with "printenv".
