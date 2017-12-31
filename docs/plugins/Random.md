# Random

## Overview
Random is a plugin which responds to various commands with a random response, some of these responses are completely incapable of being customised due to the way the plugin is randomizing the items.



## Commands

### roll
This command allows you to randomly roll any number of dice or just pick a random number. (Response formats may be different in actual bot.)

> **Syntax:** `{Command Prefix}random roll [Amount] <Sides>`
>
>If `[Amount]` isn't specified, the bot will assume it to be the "default_amount" which is assigned in the plugin configuration file.


Examples:
```
[Alkali] !random roll 2 10
[Bot] Total: 15
      Rolls: 7, 8
---------------------------------
[Alkali] !random roll 10
[Bot] Total: 4
```



### formula
This command responds with a random chemical formula, either organic or inorganic, it's just whatever formulas I feel like having in the response choices.

> **Syntax:** `{Command Prefix}random formula`


Example:
```
[Alkali] !random formula
[Bot] Phenol
```



## object
This command takes a list of arguments and randomly selects one of them. Aliased to `choice`

> **Syntax:** `{Command Prefix}random object <objects...>`

> Where `<objects...>` is a space separated list of values to pick from.

Examples:
```
[Alkali] !random object David_Tennant Matt_Smith Peter_Capaldi Christopher_Eccleston
[Bot] Choice: David_Tennant
---------------------------------
[Alkali] !random choice Linux MacOS Windows
[Bot] Choice: Linux
```



## shuffle
This command takes a list of arguments, shuffles them, then returns it to chat.

> **Syntax:** `{Command Prefix}random shuffle <objects...>`
>
> Where `<objects...>` is a space separated list of values.

Example:
```
[Alkali] !random shuffle thing1 thing2 thing3 thing4 thing5
[Bot] Ordering: thing3 thing5 thing2 thing1 thing4
```



## gif
This command responds with a gif which was pre-approved to be in the list.

> **Syntax:** `{Command Prefix}random gif`

Example:
```
[Alkali] !random gif
[Bot] https://giphy.com/gifs/jxkfRvvfI0mDm
```